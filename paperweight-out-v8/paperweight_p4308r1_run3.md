Verdict: Strong (10/14)

The paper offers solid grounding for its motivation, affected audience, prior art, and implementation experience, but it does not fully establish why the standard is the right venue, how the feature would coordinate across translation units, or why a library solution cannot suffice. The thinnest part of the case is the absence of a demonstrated need for core-language action rather than a library or tooling approach.

- The strongest support is the concrete implementation experience, including a working prototype in GCC and Clang forks and four response shapes already deployed in shipping code.
- The paper also clearly establishes who is affected, with evidence of large-scale deployment and repeated committee polling on the `noexcept` interaction.
- The most glaring omission is the lack of an established argument for why a library cannot address the problem, since the only credited passage merely repeats the build-mode dependency claim without showing it is insurmountable outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.33/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.33 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.33   corroborated 10.67   accumulate 10.33   max 12.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.33  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 11.00 / 10.00 / 10.00   (all 3 samples: 10.33)
headings: h2 13
on threshold: coordination, insufficiency
splits: motivation[5] 1/2/1  motivation[10] 1/2/2  motivation[12] 0/1/1  audience[2] 0/0/1
        audience[6] 0/0/1  prior_art[7] 1/2/2  prior_art[8] 2/2/0  vehicle[9] 2/0/0
        implementation[2] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              1/2/1  -> 1.33
  [6] 3. Background and Terms                      2/2/2  -> 2.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              1/2/2  -> 1.67
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                0/1/1  -> 0.67
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Once an implicit assertion can reach a throwing handler, an exception may escape an ordinary core-language expression that the `noexcept` operator reports as non-throwing.
candidate 2 (found by 3 of 42 passes): Moving the operator's answer would be a source-level breaking change.
candidate 3 (found by 3 of 42 passes): The build-mode dependency does not stay confined to expressions a programmer writes out by hand; it reaches the standard library's own type traits, which query `noexcept` on the expressions they are handed.
candidate 4 (found by 2 of 42 passes): This paper restores the foreclosed Option 0, adds E, F, and G, and compares all eight against requirements from P3100R8 and the public record.

## audience - grade 2.00 (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/1  -> 0.33
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): libc++ hardening runs the trap response across hundreds of millions of lines at Google [23]
candidate 2 (found by 2 of 42 passes): SG21 took seven polls on the `noexcept` interaction when it discussed P3541R1 in January 2025, and Table 3 reproduces them.
candidate 3 (found by 1 of 42 passes): Of the eight response shapes - throw, terminate, trap, or abort - four are deployed, two have prototypes, and the two that throw are not deployed.
candidate 4 (found by 1 of 42 passes): The magnitude of the breaking change is unmeasured: the public record contains no study of how much code depends on the `noexcept` of an expression P3100 would make checkable, in either direction.

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       1/2/2  -> 1.67
  [8] 5. The P3100 Options (A, B, C, D)            2/2/0  -> 1.33
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                2/2/2  -> 2.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper restores the foreclosed Option 0, adds E, F, and G, and compares all eight against requirements from P3100R8 and the public record.
candidate 2 (found by 3 of 42 passes): P3541R1 states it as its Option 1: "Any construct that might end up in either undefined behavior or contract violation is potentially-throwing and this is reflected by the noexcept-operator."
candidate 3 (found by 3 of 42 passes): Option F gives implicit contract assertions the response `assert` has carried since C: the violation handler is invoked in a non-throwing form, and then the program calls `abort()` - not `std::terminate`, and not contract-termination, but `abort()`, as `assert` does today.
candidate 4 (found by 3 of 42 passes): D4298R0 implements Option C's non-throwing semantics in the GCC and Clang forks [12], whereas Option A has no implementation of its escape path

## vehicle - grade 0.33 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/0/0  -> 0.67
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The build-mode dependency does not stay confined to expressions a programmer writes out by hand; it reaches the standard library's own type traits, which query `noexcept` on the expressions they are handed.

## coordination - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The two object files do not link, or link with mismatched declarations of one entity - the same ODR violation surfacing at link time.

## insufficiency - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The build-mode dependency does not stay confined to expressions a programmer writes out by hand; it reaches the standard library's own type traits, which query `noexcept` on the expressions they are handed.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            2/2/2  -> 2.00
  [9] 6. Option 0 (the foreclosed option)          0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                1/1/1  -> 1.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [D4298R0](https://isocpp.org/files/papers/D4298R0.pdf) [12] specifies exactly these two semantics (as `noexcept-observe` and `noexcept-enforce`) and reports an implementation in the P3850 branches of GCC and Clang on Compiler Explorer.
candidate 2 (found by 3 of 42 passes): D4298R0 is implemented in the P3850 experimental forks of GCC and Clang on Compiler Explorer, not in a release of either compiler [12]
candidate 3 (found by 3 of 42 passes): Four of the eight response shapes are deployed in shipping code, two have prototypes, and the two that throw are not.
candidate 4 (found by 2 of 42 passes): Of the eight response shapes - throw, terminate, trap, or abort - four are deployed, two have prototypes, and the two that throw are not deployed.

-->
