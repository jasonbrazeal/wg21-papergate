# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "altair>=5.4",
#     "numpy>=2",
#     "pandas>=2.2",
#     "scikit-learn>=1.5",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import math
    import os
    import re
    import sqlite3
    from pathlib import Path

    import altair as alt
    import marimo as mo
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import (
        accuracy_score,
        cohen_kappa_score,
        confusion_matrix,
        f1_score,
        mean_absolute_error,
    )
    from sklearn.model_selection import (
        StratifiedGroupKFold,
        cross_val_predict,
        learning_curve,
    )
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    alt.data_transformers.disable_max_rows()
    return (
        LogisticRegression,
        Path,
        StandardScaler,
        StratifiedGroupKFold,
        accuracy_score,
        alt,
        cohen_kappa_score,
        confusion_matrix,
        cross_val_predict,
        f1_score,
        learning_curve,
        make_pipeline,
        math,
        mean_absolute_error,
        mo,
        np,
        os,
        pd,
        re,
        sqlite3,
    )


@app.cell
def _(mo):
    mo.md(r"""
    # Papergate linear classifier

    A small student for the papergate LLM judge. The teacher labels are the
    `Verdict:` lines of the batch runs in `papergate-out/`, restricted to
    papers whose runs converged on one identical 0-14 score (at least 4 of 5
    by default), mapped to None / Weak / Adequate / Strong / Excellent with
    the thresholds from `papergate-joaquin.md`. The features
    are a few dozen hand-engineered structural and lexical counts over the
    full paper markdown, one group per criterion of the rubric. The model is
    multinomial logistic regression, cross-validated with paper *families*
    (P-number without revision) kept in the same fold so revisions never leak
    between train and test.
    """)
    return


@app.cell
def _(mo, os):
    is_script_mode = mo.app_meta().mode == "script"
    default_db = os.environ.get("WG21_DATA_DIR", "")
    default_db = f"{default_db}/paperstore.db" if default_db else "paperstore.db"
    out_dir_input = mo.ui.text(value="papergate-out", label="LLM run reports",
                               full_width=True)
    db_input = mo.ui.text(value=default_db, label="paperstore.db",
                          full_width=True)
    mo.vstack([out_dir_input, db_input])
    return db_input, is_script_mode, out_dir_input


@app.cell
def _(re):
    LABELS = ["None", "Weak", "Adequate", "Strong", "Excellent"]
    LABEL_MAX_SCORE = [0, 3, 7, 11, 14]
    FILE_RE = re.compile(r"^papergate_([a-z0-9]+)_run(\d+)\.md$")
    VERDICT_RE = re.compile(r"^Verdict:\s*(?P<label>n/a|\w+)"
                            r"(?:\s*\((?P<score>\d+)\s*/\s*\d+)?")
    PID_RE = re.compile(r"^([pdn])(\d+)(?:r(\d+))?$")

    def label_for(score: float) -> str:
        for label, max_score in zip(LABELS, LABEL_MAX_SCORE):
            if score <= max_score:
                return label
        return LABELS[-1]

    return FILE_RE, LABELS, PID_RE, VERDICT_RE, label_for


@app.cell
def _(FILE_RE, Path, VERDICT_RE, out_dir_input, pd):
    run_rows = []
    for report in sorted(Path(out_dir_input.value).glob("papergate_*_run*.md")):
        name_match = FILE_RE.match(report.name)
        if not name_match:
            continue
        with report.open(errors="replace") as handle:
            verdict = VERDICT_RE.match(handle.readline().strip())
        if not verdict:
            continue
        score = verdict.group("score")
        run_rows.append({
            "pid": name_match.group(1),
            "run": int(name_match.group(2)),
            "verdict": verdict.group("label"),
            "score": int(score) if score is not None else None,
        })
    runs = pd.DataFrame(run_rows)
    runs
    return (runs,)


@app.cell
def _(mo):
    min_agree_slider = mo.ui.slider(
        1, 5, step=1, value=4,
        label="runs that must report the identical score for a paper to be used")
    min_agree_slider
    return (min_agree_slider,)


