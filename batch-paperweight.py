#!/usr/bin/env python3
"""Batch-run the paperweight prompt over every 2026 paper in the paperstore.

Each paper is run N times (default 5). One promptforge-gateway is started for
the whole batch and torn down at the end. Each run invokes
`paperweight <PID> --prompt <prompt> --output <file>`, which loads the paper's
markdown from the paperstore named by WG21_DATA_DIR (set from --data-dir) and
writes the prompt's report to paperweight_<pid>_run<N>.md in the output
directory. Credentials live only in the process environment: the gateway
bearer is generated per invocation and VLLM_DEEPSEEK_API_KEY is inherited.

Gateway output goes to <out-dir>/gateway.log, not the terminal. Ctrl-C
terminates in-flight runs immediately; completed outputs are kept, so
re-running the same command resumes where the batch left off.
"""

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

PAPERGATE_DIR = Path("/code/wg21-papergate")
PAPERFLOW_DIR = Path("/code/wg21-paperflow")
PROMPT_DEFAULT = PAPERFLOW_DIR / "crates" / "paperweight" / "paperweight_CALIBRATION.md"
GATEWAY_CONFIG_DEFAULT = Path(__file__).resolve().parent / "batch-paperweight-gateway.toml"
PAPERWEIGHT_BIN_DEFAULT = PAPERFLOW_DIR / "target" / "release" / "paperweight"
DATA_DIR_DEFAULT = PAPERFLOW_DIR / "data"
OUT_DIR_DEFAULT = PAPERGATE_DIR / "paperweight-out"
GATEWAY_BIN_DEFAULT = Path("/code/promptforge/target/release/promptforge-gateway")
GATEWAY_PROFILE_DEFAULT = "runpod"
GATEWAY_URL_DEFAULT = "http://127.0.0.1:8082/v1"

# In-flight paperweight processes, tracked so Ctrl-C can kill them
# immediately instead of waiting for the executor to drain.
active_procs: set[subprocess.Popen[str]] = set()
active_lock = threading.Lock()
interrupted = threading.Event()


def fmt_dur(seconds: float) -> str:
    """Format a duration as minutes, or as hours once it reaches two hours."""
    minutes = seconds / 60
    return f"{minutes:.0f}m" if minutes < 120 else f"{minutes / 60:.1f}h"


def list_papers(db_path: Path, only: str | None) -> list[str]:
    """List the paper ids to run, in paper id order.

    Papers whose markdown file is recorded but missing are skipped with a
    warning, so they do not fail every run.

    Args:
        db_path: The paperstore database.
        only: A single paper id to run, of any year. Defaults to every 2026
            paper with converted markdown.

    Returns:
        The paper ids whose markdown exists on disk.
    """
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        if only:
            rows = conn.execute(
                "SELECT paper_id, markdown_path FROM papers "
                "WHERE paper_id = ? AND markdown_path != ''", (only,)
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT paper_id, markdown_path FROM papers "
                "WHERE year = '2026' AND markdown_path != '' ORDER BY paper_id"
            ).fetchall()
    finally:
        conn.close()
    papers = []
    for pid, md in rows:
        if Path(md).is_file():
            papers.append(pid)
        else:
            print(f"warning: {pid} markdown_path is set but the file is gone; "
                  f"skipped", file=sys.stderr)
    return papers


def wait_for_gateway(url: str, token: str, proc: subprocess.Popen[bytes],
                     log_path: Path, timeout: float = 120.0) -> None:
    """Block until the gateway answers its model list.

    Raises:
        RuntimeError: If the gateway exits during startup or is not ready
            within `timeout` seconds.
    """
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


