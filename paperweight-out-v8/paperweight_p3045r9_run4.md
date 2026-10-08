Verdict: Excellent (12/14)

The paper offers substantial support for its standardization case across most of the areas that matter, with particularly strong evidence for why the problem matters, who it affects, and what prior art exists. The support is thinnest in explaining why an external library cannot suffice, where the paper asserts the need but does not fully establish it.

- The paper convincingly establishes the importance of preventing unit and dimension errors, with concrete examples of costly failures and strong evidence that the affected developer population numbers in the millions.
- It demonstrates solid implementation experience through the widely adopted mp-units library, including compiler output showing performance parity with raw arithmetic and production feedback describing prevented bugs.
- The case for why this must be in the standard rather than remain a library is asserted through references to company policies and implementation-defined behavior, but the paper does not fully establish that these obstacles cannot be addressed outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 7 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 42. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 10.00   accumulate 14.00   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.67  coordination 1.50  insufficiency 1.33  implementation 2.00
sample agreement: 266 of 294 section-criterion pairs unanimous (90%)
single-sample totals would have been: 13.50 / 12.00 / 12.00   (all 3 samples: 12.00)
headings: h2 23 + bold numbered 13
on threshold: audience, vehicle, coordination, insufficiency
splits: motivation[3] 0/1/1  motivation[6] 0/0/1  motivation[17] 0/2/2  motivation[23] 0/0/1
        motivation[24] 1/2/2  motivation[26] 1/0/1  motivation[31] 0/0/2  motivation[33] 0/2/2
        motivation[34] 2/2/1  audience[29] 1/1/0  prior_art[3] 1/2/1  prior_art[22] 1/0/1
        prior_art[25] 1/1/0  prior_art[37] 0/2/2  vehicle[8] 2/2/0  vehicle[26] 0/0/1
        vehicle[37] 0/1/0  coordination[9] 1/0/1  coordination[30] 1/0/0  coordination[34] 2/0/1
        coordination[40] 0/1/0  insufficiency[17] 0/0/1  insufficiency[31] 2/0/0
        insufficiency[34] 0/1/1  insufficiency[36] 2/1/2  implementation[10] 1/1/2
        implementation[23] 0/2/2  implementation[31] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 28 of 42 sections, strong in 16)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/1  -> 0.67
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/1  -> 0.33
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types  (part 1 of 2)       2/2/2  -> 2.00
  [14] 12 Representation Types  (part 2 of 2)       1/1/1  -> 1.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          0/2/2  -> 1.33
  [18] 16 Systems of quantities and units           2/2/2  -> 2.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             2/2/2  -> 2.00
  [23] 17 Text output  (part 1 of 2)                0/0/1  -> 0.33
  [24] 17 Text output  (part 2 of 2)                1/2/2  -> 1.67
  [25] 18 Core Library Framework scope              1/1/1  -> 1.00
  [26] 1. Core library                              1/0/1  -> 0.67
  [27] 2. Quantity kinds                            2/2/2  -> 2.00
  [28] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [29] 4. The affine space                          2/2/2  -> 2.00
  [30] 5. Text output                               1/1/1  -> 1.00
  [31] 19 Safety                                    0/0/2  -> 0.67
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 0/2/2  -> 1.33
  [34] 1. Ordering                                  2/2/1  -> 1.67
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
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
  [29] 4. The affine space                          1/1/0  -> 0.67
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
  [40] 21 Teachability                              1/1/1  -> 1.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 2 (found by 2 of 126 passes): The Teachability chapter includes audience tables (following [[P1700R0]](https://wg21.link/p1700r0)) that map library features to four distinct user populations: Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 3 (found by 2 of 126 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 4 (found by 2 of 126 passes): | **Application Developers** | millions |

## prior_art - grade 2.00 (fired in 26 of 42 sections, strong in 11)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/2/1  -> 1.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/1/1  -> 1.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Representation Types  (part 1 of 2)       2/2/2  -> 2.00
  [14] 12 Representation Types  (part 2 of 2)       0/0/0  -> 0.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            1/1/1  -> 1.00
  [17] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [18] 16 Systems of quantities and units           1/1/1  -> 1.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             1/0/1  -> 0.67
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
  [37] 4. Repacking  (part 1 of 3)                  0/2/2  -> 1.33
  [38] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              1/1/1  -> 1.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 2 (found by 3 of 126 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 3 (found by 3 of 126 passes): Naming the vector CPO `norm` was considered but rejected: `std::norm` already exists in `<complex>` with a different meaning — it returns |z|² (the squared modulus), not |z|.
candidate 4 (found by 3 of 126 passes): The next example serves as a showcase of various features available in the [[mp-units]](https://mpusz.github.io/mp-units) library.

## vehicle - grade 1.67 (fired in 10 of 42 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/0  -> 1.33
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
  [26] 1. Core library                              0/0/1  -> 0.33
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
  [37] 4. Repacking  (part 1 of 3)                  0/1/0  -> 0.33
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              1/1/1  -> 1.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 126 passes): Deciding to postpone this feature will block us from providing proper SI definitions, as the units of this system should be properly constrained for specific quantity kinds.
candidate 3 (found by 3 of 126 passes): However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.
candidate 4 (found by 3 of 126 passes): If we do not intend to have text output, we should remove symbol text from the core framework class templates.

## coordination - grade 1.50 (fired in 6 of 42 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/0/1  -> 0.67
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
  [30] 5. Text output                               1/0/0  -> 0.33
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  2/0/1  -> 1.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/1/0  -> 0.33
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds
candidate 2 (found by 3 of 126 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 3 (found by 2 of 126 passes): Different code bases choose different ways to encode this information, which may be internally inconsistent.
candidate 4 (found by 2 of 126 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.

## insufficiency - grade 1.33 (fired in 5 of 42 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.67
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
  [17] 15 Why do we need typed quantities?          0/0/1  -> 0.33
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
  [29] 4. The affine space                          0/0/0  -> 0.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/0/0  -> 0.67
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  0/1/1  -> 0.67
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/1/2  -> 1.67
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/0/0  -> 0.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 2 (found by 3 of 126 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 3 (found by 2 of 126 passes): As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list.
candidate 4 (found by 1 of 126 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.

## implementation - grade 2.00  [binary: max] (fired in 13 of 42 sections, strong in 6)
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
  [10] 9 Design goals                               1/1/2  -> 1.33
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
  [22] 4. No conversion                             0/0/0  -> 0.00
  [23] 17 Text output  (part 1 of 2)                0/2/2  -> 1.33
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            0/0/0  -> 0.00
  [28] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [29] 4. The affine space                          0/0/0  -> 0.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/1/2  -> 1.67
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
candidate 1 (found by 3 of 126 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 2 (found by 3 of 126 passes): In practice, the [[mp-units]](https://mpusz.github.io/mp-units) implementation compiles to identical or faster assembly as equivalent code using raw `double` arithmetic — this can be verified via the Compiler Explorer links provided in the Usage examples chapter.
candidate 3 (found by 3 of 126 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 4 (found by 3 of 126 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

-->
