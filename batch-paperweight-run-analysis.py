# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib>=3.9",
#     "numpy>=2",
#     "playwright>=1.40",
#     "nbconvert[webpdf]",
# ]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import re
    import sqlite3
    import statistics
    from collections import Counter
    from dataclasses import dataclass
    from pathlib import Path

    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.axes import Axes

    return Counter, Path, dataclass, mo, np, plt, re, sqlite3, statistics


@app.cell
def _(mo):
    mo.md("""
    # Paperweight batch run analysis
    """)
    return


@app.cell
def _(mo):
    OUT_DIR = "/code/wg21-papergate/paperweight-out-v8"
    DB_PATH = "/code/wg21-paperflow/data/paperstore.db"
    mo.md(f"""
    - **Report directory:** `{OUT_DIR}`
    - **Paperstore DB:** `{DB_PATH}`
    """)
    return DB_PATH, OUT_DIR


@app.cell
def _(Path, dataclass, re):
    LABELS = ["None", "Weak", "Adequate", "Strong", "Excellent"]
    FILE_RE = re.compile(r"^paperweight_([a-z0-9]+)_run(\d+)\.md$")
    VERDICT_RE = re.compile(
        r"^Verdict:\s*(?P<label>n/a|\w+(?: to \w+)?)"
        r"(?:\s*\((?P<score>\d+)\s*/\s*(?P<max>\d+)\))?"
        r"\s*$"
    )

    @dataclass
    class Run:
        pid: str
        run_no: int
        label: str | None
        score: int | None
        max_score: int | None
        parse_error: str | None

        @property
        def is_na(self) -> bool:
            return self.label == "n/a"

        @property
        def bands(self) -> frozenset[str]:
            """Every band the label covers: one for a plain label, the whole
            range for an "X to Y" span, none for n/a or an unknown label."""
            if self.label is None or self.is_na:
                return frozenset()
            low, _, high = self.label.partition(" to ")
            high = high or low
            if low not in LABELS or high not in LABELS:
                return frozenset()
            return frozenset(
                LABELS[LABELS.index(low):LABELS.index(high) + 1])

    def parse_report(path: Path, pid: str, run_no: int) -> Run:
        """Parse the Verdict line (first line) of one report file."""
        try:
            with path.open(errors="replace") as handle:
                first = handle.readline().strip()
        except OSError as exc:
            return Run(pid, run_no, None, None, None,
                       f"unreadable: {exc}")
        if not first:
            return Run(pid, run_no, None, None, None, "empty file")
        match = VERDICT_RE.match(first)
        if not match:
            return Run(pid, run_no, None, None, None,
                       f"no verdict line: {first[:60]!r}")
        score = match.group("score")
        max_score = match.group("max")
        return Run(
            pid=pid,
            run_no=run_no,
            label=match.group("label"),
            score=int(score) if score is not None else None,
            max_score=int(max_score) if max_score is not None else None,
            parse_error=None,
        )

    def load_runs(out_dir: Path) -> list[Run]:
        """Parse every paperweight_<pid>_run<N>.md report in out_dir."""
        runs: list[Run] = []
        for path in sorted(out_dir.glob("paperweight_*_run*.md")):
            match = FILE_RE.match(path.name)
            if match:
                runs.append(
                    parse_report(path, match.group(1).upper(),
                                 int(match.group(2)))
                )
        return runs

    def fmt_verdict(run: Run) -> str:
        if run.parse_error:
            return f"PARSE-ERROR({run.parse_error})"
        if run.is_na:
            return "n/a"
        if run.score is not None:
            return f"{run.label}({run.score})"
        return str(run.label)

    return LABELS, Run, fmt_verdict, load_runs


@app.cell
def _(OUT_DIR, Path, load_runs, mo):
    runs = load_runs(Path(OUT_DIR))
    # Every cell below reads `runs`, and all of them divide by some count of
    # it, so an empty directory is reported once here rather than as an
    # arithmetic error further down.
    mo.stop(
        not runs,
        mo.md(f"No reports in `{OUT_DIR}` yet. Run the batch, or "
              f"set OUT_DIR to a directory that has some."),
    )
    return (runs,)