@app.cell
def _(PID_RE, label_for, pd):
    CRITERIA = ["motivation", "audience", "prior_art", "vehicle",
                "coordination", "insufficiency", "implementation"]
    HUMAN_ROWS = [
        ("A", "p3045r9", 2, 2, 2, 2, 2, 0, 2),
        ("A", "p2728r14", 1, 0, 1, 1, 0, 0, 2),
        ("A", "p0260r20", 1, 1, 2, 0, 1, 1, 2),
        ("A", "p1040r11", 2, 2, 2, 2, 2, 2, 2),
        ("A", "p3091r6", 2, 1, 1, 1, 0, 1, 2),
        ("A", "p2806r5", 2, 0, 2, 1, 0, 2, 2),
        ("A", "p3100r8", 2, 2, 2, 2, 2, 2, 2),
        ("A", "p2826r4", 2, 1, 1, 0, 0, 2, 1),
        ("A", "p2287r6", 2, 0, 1, 0, 1, 0, 2),
        ("A", "p2719r7", 2, 0, 2, 2, 2, 0, 1),
        ("B", "p3045r9", 2, 1, 1, 2, 2, 0, 2),
        ("B", "p2728r14", 0, 0, 1, 0, 0, 0, 2),
        ("B", "p0260r20", 0, 0, 2, 0, 0, 0, 1),
        ("B", "p1040r11", 2, 2, 2, 2, 0, 1, 2),
        ("B", "p3091r6", 2, 1, 1, 0, 0, 0, 2),
        ("B", "p2806r5", 2, 1, 2, 1, 0, 1, 2),
        ("B", "p3100r8", 2, 1, 2, 2, 1, 1, 0),
        ("B", "p2826r4", 2, 0, 2, 0, 0, 0, 0),
        ("B", "p2287r6", 2, 0, 2, 1, 0, 1, 2),
        ("B", "p2719r7", 2, 0, 2, 0, 2, 0, 0),
    ]
    humans = pd.DataFrame(HUMAN_ROWS, columns=["reviewer", "pid", *CRITERIA])
    humans["total"] = humans[CRITERIA].sum(axis=1)
    humans["label"] = humans["total"].map(label_for)
    holdout_pids = list(dict.fromkeys(humans["pid"]))
    holdout_parts = pd.Series(holdout_pids).str.extract(PID_RE)
    holdout_families = set(holdout_parts[0] + holdout_parts[1])
    humans
    return holdout_families, holdout_pids, humans


@app.cell
def _(PID_RE, holdout_families, label_for, min_agree_slider, mo, pd, runs):
    def aggregate_paper(group: pd.DataFrame) -> pd.Series:
        scored = group["score"].dropna().astype(int)
        modes = scored.mode()
        agreed_score = int(modes.iloc[0]) if len(modes) == 1 else None
        return pd.Series({
            "n_runs": len(group),
            "n_na": int((group["verdict"] == "n/a").sum()),
            "agreed_score": agreed_score,
            "n_agreeing": int((scored == agreed_score).sum())
            if agreed_score is not None else 0,
            "score_range": (scored.max() - scored.min()) if len(scored) else None,
        })

    all_papers = runs.groupby("pid").apply(aggregate_paper,
                                           include_groups=False).reset_index()
    # The teacher is noisy: only papers where the runs converged on one exact
    # 0-14 score are trusted as labels. A tie between two modes never counts.
    papers = all_papers[
        all_papers["n_agreeing"] >= min_agree_slider.value].copy()
    papers["label"] = papers["agreed_score"].map(label_for)
    # A score of 0 means no criterion was addressed at all; that is a
    # not-a-proposal signal for an upstream filter, not a verdict to learn.
    papers = papers[papers["label"] != "None"]
    pid_parts = papers["pid"].str.extract(PID_RE)
    papers["family"] = pid_parts[0] + pid_parts[1]
    # Every revision of a human-reviewed paper is held out, not just the
    # reviewed revision: consecutive revisions share most of their text.
    in_holdout = papers["family"].isin(holdout_families)
    n_held_out = int(in_holdout.sum())
    papers = papers[~in_holdout]
    agreement_counts = (all_papers["n_agreeing"].value_counts().sort_index()
                        .rename_axis("runs with the modal score")
                        .reset_index(name="papers"))
    mo.vstack([
        mo.md(f"**{len(papers)} of {len(all_papers)} papers** have at least "
              f"{min_agree_slider.value} runs reporting the identical score "
              f"and are kept as teacher labels; {n_held_out} more qualified "
              f"but belong to a human-reviewed family and are held out."),
        mo.ui.table(agreement_counts, selection=None),
        papers,
    ])
    return (papers,)


