#!/usr/bin/env python3
"""Batch-run the papergate-joaquin PromptForge prompt over every 2026 paper
in the paperstore, N runs each (default 5).

Starts one promptforge-gateway for the whole batch and tears it down at the
end. Per run: invoke `promptforge run` with the paper's markdown seeded into
the run's store as paper.md (--input) and the store's report.md extracted to
papergate_<pid>_run<N>.md in the output directory (--output). Credentials
live only in the process environment: the gateway bearer is generated per
invocation and VLLM_DEEPSEEK_API_KEY is inherited.

Gateway output goes to <out-dir>/gateway.log, not the terminal. Ctrl-C
terminates in-flight runs immediately; completed outputs are kept, so
re-running the same command resumes where the batch left off.
"""

from __future__ import annotations

import argparse
import os
import secrets
import sqlite3
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PROMPT_DEFAULT = "/code/wg21-papergate/papergate-joaquin-v4.md"
PROMPTFORGE_BIN_DEFAULT = "/code/promptforge-cli/target/debug/promptforge"
GATEWAY_BIN_DEFAULT = "/code/promptforge/target/release/promptforge-gateway"
GATEWAY_CONFIG_DEFAULT = Path("/code/wg21-papergate/gateway.toml")
GATEWAY_URL_DEFAULT = "http://127.0.0.1:8081/v1"

# Store files --keep-stores pulls out alongside the report, for debugging a
# run after the fact. Every one of these is written unconditionally by the
# prompt; asking for a file the run never wrote fails the whole run.
DEBUG_OUTPUTS = ("verdict.md", "evidence.md", "diagnostics.md")

# In-flight `promptforge run` processes, tracked so Ctrl-C can kill them
# immediately instead of waiting for the executor to drain.
active_procs: set[subprocess.Popen] = set()
active_lock = threading.Lock()
interrupted = threading.Event()


def fmt_dur(seconds: float) -> str:
    minutes = seconds / 60
    return f"{minutes:.0f}m" if minutes < 120 else f"{minutes / 60:.1f}h"


def list_2026_papers(db_path: Path) -> list[tuple[str, Path]]:
    """(paper_id, markdown_path) for every 2026 paper with converted markdown."""
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        rows = conn.execute(
            "SELECT paper_id, markdown_path FROM papers "
            "WHERE year = '2026' AND markdown_path != '' ORDER BY paper_id"
        ).fetchall()
    finally:
        conn.close()
    papers = []
    for pid, md in rows:
        if Path(md).is_file():
            papers.append((pid, Path(md)))
        else:
            print(f"warning: {pid} markdown_path is set but the file is gone; "
                  f"skipped", file=sys.stderr)
    return papers