@app.cell
def _(DB_PATH, Path, sqlite3):
    """Expected paper list, queried exactly like batch-paperweight.py."""
    db_error: str | None = None
    expected_pids: list[str] = []
    try:
        conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
        try:
            paper_rows = conn.execute(
                "SELECT paper_id, markdown_path FROM papers "
                "WHERE year = '2026' AND markdown_path != '' "
                "ORDER BY paper_id"
            ).fetchall()
        finally:
            conn.close()
    except (OSError, sqlite3.Error) as exc:
        db_error = f"paperstore DB unreadable: {exc}"
    else:
        expected_pids = [pid for pid, md in paper_rows
                         if Path(md).is_file()]
    return db_error, expected_pids


@app.cell
def _(Run, dataclass, statistics):
    @dataclass
    class PaperStats:
        pid: str
        runs: list[Run]
        n_labels: int
        n_scored: int
        score_range: int
        score_stdev: float
        mean_score: float | None
        category: str

    def categorize(paper_runs: list[Run]) -> str:
        if any(r.parse_error for r in paper_runs):
            return "parse error"
        parsed = [r for r in paper_runs if r.parse_error is None]
        if len(parsed) < 2:
            return "only 1 run"
        labels = {r.label for r in parsed}
        scores = [r.score for r in parsed if r.score is not None]
        n_na = sum(1 for r in parsed if r.is_na)
        if len(labels) == 1:
            if n_na == len(parsed):
                return "uniform (all n/a)"
            if len(scores) == len(parsed) and len(set(scores)) == 1:
                return "uniform (all identical)"
            return "uniform (same label)"
        if n_na:
            return "split n/a vs verdict"
        # Different labels that still share a band, e.g. "Adequate" and
        # "Adequate to Strong", are a span narrowing or widening between
        # runs, not a contradiction.
        if frozenset.intersection(*(r.bands for r in parsed)):
            return "overlapping spans"
        return "DISAGREE"

    def paper_stats(all_runs: list[Run]) -> list[PaperStats]:
        by_pid: dict[str, list[Run]] = {}
        for run in all_runs:
            by_pid.setdefault(run.pid, []).append(run)
        result: list[PaperStats] = []
        for pid, pid_runs in sorted(by_pid.items()):
            pid_runs.sort(key=lambda r: r.run_no)
            parsed = [r for r in pid_runs if r.parse_error is None]
            scores = [r.score for r in parsed if r.score is not None]
            result.append(
                PaperStats(
                    pid=pid,
                    runs=pid_runs,
                    n_labels=len({r.label for r in parsed}),
                    n_scored=len(scores),
                    score_range=(max(scores) - min(scores)
                                 if len(scores) >= 2 else 0),
                    score_stdev=(statistics.pstdev(scores)
                                 if len(scores) >= 2 else 0.0),
                    mean_score=(statistics.fmean(scores) if scores else None),
                    category=categorize(pid_runs),
                )
            )
        return result

    return (paper_stats,)


@app.cell
def _(expected_pids: list[str], paper_stats, runs):
    stats = paper_stats(runs)
    good_runs = [r for r in runs if r.parse_error is None]
    scored_runs = [r for r in good_runs if r.score is not None]
    na_runs = [r for r in good_runs if r.is_na]
    parse_errors = [r for r in runs if r.parse_error is not None]
    expected_runs = max(r.run_no for r in runs)
    present_pids = {p.pid for p in stats}
    missing_by_pid = {
        p.pid: sorted(set(range(1, expected_runs + 1))
                      - {r.run_no for r in p.runs})
        for p in stats
    }
    for pid in expected_pids:
        if pid not in present_pids:
            missing_by_pid[pid] = list(range(1, expected_runs + 1))
    missing_by_pid = {pid: m for pid, m in sorted(missing_by_pid.items())
                      if m}
    n_missing = sum(len(m) for m in missing_by_pid.values())
    n_expected_papers = len(expected_pids) if expected_pids else len(stats)
    return (
        expected_runs,
        good_runs,
        missing_by_pid,
        n_expected_papers,
        n_missing,
        na_runs,
        scored_runs,
        stats,
    )


