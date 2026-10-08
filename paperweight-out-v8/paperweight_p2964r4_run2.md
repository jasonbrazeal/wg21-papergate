Verdict: Adequate (6/14)

The paper offers solid support for the core motivation and for having considered realistic alternatives, but its case thins considerably when it comes to showing that the feature belongs in the standard rather than in a library and that it will interoperate cleanly with existing practice. The implementation experience is asserted more than demonstrated in the credited passages, and the affected audience is described only in general terms.

- The strongest part of the paper is its clear explanation of why the change matters, including the concrete limitation in `<simd>` and the risk of subtle type errors without the customization.
- The discussion of prior art and alternatives is also well established, showing that the authors examined several plausible designs and tested one in a real implementation.
- The paper only claims, without fully establishing, that the affected community is significant and that standardization is necessary rather than achievable through a library solution.
- The most glaring omission is the complete lack of established coordination and interoperability, leaving open how the proposal fits with existing and adjacent standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.67   accumulate 6.17   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 103 of 112 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 6.50 / 5.50   (all 3 samples: 6.00)
headings: h2 15
on threshold: none
splits: motivation[12] 1/2/2  motivation[14] 0/1/1  audience[5] 1/1/0  prior_art[2] 0/1/0
        prior_art[4] 2/0/0  prior_art[10] 1/0/0  vehicle[8] 0/1/0  vehicle[12] 0/1/0
        implementation[8] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 16 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Operations on User-Defined Types          2/2/2  -> 2.00
  [8] 6. Customization Points                      2/2/2  -> 2.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Extended Enum and Byte Support            1/1/1  -> 1.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/2/2  -> 1.67
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/1/1  -> 0.67
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This minimal change enables type safety, strong typedefs, enumerations, and `std::byte` while maintaining full backward compatibility.
candidate 2 (found by 3 of 48 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 48 passes): This prevents subtle bugs where user-defined operators return incorrect types.
candidate 4 (found by 3 of 48 passes): Without the customization, element-wise inference would apply the scalar `operator+` to each element. As shown in the implementation experience section (§ 7 Implementation Experience), leading compilers can often auto-vectorize such operations into the same hardware instructions.

## audience - grade 0.33 (fired in 1 of 16 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/0  -> 0.67
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): Physical units, identifiers, and other domain-specific types are commonly wrapped in strong typedefs to prevent semantic errors

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/0/0  -> 0.67
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Operations on User-Defined Types          2/2/2  -> 2.00
  [8] 6. Customization Points                      2/2/2  -> 2.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Extended Enum and Byte Support            1/0/0  -> 0.33
  [11] 9. Proposed Wording                          1/1/1  -> 1.00
  [12] 10. Conclusion                               1/1/1  -> 1.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): An alternative design considered was to define the valid sizes as implementation-defined or derived from the sizes of existing vectorizable types.
candidate 2 (found by 3 of 48 passes): We considered whether explicit customization points for min/max reductions are needed. The possible approaches are: - Respecify min/max in terms of compare-and-select, routing through the existing `simd_operator` customization for comparisons.
candidate 3 (found by 3 of 48 passes): In early revisions of this paper, we considered a design where all operations on user-defined types were implemented as customization points discovered via ADL.
candidate 4 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.

## vehicle - grade 0.67 (fired in 3 of 16 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      0/1/0  -> 0.33
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/1/0  -> 0.33
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): Compilers that don’t yet optimize as well will improve over time.
candidate 2 (found by 1 of 48 passes): Implementation experience (§ 7 Implementation Experience) demonstrates that with current leading compilers (Clang and Intel oneAPI), these types can generate assembly identical to built-in arithmetic types for standard operations.
candidate 3 (found by 1 of 48 passes): This paper proposes a minimal change to the specification in which this list is extended.
candidate 4 (found by 1 of 48 passes): The customization point provides a guarantee of optimal code generation regardless of compiler sophistication.

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
  [8] 6. Customization Points                      0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
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
  [8] 6. Customization Points                      0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 5 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      0/0/1  -> 0.33
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/1/1  -> 1.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         1/1/1  -> 1.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 2 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 3 (found by 3 of 48 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 4 (found by 2 of 48 passes): This section provides detailed assembly listings from the implementation experience, demonstrating how element-wise inference generates optimal vector code.

-->
