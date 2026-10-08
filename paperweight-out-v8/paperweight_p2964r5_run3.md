Verdict: Adequate to Strong (7/14)

The paper offers a solid conceptual case for why user-defined element types would matter and shows that the design space has been explored, but it leans heavily on implementation claims that are asserted rather than demonstrated in the document itself. The thinnest areas are the absence of any coordination or interoperability discussion and the reliance on the same brief compiler references to carry several distinct burdens.

- The strongest support is the clear explanation of the current closed type list and the motivation for opening it through trait-based constraints.
- The discussion of rejected alternatives and the relationship to separate math-function work establishes that the proposed shape is deliberate rather than accidental.
- The paper repeatedly cites implementation experience with Clang and Intel oneAPI, but provides too little detail for that experience to count as established evidence.
- The most glaring omission is any treatment of coordination and interoperability with other proposals, implementations, or the broader SIMD ecosystem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.33   accumulate 7.17   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.67  implementation 1.00
sample agreement: 108 of 119 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.00 / 7.50 / 6.00   (all 3 samples: 6.83)
headings: h2 16
on threshold: none
splits: motivation[6] 1/2/2  motivation[9] 2/2/1  motivation[10] 0/1/1  motivation[13] 1/2/2
        motivation[15] 0/1/0  audience[13] 1/0/0  vehicle[4] 0/1/0  vehicle[7] 0/2/2
        vehicle[8] 0/1/0  vehicle[13] 1/1/0  insufficiency[7] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 17 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            1/2/2  -> 1.67
  [7] 5. Opt-In vs. Opt-Out                        2/2/2  -> 2.00
  [8] 6. Operations on User-Defined Types          2/2/2  -> 2.00
  [9] 7. Customization Points                      2/2/1  -> 1.67
  [10] 8. Implementation Experience                 0/1/1  -> 0.67
  [11] 9. Extended Enum and Byte Support            1/1/1  -> 1.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               1/2/2  -> 1.67
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/1/0  -> 0.33
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): This minimal change opens simd to a wide range of user-defined types while maintaining safety through trait-based constraints.
candidate 2 (found by 3 of 51 passes): The C++ standard library includes data-parallel types in the `<simd>` header, currently restricting element types to a closed list of *built-in vectorizable* types: arithmetic types and `std::complex` specializations.
candidate 3 (found by 3 of 51 passes): To ensure user-defined types work correctly with `std::simd`, we impose constraints that match hardware capabilities and prevent subtle bugs.
candidate 4 (found by 3 of 51 passes): These provide consistency with their scalar counterparts and convenience for common conversions.

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
  [13] 11. Conclusion                               1/0/0  -> 0.33
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

## vehicle - grade 1.00 (fired in 4 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/2/2  -> 1.33
  [8] 6. Operations on User-Defined Types          0/1/0  -> 0.33
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               1/1/0  -> 0.67
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): The constraints then determine nothing; they cease to act as the gate and become merely a property that each listed type happens to possess.
candidate 2 (found by 2 of 51 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 3 (found by 1 of 51 passes): This paper proposes a minimal change to the specification in which this list is extended.
candidate 4 (found by 1 of 51 passes): This ADL approach is how C++ provides customizable scalar functions today, and `simd` deliberately reuses it rather than inventing a parallel set of `simd`-specific maths customization points.

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

## insufficiency - grade 0.67 (fired in 1 of 17 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 1 of 51 passes): The constraints then determine nothing; they cease to act as the gate and become merely a property that each listed type happens to possess.
candidate 2 (found by 1 of 51 passes): The operations of `vec<T>` are simply `T`’s own operators applied lane by lane, so default element-wise behaviour is never semantically wrong.

## implementation - grade 1.00  [binary: max] (fired in 4 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Understanding Type Constraints            0/0/0  -> 0.00
  [7] 5. Opt-In vs. Opt-Out                        0/0/0  -> 0.00
  [8] 6. Operations on User-Defined Types          0/0/0  -> 0.00
  [9] 7. Customization Points                      0/0/0  -> 0.00
  [10] 8. Implementation Experience                 1/1/1  -> 1.00
  [11] 9. Extended Enum and Byte Support            0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] 11. Conclusion                               1/1/1  -> 1.00
  [14] 12. Acknowledgements                         0/0/0  -> 0.00
  [15] 13. Appendix: Customization Point Technic... 0/0/0  -> 0.00
  [16] 14. Appendix: Assembly Code Examples         1/1/1  -> 1.00
  [17] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): To address these concerns we implemented our proposal in Intel’s `std::simd` implementation and tested it across multiple generations of Intel architectures with various user-defined types, enumerations, strong typedefs, and specialized DSP types (saturating arithmetic and fixed-point).
candidate 2 (found by 3 of 51 passes): We implemented this approach in Intel’s `std::simd` implementation and tested across multiple Intel architectures.
candidate 3 (found by 3 of 51 passes): Implementation experience with leading compilers (Clang 20, Intel oneAPI 2025.0) has shown that they can.
candidate 4 (found by 2 of 51 passes): Testing was performed with Clang 20 and Intel oneAPI 2025.0 targeting Intel Sapphire Rapids.

-->