@app.cell
def _(
    Counter,
    db_error: str | None,
    expected_runs,
    good_runs,
    missing_by_pid,
    mo,
    n_expected_papers,
    n_missing,
    na_runs,
    runs,
    scored_runs,
    statistics,
    stats,
):
    run_counts = Counter(len(p.runs) for p in stats)
    runs_per_paper = ", ".join(
        f"{n} runs x {c} papers" for n, c in sorted(run_counts.items())
    )
    scores = [r.score for r in scored_runs]
    if db_error is None:
        expected_line = (
            f"expected: **{n_expected_papers * expected_runs}** report "
            f"files across **{n_expected_papers}** papers "
            f"({expected_runs} runs x {n_expected_papers} papers, "
            f"from paperstore DB)"
        )
    else:
        expected_line = (
            f"expected: unknown — paperstore DB unreadable "
            f"({db_error}); papers with zero reports are invisible"
        )
    mo.md(
        f"""
        ## Batch overview

        - **{len(runs)}** report files across **{len(stats)}** papers ({runs_per_paper})
        - {expected_line}
        - missing: **{n_missing}** across **{len(missing_by_pid)}** papers
        - n/a verdicts: **{len(na_runs)}** ({100 * len(na_runs) / len(good_runs):.1f}% of parsed) — a triage turn that reads only the paper's front matter (title, abstract and anything before the first heading) classified it as not a proposal, so the criteria were not applied
        - score (x/{scored_runs[0].max_score}) over {len(scores)} scored runs: min {min(scores)}, max {max(scores)}, mean {statistics.fmean(scores):.2f}, median {statistics.median(scores):.0f}, stdev {statistics.pstdev(scores):.2f}

        **What the score is.** Each run grades the paper on 7 criteria:
        why it matters, who is affected, prior art and alternatives, why
        the standard, coordination and interoperability, why a library
        will not do, and implementation experience. The paper is split
        into units, one per H2 section plus the front matter (sections
        over 30,000 characters are split into parts), and every
        criterion is graded on every unit by 3 independent samples:
        0 (not addressed), 1 (asserted, with nothing supporting it) or
        2 (supported with specifics). A non-zero grade only stands if
        it is backed by a verbatim quote of 3–40 words found in the
        paper, and bookkeeping sections (revision history,
        acknowledgements, references, poll records, wording) are graded
        0 whatever they mention.

        A unit's grade is the mean of its 3 samples. A criterion's grade
        is the mean of its two best units, except implementation
        experience, which takes its single best unit, since one checkable
        pointer is enough. The score is the sum of the 7 criterion
        grades, a fraction from 0 to {scored_runs[0].max_score}, and the
        report shows it rounded to the nearest integer. The verdict
        label is a fixed lookup on that integer: None = 0, Weak <= 3,
        Adequate <= 7, Strong <= 11, Excellent <= 14.

        **Span labels.** The run also computes the total each of the 3
        samples would have produced alone. When those totals fall in
        different bands from the verdict's, the label becomes a span
        from the lowest band reached to the highest, e.g. "Adequate to
        Strong (7/14)". The number is still the verdict's own score, so
        it sits in one of the span's bands, not necessarily the first.
        """
    )
    return


@app.cell
def _(plt):
    plt.rcParams.update({
        "figure.facecolor": "#ffffff",
        "axes.facecolor": "#ffffff",
        "axes.edgecolor": "#cccccc",
        "axes.labelcolor": "#333333",
        "axes.grid": False,
        "grid.color": "#e5e5e5",
        "grid.linewidth": 0.7,
        "text.color": "#333333",
        "xtick.color": "#555555",
        "ytick.color": "#555555",
        "figure.dpi": 110,
        "savefig.facecolor": "#ffffff",
    })
    THEME = {
        "blue": "#4c72b0",
        "green": "#55a868",
        "lightgreen": "#8fbf9f",
        "orange": "#dd8452",
        "red": "#c44e52",
        "purple": "#8172b3",
        "gray": "#8c8c8c",
        "bad": "#e0e0e0",
    }
    VERDICT_COLORS = {
        "None": THEME["red"],
        "Weak": THEME["orange"],
        "Adequate": THEME["blue"],
        "Strong": THEME["green"],
        "Excellent": THEME["purple"],
        "n/a": THEME["gray"],
    }
    return THEME, VERDICT_COLORS


@app.cell
def _(mo):
    mo.md("""
    ## Verdicts and scores

    **Verdict distribution:** how many runs received each verdict label.
    Plain bands and "X to Y" spans are separate bars, ordered top to bottom
    by the bands they cover, so each span sits between the bands it joins.
    A span is colored like its lower band. n/a is last.
    """)
    return


