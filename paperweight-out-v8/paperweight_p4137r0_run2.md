Verdict: Adequate (5/14)

The paper gives real support on the analytical side—it identifies the verifiable subset, the false-positive gap, and the prior work it builds on—but it leaves the standardization case largely unproven where it matters most: who is affected, why a standard is needed, and whether the rules work outside a tool prototype.

- The strongest support is the concrete measurement of the structural false-positive gap between what the profile promises and what its rules can actually verify.
- The paper also grounds its approach in existing proposals and lifetime-safety work, showing the rule set and suppression mechanisms are not invented from nothing.
- The thinnest support is the absence of any real-codebase measurement showing how much existing C++ falls inside the verifiable subset.
- The most glaring omission is that the paper never establishes who is affected, why the standard is the right vehicle, or why a library or tooling specification would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.67   accumulate 4.67   max 4.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 93 of 98 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 4.00 / 5.00   (all 3 samples: 4.50)
headings: h2 13
on threshold: none
splits: prior_art[8] 2/1/2  prior_art[9] 0/2/0  prior_art[10] 1/0/0  implementation[2] 1/0/1
        implementation[6] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          2/2/2  -> 2.00
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        2/2/2  -> 2.00
  [8] 5. Phase 2: Semantic Analysis                1/1/1  -> 1.00
  [9] 6. Phase 3: Annotation Inference             1/1/1  -> 1.00
  [10] 7. Implications                              1/1/1  -> 1.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              1/1/1  -> 1.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It does not measure how much of a real codebase those rules can verify.
candidate 2 (found by 3 of 42 passes): What the paper does not provide is a measurement. How much of a real codebase falls in the verifiable subset?
candidate 3 (found by 3 of 42 passes): Until someone fills in the table for a real codebase, the committee is standardizing a guarantee without knowing its scope.
candidate 4 (found by 3 of 42 passes): The structural false positive category is the most important finding. It measures the irreducible gap between what the profile promises and what it can deliver.

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

## prior_art - grade 1.83 (fired in 6 of 14 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          2/2/2  -> 2.00
  [6] 3. The Profile Rules as AST Predicates       1/1/1  -> 1.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                2/1/2  -> 1.67
  [9] 6. Phase 3: Annotation Inference             0/2/0  -> 0.67
  [10] 7. Implications                              1/0/0  -> 0.33
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)[1] defines the rules.
candidate 2 (found by 3 of 42 passes): [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)[1] introduces this attribute and notes that the compiler can verify it.
candidate 3 (found by 2 of 42 passes): The invalidation analysis builds on the lifetime safety work in [P1179R1], "Lifetime safety: Preventing common dangling," and the dangling-pointer elimination described in [P3346R0], "Profile invalidation - eliminating dangling pointers."
candidate 4 (found by 2 of 42 passes): e.g., `[[suppress(profiles)]]` per [P3589R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3589r2.pdf)[3]

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

## implementation - grade 0.67  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          0/0/0  -> 0.00
  [6] 3. The Profile Rules as AST Predicates       1/0/1  -> 0.67
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): The tools exist today.
candidate 2 (found by 2 of 42 passes): A clang-tidy check or libTooling pass implementing them is a few hundred lines of code against the AST.

-->
