Verdict: Adequate (7/14)

The paper offers meaningful support in the areas that matter most for motivating the change and showing that alternatives were seriously considered, but it leaves several practical and procedural questions unresolved. The thinnest support concerns coordination with the broader ecosystem, proof that a library-only solution is insufficient, and independent evidence of implementation experience.

- The strongest support is the clear motivation for extending `std::simd` beyond built-in types and the documented exploration of alternative designs.
- The paper credibly establishes that prior approaches were considered and tested, including ADL-based customization and implementation-defined sizing.
- The most glaring omission is the absence of any established coordination or interoperability discussion, leaving unclear how this would interact with existing practice or other standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 6.67   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.17  implementation 1.33
sample agreement: 102 of 112 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.00 / 7.00 / 6.00   (all 3 samples: 6.67)
headings: h2 15
on threshold: none
splits: motivation[6] 2/1/2  motivation[8] 0/2/2  motivation[9] 1/0/2  motivation[12] 2/2/1
        audience[5] 1/0/0  prior_art[10] 0/1/0  prior_art[11] 0/1/0  insufficiency[8] 1/0/0
        implementation[8] 0/1/0  implementation[15] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 16 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/1/2  -> 1.67
  [7] 5. Operations on User-Defined Types          2/2/2  -> 2.00
  [8] 6. Customization Points                      0/2/2  -> 1.33
  [9] 7. Implementation Experience                 1/0/2  -> 1.00
  [10] 8. Extended Enum and Byte Support            1/1/1  -> 1.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               2/2/1  -> 1.67
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 1/1/1  -> 1.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This minimal change enables type safety, strong typedefs, enumerations, and `std::byte` while maintaining full backward compatibility.
candidate 2 (found by 3 of 48 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 48 passes): To ensure user-defined types work correctly with `std::simd`, we impose constraints that match hardware capabilities and prevent subtle bugs.
candidate 4 (found by 3 of 48 passes): Unlike operators, which map directly to simple scalar operations that compilers can reliably auto-vectorize, maths functions typically involve internal loops, conditionals, and table lookups that would prevent the compiler from producing efficient vectorized code through element-wise inference.

## audience - grade 0.17 (fired in 1 of 16 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/0/0  -> 0.33
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
candidate 1 (found by 1 of 48 passes): They are widely used for state machines, flags, and encoded data.

## prior_art - grade 2.00 (fired in 8 of 16 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            2/2/2  -> 2.00
  [7] 5. Operations on User-Defined Types          2/2/2  -> 2.00
  [8] 6. Customization Points                      2/2/2  -> 2.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Extended Enum and Byte Support            0/1/0  -> 0.33
  [11] 9. Proposed Wording                          0/1/0  -> 0.33
  [12] 10. Conclusion                               2/2/2  -> 2.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): An alternative design considered was to define the valid sizes as implementation-defined or derived from the sizes of existing vectorizable types.
candidate 2 (found by 3 of 48 passes): In early revisions of this paper, we considered a design where all operations on user-defined types were implemented as customization points discovered via ADL.
candidate 3 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 4 (found by 2 of 48 passes): We considered whether explicit customization points for min/max reductions are needed. The possible approaches are: - Respecify min/max in terms of compare-and-select, routing through the existing `simd_operator` customization for comparisons.

## vehicle - grade 1.00 (fired in 2 of 16 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/1/1  -> 1.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): This proposal allows `simd` to support user-defined types, `std::byte`, enumerations, and other types beyond the current closed list of types.
candidate 2 (found by 2 of 48 passes): The proposal includes ADL-based customization points (`simd_operator` for operations, `simd_convert` for conversions) that enable users to provide optimized implementations where compiler inference is insufficient.
candidate 3 (found by 1 of 48 passes): This proves the approach is viable. Compilers that don’t yet optimize as well will improve over time.
candidate 4 (found by 1 of 48 passes): By changing only the gate-keeping logic for vectorizable types, we enable type safety for strong typedefs, domain-specific types for signal processing and other specialized domains, enumerations, `std::byte`, and small compound types.

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

## insufficiency - grade 0.17 (fired in 1 of 16 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Operations on User-Defined Types          0/0/0  -> 0.00
  [8] 6. Customization Points                      1/0/0  -> 0.33
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               0/0/0  -> 0.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): The customization point provides a guarantee of optimal code generation regardless of compiler sophistication.

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
  [8] 6. Customization Points                      0/1/0  -> 0.33
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Extended Enum and Byte Support            0/0/0  -> 0.00
  [11] 9. Proposed Wording                          0/0/0  -> 0.00
  [12] 10. Conclusion                               1/1/1  -> 1.00
  [13] 11. Acknowledgements                         0/0/0  -> 0.00
  [14] 12. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [15] 13. Appendix: Assembly Code Examples         1/2/1  -> 1.33
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 2 (found by 3 of 48 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 3 (found by 3 of 48 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 4 (found by 2 of 48 passes): This section provides detailed assembly listings from the implementation experience, demonstrating how element-wise inference generates optimal vector code.

-->