@app.cell
def _(Counter, LABELS, THEME, VERDICT_COLORS, good_runs, plt):
    label_counts = Counter(r.label for r in good_runs)

    def label_order(label: str) -> tuple[int, int, int]:
        """Sort bands and "X to Y" spans by their bounds, n/a and unknowns last."""
        if label == "n/a":
            return (len(LABELS), 0, 0)
        low, _, high = label.partition(" to ")
        high = high or low
        if low in LABELS and high in LABELS:
            return (LABELS.index(low), LABELS.index(high), 0)
        return (len(LABELS), 1, 0)

    def label_color(label: str) -> str:
        """Color a span by its lower band."""
        return VERDICT_COLORS.get(label.partition(" to ")[0], THEME["red"])

    ordered_labels = sorted(label_counts, key=lambda lb: (label_order(lb), lb))
    label_fig, ax_labels = plt.subplots(
        figsize=(10, 0.4 * len(ordered_labels) + 1.2))
    label_bars = ax_labels.barh(
        ordered_labels,
        [label_counts[label] for label in ordered_labels],
        color=[label_color(label) for label in ordered_labels],
    )
    ax_labels.invert_yaxis()
    ax_labels.bar_label(label_bars, padding=3)
    ax_labels.margins(x=0.08)
    ax_labels.set_title(f"Verdict distribution ({len(good_runs)} parsed runs)")
    ax_labels.set_xlabel("runs")
    label_fig.tight_layout()
    label_fig
    return


@app.cell
def _(mo):
    mo.md("""
    **Score histogram:** how many scored runs received each score. This is
    the rounded integer shown on the verdict line; n/a runs have no score
    and are not counted.
    """)
    return


@app.cell
def _(Counter, THEME, plt, scored_runs):
    score_counts = Counter(r.score for r in scored_runs)
    score_fig, ax_scores = plt.subplots(figsize=(10, 4))
    score_xs = list(range(min(score_counts), max(score_counts) + 1))
    ax_scores.bar(score_xs, [score_counts.get(x, 0) for x in score_xs],
                  color=THEME["blue"])
    ax_scores.set_title(
        f"Score histogram ({len(scored_runs)} scored runs, "
        f"x/{scored_runs[0].max_score})"
    )
    ax_scores.set_xlabel("score")
    ax_scores.set_ylabel("runs")
    ax_scores.set_xticks(score_xs)
    score_fig.tight_layout()
    score_fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## Scores across runs

    One row per paper and one column per run, colored by the run's score.
    Papers are sorted by their mean score, lowest at the top. A row that
    changes color across runs is a paper whose score moves between runs;
    gray cells are n/a or missing runs.
    """)
    return


@app.cell
def _(THEME, np, plt, scored_runs, stats):
    papers_by_score = sorted(
        stats,
        key=lambda p: (p.mean_score is None,
                       p.mean_score if p.mean_score is not None else 0.0),
    )
    max_run = max(r.run_no for p in stats for r in p.runs)
    grid = np.full((len(papers_by_score), max_run), np.nan)
    for row, paper in enumerate(papers_by_score):
        for run in paper.runs:
            if run.score is not None:
                grid[row, run.run_no - 1] = run.score
    cmap = plt.colormaps["viridis"].copy()
    cmap.set_bad(THEME["bad"])

    heat_fig, ax = plt.subplots(figsize=(10, 4))
    image = ax.imshow(np.ma.masked_invalid(grid), aspect="auto", cmap=cmap,
                      vmin=0, vmax=scored_runs[0].max_score,
                      interpolation="nearest")
    ax.set_xticks(range(max_run), [str(i + 1) for i in range(max_run)])
    ax.set_xlabel("run #")
    ax.set_yticks([])
    ax.set_ylabel(f"{len(papers_by_score)} papers (sorted by mean score)")
    ax.grid(False)
    ax.set_title("Per-paper scores across runs — gray = n/a or missing")
    heat_fig.colorbar(image, ax=ax, label="score", shrink=0.6)
    heat_fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## Consistency between runs

    Every paper is run several times, and each paper is placed in exactly
    one category by comparing the verdict labels of its runs:

    - **uniform (all identical):** every run has the same label and the
      same score.
    - **uniform (same label):** every run has the same label, but the
      scores differ.
    - **uniform (all n/a):** every run classified the document as not a
      proposal.
    - **overlapping spans:** the labels differ, but there is at least one
      band that every run's label covers. For example, "Adequate",
      "Adequate to Strong" and "Weak to Adequate" all cover Adequate. The
      runs agree on that band and differ only in how wide the span is, so
      this is not counted as a disagreement.
    - **split n/a vs verdict:** some runs classified the document as not a
      proposal and others graded it.
    - **DISAGREE:** the labels differ and no single band is covered by
      every run, e.g. "Weak" in one run and "Strong" in another.
    - **only 1 run / parse error:** too few readable reports to compare.

    **Per-paper verdict consistency:** how many papers fall in each
    category.
    """)
    return


