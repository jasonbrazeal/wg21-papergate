Verdict: Excellent (13/14)

The paper offers substantial support for standardizing its proposed library, with strong evidence of committee interest, real-world impact, affected audiences, prior art, and implementation experience. The thinnest part of its case is the argument that a library alone will not suffice, which is asserted more than demonstrated.

- The strongest support comes from documented committee engagement, production feedback, and widespread adoption of the underlying libraries, showing both demand and practical viability.
- The paper clearly identifies who would benefit and why standardization matters, including concrete failure cases and endorsements from bodies like BSI.
- Prior art and interoperability concerns are well covered, with explicit references to existing standards and mechanisms for cross-library compatibility.
- The most glaring omission is a convincing explanation of why an out-of-standard library cannot adequately address the need, since the paper claims this but does not establish it with evidence.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.83/14)

Provisionally addressed: 7 of 7. Provisional points: 12.83 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 41. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.83   corroborated 12.00   accumulate 14.00   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.33  implementation 2.00
sample agreement: 252 of 287 section-criterion pairs unanimous (88%)
single-sample totals would have been: 13.50 / 13.00 / 12.50   (all 3 samples: 12.83)
headings: h2 23 + bold numbered 13
on threshold: audience, insufficiency
splits: motivation[6] 0/0/1  motivation[7] 0/1/1  motivation[12] 2/2/0  motivation[13] 0/2/0
        motivation[16] 2/0/0  motivation[17] 1/2/2  motivation[23] 2/1/2  motivation[32] 0/0/2
        motivation[36] 2/2/0  audience[27] 0/0/1  audience[36] 1/0/0  audience[39] 0/0/1
        prior_art[3] 0/2/2  prior_art[5] 0/1/0  prior_art[9] 0/1/1  prior_art[10] 2/2/1
        prior_art[21] 2/0/0  prior_art[27] 0/1/0  prior_art[37] 2/0/2  vehicle[10] 0/1/1
        vehicle[25] 0/0/1  vehicle[39] 1/2/2  coordination[27] 1/0/1  coordination[29] 0/1/1
        coordination[33] 2/1/2  coordination[39] 0/1/0  insufficiency[16] 2/0/1
        insufficiency[26] 1/0/0  insufficiency[28] 1/0/1  insufficiency[30] 2/2/1
        insufficiency[32] 0/0/1  insufficiency[33] 0/0/1  implementation[10] 1/2/2
        implementation[21] 0/1/1  implementation[38] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 27 of 41 sections, strong in 14)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/1  -> 0.33
  [7] 6 About authors                              0/1/1  -> 0.67
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              2/2/0  -> 1.33
  [13] 12 Representation Types                      0/2/0  -> 0.67
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          2/0/0  -> 0.67
  [17] 16 Systems of quantities and units           1/2/2  -> 1.67
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             2/2/2  -> 2.00
  [22] 17 Text output  (part 1 of 2)                1/1/1  -> 1.00
  [23] 17 Text output  (part 2 of 2)                2/1/2  -> 1.67
  [24] 18 Core Library Framework scope              1/1/1  -> 1.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            2/2/2  -> 2.00
  [27] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [28] 4. The affine space                          2/2/2  -> 2.00
  [29] 5. Text output                               1/1/1  -> 1.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/2  -> 0.67
  [33] 1. Ordering                                  2/2/2  -> 2.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/0  -> 1.33
  [37] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              2/2/2  -> 2.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Several groups in the ISO C++ Committee reviewed the “P1935: A C++ Approach to Physical Units” proposal in Belfast 2019 and Prague 2020. All those groups expressed interest in the potential standardization of such a library and encouraged further work.
