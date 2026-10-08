Verdict: Adequate (5/14)

The paper offers meaningful support in a few narrow areas, chiefly by grounding its analysis in existing proposals and by identifying a measurable gap between profile promises and verifiable results. But it leaves the core standardization rationale largely unaddressed: it does not show who would be affected, why the feature belongs in the standard rather than in tooling or a library, or how it would coordinate with existing and future specifications. The thinnest parts are exactly those a committee most needs before acting.

- The strongest support is the paper’s engagement with prior art, including P3984R0, P3589R2, P1179R1, and P3346R0, which anchors the discussion in ongoing committee work.
- The paper also establishes why the problem matters by distinguishing structural false positives from annotation-dependent gains, making clear that the guarantee’s scope is currently unknown for real codebases.
- The most glaring omission is the absence of any established case for why standardization, as opposed to a library or external tool, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 3 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.00   accumulate 5.00   max 5.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 94 of 98 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.50 / 5.00 / 4.50   (all 3 samples: 4.67)
headings: h2 13
on threshold: motivation
splits: motivation[7] 1/2/1  motivation[12] 0/0/1  prior_art[11] 0/1/0  implementation[2] 1/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 7 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          2/2/2  -> 2.00
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        1/2/1  -> 1.33
  [8] 5. Phase 2: Semantic Analysis                1/1/1  -> 1.00
  [9] 6. Phase 3: Annotation Inference             1/1/1  -> 1.00
  [10] 7. Implications                              1/1/1  -> 1.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/1  -> 0.33
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It does not measure how much of a real codebase those rules can verify.
candidate 2 (found by 3 of 42 passes): Until someone fills in the table for a real codebase, the committee is standardizing a guarantee without knowing its scope.
candidate 3 (found by 3 of 42 passes): The structural false positive category is the most important finding. It measures the irreducible gap between what the profile promises and what it can deliver.
candidate 4 (found by 3 of 42 passes): The annotation dividend therefore measures a narrow but real lever.

## audience - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          0/0/0  -> 0.00
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          2/2/2  -> 2.00
  [6] 3. The Profile Rules as AST Predicates       1/1/1  -> 1.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                2/2/2  -> 2.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/1/0  -> 0.33
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)[1] defines the rules.
candidate 2 (found by 3 of 42 passes): e.g., `[[suppress(profiles)]]` per [P3589R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3589r2.pdf)[3]
candidate 3 (found by 3 of 42 passes): [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)[1] introduces this attribute and notes that the compiler can verify it.
candidate 4 (found by 2 of 42 passes): The invalidation analysis builds on the lifetime safety work in [P1179R1][6], "Lifetime safety: Preventing common dangling," and the dangling-pointer elimination described in [P3346R0][7], "Profile invalidation - eliminating dangling pointers."

## vehicle - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          0/0/0  -> 0.00
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          0/0/0  -> 0.00
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          0/0/0  -> 0.00
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          0/0/0  -> 0.00
  [6] 3. The Profile Rules as AST Predicates       1/1/1  -> 1.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): A clang-tidy check or libTooling pass implementing them is a few hundred lines of code against the AST.
candidate 2 (found by 2 of 42 passes): The tools exist today.

-->