@app.cell
def _(Counter, THEME, plt, stats):
    CATEGORY_COLORS = {
        "uniform (all identical)": THEME["green"],
        "uniform (same label)": THEME["lightgreen"],
        "uniform (all n/a)": THEME["gray"],
        "overlapping spans": THEME["blue"],
        "split n/a vs verdict": THEME["orange"],
        "DISAGREE": THEME["red"],
        "only 1 run": THEME["gray"],
        "parse error": THEME["red"],
    }
    category_counts = Counter(p.category for p in stats)
    categories = [c for c in CATEGORY_COLORS if category_counts.get(c)]

    consistency_fig, ax_cat = plt.subplots(figsize=(10, 4))
    category_bars = ax_cat.barh(
        categories,
        [category_counts[c] for c in categories],
        color=[CATEGORY_COLORS[c] for c in categories],
    )
    ax_cat.invert_yaxis()
    ax_cat.bar_label(category_bars, padding=3)
    ax_cat.margins(x=0.08)
    ax_cat.set_title(f"Per-paper verdict consistency ({len(stats)} papers)")
    ax_cat.set_xlabel("papers")
    consistency_fig.tight_layout()
    consistency_fig
    return


@app.cell
def _(mo):
    mo.md("""
    **Score spread per paper:** each paper's highest run score minus its
    lowest, over papers with at least two scored runs.
    """)
    return


@app.cell
def _(Counter, THEME, plt, stats):
    spread_counts = Counter(p.score_range for p in stats if p.n_scored >= 2)
    n_spread = sum(spread_counts.values())
    spread_fig, ax_spread = plt.subplots(figsize=(10, 4))
    spread_xs = list(range(max(spread_counts) + 1))
    ax_spread.bar(spread_xs, [spread_counts.get(x, 0) for x in spread_xs],
                  color=THEME["orange"])
    ax_spread.set_title(
        f"Score spread (max-min) per paper "
        f"({n_spread} papers with >=2 scored runs)"
    )
    ax_spread.set_xlabel("score spread")
    ax_spread.set_ylabel("papers")
    ax_spread.set_xticks(spread_xs)
    spread_fig.tight_layout()
    spread_fig
    return


@app.cell
def _(mo, statistics, stats):
    n_papers = len(stats)
    uniform = [p for p in stats if p.category.startswith("uniform")]
    identical = [p for p in stats if p.category == "uniform (all identical)"]
    all_na = [p for p in stats if p.category == "uniform (all n/a)"]
    overlapping = [p for p in stats if p.category == "overlapping spans"]
    disagree = [p for p in stats if p.category == "DISAGREE"]
    split = [p for p in stats if p.category == "split n/a vs verdict"]
    partial = [p for p in stats
               if p.category in ("only 1 run", "parse error")]
    ranges = [p.score_range for p in stats if p.n_scored >= 2]
    stdevs = [p.score_stdev for p in stats if p.n_scored >= 2]
    mo.md(
        f"""
        ## Consistency aggregates

        - all runs same verdict label: **{len(uniform)}/{n_papers} ({100 * len(uniform) / n_papers:.0f}%)** — of which {len(identical)} identical scores, {len(all_na)} uniformly n/a
        - different labels that all share a band (e.g. "Adequate" and "Adequate to Strong"): **{len(overlapping)}/{n_papers} ({100 * len(overlapping) / n_papers:.0f}%)**
        - label disagreement, no band common to every run: **{len(disagree)}/{n_papers} ({100 * len(disagree) / n_papers:.0f}%)**
        - split n/a vs a real verdict (triage disagreed between runs): **{len(split)}**
        - missing/unparseable runs: **{len(partial)}**

        Category definitions are listed above the consistency chart.

        ### Score spread within papers

        Scores here are the rounded integers on the verdict line, so a
        spread of 1 can come from two runs whose exact scores were only
        slightly apart but rounded to neighboring integers.

        Max minus min of a paper's scores, over **{len(ranges)}** papers
        with 2+ scored runs: mean **{statistics.fmean(ranges):.2f}**,
        median **{statistics.median(ranges):.1f}**, max **{max(ranges)}**.
        Per-paper score stdev: mean **{statistics.fmean(stdevs):.2f}**,
        max **{max(stdevs):.2f}**.

        | Spread | Papers |
        |-------:|-------:|
        | 0 | {sum(1 for x in ranges if x == 0)} |
        | 1 | {sum(1 for x in ranges if x == 1)} |
        | 2 | {sum(1 for x in ranges if x == 2)} |
        | 3+ | {sum(1 for x in ranges if x >= 3)} |
        """
    )
    return


