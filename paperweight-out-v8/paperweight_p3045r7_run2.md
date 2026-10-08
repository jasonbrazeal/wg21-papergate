Verdict: Excellent (12/14)

The paper offers substantial support for standardizing its proposed quantities and units library, with particularly strong evidence of real-world relevance, existing implementation experience, and interoperability concerns. The thinnest part of the case is the argument that a library alone cannot suffice, where the paper asserts constraints and limitations without fully demonstrating why they require standardization rather than continued library evolution.

- The strongest support comes from the demonstrated demand and adoption of the authors’ existing libraries, including their dominant presence among C++ dimensional-analysis projects and explicit institutional interest from BSI.
- The paper also convincingly establishes why the feature matters, citing concrete failure modes and the value of compiler-checkable correctness for safety-critical code.
- Coordination and interoperability are well supported through the proposed `QuantityLike` concept and the connection to P2830R10 for consistent type ordering.
- The most glaring omission is the lack of established evidence that a library cannot adequately address the identified needs, leaving the necessity of standardization less fully justified than the other aspects of the proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 39. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 11.00   accumulate 13.50   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 2.00  insufficiency 1.17  implementation 2.00
sample agreement: 247 of 273 section-criterion pairs unanimous (90%)
single-sample totals would have been: 12.50 / 13.00 / 12.00   (all 3 samples: 12.17)
headings: h2 21 + bold numbered 13
on threshold: audience, vehicle
splits: motivation[3] 0/1/1  motivation[12] 2/0/2  motivation[14] 2/0/2  motivation[28] 2/0/0
        motivation[29] 2/0/2  prior_art[6] 1/2/2  prior_art[9] 1/0/1  prior_art[15] 1/2/1
        prior_art[22] 0/1/1  vehicle[28] 1/0/0  vehicle[29] 1/0/0  coordination[9] 0/1/0
        coordination[24] 1/1/0  coordination[27] 1/0/0  insufficiency[8] 1/1/0
        insufficiency[14] 2/0/0  insufficiency[28] 1/2/0  insufficiency[30] 0/1/0
        insufficiency[31] 1/0/1  insufficiency[33] 1/2/1  insufficiency[34] 0/0/1
        implementation[3] 0/1/1  implementation[8] 1/2/2  implementation[20] 2/0/2
        implementation[28] 2/1/2  implementation[30] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 25 of 39 sections, strong in 14)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/1  -> 0.67
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/1/1  -> 1.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              2/0/2  -> 1.33
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          2/0/2  -> 1.33
  [15] 14 Systems of quantities and units           2/2/2  -> 2.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             2/2/2  -> 2.00
  [20] 15 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [21] 15 Text output  (part 2 of 2)                1/1/1  -> 1.00
  [22] 16 Core Library Framework scope              1/1/1  -> 1.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            2/2/2  -> 2.00
  [25] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [26] 4. The affine space                          2/2/2  -> 2.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    2/0/0  -> 0.67
  [29] 18 Design details and rationale  (part 1 ... 2/0/2  -> 1.33
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  2/2/2  -> 2.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              2/2/2  -> 2.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
candidate 2 (found by 3 of 117 passes): We should also mention the potential confusion of users with having two different ways to deal with time abstractions in the C++ standard library.
candidate 3 (found by 3 of 117 passes): Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.
candidate 4 (found by 3 of 117 passes): The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.

## audience - grade 1.50 (fired in 2 of 39 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
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
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/0/0  -> 0.00
  [15] 14 Systems of quantities and units           0/0/0  -> 0.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             0/0/0  -> 0.00
  [20] 15 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [21] 15 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            0/0/0  -> 0.00
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  0/0/0  -> 0.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            0/0/0  -> 0.00
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 2 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them have more than 90% of all the stars on GitHub in the field of physical units libraries for C++.
candidate 3 (found by 1 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).

## prior_art - grade 2.00 (fired in 24 of 39 sections, strong in 13)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/2/2  -> 1.67
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/0/1  -> 0.67
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Usage examples                            1/1/1  -> 1.00
  [14] 13 Why do we need typed quantities?          2/2/2  -> 2.00
  [15] 14 Systems of quantities and units           1/2/1  -> 1.33
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             2/2/2  -> 2.00
  [20] 15 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [21] 15 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [22] 16 Core Library Framework scope              0/1/1  -> 0.67
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            1/1/1  -> 1.00
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    2/2/2  -> 2.00
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  1/1/1  -> 1.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              1/1/1  -> 1.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 2 (found by 3 of 117 passes): Units should not be associated with User-Defined Literals (UDLs), as it is the case with `std::chrono::duration`.
candidate 3 (found by 3 of 117 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 4 (found by 3 of 117 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.

## vehicle - grade 1.50 (fired in 9 of 39 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/0/0  -> 0.00
  [15] 14 Systems of quantities and units           0/0/0  -> 0.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             0/0/0  -> 0.00
  [20] 15 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [21] 15 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            1/1/1  -> 1.00
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    1/0/0  -> 0.33
  [29] 18 Design details and rationale  (part 1 ... 1/0/0  -> 0.33
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/1/1  -> 1.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            0/0/0  -> 0.00
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 117 passes): Having the physical quantities and units library standardized would solve those issues for many customers, and would allow them to produce safer code for projects on which human life depends every single day.
candidate 3 (found by 3 of 117 passes): if we never decide to standardize it, then all the symbols provided in unit and dimension definitions will be useless.
candidate 4 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.

## coordination - grade 2.00 (fired in 7 of 39 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 8 Common smells when there is no library ... 0/1/0  -> 0.33
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/0/0  -> 0.00
  [15] 14 Systems of quantities and units           0/0/0  -> 0.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             0/0/0  -> 0.00
  [20] 15 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [21] 15 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            1/1/0  -> 0.67
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               1/0/0  -> 0.33
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/1/1  -> 1.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            0/0/0  -> 0.00
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 3 of 117 passes): `QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type
candidate 3 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 4 (found by 2 of 117 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds

## insufficiency - grade 1.17 (fired in 7 of 39 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 1/1/0  -> 0.67
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          2/0/0  -> 0.67
  [15] 14 Systems of quantities and units           0/0/0  -> 0.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             0/0/0  -> 0.00
  [20] 15 Text output  (part 1 of 2)                0/0/0  -> 0.00
  [21] 15 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            0/0/0  -> 0.00
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          0/0/0  -> 0.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    1/2/0  -> 1.00
  [29] 18 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [30] 18 Design details and rationale  (part 2 ... 0/1/0  -> 0.33
  [31] 1. Ordering                                  1/0/1  -> 0.67
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            1/2/1  -> 1.33
  [34] 4. Repacking  (part 1 of 3)                  0/0/1  -> 0.33
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 2 (found by 2 of 117 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 2 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 4 (found by 1 of 117 passes): However, it is impossible to predefine one fixed conversion factor for those, as a currency exchange rate varies over time, and the library’s framework can’t provide such an information as an input to the built-in conversion function.

## implementation - grade 2.00  [binary: max] (fired in 14 of 39 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/1  -> 0.67
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              2/2/2  -> 2.00
  [8] 7 Motivation                                 1/2/2  -> 1.67
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Usage examples                            2/2/2  -> 2.00
  [14] 13 Why do we need typed quantities?          0/0/0  -> 0.00
  [15] 14 Systems of quantities and units           0/0/0  -> 0.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             0/0/0  -> 0.00
  [20] 15 Text output  (part 1 of 2)                2/0/2  -> 1.33
  [21] 15 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            0/0/0  -> 0.00
  [25] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [26] 4. The affine space                          0/0/0  -> 0.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    2/1/2  -> 1.67
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/2  -> 0.67
  [31] 1. Ordering                                  0/0/0  -> 0.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              1/1/1  -> 1.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): He is the creator and lead developer of [[Au]](https://aurora-opensource.github.io/au), a widely-adopted zero-dependency units library with novel features including vector space magnitudes and adaptive overflow protection.
candidate 2 (found by 3 of 117 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 3 (found by 3 of 117 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 4 (found by 3 of 117 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

-->
