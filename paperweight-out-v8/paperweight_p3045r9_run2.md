Verdict: Excellent (12/14)

The paper offers substantial support for standardization in several key areas, particularly in demonstrating committee interest, prior art, implementation experience, and the need for a standard rather than another library. The case is thinnest around who is affected and why a library will not do, where the paper asserts broad impact and implementation constraints without fully backing those claims.

- The strongest support comes from documented committee engagement and production implementation experience, including compiler-verified performance parity with raw arithmetic.
- The paper clearly establishes why a standard is needed by pointing to interoperability failures and the incompatibility of internal libraries across organizations.
- The least supported claim is the scale and composition of the affected audience, which relies on rough categorizations and indirect signals rather than concrete evidence.
- The most glaring omission is a convincing demonstration that the identified library-level limitations cannot be adequately addressed outside the standard, since the paper reports dissatisfaction with its own results but does not establish that no library could succeed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 7 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 42. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 11.00   accumulate 13.33   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 2.00  coordination 1.50  insufficiency 1.17  implementation 2.00
sample agreement: 255 of 294 section-criterion pairs unanimous (87%)
single-sample totals would have been: 12.50 / 12.50 / 12.00   (all 3 samples: 12.00)
headings: h2 23 + bold numbered 13
on threshold: audience, coordination, insufficiency
splits: motivation[7] 0/0/1  motivation[10] 1/1/0  motivation[12] 0/0/2  motivation[13] 2/0/0
        motivation[14] 0/1/1  motivation[20] 0/1/0  motivation[26] 1/1/0  motivation[33] 1/1/0
        motivation[34] 2/2/1  audience[3] 1/0/1  audience[9] 0/1/0  audience[29] 0/1/1
        audience[37] 0/1/0  prior_art[6] 1/2/1  prior_art[7] 0/0/1  prior_art[10] 1/1/2
        prior_art[18] 2/1/2  prior_art[22] 0/0/2  prior_art[25] 1/0/1  prior_art[28] 1/0/0
        prior_art[34] 2/2/1  vehicle[6] 1/0/0  vehicle[27] 1/0/0  vehicle[31] 0/0/1
        vehicle[40] 1/2/2  coordination[9] 1/0/1  coordination[27] 1/0/1  coordination[30] 0/1/1
        coordination[32] 0/2/0  coordination[34] 0/2/1  insufficiency[8] 1/0/0
        insufficiency[34] 1/0/1  insufficiency[36] 2/2/1  implementation[7] 2/2/0
        implementation[10] 2/1/1  implementation[31] 2/2/1  implementation[32] 0/2/2
        implementation[38] 2/1/1  implementation[40] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 29 of 42 sections, strong in 16)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/1/1  -> 1.00
  [7] 6 About authors                              0/0/1  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/0  -> 0.67
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/2  -> 0.67
  [13] 12 Representation Types  (part 1 of 2)       2/0/0  -> 0.67
  [14] 12 Representation Types  (part 2 of 2)       0/1/1  -> 0.67
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            0/0/0  -> 0.00
  [17] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [18] 16 Systems of quantities and units           2/2/2  -> 2.00
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/1/0  -> 0.33
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             2/2/2  -> 2.00
  [23] 17 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [24] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [25] 18 Core Library Framework scope              1/1/1  -> 1.00
  [26] 1. Core library                              1/1/0  -> 0.67
  [27] 2. Quantity kinds                            2/2/2  -> 2.00
  [28] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [29] 4. The affine space                          2/2/2  -> 2.00
  [30] 5. Text output                               1/1/1  -> 1.00
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 1/1/0  -> 0.67
  [34] 1. Ordering                                  2/2/1  -> 1.67
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              2/2/2  -> 2.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Several groups in the ISO C++ Committee reviewed the “P1935: A C++ Approach to Physical Units” proposal in Belfast 2019 and Prague 2020. All those groups expressed interest in the potential standardization of such a library and encouraged further work.
candidate 2 (found by 3 of 126 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
candidate 3 (found by 3 of 126 passes): We should also mention the potential confusion of users with having two different ways to deal with time abstractions in the C++ standard library.
candidate 4 (found by 3 of 126 passes): Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.

## audience - grade 1.33 (fired in 5 of 42 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/1/0  -> 0.33
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
  [29] 4. The affine space                          0/1/1  -> 0.67
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  0/0/0  -> 0.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/1/0  -> 0.33
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/0/0  -> 0.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 2 (found by 2 of 126 passes): Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 3 (found by 2 of 126 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 4 (found by 1 of 126 passes): A quick search through open source C++ code bases reveals that, for example, the `RAD_TO_DEG` macro is defined in a multitude of different ways – sometimes even within the same repository:

## prior_art - grade 2.00 (fired in 29 of 42 sections, strong in 15)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/2/1  -> 1.33
  [7] 6 About authors                              0/0/1  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
  [10] 9 Design goals                               1/1/2  -> 1.33
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Representation Types  (part 1 of 2)       2/2/2  -> 2.00
  [14] 12 Representation Types  (part 2 of 2)       2/2/2  -> 2.00
  [15] 13 Hello units                               0/0/0  -> 0.00
  [16] 14 Usage examples                            1/1/1  -> 1.00
  [17] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [18] 16 Systems of quantities and units           2/1/2  -> 1.67
  [19] 1. Implicit conversions                      0/0/0  -> 0.00
  [20] 2. Explicit conversions                      0/0/0  -> 0.00
  [21] 3. Explicit casts                            0/0/0  -> 0.00
  [22] 4. No conversion                             0/0/2  -> 0.67
  [23] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [24] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [25] 18 Core Library Framework scope              1/0/1  -> 0.67
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            1/1/1  -> 1.00
  [28] 3. Various quantities of the same kind       1/0/0  -> 0.33
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [34] 1. Ordering                                  2/2/1  -> 1.67
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              1/1/1  -> 1.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): Several groups in the ISO C++ Committee reviewed the “P1935: A C++ Approach to Physical Units” [[P1935R2]](https://wg21.link/p1935r2) proposal in Belfast 2019 and Prague 2020.
candidate 2 (found by 3 of 126 passes): UDLs do not compose, have very limited scope and functionality, and are expensive to standardize.
candidate 3 (found by 3 of 126 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 4 (found by 3 of 126 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.

## vehicle - grade 2.00 (fired in 10 of 42 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/0/0  -> 0.33
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
  [27] 2. Quantity kinds                            1/0/0  -> 0.33
  [28] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               1/1/1  -> 1.00
  [31] 19 Safety                                    0/0/1  -> 0.33
  [32] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  1/1/1  -> 1.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              1/2/2  -> 1.67
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 126 passes): The primary motivation is **error message quality**: when a type mismatch occurs, the compiler reports the full qualified name of every type involved.
candidate 3 (found by 3 of 126 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 4 (found by 3 of 126 passes): The standardization aspect is crucial here—without it, each company uses incompatible internal libraries or ad-hoc approaches, forcing new graduates to relearn concepts they should already know.

## coordination - grade 1.50 (fired in 7 of 42 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [27] 2. Quantity kinds                            1/0/1  -> 0.67
  [28] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [29] 4. The affine space                          1/1/1  -> 1.00
  [30] 5. Text output                               0/1/1  -> 0.67
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 0/2/0  -> 0.67
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  0/2/1  -> 1.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            0/0/0  -> 0.00
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/0/0  -> 0.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 2 of 126 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 3 (found by 1 of 126 passes): We desperately need to be able to express more quantities and units in a standardized way so different libraries get means to communicate with each other.
candidate 4 (found by 1 of 126 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds

## insufficiency - grade 1.17 (fired in 3 of 42 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 1/0/0  -> 0.33
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
  [29] 4. The affine space                          0/0/0  -> 0.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  1/0/1  -> 0.67
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/1  -> 1.67
  [37] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [39] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [40] 21 Teachability                              0/0/0  -> 0.00
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 2 (found by 1 of 126 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 1 of 126 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 4 (found by 1 of 126 passes): As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list.

## implementation - grade 2.00  [binary: max] (fired in 15 of 42 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              2/2/0  -> 1.33
  [8] 7 Motivation                                 1/1/1  -> 1.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               2/1/1  -> 1.33
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
  [22] 4. No conversion                             1/1/1  -> 1.00
  [23] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [24] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [25] 18 Core Library Framework scope              0/0/0  -> 0.00
  [26] 1. Core library                              0/0/0  -> 0.00
  [27] 2. Quantity kinds                            0/0/0  -> 0.00
  [28] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [29] 4. The affine space                          0/0/0  -> 0.00
  [30] 5. Text output                               0/0/0  -> 0.00
  [31] 19 Safety                                    2/2/1  -> 1.67
  [32] 20 Design details and rationale  (part 1 ... 0/2/2  -> 1.33
  [33] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [34] 1. Ordering                                  0/0/0  -> 0.00
  [35] 2. Aggregation                               0/0/0  -> 0.00
  [36] 3. Simplification                            2/2/2  -> 2.00
  [37] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 2 of 3)                  2/1/1  -> 1.33
  [39] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [40] 21 Teachability                              0/1/1  -> 0.67
  [41] 22 Acknowledgements                          0/0/0  -> 0.00
  [42] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 126 passes): In the following years, the library’s authors focused on getting more feedback from the production about the design and developed version 2 of the mp-units library that resolves the issues raised by the users and Committee members.
candidate 2 (found by 3 of 126 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain.
candidate 3 (found by 3 of 126 passes): In practice, the [[mp-units]](https://mpusz.github.io/mp-units) implementation compiles to identical or faster assembly as equivalent code using raw `double` arithmetic — this can be verified via the Compiler Explorer links provided in the Usage examples chapter.
candidate 4 (found by 3 of 126 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).

-->
