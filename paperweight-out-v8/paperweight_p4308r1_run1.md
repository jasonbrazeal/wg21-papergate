Verdict: Strong (10/14)

The paper offers substantial support for its standardization case in the areas that matter most: it clearly establishes why the `noexcept` interaction is consequential, who is affected, what alternatives exist, and that the proposed response shapes have real implementation experience. The support is thinnest where the argument needs to move from describing a problem to showing that only a core-language change can solve it, since the claims about standard library type traits, link-time coordination, and the inadequacy of a library-only approach are asserted rather than demonstrated.

- The strongest support is the implementation experience, with four of eight response shapes deployed in shipping code and two more prototyped in compiler forks.
- The paper also firmly establishes why the issue matters and who is affected, including the scale of libc++ hardening at Google and the seven SG21 polls on the `noexcept` interaction.
- The most glaring omission is the failure to establish why a library solution will not do, since the key claim about standard library type traits querying `noexcept` is only asserted, not shown to be insurmountable outside the core language.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 7 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 9.67   accumulate 10.17   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.33  implementation 2.00
sample agreement: 87 of 98 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.00 / 9.00 / 11.00   (all 3 samples: 10.00)
headings: h2 13
on threshold: audience, vehicle, coordination
splits: motivation[12] 1/0/1  audience[10] 2/0/2  audience[12] 1/0/0  prior_art[2] 2/1/2
        prior_art[4] 1/2/2  prior_art[6] 2/2/0  prior_art[7] 1/2/1  prior_art[9] 0/2/2
        prior_art[10] 2/0/2  insufficiency[9] 0/0/2  implementation[12] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              2/2/2  -> 2.00
  [6] 3. Background and Terms                      2/2/2  -> 2.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          2/2/2  -> 2.00
  [10] 7. Additional Options (E, F, G)              2/2/2  -> 2.00
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                1/0/1  -> 0.67
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Once an implicit assertion can reach a throwing handler, an exception may escape an ordinary core-language expression that the `noexcept` operator reports as non-throwing.
candidate 2 (found by 3 of 42 passes): The build-mode dependency does not stay confined to expressions a programmer writes out by hand; it reaches the standard library's own type traits, which query `noexcept` on the expressions they are handed.
candidate 3 (found by 2 of 42 passes): C++26 Contracts let a violation handler throw, and P3100 extends that mechanism to implicit assertions on core-language undefined behavior while holding the noexcept operator's value fixed, narrowing the response to Options A through D.
candidate 4 (found by 2 of 42 passes): Moving the operator's answer would be a source-level breaking change.

## audience - grade 1.67 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      0/0/0  -> 0.00
  [7] 4. Options at a Glance                       0/0/0  -> 0.00
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          0/0/0  -> 0.00
  [10] 7. Additional Options (E, F, G)              2/0/2  -> 1.33
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                1/0/0  -> 0.33
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): libc++ hardening runs the trap response across hundreds of millions of lines at Google [23]
candidate 2 (found by 2 of 42 passes): SG21 took seven polls on the `noexcept` interaction when it discussed P3541R1 in January 2025, and Table 3 reproduces them.
candidate 3 (found by 1 of 42 passes): The terminating, trapping, and aborting shapes of Options B, D, E, and F ship through the `noexcept` boundary, libc++ hardening, and `assert`; Options C and G have prototypes in the contracts forks and in GCC 16.1

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/2  -> 1.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/2/2  -> 1.67
  [5] 2. Introduction                              0/0/0  -> 0.00
  [6] 3. Background and Terms                      2/2/0  -> 1.33
  [7] 4. Options at a Glance                       1/2/1  -> 1.33
  [8] 5. The P3100 Options (A, B, C, D)            0/0/0  -> 0.00
  [9] 6. Option 0 (the foreclosed option)          0/2/2  -> 1.33
  [10] 7. Additional Options (E, F, G)              2/0/2  -> 1.33
  [11] 8. Reading the Comparison                    2/2/2  -> 2.00
  [12] 9. Conclusion                                2/2/2  -> 2.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper restores the foreclosed Option 0, adds E, F, and G, and compares all eight against requirements from P3100R8 and the public record.
candidate 2 (found by 3 of 42 passes): This paper presents all eight against one comparison: six requirements drawn from P3100R8, and five further dimensions from the public record - deployment lineage, security posture, compatibility direction, diagnostics, and implementation experience.
candidate 3 (found by 2 of 42 passes): The options labeled A through D come from [P3100R8](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3100r8.pdf) [1]; the authors characterize that published position, do not speak for its authors, and have written the A-D material to a standard its authors could endorse.
candidate 4 (found by 2 of 42 passes): It builds on the C++26 Contracts facility rather than changing it.

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

## insufficiency - grade 0.33 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
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
  [9] 6. Option 0 (the foreclosed option)          0/0/2  -> 0.67
  [10] 7. Additional Options (E, F, G)              0/0/0  -> 0.00
  [11] 8. Reading the Comparison                    0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The build-mode dependency does not stay confined to expressions a programmer writes out by hand; it reaches the standard library's own type traits, which query `noexcept` on the expressions they are handed.

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
  [12] 9. Conclusion                                1/1/2  -> 1.33
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Of the eight response shapes - throw, terminate, trap, or abort - four are deployed, two have prototypes, and the two that throw are not deployed.
candidate 2 (found by 3 of 42 passes): [D4298R0](https://isocpp.org/files/papers/D4298R0.pdf) [12] specifies exactly these two semantics (as `noexcept-observe` and `noexcept-enforce`) and reports an implementation in the P3850 branches of GCC and Clang on Compiler Explorer.
candidate 3 (found by 3 of 42 passes): D4298R0 is implemented in the P3850 experimental forks of GCC and Clang on Compiler Explorer, not in a release of either compiler [12]
candidate 4 (found by 3 of 42 passes): Four of the eight response shapes are deployed in shipping code, two have prototypes, and the two that throw are not.

-->