candidate 2 (found by 3 of 123 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
candidate 3 (found by 3 of 123 passes): Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.
candidate 4 (found by 3 of 123 passes): The abundance of `double` parameters makes it easy to accidentally switch values and there is no way of noticing such a mistake at compile-time.

## audience - grade 1.50 (fired in 6 of 41 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [13] 12 Representation Types                      0/0/0  -> 0.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [17] 16 Systems of quantities and units           0/0/0  -> 0.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             0/0/0  -> 0.00
  [22] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [23] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            0/0/0  -> 0.00
  [27] 3. Various quantities of the same kind       0/0/1  -> 0.33
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  0/0/0  -> 0.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  1/0/0  -> 0.33
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/1  -> 0.33
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 2 (found by 3 of 123 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 3 (found by 3 of 123 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 4 (found by 1 of 123 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

## prior_art - grade 2.00 (fired in 28 of 41 sections, strong in 13)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/2/2  -> 1.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/1/0  -> 0.33
  [6] 5 Impact on the C++ standard                 1/1/1  -> 1.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/1/1  -> 0.67
  [10] 9 Design goals                               2/2/1  -> 1.67
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Representation Types                      2/2/2  -> 2.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            1/1/1  -> 1.00
  [16] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [17] 16 Systems of quantities and units           1/1/1  -> 1.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             2/0/0  -> 0.67
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [24] 18 Core Library Framework scope              1/1/1  -> 1.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            1/1/1  -> 1.00
  [27] 3. Various quantities of the same kind       0/1/0  -> 0.33
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    2/2/2  -> 2.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [33] 1. Ordering                                  2/2/2  -> 2.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  2/0/2  -> 1.33
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): The features in this chapter are heavily used in the library but are not domain-specific.
candidate 2 (found by 3 of 123 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 3 (found by 3 of 123 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 4 (found by 3 of 123 passes): The next example serves as a showcase of various features available in the [[mp-units]](https://mpusz.github.io/mp-units) library.

## vehicle - grade 2.00 (fired in 10 of 41 sections, strong in 3)  (SHARED PASSAGE)
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
  [10] 9 Design goals                               0/1/1  -> 0.67
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types                      0/0/0  -> 0.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [17] 16 Systems of quantities and units           0/0/0  -> 0.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             0/0/0  -> 0.00
  [22] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [23] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/1  -> 0.33
  [26] 2. Quantity kinds                            1/1/1  -> 1.00
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               1/1/1  -> 1.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  1/1/1  -> 1.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              1/2/2  -> 1.67
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 123 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 3 of 123 passes): Deciding to postpone this feature will block us from providing proper SI definitions, as the units of this system should be properly constrained for specific quantity kinds (possibly of the same dimension).
candidate 4 (found by 3 of 123 passes): Skipping this feature also means that we will lack very important building block in modeling many problems in engineering.

## coordination - grade 2.00 (fired in 9 of 41 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types                      0/0/0  -> 0.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [17] 16 Systems of quantities and units           0/0/0  -> 0.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             0/0/0  -> 0.00
  [22] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [23] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            1/1/1  -> 1.00
  [27] 3. Various quantities of the same kind       1/0/1  -> 0.67
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/1/1  -> 0.67
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [33] 1. Ordering                                  2/1/2  -> 1.67
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              0/1/0  -> 0.33
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds
candidate 2 (found by 3 of 123 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 3 (found by 3 of 123 passes): `QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type
candidate 4 (found by 3 of 123 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.

## insufficiency - grade 1.33 (fired in 8 of 41 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [13] 12 Representation Types                      0/0/0  -> 0.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          2/0/1  -> 1.00
  [17] 16 Systems of quantities and units           0/0/0  -> 0.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             0/0/0  -> 0.00
  [22] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [23] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            1/0/0  -> 0.33
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/0/1  -> 0.67
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    2/2/1  -> 1.67
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/1  -> 0.33
  [33] 1. Ordering                                  0/0/1  -> 0.33
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            1/1/1  -> 1.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 2 (found by 2 of 123 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 2 of 123 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.
candidate 4 (found by 2 of 123 passes): [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.

## implementation - grade 2.00  [binary: max] (fired in 14 of 41 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              2/2/2  -> 2.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               1/2/2  -> 1.67
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types                      0/0/0  -> 0.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            2/2/2  -> 2.00
  [16] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [17] 16 Systems of quantities and units           0/0/0  -> 0.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             0/1/1  -> 0.67
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            0/0/0  -> 0.00
  [27] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [28] 4. The affine space                          0/0/0  -> 0.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    2/2/2  -> 2.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  0/0/0  -> 0.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [38] 4. Repacking  (part 3 of 3)                  2/1/2  -> 1.67
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): He is the creator and lead developer of [[Au]](https://aurora-opensource.github.io/au), a widely-adopted zero-dependency units library with novel features including vector space magnitudes and adaptive overflow protection.
candidate 2 (found by 3 of 123 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 3 (found by 3 of 123 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 4 (found by 3 of 123 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

-->
