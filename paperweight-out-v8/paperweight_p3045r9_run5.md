Verdict: Excellent (13/14)

The paper offers substantial support for its own standardization, with nearly every required element backed by concrete evidence from implementation experience, community adoption, and recognized standards bodies. The support is thinnest where the paper relies on assertions about industry impact and certification requirements without always connecting those claims to specific standardization outcomes.

- The strongest support comes from implementation experience, where the mp-units library demonstrates production maturity, broad adoption, and assembly-level performance parity with raw arithmetic.
- The paper also clearly establishes why a library alone will not suffice, citing certification requirements, MISRA compliance policies, and the unique safety guarantees that only a standardized specification can anchor.
- The most glaring omission is that the paper does not fully establish why the standard itself is necessary beyond the existence of a successful library, leaving some arguments as claims rather than demonstrated standardization needs.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.67/14)

Provisionally addressed: 7 of 7. Provisional points: 12.67 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 42. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.67   corroborated 11.00   accumulate 14.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 1.50  insufficiency 1.67  implementation 2.00
sample agreement: 268 of 294 section-criterion pairs unanimous (91%)
single-sample totals would have been: 13.00 / 13.00 / 12.50   (all 3 samples: 12.67)
headings: h2 23 + bold numbered 13
on threshold: audience, coordination, insufficiency
splits: motivation[7] 0/1/0  motivation[14] 2/0/0  motivation[24] 1/2/2  motivation[26] 1/0/0
        motivation[29] 2/2/1  motivation[31] 0/2/2  motivation[34] 1/1/2  motivation[37] 1/2/0
        audience[40] 0/1/1  prior_art[3] 2/2/0  prior_art[7] 0/1/0  prior_art[14] 0/2/2
        prior_art[22] 0/2/0  prior_art[25] 1/1/0  vehicle[40] 2/1/1  coordination[3] 1/0/0
        coordination[13] 0/0/1  coordination[28] 0/0/1  coordination[30] 0/1/1
        insufficiency[29] 0/0/1  insufficiency[31] 2/2/0  insufficiency[34] 1/0/0
        insufficiency[37] 0/1/0  implementation[7] 0/2/2  implementation[22] 0/0/1
        implementation[23] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 28 of 42 sections, strong in 16)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/1/0  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       2/2/2  -> 2.00
  [14] 12 Representation Types  (part 2 of 2)       2/0/0  -> 0.67
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [18] 16 Systems of quantities and units           2/2/2  -> 2.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             2/2/2  -> 2.00
  [23] 17 Text output  (part 1 of 2)                1/1/1  -> 1.00
  [24] 17 Text output  (part 2 of 2)                1/2/2  -> 1.67
  [25] 18 Core Library Framework scope              1/1/1  -> 1.00
  [26] 1. Core library                              1/0/0  -> 0.33
  [27] 2. Quantity kinds                            2/2/2  -> 2.00
  [28] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [29] 4. The affine space                          2/2/1  -> 1.67
  [30] 5. Text output                               1/1/1  -> 1.00
  [31] 19 Safety                                    0/2/2  -> 1.33
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [34] 1. Ordering                                  1/1/2  -> 1.33
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  1/2/0  -> 1.00
  [38] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              2/2/2  -> 2.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
candidate 2 (found by 3 of 126 passes): Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.
candidate 3 (found by 3 of 126 passes): The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.
candidate 4 (found by 3 of 126 passes): The library tracks **character in the quantity specification** (what the quantity represents) and verifies that the **representation type provides the required capabilities**.

