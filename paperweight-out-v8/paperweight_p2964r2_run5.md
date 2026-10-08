Verdict: Adequate to Strong (7/14)

The paper gives a reasonably grounded account of why the change would be useful and that it can be implemented, but it leaves several parts of the standardization case asserted rather than demonstrated, especially around the need for a standard rather than a library solution and how the feature would fit with existing practice.

- The strongest support is the implementation experience, which shows the approach working in a real `std::simd` implementation across multiple architectures and with user-defined types.
- The paper also establishes a clear motivation and prior art, including committee feedback and related proposals, for moving from a closed type list to trait-based constraints.
- The case for who is affected is thinner, since the cited testing is limited to specific compilers and one target architecture without broader evidence about the user population.
- The most glaring omission is the absence of any established argument for why this cannot be done as a library or why standardization, rather than a vendor extension or library facility, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.33   accumulate 7.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.83  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 103 of 112 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.50 / 7.00 / 6.50   (all 3 samples: 6.83)
headings: h2 15
on threshold: implementation
splits: motivation[6] 1/2/2  motivation[7] 1/2/1  motivation[14] 1/1/0  audience[8] 1/0/0
        prior_art[2] 0/1/0  prior_art[8] 1/2/1  prior_art[12] 2/1/2  prior_art[14] 1/1/0
        vehicle[12] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            1/2/2  -> 1.67
  [7] 5. Operations on User-Defined Types          1/2/1  -> 1.33
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Design Alternative: Customization Points  0/0/0  -> 0.00
  [10] 8. Design Options for Enum and Byte Support  1/1/1  -> 1.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               2/2/2  -> 2.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 1/1/0  -> 0.67
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This minimal change enables type safety, strong typedefs, enumerations, and `std::byte` while maintaining full backward compatibility.
candidate 2 (found by 3 of 48 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 48 passes): This prevents subtle bugs where user-defined operators return incorrect types.
candidate 4 (found by 3 of 48 passes): These provide consistency with their scalar counterparts and convenience for common conversions.

## audience - grade 0.17 (fired in 1 of 16 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/0/0  -> 0.33
  [9] 7. Design Alternative: Customization Points  0/0/0  -> 0.00
  [10] 8. Design Options for Enum and Byte Support  0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): Testing was performed with Clang 20 and Intel oneAPI 2025.0 targeting Intel Sapphire Rapids.

## prior_art - grade 1.83 (fired in 9 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          1/1/1  -> 1.00
  [8] 6. Implementation Experience                 1/2/1  -> 1.33
  [9] 7. Design Alternative: Customization Points  1/1/1  -> 1.00
  [10] 8. Design Options for Enum and Byte Support  1/1/1  -> 1.00
  [11] 9. Proposed Wording                          1/1/1  -> 1.00
  [12] 10. Conclusion                               2/1/2  -> 1.67
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 1/1/0  -> 0.67
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Committee feedback encouraged us to explore element-wise inference instead, making use of the Working Draft’s wording in which everything is defined in terms of element operations and element-wise application of those operations.
candidate 2 (found by 3 of 48 passes): The identified limitations motivated the customization design presented in § 7 Design Alternative: Customization Points.
candidate 3 (found by 3 of 48 passes): These provide consistency with their scalar counterparts and convenience for common conversions.
candidate 4 (found by 3 of 48 passes): [P4006] proposes adding `bit_lshift<>` and `bit_rshift<>` function objects for the shift operators.

## vehicle - grade 0.83 (fired in 2 of 16 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Design Alternative: Customization Points  0/0/0  -> 0.00
  [10] 8. Design Options for Enum and Byte Support  0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/1/0  -> 0.67
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): By relying on compiler optimization, we can open `simd` to user-defined types without requiring customization points for basic operations.
candidate 2 (found by 1 of 48 passes): By changing only the gate-keeping logic for vectorizable types, we enable type safety for strong typedefs, domain-specific types for signal processing and other specialized domains, enumerations, `std::byte`, and small compound types.
candidate 3 (found by 1 of 48 passes): This proposal extends `std::simd` to support user-defined element types through a minimal, principled change where the closed list of vectorizable types is replaced with trait-based constraints.

## coordination - grade 0.00 (fired in 0 of 16 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Design Alternative: Customization Points  0/0/0  -> 0.00
  [10] 8. Design Options for Enum and Byte Support  0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 16 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Design Alternative: Customization Points  0/0/0  -> 0.00
  [10] 8. Design Options for Enum and Byte Support  0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Design Alternative: Customization Points  1/1/1  -> 1.00
  [10] 8. Design Options for Enum and Byte Support  0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/1/1  -> 1.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         2/2/2  -> 2.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 2 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 3 (found by 3 of 48 passes): Implementation experience demonstrated that element-wise inference produces correct, performant code for most operations.
candidate 4 (found by 3 of 48 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.

-->
