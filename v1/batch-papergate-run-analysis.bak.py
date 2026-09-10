#!/usr/bin/env python3
"""Summarize verdict consistency across papergate batch runs.

Reads every papergate_<pid>_run<N>.md in the output directory (default:
papergate-out), parses the "Verdict:" line from each report, and writes a
markdown report of summary stats to <out-dir>/summary.md, aimed at the
question: are verdicts consistent across runs?

Verdict line shapes seen in the wild:
    Verdict: Strong (8/14, close to Adequate)
    Verdict: Excellent (14/14)
    Verdict: n/a

Usage: summarize-batch-papergate-run.py [out-dir]
"""

from __future__ import annotations

import re
import statistics
import sys
from collections import Counter
from pathlib import Path

# Ordered verdict scale; n/a is tracked separately (not on the scale).
LABELS = ["None", "Weak", "Adequate", "Strong", "Excellent"]
LABEL_RANK = {label: i for i, label in enumerate(LABELS)}

FILE_RE = re.compile(r"^papergate_([a-z0-9]+)_run(\d+)\.md$")
VERDICT_RE = re.compile(
    r"^Verdict:\s*(?P<label>n/a|\w+)"
    r"(?:\s*\((?P<score>\d+)\s*/\s*(?P<max>\d+)"
    r"(?:\s*,\s*close to\s*(?P<close>\w+))?\))?"
    r"\s*$"
)


class Run:
    def __init__(self, path: Path, pid: str, run_no: int):
        self.path = path
        self.pid = pid
        self.run_no = run_no
        self.label: str | None = None      # e.g. "Strong", or "n/a"
        self.score: int | None = None      # numeric part of (x/14)
        self.max_score: int | None = None
        self.close_to: str | None = None
        self.parse_error: str | None = None
        self._parse()

    def _parse(self) -> None:
        try:
            first = self.path.read_text(errors="replace").splitlines()[0]
        except IndexError:
            self.parse_error = "empty file"
            return
        except OSError as exc:
            self.parse_error = f"unreadable: {exc}"
            return
        m = VERDICT_RE.match(first.strip())
        if not m:
            self.parse_error = f"no verdict line: {first.strip()[:60]!r}"
            return
        self.label = m.group("label")
        if m.group("score") is not None:
            self.score = int(m.group("score"))
            self.max_score = int(m.group("max"))
        if m.group("close"):
            self.close_to = m.group("close")

    @property
    def is_na(self) -> bool:
        return self.label == "n/a"

    @property
    def on_scale(self) -> bool:
        return self.label in LABEL_RANK