def run_one(prompt: Path, pid: str, run_no: int, out_dir: Path,
            env: dict[str, str], paperweight_bin: Path, model: str | None,
            timeout: int, retries: int) -> tuple[str, int, bool, str]:
    """Run one (paper, run) job, skipping it when its report already exists.

    On failure the run's full stderr is written to
    <out_dir>/.errors/<pid>_run<N>.err.

    Returns:
        The paper id, the run number, whether the run succeeded, and a
        one-line status message.
    """
    out_file = out_dir / f"paperweight_{pid.lower()}_run{run_no}.md"
    if out_file.exists():
        return pid, run_no, True, "skipped (exists)"
    if interrupted.is_set():
        return pid, run_no, False, "interrupted"

    # The report lands on a .partial path first so an interrupted write can
    # never look like a finished run to the skip-if-exists check above.
    partial = out_file.with_name(out_file.name + ".partial")
    cmd = [str(paperweight_bin), pid,
           "--prompt", str(prompt),
           "--output", str(partial)]
    if model:
        cmd += ["--model", model]

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
                    last_err = "run succeeded but the report file was not written"
                else:
                    # The useful message is often several lines above the
                    # last one: a fanout arm that dies reports the abort, not
                    # the cause.
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
    """Run the batch and return the process exit code."""
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", type=Path,
                    default=Path(os.environ.get("WG21_DATA_DIR") or DATA_DIR_DEFAULT),
                    help="paperstore workspace (default: $WG21_DATA_DIR, "
                         f"else {DATA_DIR_DEFAULT})")
    ap.add_argument("--out-dir", type=Path, default=OUT_DIR_DEFAULT)
    ap.add_argument("--prompt", type=Path, default=PROMPT_DEFAULT)
    ap.add_argument("--runs", type=int, default=5, help="runs per paper")
    ap.add_argument("--jobs", type=int, default=5, help="concurrent runs")
    ap.add_argument("--only", metavar="PAPER_ID",
                    help="run just this one paper, of any year (e.g. P0085R3); "
                         "default: every 2026 paper")
    ap.add_argument("--timeout", type=int, default=1800, help="seconds per run")
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--model", metavar="ID",
                    help="gateway model id the prompt binds to (default: the "
                         "first chat model the gateway lists)")
    ap.add_argument("--paperweight-bin", type=Path, default=PAPERWEIGHT_BIN_DEFAULT)
    ap.add_argument("--gateway-bin", type=Path, default=GATEWAY_BIN_DEFAULT)
    ap.add_argument("--gateway-config", type=Path, default=GATEWAY_CONFIG_DEFAULT)
    ap.add_argument("--gateway-profile", default=GATEWAY_PROFILE_DEFAULT,
                    help="profile the gateway boots with")
    ap.add_argument("--gateway-url", default=GATEWAY_URL_DEFAULT,
                    help="must match the bind address in --gateway-config")
    args = ap.parse_args()

    data_dir: Path = args.data_dir.resolve()
    out_dir: Path = args.out_dir.resolve()
    prompt: Path = args.prompt.resolve()
    if not (data_dir / "paperstore.db").is_file():
        ap.error(f"paperstore.db not found in {data_dir}; set --data-dir")
    if not prompt.is_file():
        ap.error(f"prompt not found: {prompt}")
    if not args.gateway_config.is_file():
        ap.error(f"gateway config not found: {args.gateway_config}")
    for label, binary in (("paperweight", args.paperweight_bin),
                          ("gateway", args.gateway_bin)):
        if not os.access(binary, os.X_OK):
            ap.error(f"{label} binary not executable: {binary}")
    if not os.environ.get("VLLM_DEEPSEEK_API_KEY"):
        ap.error("VLLM_DEEPSEEK_API_KEY is not set; the gateway needs it "
                 "for the RunPod endpoint")

    wanted = args.only.strip().upper() if args.only else None
    papers = list_papers(data_dir / "paperstore.db", wanted)
    if wanted and not papers:
        ap.error(f"{wanted} has no converted markdown in the paperstore")
    if not papers:
        print("no 2026 papers with converted markdown found", file=sys.stderr)
        return 1
    total = len(papers) * args.runs
    print(f"{len(papers)} papers x {args.runs} runs = {total} runs, "
          f"{args.jobs} at a time")

    # The gateway allows one instance per home directory, so it gets a
    # private HOME to coexist with a gateway the user already has running.
    out_dir.mkdir(parents=True, exist_ok=True)
    gateway_home = out_dir / ".gateway-home"
    gateway_home.mkdir(exist_ok=True)
    gw_log_path = out_dir / "gateway.log"
    token = secrets.token_hex(16)
    failures: list[tuple[str, int, str]] = []
    done = 0
    with gw_log_path.open("w") as gw_log:
        gateway_proc = subprocess.Popen(
            [str(args.gateway_bin), "--config", str(args.gateway_config.resolve()),
             "--profile", args.gateway_profile, "--no-tray"],
            env=dict(os.environ, HOME=str(gateway_home),
                     PROMPTFORGE_GATEWAY_API_KEY=token),
            stdout=gw_log, stderr=subprocess.STDOUT)
        pool = ThreadPoolExecutor(max_workers=args.jobs)
        try:
            wait_for_gateway(args.gateway_url, token, gateway_proc, gw_log_path)
            print(f"gateway up at {args.gateway_url} (pid {gateway_proc.pid}, "
                  f"log: {gw_log_path})", flush=True)

            child_env = dict(os.environ,
                             PROMPTFORGE_GATEWAY_URL=args.gateway_url,
                             PROMPTFORGE_GATEWAY_API_KEY=token,
                             WG21_DATA_DIR=str(data_dir))

            started = time.monotonic()
            futures = [
                pool.submit(run_one, prompt, pid, run_no, out_dir, child_env,
                            args.paperweight_bin, args.model, args.timeout,
                            args.retries)
                for pid in papers
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

    print(f"\n{total - len(failures)}/{total} succeeded")
    if failures:
        for pid, run_no, msg in failures:
            print(f"  failed: {pid} run{run_no}: {msg}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