@app.cell
def _(mo, stats):
    inconsistent = sorted(
        (p for p in stats
         if p.category in ("DISAGREE", "split n/a vs verdict")),
        key=lambda p: (p.score_range, p.score_stdev),
        reverse=True,
    )
    mo.md(
        f"""
        ## Inconsistent papers — interactive dataframe

        All {len(inconsistent)} papers in the DISAGREE or split n/a vs
        verdict categories, sorted by score spread then score standard
        deviation, largest first. Papers with overlapping spans are not
        listed, because their runs share a band. **Spread** is the paper's
        highest run score minus its lowest, **stdev** is the population
        standard deviation of its run scores, and **verdicts** lists every
        run in run order as label(score). This is the sortable, paginated
        dataframe; a plain-text version of the same table follows below.
        """
    )
    return (inconsistent,)


@app.cell
def _(fmt_verdict, inconsistent, mo):
    # Wrapped so the PDF export rasterizes the table instead of printing
    # its raw data.
    mo.vstack([mo.ui.table(
        [
            {
                "paper": p.pid,
                "category": p.category,
                "spread": p.score_range,
                "stdev": round(p.score_stdev, 2),
                "verdicts": " ".join(fmt_verdict(r) for r in p.runs),
            }
            for p in inconsistent
        ],
        pagination=True,
    )])
    return


@app.cell
def _(fmt_verdict, inconsistent, mo):
    if not inconsistent:
        inconsistent_text = mo.md("")
    else:
        inc_rows = [
            f"| {p.pid} | {p.category} | {p.score_range} "
            f"| {p.score_stdev:.2f} "
            f"| {' '.join(fmt_verdict(r) for r in p.runs)} |"
            for p in inconsistent
        ]
        inconsistent_text = mo.md(
            f"## Inconsistent papers ({len(inconsistent)})\n\n"
            "Same papers and columns as the dataframe above, as plain "
            "text.\n\n"
            "| Paper | Category | Spread | Stdev | Verdicts |\n"
            "|-------|----------|-------:|------:|----------|\n"
            + "\n".join(inc_rows)
        )
    inconsistent_text
    return


@app.cell
def _(THEME, expected_runs, n_expected_papers, n_missing, plt, runs):
    n_present = len(runs)
    n_expected = n_expected_papers * expected_runs
    pie_out, ax_pie = plt.subplots(figsize=(10, 4))
    ax_pie.pie(
        [n_present, n_missing],
        labels=[f"reports present\n{n_present}", f"missing\n{n_missing}"],
        colors=[THEME["green"], THEME["red"]],
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=90,
        wedgeprops={"edgecolor": "#ffffff", "linewidth": 2},
    )
    ax_pie.set_title(
        f"Expected runs ({n_expected} = {n_expected_papers} papers "
        f"x {expected_runs} runs)"
    )
    pie_out.tight_layout()
    pie_out
    return


@app.cell
def _(
    db_error: str | None,
    expected_runs,
    missing_by_pid,
    mo,
    n_expected_papers,
):
    if db_error is None:
        source_note = (
            f"Expected paper list from the paperstore DB "
            f"({n_expected_papers} papers); {expected_runs} runs per "
            f"paper (from max run number)."
        )
    else:
        source_note = (
            f"Paperstore DB unreadable ({db_error}) — only papers with "
            f"at least one report are considered."
        )
    if not missing_by_pid:
        missing_table = mo.md(
            f"## Missing runs\n\nAll expected reports are present. "
            f"{source_note}"
        )
    else:
        miss_rows = [
            f"| {pid} | {expected_runs - len(missing)} "
            f"| {', '.join(str(n) for n in missing)} |"
            for pid, missing in sorted(missing_by_pid.items())
        ]
        missing_table = mo.md(
            "## Missing runs (no report file on disk)\n\n"
            f"{source_note}\n\n"
            "| Paper | Reports on disk | Missing run numbers |\n"
            "|-------|----------------:|---------------------|\n"
            + "\n".join(miss_rows)
        )
    missing_table
    return


if __name__ == "__main__":
    app.run()
