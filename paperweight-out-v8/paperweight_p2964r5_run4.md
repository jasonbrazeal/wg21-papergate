Verdict: Adequate to Strong (7/14)

The paper offers solid support for the core motivation and for having explored plausible alternatives, but its case for standardization is uneven: the argument for why a library solution is insufficient and the evidence of real-world implementation experience are asserted rather than demonstrated, and the coordination story is absent.

- The strongest support is the clear explanation of why the current closed list of element types matters and how the proposed change addresses a real limitation.
- The discussion of rejected alternatives and the relationship to existing ADL-based customization is also well established and helps situate the proposal.
- The thinnest support is the implementation experience, which is repeatedly claimed but never backed by reproducible detail or independent confirmation.
- The most glaring omission is coordination and interoperability, where the paper offers nothing to show how this change fits with related standardization efforts or existing practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.33   accumulate 7.83   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.67  coordination 0.00  insufficiency 0.33  implementation 1.33
sample agreement: 111 of 119 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 8.00 / 7.00   (all 3 samples: 7.50)
headings: h2 16
on threshold: vehicle
splits: motivation[6] 2/2/1  motivation[9] 2/1/1  motivation[15] 1/0/1  audience[13] 0/1/0
        vehicle[8] 1/1/2  insufficiency[7] 0/2/0  implementation[9] 0/0/1
        implementation[16] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 17 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/1  -> 1.67
  [7] 5. Opt-In vs. Opt-Out                        2/2/2  -> 2.00
  [8] 6. Operations on User-Defined Types          2/2/2  -> 2.00
  [9] 7. Customization Points                      2/1/1  -> 1.33
  [10] 8. Implementation Experience                 1/1/1  -> 1.00
  [11] 9. Extended Enum and Byte Support            1/1/1  -> 1.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               2/2/2  -> 2.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 1/0/1  -> 0.67
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): This minimal change opens simd to a wide range of user-defined types while maintaining safety through trait-based constraints.
candidate 2 (found by 3 of 51 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 51 passes): This prevents subtle bugs where user-defined operators return incorrect types.
candidate 4 (found by 3 of 51 passes): The identified limitations motivated the customization design presented in § 7 Customization Points.

## audience - grade 0.17 (fired in 1 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/0/0  -> 0.00
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               0/1/0  -> 0.33
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 51 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.

## prior_art - grade 2.00 (fired in 7 of 17 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Opt-In vs. Opt-Out                        2/2/2  -> 2.00
  [8] 6. Operations on User-Defined Types          2/2/2  -> 2.00
  [9] 7. Customization Points                      2/2/2  -> 2.00
  [10] 8. Implementation Experience                 1/1/1  -> 1.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         1/1/1  -> 1.00
  [13] 11. Conclusion                               1/1/1  -> 1.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): An alternative design considered was to define the valid sizes as implementation-defined or derived from the sizes of existing vectorizable types.
candidate 2 (found by 3 of 51 passes): The possibility of excluding padded types automatically, for instance by means of `has_unique_object_representations`, was considered and rejected.
candidate 3 (found by 3 of 51 passes): A general mechanism to make functions such as `std::sqrt` customizable without that constraint is being developed separately in [P4188] (Extensible Math Functions).
candidate 4 (found by 3 of 51 passes): In early revisions of this paper, we considered a design where all operations on user-defined types were implemented as customization points discovered via ADL.

## vehicle - grade 1.67 (fired in 3 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        2/2/2  -> 2.00
  [8] 6. Operations on User-Defined Types          1/1/2  -> 1.33
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               0/0/0  -> 0.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): By relying on compiler optimization, we can open `simd` to user-defined types without requiring customization points for basic operations.
candidate 2 (found by 3 of 51 passes): This ADL approach is how C++ provides customizable scalar functions today, and `simd` deliberately reuses it rather than inventing a parallel set of `simd`-specific maths customization points.
candidate 3 (found by 1 of 51 passes): Opt-in reverses this arrangement to no advantage. Any type placed on an opt-in list must already be trivially copyable and correctly sized, since otherwise `vec<T>` cannot function, so every entry is a type the constraints already admit.
candidate 4 (found by 1 of 51 passes): The constraints then determine nothing; they cease to act as the gate and become merely a property that each listed type happens to possess.

## coordination - grade 0.00 (fired in 0 of 17 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/0/0  -> 0.00
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               0/0/0  -> 0.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 17 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/2/0  -> 0.67
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               0/0/0  -> 0.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 51 passes): `std::is_trivially_copyable` is not opt-in which makes it very composable.

## implementation - grade 1.33  [binary: max] (fired in 5 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/0/0  -> 0.00
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/0/1  -> 0.33
  [10] 8. Implementation Experience                 1/1/1  -> 1.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               1/1/1  -> 1.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         2/1/1  -> 1.33
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 2 (found by 3 of 51 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 3 (found by 3 of 51 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 4 (found by 2 of 51 passes): Testing was performed with Clang 20 and Intel oneAPI 2025.0 targeting Intel Sapphire Rapids.

-->
