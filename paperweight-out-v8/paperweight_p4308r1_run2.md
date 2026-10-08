Verdict: Strong (11/14)

The paper offers substantial support for its standardization case in the areas that are easiest to verify: it documents real implementation experience, reproduces relevant committee polling, and grounds its comparison of options in the public record. The support is thinnest where the argument must connect those observations to a need for core-language standardization rather than a library or tooling solution, and where it must show how the proposed semantics would interoperate with existing code and build modes.

- The strongest support is the implementation record, with four response shapes deployed in shipping code, two prototyped, and the throwing options absent from deployment.
- The paper also establishes who is affected by citing SG21’s seven polls on the `noexcept` interaction and the scale of libc++ hardening use at Google.
- The case for why the standard must address this, rather than a library, rests mainly on a claimed effect on standard library type traits and is not established.
- The most glaring omission is the lack of an established account of coordination and interoperability, where the paper only claims a link-time ODR-style failure without demonstrating it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 11.00   accumulate 10.67   max 13.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.67  implementation 2.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 11.00 / 10.00 / 11.00   (all 3 samples: 10.67)
headings: h2 13
on threshold: vehicle, coordination
splits: motivation[5] 2/1/2  motivation[12] 0/0/2  audience[6] 0/0/1  audience[12] 0/0/1
        prior_art[2] 2/1/2  prior_art[7] 1/2/1  insufficiency[9] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              2/1/2  -> 1.67
  [6] 3. Background and Terms                      2/2/2  -> 2.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                0/0/2  -> 0.67
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper restores the foreclosed Option 0, adds E, F, and G, and compares all eight against requirements from P3100R8 and the public record.
candidate 2 (found by 3 of 42 passes): Once an implicit assertion can reach a throwing handler, an exception may escape an ordinary core-language expression that the `noexcept` operator reports as non-throwing.
candidate 3 (found by 3 of 42 passes): Option E's core case is that one-sentence restriction, and its real cost is the observe gap.
candidate 4 (found by 2 of 42 passes): Moving the operator's answer would be a source-level breaking change.

## audience - grade 2.00 (fired in 4 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/1  -> 0.33
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                0/0/1  -> 0.33
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): SG21 took seven polls on the `noexcept` interaction when it discussed P3541R1 in January 2025, and Table 3 reproduces them.
candidate 2 (found by 3 of 42 passes): libc++ hardening runs the trap response across hundreds of millions of lines at Google [23]
candidate 3 (found by 1 of 42 passes): The magnitude of the breaking change is unmeasured: the public record contains no study of how much code depends on the `noexcept` of an expression P3100 would make checkable, in either direction.
candidate 4 (found by 1 of 42 passes): The premise used to narrow it, that the `noexcept` operator's value must not change, stands on the record as a design principle and a poll, and stands unquantified as a breaking-change magnitude.

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/2  -> 1.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      2/2/2  -> 2.00
  [7] 4. Options at a Glance                       1/2/1  -> 1.33
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                2/2/2  -> 2.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper restores the foreclosed Option 0, adds E, F, and G, and compares all eight against requirements from P3100R8 and the public record.
candidate 2 (found by 3 of 42 passes): The options labeled A through D come from [P3100R8](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3100r8.pdf) [1]; the authors characterize that published position, do not speak for its authors, and have written the A-D material to a standard its authors could endorse.
candidate 3 (found by 3 of 42 passes): Option F gives implicit contract assertions the response `assert` has carried since C: the violation handler is invoked in a non-throwing form, and then the program calls `abort()` - not `std::terminate`, and not contract-termination, but `abort()`, as `assert` does today.
candidate 4 (found by 3 of 42 passes): D4298R0 implements Option C's non-throwing semantics in the GCC and Clang forks [12], whereas Option A has no implementation of its escape path, and P3100R8 Section 5.5 itself notes the new codegen that path requires [1].

## vehicle - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## insufficiency - grade 0.67 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/0/2  -> 1.33
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): The build-mode dependency does not stay confined to expressions a programmer writes out by hand; it reaches the standard library's own type traits, which query `noexcept` on the expressions they are handed.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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
candidate 1 (found by 3 of 42 passes): Of the eight response shapes - throw, terminate, trap, or abort - four are deployed, two have prototypes, and the two that throw are not deployed.
candidate 2 (found by 3 of 42 passes): [D4298R0](https://isocpp.org/files/papers/D4298R0.pdf) [12] specifies exactly these two semantics (as `noexcept-observe` and `noexcept-enforce`) and reports an implementation in the P3850 branches of GCC and Clang on Compiler Explorer.
candidate 3 (found by 3 of 42 passes): D4298R0 is implemented in the P3850 experimental forks of GCC and Clang on Compiler Explorer, not in a release of either compiler [12]
candidate 4 (found by 3 of 42 passes): Four of the eight response shapes are deployed in shipping code, two have prototypes, and the two that throw are not.

-->
