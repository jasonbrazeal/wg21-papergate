Verdict: Adequate (4/14)

The paper offers a narrow but genuine foundation for its standardization case: it connects the proposed facility to prior work and explains why the annotation has some practical value, but it leaves most of the burden of justification unaddressed. The thinnest areas are the absence of any measured scope in real code, the lack of a standard-based rationale, and the silence on coordination, interoperability, and why a library solution would not suffice.

- The strongest support is the paper’s grounding in prior art, with clear references to P3984R0, P1179R1, and P3346R0 establishing the technical lineage of the invalidation analysis.
- The paper also establishes a limited but real motivation by acknowledging that the annotation dividend measures a narrow lever, even while conceding it does not measure how much real code falls in the verifiable subset.
- The most glaring omission is the failure to establish who is affected, leaving the proposal without any demonstrated constituency or measured impact on real codebases.
- Equally unaddressed are why the standard is the right venue, how the feature coordinates with existing or planned facilities, and why a library-only approach cannot deliver the same guarantee.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 3 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 3.67   accumulate 4.67   max 4.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 93 of 98 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 3.50 / 4.50   (all 3 samples: 4.33)
headings: h2 13
on threshold: motivation
splits: motivation[8] 2/1/1  motivation[12] 1/1/0  prior_art[6] 1/0/1  implementation[2] 1/0/1
        implementation[9] 0/0/1
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
  [7] 4. Phase 1: Mechanical Classification        1/1/1  -> 1.00
  [8] 5. Phase 2: Semantic Analysis                2/1/1  -> 1.33
  [9] 6. Phase 3: Annotation Inference             1/1/1  -> 1.00
  [10] 7. Implications                              1/1/1  -> 1.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              1/1/0  -> 0.67
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It does not measure how much of a real codebase those rules can verify.
candidate 2 (found by 3 of 42 passes): What the paper does not provide is a measurement. How much of a real codebase falls in the verifiable subset?
candidate 3 (found by 3 of 42 passes): Until someone fills in the table for a real codebase, the committee is standardizing a guarantee without knowing its scope.
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

## prior_art - grade 2.00 (fired in 4 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence Gap                          2/2/2  -> 2.00
  [6] 3. The Profile Rules as AST Predicates       1/0/1  -> 0.67
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                2/2/2  -> 2.00
  [9] 6. Phase 3: Annotation Inference             0/0/0  -> 0.00
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)[1] defines the rules.
candidate 2 (found by 3 of 42 passes): [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)[1] introduces this attribute and notes that the compiler can verify it.
candidate 3 (found by 2 of 42 passes): The invalidation analysis builds on the lifetime safety work in [P1179R1][6], "Lifetime safety: Preventing common dangling," and the dangling-pointer elimination described in [P3346R0][7], "Profile invalidation - eliminating dangling pointers."
candidate 4 (found by 1 of 42 passes): The invalidation analysis builds on the lifetime safety work in [P1179R1], "Lifetime safety: Preventing common dangling," and the dangling-pointer elimination described in [P3346R0], "Profile invalidation - eliminating dangling pointers."

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
  [6] 3. The Profile Rules as AST Predicates       0/0/0  -> 0.00
  [7] 4. Phase 1: Mechanical Classification        0/0/0  -> 0.00
  [8] 5. Phase 2: Semantic Analysis                0/0/0  -> 0.00
  [9] 6. Phase 3: Annotation Inference             0/0/1  -> 0.33
  [10] 7. Implications                              0/0/0  -> 0.00
  [11] 8. The Tools Exist                           0/0/0  -> 0.00
  [12] 9. Availability                              0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): The tools exist today.
candidate 2 (found by 1 of 42 passes): An LLM scanning a codebase can generate `[[not_invalidating]]` annotations for every non-const function that does not invalidate.

-->