## audience - grade 1.50 (fired in 4 of 42 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       0/0/0  -> 0.00
  [14] 12 Representation Types  (part 2 of 2)       0/0/0  -> 0.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [18] 16 Systems of quantities and units           0/0/0  -> 0.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/0/0  -> 0.00
  [23] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            0/0/0  -> 0.00
  [28] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  0/0/0  -> 0.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/1/1  -> 0.67
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 2 (found by 2 of 126 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 3 (found by 2 of 126 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 4 (found by 2 of 126 passes): Through the last years [[mp-units]](https://mpusz.github.io/mp-units) library proved to be very intuitive to both novices in the domain and non-C++ experts.

## prior_art - grade 2.00 (fired in 28 of 42 sections, strong in 13)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/0  -> 1.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 2/2/2  -> 2.00
  [7] 6 About authors                              0/1/0  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Representation Types  (part 1 of 2)       2/2/2  -> 2.00
  [14] 12 Representation Types  (part 2 of 2)       0/2/2  -> 1.33
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            1/1/1  -> 1.00
  [17] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [18] 16 Systems of quantities and units           1/1/1  -> 1.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/2/0  -> 0.67
  [23] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [24] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [25] 18 Core Library Framework scope              1/1/0  -> 0.67
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            1/1/1  -> 1.00
  [28] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [34] 1. Ordering                                  1/1/1  -> 1.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              1/1/1  -> 1.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 2 (found by 3 of 126 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 3 (found by 3 of 126 passes): Naming the vector CPO `norm` was considered but rejected: `std::norm` already exists in `<complex>` with a different meaning — it returns |z|² (the squared modulus), not |z|.
candidate 4 (found by 3 of 126 passes): The next example serves as a showcase of various features available in the [[mp-units]](https://mpusz.github.io/mp-units) library.

## vehicle - grade 2.00 (fired in 8 of 42 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       0/0/0  -> 0.00
  [14] 12 Representation Types  (part 2 of 2)       0/0/0  -> 0.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [18] 16 Systems of quantities and units           0/0/0  -> 0.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/0/0  -> 0.00
  [23] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            1/1/1  -> 1.00
  [28] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               1/1/1  -> 1.00
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  1/1/1  -> 1.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              2/1/1  -> 1.33
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 126 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 3 of 126 passes): However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.
candidate 4 (found by 3 of 126 passes): If we do not intend to have text output, we should remove symbol text from the core framework class templates.

## coordination - grade 1.50 (fired in 8 of 42 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/0  -> 0.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       0/0/1  -> 0.33
  [14] 12 Representation Types  (part 2 of 2)       0/0/0  -> 0.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [18] 16 Systems of quantities and units           0/0/0  -> 0.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/0/0  -> 0.00
  [23] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            0/0/0  -> 0.00
  [28] 3. Various quantities of the same kind       0/0/1  -> 0.33
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               0/1/1  -> 0.67
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  1/1/1  -> 1.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/0/0  -> 0.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds
candidate 2 (found by 3 of 126 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 3 (found by 2 of 126 passes): Different code bases choose different ways to encode this information, which may be internally inconsistent.
candidate 4 (found by 2 of 126 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.

## insufficiency - grade 1.67 (fired in 6 of 42 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 1/1/1  -> 1.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       0/0/0  -> 0.00
  [14] 12 Representation Types  (part 2 of 2)       0/0/0  -> 0.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [18] 16 Systems of quantities and units           0/0/0  -> 0.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/0/0  -> 0.00
  [23] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            0/0/0  -> 0.00
  [28] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [29] 4. The affine space                          0/0/1  -> 0.33
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/2/0  -> 1.33
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  1/0/0  -> 0.33
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  0/1/0  -> 0.33
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/0/0  -> 0.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 2 (found by 2 of 126 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 2 of 126 passes): [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.
candidate 4 (found by 1 of 126 passes): Such certification requires a specification to be certified against, and those tools often do not have one.

## implementation - grade 2.00  [binary: max] (fired in 15 of 42 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/2/2  -> 1.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               2/2/2  -> 2.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       0/0/0  -> 0.00
  [14] 12 Representation Types  (part 2 of 2)       0/0/0  -> 0.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            2/2/2  -> 2.00
  [17] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [18] 16 Systems of quantities and units           0/0/0  -> 0.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/0/1  -> 0.33
  [23] 17 Text output  (part 1 of 2)                0/2/2  -> 1.33
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            0/0/0  -> 0.00
  [28] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [29] 4. The affine space                          0/0/0  -> 0.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 1 ... 1/1/1  -> 1.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  0/0/0  -> 0.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              1/1/1  -> 1.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): In the following years, the library’s authors focused on getting more feedback from the production about the design and developed version 2 of the [[mp-units]](https://mpusz.github.io/mp-units) library that resolves the issues raised by the users and Committee members.
candidate 2 (found by 3 of 126 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 3 (found by 3 of 126 passes): In practice, the [[mp-units]](https://mpusz.github.io/mp-units) implementation compiles to identical or faster assembly as equivalent code using raw `double` arithmetic — this can be verified via the Compiler Explorer links provided in the Usage examples chapter.
candidate 4 (found by 3 of 126 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).

-->