def fmt_verdict(run: Run) -> str:
    if run.parse_error:
        return f"PARSE-ERROR({run.parse_error})"
    if run.is_na:
        return "n/a"
    if run.score is not None:
        return f"{run.label}({run.score})"
    return str(run.label)


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("papergate-out")
    if not out_dir.is_dir():
        print(f"error: {out_dir} is not a directory", file=sys.stderr)
        return 1

    runs: list[Run] = []
    skipped: list[Path] = []
    for path in sorted(out_dir.glob("papergate_*_run*.md")):
        m = FILE_RE.match(path.name)
        if not m:
            skipped.append(path)
            continue
        runs.append(Run(path, m.group(1).upper(), int(m.group(2))))

    if not runs:
        print(f"no papergate_*_run*.md files found in {out_dir}",
              file=sys.stderr)
        return 1

    by_paper: dict[str, list[Run]] = {}
    for run in runs:
        by_paper.setdefault(run.pid, []).append(run)
    for prs in by_paper.values():
        prs.sort(key=lambda r: r.run_no)

    parse_errors = [r for r in runs if r.parse_error]
    good = [r for r in runs if not r.parse_error]
    scored = [r for r in good if r.score is not None]
    na_runs = [r for r in good if r.is_na]
    off_scale = [r for r in good
                 if not r.is_na and not r.on_scale and r.score is None]

    md: list[str] = []
    md.append("# Papergate batch verdict consistency summary")
    md.append("")
    md.append(f"- directory scanned: `{out_dir}`")
    md.append(f"- report files: {len(runs)}"
              + (f" (+{len(skipped)} non-matching filenames skipped)"
                 if skipped else ""))
    md.append(f"- papers: {len(by_paper)}")
    runs_per_paper = Counter(len(prs) for prs in by_paper.values())
    md.append("- runs per paper: "
              + ", ".join(f"{n} runs x {c} papers"
                          for n, c in sorted(runs_per_paper.items())))
    md.append(f"- parse errors: {len(parse_errors)}")
    md.append(f"- n/a verdicts: {len(na_runs)} "
              f"({100 * len(na_runs) / len(good):.1f}% of parsed)")
    if off_scale:
        md.append(f"- WARNING: {len(off_scale)} verdicts with an "
                  f"unrecognized label: "
                  f"{sorted({r.label for r in off_scale})}")

    md.append("")
    md.append("## Overall verdict distribution")
    md.append("")
    md.append("| Verdict | Count | Share |")
    md.append("|---------|------:|------:|")
    label_counts = Counter(r.label for r in good)
    for label in LABELS + ["n/a"]:
        c = label_counts.get(label, 0)
        if c:
            md.append(f"| {label} | {c} | {100 * c / len(good):.1f}% |")
    for label, c in sorted(label_counts.items()):
        if label not in LABELS and label != "n/a":
            md.append(f"| {label} (unrecognized) | {c} | "
                      f"{100 * c / len(good):.1f}% |")
    if scored:
        scores = [r.score for r in scored]
        md.append("")
        md.append(f"Score (x/{scored[0].max_score}) over {len(scored)} "
                  f"scored runs: min {min(scores)}, max {max(scores)}, "
                  f"mean {statistics.fmean(scores):.2f}, "
                  f"median {statistics.median(scores):.0f}, "
                  f"stdev {statistics.pstdev(scores):.2f}")
        score_counts = Counter(scores)
        md.append("")
        md.append("Score histogram: "
                  + ", ".join(f"{s}:{c}"
                              for s, c in sorted(score_counts.items())))

    md.append("")
    md.append("## Per-paper detail")
    md.append("")
    md.append("Runs in run-number order. sprd = score spread (max-min).")
    md.append("")
    md.append("| Paper | Runs | Verdicts | Labels | Sprd | Range | Stdev "
              "| Consistent? |")
    md.append("|-------|-----:|----------|-------:|-----:|-------|------:"
              "|-------------|")

    # per-paper consistency records for the aggregate section
    # (pid, n_runs, n_labels, n_scored, score_range, score_stdev, category)
    records = []
    for pid in sorted(by_paper):
        prs = by_paper[pid]
        parsed = [r for r in prs if not r.parse_error]
        verdicts = " ".join(fmt_verdict(r) for r in prs)
        labels = {r.label for r in parsed}
        pscores = [r.score for r in parsed if r.score is not None]
        n_na = sum(1 for r in parsed if r.is_na)
        n_err = sum(1 for r in prs if r.parse_error)

        score_range = max(pscores) - min(pscores) if len(pscores) >= 2 else 0
        score_stdev = (statistics.pstdev(pscores) if len(pscores) >= 2
                       else 0.0)

        # categorize consistency
        if n_err:
            cat = f"PARSE-ERROR x{n_err}"
        elif len(parsed) < 2:
            cat = "only 1 run"
        elif len(labels) == 1:
            cat = ("uniform " + ("(all n/a)" if n_na == len(parsed)
                                 else "(all identical)"
                                 if len(pscores) == len(parsed)
                                 and len(set(pscores)) == 1
                                 else "(same label)"))
        elif n_na and len(labels - {"n/a"}) == 1:
            cat = "split n/a vs " + next(iter(labels - {"n/a"}))
        else:
            scale_labels = [l for l in labels if l in LABEL_RANK]
            if len(scale_labels) >= 2:
                ranks = [LABEL_RANK[l] for l in scale_labels]
                steps = max(ranks) - min(ranks)
                cat = f"DISAGREE ({steps}-step spread)"
            else:
                cat = "DISAGREE"

        records.append((pid, len(prs), len(labels), len(pscores),
                        score_range, score_stdev, cat))
        rng = f"{min(pscores)}-{max(pscores)}" if pscores else "-"
        md.append(f"| {pid} | {len(prs)} | {verdicts} | {len(labels)} "
                  f"| {score_range} | {rng} | {score_stdev:.2f} | {cat} |")

    md.append("")
    md.append("## Consistency aggregates")
    md.append("")
    uniform = [rec for rec in records
               if rec[2] == 1 and rec[6].startswith("uniform")]
    uniform_identical = [rec for rec in records
                         if rec[6] == "uniform (all identical)"]
    uniform_na = [rec for rec in records if rec[6] == "uniform (all n/a)"]
    disagree = [rec for rec in records if rec[6].startswith("DISAGREE")]
    split_na = [rec for rec in records if rec[6].startswith("split n/a")]
    partial = [rec for rec in records if rec[6] == "only 1 run"
               or rec[6].startswith("PARSE-ERROR")]

    n = len(records)
    md.append(f"- papers with all runs same verdict label: "
              f"**{len(uniform)}/{n} ({100 * len(uniform) / n:.0f}%)**")
    md.append(f"  - of which every run identical score: "
              f"{len(uniform_identical)}")
    md.append(f"  - of which uniformly n/a: {len(uniform_na)}")
    md.append(f"- papers with label disagreement: "
              f"**{len(disagree)}/{n} ({100 * len(disagree) / n:.0f}%)**")
    md.append(f"- papers split n/a vs a real verdict: {len(split_na)}")
    if partial:
        md.append(f"- papers with missing/unparseable runs: {len(partial)}")

    scored_recs = [rec for rec in records if rec[3] >= 2]
    ranges = [rec[4] for rec in scored_recs]
    stdevs = [rec[5] for rec in scored_recs]
    if ranges:
        md.append("")
        md.append(f"Per-paper score range (max-min) over {len(ranges)} "
                  f"papers with >=2 scored runs:")
        md.append("")
        md.append(f"- mean {statistics.fmean(ranges):.2f}, "
                  f"median {statistics.median(ranges):.1f}, "
                  f"max {max(ranges)}")
        md.append(f"- papers with score range 0: "
                  f"{sum(1 for x in ranges if x == 0)}")
        md.append(f"- papers with score range <=1: "
                  f"{sum(1 for x in ranges if x <= 1)}")
        md.append(f"- papers with score range <=2: "
                  f"{sum(1 for x in ranges if x <= 2)}")
        md.append(f"- papers with score range >=3: "
                  f"{sum(1 for x in ranges if x >= 3)}")
        md.append(f"- per-paper score stdev: mean "
                  f"{statistics.fmean(stdevs):.2f}, max {max(stdevs):.2f}")

    if disagree:
        md.append("")
        md.append("## Papers with label disagreement")
        md.append("")
        md.append("| Paper | Category | Score range | Stdev | Verdicts |")
        md.append("|-------|----------|------------:|------:|----------|")
        for pid, _, _, _, srange, sstdev, cat in disagree:
            prs = [r for r in by_paper[pid] if not r.parse_error]
            verdicts = " ".join(fmt_verdict(r) for r in prs)
            md.append(f"| {pid} | {cat} | {srange} | {sstdev:.2f} "
                      f"| {verdicts} |")
    if split_na:
        md.append("")
        md.append("## Papers split between n/a and a real verdict")
        md.append("")
        for pid, _, _, _, _, _, cat in split_na:
            prs = [r for r in by_paper[pid] if not r.parse_error]
            verdicts = " ".join(fmt_verdict(r) for r in prs)
            md.append(f"- {pid} — {cat} [{verdicts}]")

    if parse_errors:
        md.append("")
        md.append("## Files that failed to parse")
        md.append("")
        for r in parse_errors:
            md.append(f"- `{r.path.name}`: {r.parse_error}")
    if skipped:
        md.append("")
        md.append("## Non-matching filenames skipped")
        md.append("")
        for p in skipped:
            md.append(f"- `{p.name}`")

    md.append("")
    out_path = out_dir / "summary.md"
    out_path.write_text("\n".join(md))
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
