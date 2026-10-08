Verdict: Adequate (6/14)

The paper offers a reasonably clear motivation for opening `std::simd` to user-defined types and shows that plausible alternatives were considered, but it leaves several essential parts of the standardization case largely asserted rather than demonstrated. The thinnest support concerns why this cannot be done outside the standard and how the change would coordinate with existing library and language machinery.

- The strongest support is the explanation of the type-safety and consistency problems that the current closed set of vectorizable types creates.
- The discussion of rejected design alternatives, including ADL-based customization and implementation-defined sizes, is credited as established prior art.
- The paper claims implementation experience and compiler support, but does not establish them in enough detail to carry the standardization argument.
- The most glaring omission is the absence of any established case for why a library solution would not suffice or how the proposal coordinates with the broader standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.33   accumulate 6.00   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 104 of 112 section-criterion pairs unanimous (93%)
single-sample totals would have been: 5.00 / 6.00 / 7.00   (all 3 samples: 6.00)
headings: h2 15
on threshold: none
splits: motivation[8] 2/1/2  motivation[9] 1/2/1  audience[9] 0/0/1  prior_art[10] 1/0/0
        vehicle[4] 0/1/1  vehicle[12] 0/1/0  implementation[8] 0/0/1  implementation[15] 1/1/2
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
  [8] 6. Customization Points                      2/1/2  -> 1.67
  [9] 7. Implementation Experience                 1/2/1  -> 1.33
  [10] 8. Extended Enum and Byte Support            1/1/1  -> 1.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               2/2/2  -> 2.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 1/1/1  -> 1.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This minimal change enables type safety, strong typedefs, enumerations, and `std::byte` while maintaining full backward compatibility.
candidate 2 (found by 3 of 48 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 48 passes): This prevents subtle bugs where user-defined operators return incorrect types.
candidate 4 (found by 3 of 48 passes): These provide consistency with their scalar counterparts and convenience for common conversions.

## audience - grade 0.17 (fired in 1 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/1  -> 0.33
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.

## prior_art - grade 2.00 (fired in 7 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
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
candidate 2 (found by 3 of 48 passes): In early revisions of this paper, we considered a design where all operations on user-defined types were implemented as customization points discovered via ADL.
candidate 3 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 4 (found by 3 of 48 passes): Shift operators are not listed because the C++ standard library does not currently provide transparent function objects for them. See [P4006].

## vehicle - grade 0.50 (fired in 2 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
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
  [12] 10. Conclusion                               0/1/0  -> 0.33
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): By relying on compiler optimization, we can open `simd` to user-defined types without requiring customization points for basic operations.
candidate 2 (found by 1 of 48 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.

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
  [15] 13. Appendix: Assembly Code Examples         1/1/2  -> 1.33
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 2 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 3 (found by 3 of 48 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 4 (found by 2 of 48 passes): This section provides detailed assembly listings from the implementation experience, demonstrating how element-wise inference generates optimal vector code.

-->