def wait_for_gateway(url: str, token: str, proc: subprocess.Popen,
                     log_path: Path, timeout: float = 120.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            try:
                tail = "\n".join(
                    log_path.read_text(errors="replace").splitlines()[-15:])
            except OSError:
                tail = "(gateway.log unreadable)"
            raise RuntimeError(
                f"gateway exited during startup (rc={proc.returncode}); "
                f"last log lines:\n{tail}")
        req = urllib.request.Request(
            f"{url}/models", headers={"Authorization": f"Bearer {token}"})
        try:
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    return
        except (urllib.error.URLError, ConnectionError, OSError):
            pass
        time.sleep(1.0)
    raise RuntimeError(f"gateway not ready after {timeout:.0f}s at {url}; "
                       f"see {log_path}")


def run_one(prompt: Path, pid: str, run_no: int, md_path: Path, out_dir: Path,
            env: dict, promptforge_bin: Path, timeout: int, retries: int,
            keep_stores: bool) -> tuple[str, int, bool, str]:
    """One (paper, run) job. Returns (pid, run_no, ok, message)."""
    out_file = out_dir / f"papergate_{pid.lower()}_run{run_no}.md"
    if out_file.exists():
        return pid, run_no, True, "skipped (exists)"
    if interrupted.is_set():
        return pid, run_no, False, "interrupted"

    # The run's store lives inside the engine, not on disk: the paper goes in
    # through --input under the name the prompt reads, and every file worth
    # keeping comes back out through --output. The report lands on a .partial
    # path first so an interrupted copy can never look like a finished run to
    # the skip-if-exists check above.
    partial = out_file.with_name(out_file.name + ".partial")
    cmd = [str(promptforge_bin), "run",
           "--input", f"paper.md={md_path}",
           "--output", f"report.md={partial}"]
    if keep_stores:
        debug_dir = out_dir / ".stores" / f"pg_{pid.lower()}_run{run_no}"
        debug_dir.mkdir(parents=True, exist_ok=True)
        for name in DEBUG_OUTPUTS:
            cmd += ["--output", f"{name}={debug_dir / name}"]
    cmd.append(str(prompt))

    print(f"  started {pid} run{run_no}", flush=True)
    last_err = ""
    try:
        for attempt in range(1 + retries):
            if interrupted.is_set():
                return pid, run_no, False, "interrupted"
            proc = subprocess.Popen(cmd, env=env, stdout=subprocess.DEVNULL,
                                    stderr=subprocess.PIPE, text=True)
            with active_lock:
                active_procs.add(proc)
            try:
                _, stderr = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.communicate()
                last_err = f"timeout after {timeout}s"
            else:
                if proc.returncode == 0:
                    if partial.is_file():
                        partial.replace(out_file)
                        return pid, run_no, True, "ok"
                    last_err = "run succeeded but report.md was not produced"
                else:
                    # The whole of stderr goes to a file, because the useful
                    # message is often several lines above the traceback tail
                    # a one-line summary would keep: a fanout arm that dies
                    # reports the abort, not the cause.
                    lines = (stderr or "").strip().splitlines()
                    last_err = lines[-1] if lines else f"rc={proc.returncode}"
                    if stderr:
                        err_dir = out_dir / ".errors"
                        err_dir.mkdir(parents=True, exist_ok=True)
                        err_file = err_dir / f"{pid.lower()}_run{run_no}.err"
                        err_file.write_text(stderr, encoding="utf-8")
                        last_err = f"{last_err} [full stderr: {err_file}]"
            finally:
                with active_lock:
                    active_procs.discard(proc)
            if attempt < retries and not interrupted.is_set():
                time.sleep(5 * (attempt + 1))
        return pid, run_no, False, last_err
    finally:
        partial.unlink(missing_ok=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path,
                    default=Path(os.environ.get("WG21_DATA_DIR", "")),
                    help="paperstore workspace (default: $WG21_DATA_DIR)")
    ap.add_argument("--out-dir", type=Path, default=Path("papergate-out"))
    ap.add_argument("--prompt", type=Path, default=Path(PROMPT_DEFAULT))
    ap.add_argument("--runs", type=int, default=5, help="runs per paper")
    ap.add_argument("--jobs", type=int, default=5, help="concurrent runs")
    ap.add_argument("--only", metavar="PAPER_ID",
                    help="run just this one paper (e.g. P1234R0)")
    ap.add_argument("--timeout", type=int, default=1800, help="seconds per run")
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--keep-stores", action="store_true",
                    help=f"also extract {', '.join(DEBUG_OUTPUTS)} per run "
                         f"into <out-dir>/.stores/ for debugging")
    ap.add_argument("--promptforge-bin", type=Path,
                    default=Path(PROMPTFORGE_BIN_DEFAULT))
    ap.add_argument("--gateway-bin", type=Path, default=Path(GATEWAY_BIN_DEFAULT))
    ap.add_argument("--gateway-config", type=Path,
                    default=Path(GATEWAY_CONFIG_DEFAULT))
    ap.add_argument("--gateway-profile", default="runpod",
                    help="profile the gateway boots with (required by the gateway)")
    ap.add_argument("--gateway-url", default=GATEWAY_URL_DEFAULT)
    args = ap.parse_args()

    if not args.data_dir or not (args.data_dir / "paperstore.db").is_file():
        ap.error("paperstore.db not found; set --data-dir or $WG21_DATA_DIR")
    if not args.prompt.is_file():
        ap.error(f"prompt not found: {args.prompt}")
    for label, binary in (("promptforge", args.promptforge_bin),
                          ("gateway", args.gateway_bin)):
        if not os.access(binary, os.X_OK):
            ap.error(f"{label} binary not executable: {binary}")
    if not os.environ.get("VLLM_DEEPSEEK_API_KEY"):
        ap.error("VLLM_DEEPSEEK_API_KEY is not set; the gateway needs it "
                 "for the RunPod endpoint")

    papers = list_2026_papers(args.data_dir / "paperstore.db")
    if args.only:
        wanted = args.only.strip().upper()
        papers = [(pid, md) for pid, md in papers if pid == wanted]
        if not papers:
            ap.error(f"{wanted} is not a 2026 paper with converted markdown")
    if not papers:
        print("no 2026 papers with converted markdown found", file=sys.stderr)
        return 1
    total = len(papers) * args.runs
    print(f"{len(papers)} papers x {args.runs} runs = {total} runs, "
          f"{args.jobs} at a time")

    # One gateway for the whole batch, with a generated bearer known only to
    # this process and its children. Gateway output goes to a log file so its
    # progress bar and INFO lines never drown the run progress below.
    args.out_dir.mkdir(parents=True, exist_ok=True)
    gw_log_path = args.out_dir / "gateway.log"
    gw_log = open(gw_log_path, "w")
    token = secrets.token_hex(16)
    gateway_proc = subprocess.Popen(
        [str(args.gateway_bin), "--config", str(args.gateway_config),
         "--profile", args.gateway_profile, "--no-tray"],
        env=dict(os.environ, PROMPTFORGE_GATEWAY_API_KEY=token),
        stdout=gw_log, stderr=subprocess.STDOUT)
    failures: list[tuple[str, int, str]] = []
    done = 0
    pool = ThreadPoolExecutor(max_workers=args.jobs)
    try:
        wait_for_gateway(args.gateway_url, token, gateway_proc, gw_log_path)
        print(f"gateway up at {args.gateway_url} (pid {gateway_proc.pid}, "
              f"log: {gw_log_path})", flush=True)

        child_env = dict(os.environ,
                         PROMPTFORGE_GATEWAY_URL=args.gateway_url,
                         PROMPTFORGE_GATEWAY_API_KEY=token)

        started = time.monotonic()
        futures = [
            pool.submit(run_one, args.prompt, pid, run_no, md,
                        args.out_dir, child_env, args.promptforge_bin,
                        args.timeout, args.retries, args.keep_stores)
            for pid, md in papers
            for run_no in range(1, args.runs + 1)
        ]
        for fut in as_completed(futures):
            pid, run_no, ok, msg = fut.result()
            done += 1
            elapsed = time.monotonic() - started
            eta = (elapsed / done) * (total - done)
            print(f"[{done}/{total}] {pid} run{run_no}: "
                  f"{'ok' if ok else 'FAILED'} ({msg}) "
                  f"- elapsed {fmt_dur(elapsed)}, eta {fmt_dur(eta)}",
                  flush=True)
            if not ok:
                failures.append((pid, run_no, msg))
    except KeyboardInterrupt:
        interrupted.set()
        print("\ninterrupted - killing in-flight runs; completed outputs "
              "are kept", file=sys.stderr, flush=True)
        with active_lock:
            for proc in list(active_procs):
                proc.terminate()
        failures.append(("*", 0, "interrupted"))
    finally:
        pool.shutdown(wait=True, cancel_futures=True)
        gateway_proc.terminate()
        try:
            gateway_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            gateway_proc.kill()
        gw_log.close()

    print(f"\n{total - len(failures)}/{total} succeeded")
    if failures:
        for pid, run_no, msg in failures:
            print(f"  failed: {pid} run{run_no}: {msg}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