@app.cell
def _(Path, db_input, holdout_pids, papers, re, sqlite3):
    IMAGE_DATA_URI = re.compile(r"!\[([^\]]*)\]\(data:image/[^)]*\)")

    conn = sqlite3.connect(f"file:{db_input.value}?mode=ro", uri=True)
    md_rows = conn.execute(
        "SELECT lower(paper_id), markdown_path FROM papers "
        "WHERE markdown_path != ''").fetchall()
    conn.close()
    md_paths = {pid: Path(md) for pid, md in md_rows}

    texts = {}
    for pid in [*papers["pid"], *holdout_pids]:
        md_path = md_paths.get(pid)
        if md_path is not None and md_path.is_file():
            raw = md_path.read_text(encoding="utf-8", errors="replace")
            texts[pid] = IMAGE_DATA_URI.sub(r"[image: \1]", raw)
    return (texts,)


@app.cell
def _(math, re):
    HEADING_RE = re.compile(r"^#{1,4}\s+(.+)$", re.MULTILINE)
    FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
    WORD_RE = re.compile(r"\w+")

    # Heading groups mirror the rubric: a paper that has a section for a
    # criterion has at least tried to address it.
    HEADING_GROUPS = {
        "h_motivation": r"motivation|introduction|problem|rationale|background",
        "h_prior_art": r"prior art|alternativ|related work|existing practice|"
                       r"comparison|other languages|existing (solutions|"
                       r"libraries|implementations)|survey",
        "h_implementation": r"implementation|experience|deployment|prototype|"
                            r"usage",
        "h_design": r"design|proposal|proposed",
        "h_wording": r"wording|specification",
        "h_faq": r"faq|questions|polls?|feedback",
        "h_housekeeping": r"revision|change ?log|changes since|acknowledg|"
                          r"references|bibliography",
    }

    # Lexical groups, counted per 1000 words. Each maps to one criterion.
    LEXICAL_GROUPS = {
        "lx_numbers": r"\b\d+(?:\.\d+)?\s?%|\b\d{2,}(?:,\d{3})*\b",
        "lx_urls": r"https?://",
        "lx_paper_refs": r"\b[PNDpnd]\d{4}(?:[Rr]\d+)?\b",
        "lx_named_prior_art": r"\b(Boost|Abseil|folly|Qt|LLVM|libstdc\+\+|"
                              r"libc\+\+|MSVC|GCC|Clang|EDG|Rust|Python|Java|"
                              r"Swift|Kotlin|Haskell|C#|Go|D|Zig|Carbon|"
                              r"range-v3|fmt|TBB|Intel|Google|Microsoft|"
                              r"Bloomberg|Facebook|Meta|Apple|Nvidia)\b",
        "lx_implementation": r"\b(implemented|implementation experience|"
                             r"shipped|shipping|production|deployed|"
                             r"prototype|compiler explorer|godbolt|branch|"
                             r"fork|in use|has been used|we have used)\b",
        "lx_audience": r"\b(survey|poll|respondents?|codebases?|users|"
                       r"downloads?|GitHub|projects|ecosystem|percent|"
                       r"widely|common(ly)?|frequently)\b",
        "lx_coordination": r"\b(ABI|interoperab\w*|vocabulary|vendors?|"
                           r"agree(ment)?|across (libraries|codebases|"
                           r"projects|vendors|implementations)|boundary|"
                           r"incompatible)\b",
        "lx_insufficiency": r"\b(cannot (be )?(implement|express|do|achieve|"
                            r"detect|portably)\w*|impossible|not possible|"
                            r"without (language|compiler) support|requires "
                            r"(compiler|language) support|core language|"
                            r"quality of implementation|QoI|unimplementable|"
                            r"library solution|library cannot)\b",
        "lx_vehicle": r"\b(standardi[sz]\w*|third[- ]party|portab\w*|"
                      r"in the standard|standard library|the committee|"
                      r"WG21|belongs in)\b",
    }

    def split_sections(text: str) -> list[tuple[str, str]]:
        positions = [(m.start(), m.group(1)) for m in HEADING_RE.finditer(text)]
        sections = []
        for i, (start, heading) in enumerate(positions):
            end = positions[i + 1][0] if i + 1 < len(positions) else len(text)
            sections.append((heading.lower(), text[start:end]))
        return sections

    def extract_features(text: str) -> dict[str, float]:
        words = len(WORD_RE.findall(text))
        per_k = 1000.0 / max(words, 1)
        code_chars = sum(len(m.group(0)) for m in FENCE_RE.finditer(text))
        sections = split_sections(text)
        feats: dict[str, float] = {
            "log_words": math.log10(max(words, 1)),
            "n_headings": float(len(sections)),
            "code_fraction": code_chars / max(len(text), 1),
        }
        for name, pattern in HEADING_GROUPS.items():
            heading_re = re.compile(pattern, re.IGNORECASE)
            matched = [body for heading, body in sections
                       if heading_re.search(heading)]
            feats[name] = float(bool(matched))
            feats[name + "_words"] = float(
                sum(len(WORD_RE.findall(body)) for body in matched))
        for name, pattern in LEXICAL_GROUPS.items():
            count = len(re.findall(pattern, text, flags=re.IGNORECASE))
            feats[name] = count * per_k
        return feats

    return (extract_features,)


