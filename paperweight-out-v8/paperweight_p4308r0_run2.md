Verdict: Strong (9/14)

The paper offers substantial support for its standardization case in the areas that matter most: it establishes why the problem is significant, who is affected, what alternatives exist, and that the proposed semantics have implementation experience. The support is thinnest where the proposal must justify standardization itself, since the paper does not establish why the standard is the right venue or why a library solution will not do, and its coordination and interoperability claims remain only asserted rather than demonstrated.

- The strongest support comes from the implementation experience, with working prototypes in GCC and Clang branches and four of the eight response shapes already deployed in production.
- The paper also firmly establishes why the issue matters and who is affected, including SG21 polling data and large-scale deployment of related hardening modes.
- The prior art and alternatives section is well grounded, restoring a foreclosed option and comparing all eight against requirements drawn from the public record.
- The most glaring omission is the absence of any established case for why this requires a standard rather than a library facility, leaving the core standardization rationale unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 5 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 12
on threshold: coordination, implementation
splits: audience[2] 1/1/0  audience[6] 1/0/0  prior_art[2] 1/2/1  prior_art[5] 0/0/2
        prior_art[8] 2/2/0  implementation[8] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              1/1/1  -> 1.00
  [6] 3. Background and Terms                      2/2/2  -> 2.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0                                  2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Once an implicit assertion can reach a throwing handler, an exception may escape an ordinary core-language expression that the `noexcept` operator reports as non-throwing.
candidate 2 (found by 3 of 39 passes): Moving the operator's answer would be a source-level breaking change.
candidate 3 (found by 3 of 39 passes): The completed column carries the asymmetry the requirements grid cannot show: the terminating, trapping, and aborting response shapes are deployed, while the throwing response of Options A and 0 has no implementation, and only the capability analogues exist for it.
candidate 4 (found by 2 of 39 passes): C++26 Contracts let a violation handler throw, and P3100 extends that mechanism to implicit assertions on core-language undefined behavior while holding the noexcept operator's value fixed, narrowing the response to Options A through D.

## audience - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      1/0/0  -> 0.33
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0                                  0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): SG21 took seven polls on the `noexcept` interaction when it discussed P3541R1 in January 2025, and Table 3 reproduces them.
candidate 2 (found by 3 of 39 passes): libc++ hardening runs the trap response across hundreds of millions of lines at Google [23]
candidate 3 (found by 2 of 39 passes): of the eight response shapes, four are deployed and two have prototypes and the two that throw are not deployed
candidate 4 (found by 1 of 39 passes): The magnitude of the breaking change is unmeasured: the public record contains no study of how much code depends on the `noexcept` of an expression P3100 would make checkable, in either direction.

## prior_art - grade 2.00 (fired in 8 of 13 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
  [5] 2. Introduction                              0/0/2  -> 0.67
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       2/2/2  -> 2.00
  [8] 5. The P3100 Options (A, B, C, D)            2/2/0  -> 1.33
  [9] 6. Option 0                                  2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This paper restores the foreclosed Option 0, adds E, F, and G, and compares all eight against requirements from P3100R8 and the public record
candidate 2 (found by 3 of 39 passes): Option F gives implicit contract assertions the response `assert` has carried since C: the violation handler is invoked in a non-throwing form, and then the program calls `abort()` - not `std::terminate`, and not contract-termination, but `abort()`, as `assert` does today.
candidate 3 (found by 2 of 39 passes): The options labeled A through D come from [P3100R8](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3100r8.pdf) [1]; the authors characterize that published position, do not speak for its authors, and have written the A-D material to a standard its authors could endorse.
candidate 4 (found by 2 of 39 passes): Table 1 scores each option against six requirements drawn from P3100R8's prose, in the section order A, B, C, D, 0, E, F, G.

## vehicle - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0                                  0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
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
  [9] 6. Option 0                                  2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The two object files do not link, or link with mismatched declarations of one entity - the same ODR violation surfacing at link time.

## insufficiency - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0                                  0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            2/0/2  -> 1.33
  [9] 6. Option 0                                  0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): D4298R0 is implemented in the P3850 experimental forks of GCC and Clang on Compiler Explorer, not in a release of either compiler [12]
candidate 2 (found by 2 of 39 passes): of the eight response shapes, four are deployed and two have prototypes and the two that throw are not deployed
candidate 3 (found by 2 of 39 passes): [D4298R0](https://isocpp.org/files/papers/D4298R0.pdf) [12] specifies exactly these two semantics (as `noexcept-observe` and `noexcept-enforce`) and reports an implementation in the P3850 branches of GCC and Clang on Compiler Explorer.
candidate 4 (found by 1 of 39 passes): of the eight response shapes, four are deployed and two have prototypes and the two that throw are not deployed.

-->
