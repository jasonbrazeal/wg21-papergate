Verdict: Excellent (12/14)

The paper offers substantial support for standardizing the feature it describes, with particularly strong evidence of real-world impact, existing implementation experience, and broad stakeholder interest. The case is thinnest where it must show why a library cannot suffice, since several of the arguments there are asserted rather than demonstrated.

- The strongest support comes from concrete production feedback and a working implementation available for testing, which grounds the proposal in demonstrated use rather than speculation.
- The paper also establishes clear affected audiences and shows coordination with external standards bodies and other C++ proposals.
- The most glaring omission is a convincing demonstration that the feature cannot be delivered adequately as a library, since the cited constraints rely on claims about company policy and implementation-defined behavior without showing why standardization is the only viable path.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 7 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 41. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 11.00   accumulate 13.50   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 1.67  insufficiency 0.83  implementation 2.00
sample agreement: 257 of 287 section-criterion pairs unanimous (90%)
single-sample totals would have been: 12.00 / 12.50 / 13.00   (all 3 samples: 12.00)
headings: h2 23 + bold numbered 13
on threshold: audience, coordination
splits: motivation[3] 1/0/1  motivation[6] 0/0/1  motivation[12] 2/2/0  motivation[13] 2/2/1
        motivation[21] 1/2/2  motivation[33] 1/2/1  audience[37] 0/0/1  audience[39] 1/0/0
        prior_art[6] 2/1/2  prior_art[13] 2/2/0  prior_art[16] 0/2/2  prior_art[24] 0/1/0
        vehicle[24] 0/1/0  vehicle[35] 0/0/1  coordination[3] 0/1/0  coordination[9] 1/1/0
        coordination[26] 0/1/0  coordination[29] 0/0/1  coordination[32] 0/2/2
        insufficiency[30] 0/0/2  insufficiency[33] 1/1/0  insufficiency[35] 0/0/1
        insufficiency[36] 1/0/0  implementation[3] 1/1/0  implementation[8] 1/1/2
        implementation[10] 1/2/1  implementation[21] 1/0/1  implementation[22] 0/2/2
        implementation[23] 0/2/0  implementation[31] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 27 of 41 sections, strong in 17)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/1  -> 0.33
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              2/2/0  -> 1.33
  [13] 12 Representation Types                      2/2/1  -> 1.67
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [17] 16 Systems of quantities and units           2/2/2  -> 2.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             1/2/2  -> 1.67
  [22] 17 Text output  (part 1 of 2)                1/1/1  -> 1.00
  [23] 17 Text output  (part 2 of 2)                1/1/1  -> 1.00
  [24] 18 Core Library Framework scope              1/1/1  -> 1.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            2/2/2  -> 2.00
  [27] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [28] 4. The affine space                          2/2/2  -> 2.00
  [29] 5. Text output                               1/1/1  -> 1.00
  [30] 19 Safety                                    2/2/2  -> 2.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [33] 1. Ordering                                  1/2/1  -> 1.33
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              2/2/2  -> 2.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
candidate 2 (found by 3 of 123 passes): Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.
candidate 3 (found by 3 of 123 passes): The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.
candidate 4 (found by 3 of 123 passes): Dimensional analysis does not adequately model the semantics of measurement data.

## audience - grade 1.50 (fired in 5 of 41 sections, strong in 1)  (ON THRESHOLD)
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
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  0/0/0  -> 0.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/1  -> 0.33
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              1/0/0  -> 0.33
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 2 (found by 3 of 123 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 3 (found by 3 of 123 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 4 (found by 1 of 123 passes): However, the feedback we got from the production usage was that such an approach is really bad for generic programming.

## prior_art - grade 2.00 (fired in 25 of 41 sections, strong in 11)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 2/1/2  -> 1.67
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Representation Types                      2/2/0  -> 1.33
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            1/1/1  -> 1.00
  [16] 15 Why do we need typed quantities?          0/2/2  -> 1.33
  [17] 16 Systems of quantities and units           1/1/1  -> 1.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             1/1/1  -> 1.00
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [24] 18 Core Library Framework scope              0/1/0  -> 0.33
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            1/1/1  -> 1.00
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    2/2/2  -> 2.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [33] 1. Ordering                                  1/1/1  -> 1.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 2 (found by 3 of 123 passes): UDLs do not compose, have very limited scope and functionality, and are expensive to standardize.
candidate 3 (found by 3 of 123 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 4 (found by 3 of 123 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.

## vehicle - grade 2.00 (fired in 10 of 41 sections, strong in 2)  (SHARED PASSAGE)
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
  [24] 18 Core Library Framework scope              0/1/0  -> 0.33
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            1/1/1  -> 1.00
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               1/1/1  -> 1.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  1/1/1  -> 1.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/1  -> 0.33
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 123 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 3 of 123 passes): Deciding to postpone this feature will block us from providing proper SI definitions, as the units of this system should be properly constrained for specific quantity kinds (possibly of the same dimension).
candidate 4 (found by 3 of 123 passes): However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.

## coordination - grade 1.67 (fired in 8 of 41 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/0  -> 0.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/0  -> 0.67
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
  [26] 2. Quantity kinds                            0/1/0  -> 0.33
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/1  -> 0.33
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/2/2  -> 1.33
  [33] 1. Ordering                                  1/1/1  -> 1.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 3 of 123 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 3 (found by 2 of 123 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds
candidate 4 (found by 2 of 123 passes): `QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type

## insufficiency - grade 0.83 (fired in 5 of 41 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.50   max 1.00
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
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          0/0/0  -> 0.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/0/2  -> 0.67
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  1/1/0  -> 0.67
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/1  -> 0.33
  [36] 4. Repacking  (part 1 of 3)                  1/0/0  -> 0.33
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 2 (found by 2 of 123 passes): As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list.
candidate 3 (found by 1 of 123 passes): [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.
candidate 4 (found by 1 of 123 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.

## implementation - grade 2.00  [binary: max] (fired in 15 of 41 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/0  -> 0.67
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 1/1/2  -> 1.33
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               1/2/1  -> 1.33
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
  [21] 4. No conversion                             1/0/1  -> 0.67
  [22] 17 Text output  (part 1 of 2)                0/2/2  -> 1.33
  [23] 17 Text output  (part 2 of 2)                0/2/0  -> 0.67
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            0/0/0  -> 0.00
  [27] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [28] 4. The affine space                          0/0/0  -> 0.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    1/1/1  -> 1.00
  [31] 20 Design details and rationale  (part 1 ... 0/1/0  -> 0.33
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  0/0/0  -> 0.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 2 (found by 3 of 123 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.
candidate 3 (found by 3 of 123 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin.
candidate 4 (found by 3 of 123 passes): However, [[mp-units]](https://mpusz.github.io/mp-units) users [requested the following use case](https://github.com/mpusz/mp-units/issues/621):

-->