@app.cell
def _(PID_RE, extract_features, np, papers, pd, texts):
    def featurize(pids: list[str]) -> pd.DataFrame:
        rows = [{"pid": pid, **extract_features(texts[pid])}
                for pid in pids if pid in texts]
        frame = pd.DataFrame(rows).set_index("pid")
        word_columns = [c for c in frame.columns if c.endswith("_words")]
        frame[word_columns] = np.log1p(frame[word_columns])
        parts = frame.index.to_series().str.extract(PID_RE)
        frame["revision"] = np.log1p(parts[2].fillna("0").astype(int)).to_numpy()
        frame["is_draft"] = (parts[0] == "d").astype(int).to_numpy()
        return frame

    features = featurize(list(papers["pid"]))
    feature_columns = list(features.columns)
    data = papers.set_index("pid").join(features, how="inner").reset_index()
    data
    return data, feature_columns, featurize


@app.cell
def _(LABELS, alt, data, mo):
    label_counts = data["label"].value_counts().reindex(LABELS, fill_value=0)
    label_chart = (
        alt.Chart(label_counts.rename_axis("label").reset_index(name="papers"))
        .mark_bar()
        .encode(x=alt.X("label:N", sort=LABELS), y="papers:Q",
                tooltip=["label", "papers"])
        .properties(title=f"Teacher labels ({len(data)} papers)", width=360)
    )
    mo.vstack([
        mo.md(f"**{len(data)} labelled papers** in "
              f"**{data['family'].nunique()} families**; "
              f"{int(data['is_draft'].sum())} are D-drafts. Median run-to-run "
              f"score range within a paper: {data['score_range'].median():.0f} "
              f"points."),
        label_chart,
    ])
    return


@app.cell
def _(mo):
    c_slider = mo.ui.slider(-3, 2, step=0.5, value=0.0,
                            label="log10 C (inverse L2 strength)")
    folds_slider = mo.ui.slider(3, 10, step=1, value=5, label="CV folds")
    seed_input = mo.ui.number(0, 9999, value=0, label="seed")
    mo.hstack([c_slider, folds_slider, seed_input])
    return c_slider, folds_slider, seed_input


@app.cell
def _(
    LABELS,
    LogisticRegression,
    StandardScaler,
    StratifiedGroupKFold,
    c_slider,
    data,
    feature_columns,
    folds_slider,
    make_pipeline,
    seed_input,
):
    X = data[feature_columns].to_numpy(dtype=float)
    y = data["label"].map(LABELS.index).to_numpy()
    groups = data["family"].to_numpy()
    present_labels = sorted(set(y))

    def make_model() -> object:
        return make_pipeline(
            StandardScaler(),
            LogisticRegression(C=10 ** c_slider.value, class_weight="balanced",
                               max_iter=5000),
        )

    # Materialised once so the classifier and the ordinal baseline are scored
    # on identical family-grouped folds.
    cv = list(StratifiedGroupKFold(
        n_splits=folds_slider.value, shuffle=True,
        random_state=seed_input.value).split(X, y, groups))
    return X, cv, groups, make_model, present_labels, y


