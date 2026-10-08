Verdict: Adequate (6/14)

The paper offers meaningful support in its motivation and its exploration of prior approaches, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest areas concern who would be affected by the change, how it would interact with existing practice, and why the work cannot be delivered as a library rather than a core language or specification change.

- The strongest support is the clear explanation of why opening `std::simd` to user-defined types matters for type safety and consistency with existing library types.
- The paper also establishes that alternatives were considered and that a simpler compiler-driven approach was chosen after earlier customization-point designs proved too complicated.
- The most glaring omission is the absence of any established account of who is affected, which leaves the audience and impact of the proposal unclear.
- Equally unestablished are coordination and interoperability concerns, as well as any argument for why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 102 of 112 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.50 / 5.50 / 6.00   (all 3 samples: 6.00)
headings: h2 15
on threshold: none
splits: motivation[9] 1/2/2  motivation[14] 0/1/1  prior_art[2] 1/0/1  prior_art[3] 0/0/1
        prior_art[10] 0/1/0  prior_art[11] 1/0/1  vehicle[4] 0/1/1  vehicle[12] 1/0/1
        implementation[4] 2/1/1  implementation[8] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 16 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            1/1/1  -> 1.00
  [7] 5. Operations on User-Defined Types          2/2/2  -> 2.00
  [8] 6. Customization Points                      2/2/2  -> 2.00
  [9] 7. Implementation Experience                 1/2/2  -> 1.67
  [10] 8. Extended Enum and Byte Support            1/1/1  -> 1.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               2/2/2  -> 2.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/1/1  -> 0.67
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This minimal change enables type safety, strong typedefs, enumerations, and `std::byte` while maintaining full backward compatibility.
candidate 2 (found by 3 of 48 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 48 passes): To ensure user-defined types work correctly with `std::simd`, we impose constraints that match hardware capabilities and prevent subtle bugs.
candidate 4 (found by 3 of 48 passes): This prevents subtle bugs where user-defined operators return incorrect types.

## audience - grade 0.00 (fired in 0 of 16 sections, strong in 0)
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

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Revision History                          0/0/1  -> 0.33
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Operations on User-Defined Types          2/2/2  -> 2.00
  [8] 6. Customization Points                      2/2/2  -> 2.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Extended Enum and Byte Support            0/1/0  -> 0.33
  [11] 9. Proposed Wording                          1/0/1  -> 0.67
  [12] 10. Conclusion                               1/1/1  -> 1.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): We considered whether explicit customization points for min/max reductions are needed. The possible approaches are:
candidate 2 (found by 3 of 48 passes): In early revisions of this paper, we considered a design where all operations on user-defined types were implemented as customization points discovered via ADL.
candidate 3 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 4 (found by 3 of 48 passes): Earlier revisions explored explicit customization mechanisms, leading to complicated designs.

## vehicle - grade 0.67 (fired in 2 of 16 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/0/1  -> 0.67
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The proposal includes ADL-based customization points (`simd_operator` for operations, `simd_convert` for conversions) that enable users to provide optimized implementations where compiler inference is insufficient.
candidate 2 (found by 1 of 48 passes): By relying on compiler optimization, we can open `simd` to user-defined types without requiring customization points for basic operations.
candidate 3 (found by 1 of 48 passes): This proves the approach is viable. Compilers that don’t yet optimize as well will improve over time.

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

## implementation - grade 1.33  [binary: max] (fired in 5 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/1/1  -> 1.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      1/0/1  -> 0.67
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
candidate 4 (found by 2 of 48 passes): As shown in the implementation experience section (§ 7 Implementation Experience), leading compilers can often auto-vectorize such operations into the same hardware instructions.

-->
