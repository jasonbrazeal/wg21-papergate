Verdict: Strong (8/14)

The paper gives a reasonably clear account of why the change matters and why it belongs in the standard, but its support for the practical and coordination side of the case is much thinner, resting largely on assertions about implementation and compiler behavior rather than demonstrated evidence.

- The strongest support is the explanation of how the proposal fits existing C++ customization mechanisms and why the trait-based gatekeeping change is independently valuable.
- The discussion of prior alternatives is also well grounded, showing that the authors considered and rejected other designs with concrete reasoning.
- The weakest area is implementation experience, where the paper repeatedly cites Intel’s implementation and testing but does not establish enough detail to substantiate the claim.
- The most glaring omission is coordination and interoperability, where the only credited passage discusses an ABI break in a hypothetical type rather than showing how the proposal coordinates with existing or future standard library components.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 7 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.33   accumulate 8.67   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.67  coordination 0.67  insufficiency 0.33  implementation 1.33
sample agreement: 107 of 119 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.00 / 7.50 / 9.00   (all 3 samples: 8.33)
headings: h2 16
on threshold: vehicle
splits: motivation[8] 1/2/2  motivation[9] 0/2/2  audience[10] 0/0/1  audience[13] 0/0/1
        prior_art[9] 0/2/2  prior_art[11] 1/0/0  vehicle[7] 2/0/2  vehicle[13] 1/0/1
        coordination[7] 2/2/0  insufficiency[7] 0/0/2  implementation[7] 0/1/0
        implementation[16] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 17 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Opt-In vs. Opt-Out                        2/2/2  -> 2.00
  [8] 6. Operations on User-Defined Types          1/2/2  -> 1.67
  [9] 7. Customization Points                      0/2/2  -> 1.33
  [10] 8. Implementation Experience                 2/2/2  -> 2.00
  [11] 9. Extended Enum and Byte Support            1/1/1  -> 1.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               2/2/2  -> 2.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 1/1/1  -> 1.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): This minimal change opens simd to a wide range of user-defined types while maintaining safety through trait-based constraints.
candidate 2 (found by 3 of 51 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 51 passes): To ensure user-defined types work correctly with `std::simd`, we impose constraints that match hardware capabilities and prevent subtle bugs.
candidate 4 (found by 3 of 51 passes): These provide consistency with their scalar counterparts and convenience for common conversions.

## audience - grade 0.33 (fired in 2 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
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
  [10] 8. Implementation Experience                 0/0/1  -> 0.33
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               0/0/1  -> 0.33
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 51 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 2 (found by 1 of 51 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.

## prior_art - grade 2.00 (fired in 7 of 17 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Opt-In vs. Opt-Out                        2/2/2  -> 2.00
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/2/2  -> 1.33
  [10] 8. Implementation Experience                 1/1/1  -> 1.00
  [11] 9. Extended Enum and Byte Support            1/0/0  -> 0.33
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               2/2/2  -> 2.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Heterogeneous operations would require changing `simd` itself and would introduce fundamentally different design problems that do not arise in this proposal:
candidate 2 (found by 3 of 51 passes): An alternative design considered was to define the valid sizes as implementation-defined or derived from the sizes of existing vectorizable types.
candidate 3 (found by 3 of 51 passes): The possibility of excluding padded types automatically, for instance by means of `has_unique_object_representations`, was considered and rejected.
candidate 4 (found by 3 of 51 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.

## vehicle - grade 1.67 (fired in 4 of 17 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        2/0/2  -> 1.33
  [8] 6. Operations on User-Defined Types          2/2/2  -> 2.00
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               1/0/1  -> 0.67
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): This ADL approach is how C++ provides customizable scalar functions today, and `simd` deliberately reuses it rather than inventing a parallel set of `simd`-specific maths customization points.
candidate 2 (found by 2 of 51 passes): The constraints then determine nothing; they cease to act as the gate and become merely a property that each listed type happens to possess.
candidate 3 (found by 2 of 51 passes): By changing only the gate-keeping logic for vectorizable types, we enable type safety for strong typedefs, domain-specific types for signal processing and other specialized domains, enumerations, `std::byte`, and small compound types.
candidate 4 (found by 1 of 51 passes): The trait-based gatekeeper change provides substantial value independently, enabling these use cases without requiring the committee to solve significantly harder problems.

## coordination - grade 0.67 (fired in 1 of 17 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        2/2/0  -> 1.33
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
candidate 1 (found by 1 of 51 passes): Removing a byte from `rgb` is an ABI-breaking change to `rgb` itself, made by its author, and it disrupts every contiguous or aggregate use of the type in the same manner:
candidate 2 (found by 1 of 51 passes): Removing a byte from `rgb` is an ABI-breaking change to `rgb` itself, made by its author, and it disrupts every contiguous or aggregate use of the type in the same manner.

## insufficiency - grade 0.33 (fired in 1 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/0/2  -> 0.67
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
candidate 1 (found by 1 of 51 passes): The constraints then determine nothing; they cease to act as the gate and become merely a property that each listed type happens to possess.

## implementation - grade 1.33  [binary: max] (fired in 5 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/1/0  -> 0.33
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 1/1/1  -> 1.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               1/1/1  -> 1.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         2/1/1  -> 1.33
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 2 (found by 3 of 51 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 3 (found by 2 of 51 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 4 (found by 2 of 51 passes): Testing was performed with Clang 20 and Intel oneAPI 2025.0 targeting Intel Sapphire Rapids.

-->