@app.cell
def _(
    LABELS,
    X,
    accuracy_score,
    cohen_kappa_score,
    cross_val_predict,
    cv,
    f1_score,
    groups,
    make_model,
    mean_absolute_error,
    mo,
    np,
    y,
):
    y_pred = cross_val_predict(make_model(), X, y, cv=cv, groups=groups)
    majority = np.full_like(y, np.bincount(y).argmax())

    class_prior = np.bincount(y, minlength=len(LABELS)) / len(y)

    def metrics(pred: np.ndarray) -> dict[str, float]:
        return {
            "accuracy": accuracy_score(y, pred),
            "within one band": float((np.abs(y - pred) <= 1).mean()),
            "macro F1": f1_score(y, pred, average="macro"),
            "quadratic kappa": cohen_kappa_score(y, pred, weights="quadratic"),
            "MAE (label steps)": mean_absolute_error(y, pred),
        }

    lr_metrics = metrics(y_pred)
    majority_metrics = metrics(majority)
    # Expected accuracy of guessing at random in proportion to the priors.
    chance_accuracy = float((class_prior ** 2).sum())
    metrics_md = "| metric | logistic regression | majority class |\n|---|---|---|\n"
    metrics_md += "\n".join(
        f"| {name} | {lr_metrics[name]:.3f} | {majority_metrics[name]:.3f} |"
        for name in lr_metrics)
    metrics_md += (f"\n\nChance accuracy (guessing in proportion to the class "
                   f"priors) is {chance_accuracy:.3f}.")
    per_class_md = "| label | papers | recall |\n|---|---|---|\n" + "\n".join(
        f"| {LABELS[k]} | {int((y == k).sum())} | "
        f"{float((y_pred[y == k] == k).mean()):.2f} |"
        for k in sorted(set(y)))
    metrics_md += "\n\n" + per_class_md
    mo.md(
        f"## Cross-validated performance ({LABELS[int(majority[0])]} is the "
        f"majority class)\n\n{metrics_md}"
    )
    return metrics_md, y_pred


@app.cell
def _(LABELS, alt, confusion_matrix, pd, present_labels, y, y_pred):
    cm = confusion_matrix(y, y_pred, labels=present_labels)
    cm_norm = cm / cm.sum(axis=1, keepdims=True).clip(min=1)
    cm_rows = [
        {"true": LABELS[t], "predicted": LABELS[p],
         "count": int(cm[i, j]), "fraction": float(cm_norm[i, j])}
        for i, t in enumerate(present_labels)
        for j, p in enumerate(present_labels)
    ]
    cm_df = pd.DataFrame(cm_rows)
    present_names = [LABELS[i] for i in present_labels]
    cm_base = alt.Chart(cm_df).encode(
        x=alt.X("predicted:N", sort=present_names),
        y=alt.Y("true:N", sort=present_names),
    )
    confusion_chart = (
        cm_base.mark_rect().encode(
            color=alt.Color("fraction:Q", scale=alt.Scale(scheme="blues"),
                            title="row fraction"),
            tooltip=["true", "predicted", "count",
                     alt.Tooltip("fraction:Q", format=".2f")])
        + cm_base.mark_text().encode(
            text="count:Q",
            color=alt.condition("datum.fraction > 0.5", alt.value("white"),
                                alt.value("black")))
    ).properties(title="Confusion matrix (cross-validated)", width=320,
                 height=320)
    confusion_chart
    return


@app.cell
def _(X, alt, cv, groups, learning_curve, make_model, np, pd, y):
    train_sizes, train_scores, test_scores = learning_curve(
        make_model(), X, y, groups=groups, cv=cv, scoring="f1_macro",
        train_sizes=np.linspace(0.2, 1.0, 7), shuffle=True, random_state=0)
    curve_rows = []
    for size, tr, te in zip(train_sizes, train_scores, test_scores):
        curve_rows.append({"train size": int(size), "split": "train",
                           "macro F1": tr.mean(), "std": tr.std()})
        curve_rows.append({"train size": int(size), "split": "validation",
                           "macro F1": te.mean(), "std": te.std()})
    curve_df = pd.DataFrame(curve_rows)
    curve_df["lo"] = curve_df["macro F1"] - curve_df["std"]
    curve_df["hi"] = curve_df["macro F1"] + curve_df["std"]
    curve_base = alt.Chart(curve_df).encode(x="train size:Q", color="split:N")
    learning_chart = (
        curve_base.mark_area(opacity=0.2).encode(y="lo:Q", y2="hi:Q")
        + curve_base.mark_line(point=True).encode(
            y=alt.Y("macro F1:Q", scale=alt.Scale(domain=[0, 1])),
            tooltip=["split", "train size",
                     alt.Tooltip("macro F1:Q", format=".3f")])
    ).properties(title="Learning curve (macro F1, grouped CV)", width=480)
    learning_chart
    return


@app.cell
def _(LABELS, X, alt, feature_columns, make_model, pd, present_labels, y):
    fitted = make_model().fit(X, y)
    coefs = fitted[-1].coef_
    coef_rows = [
        {"feature": feature_columns[j], "label": LABELS[present_labels[i]],
         "coefficient": float(coefs[i, j])}
        for i in range(coefs.shape[0]) for j in range(coefs.shape[1])
    ]
    coef_df = pd.DataFrame(coef_rows)
    feature_order = (coef_df.groupby("feature")["coefficient"]
                     .apply(lambda s: s.abs().max())
                     .sort_values(ascending=False).index.tolist())
    coef_chart = (
        alt.Chart(coef_df).mark_rect().encode(
            x=alt.X("label:N", sort=[LABELS[i] for i in present_labels]),
            y=alt.Y("feature:N", sort=feature_order),
            color=alt.Color("coefficient:Q",
                            scale=alt.Scale(scheme="redblue", domainMid=0)),
            tooltip=["feature", "label",
                     alt.Tooltip("coefficient:Q", format=".2f")])
        .properties(title="Standardised coefficients (fit on all data)",
                    width=320, height=20 * len(feature_columns))
    )
    coef_chart
    return feature_order, fitted


@app.cell
def _(LABELS, alt, data, feature_order, pd):
    top_features = feature_order[:6]
    long_df = pd.melt(data, id_vars=["pid", "label"], value_vars=top_features,
                      var_name="feature", value_name="value")
    box_chart = (
        alt.Chart(long_df).mark_boxplot(extent="min-max").encode(
            x=alt.X("label:N", sort=LABELS, title=None),
            y=alt.Y("value:Q", title=None),
            color=alt.Color("label:N", sort=LABELS, legend=None))
        .properties(width=140, height=160)
        .facet(column=alt.Column("feature:N", sort=top_features, title=None))
        .resolve_scale(y="independent")
        .properties(title="Most influential features by teacher label")
    )
    box_chart
    return


@app.cell
def _(
    LABELS,
    data,
    feature_columns,
    featurize,
    fitted,
    holdout_families,
    holdout_pids,
    humans,
    mo,
    pd,
):
    assert not set(data["family"]) & holdout_families, \
        "a human-reviewed family leaked into the training set"

    holdout_features = featurize(holdout_pids)
    student_labels = pd.Series(
        [LABELS[k] for k in fitted.predict(
            holdout_features[feature_columns].to_numpy(dtype=float))],
        index=holdout_features.index, name="student")

    holdout = humans.pivot(index="pid", columns="reviewer", values="label")
    holdout.columns = [f"human {r}" for r in holdout.columns]
    holdout = holdout.join(student_labels).reset_index()

    def label_agreement(human: pd.Series) -> str:
        ih = human.map(LABELS.index)
        istudent = holdout["student"].map(LABELS.index)
        return (f"{int((ih == istudent).sum())}/{len(holdout)} exact, "
                f"{int(((ih - istudent).abs() <= 1).sum())}/{len(holdout)} "
                f"within one band")

    holdout_md = (
        f"## Final test on the {len(holdout)} human-reviewed papers\n\n"
        f"The classifier is refit on all {len(data)} training papers (no "
        f"revision of these papers included) and applied once.\n\n"
        f"- student vs human A: {label_agreement(holdout['human A'])}\n"
        f"- student vs human B: {label_agreement(holdout['human B'])}\n"
        f"- human A vs human B: "
        f"{int((holdout['human A'] == holdout['human B']).sum())}/{len(holdout)} "
        f"exact")
    mo.vstack([mo.md(holdout_md), mo.ui.table(holdout, selection=None)])
    return holdout, holdout_md


@app.cell
def _(data, holdout, holdout_md, is_script_mode, metrics_md, mo, y, y_pred):
    summary = (f"{len(data)} papers in {data['family'].nunique()} families, "
               f"{int((y == y_pred).sum())} correct "
               f"({(y == y_pred).mean():.3f} accuracy)")
    if is_script_mode:
        print(summary)
        print()
        print(metrics_md)
        print()
        print(holdout_md)
        print()
        print(holdout.to_string(index=False))
    mo.md(f"*{summary}*")
    return


if __name__ == "__main__":
    app.run()
