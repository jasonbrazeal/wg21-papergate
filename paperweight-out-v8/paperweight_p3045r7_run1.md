Verdict: Excellent (12/14)

The paper offers substantial support for standardization in its motivation, affected audience, prior art, coordination concerns, and implementation experience, but its case is thinner when explaining why the work belongs in the standard itself and why a library solution is insufficient. The strongest material is concrete and external—committee interest, BSI positions, widespread library adoption, and documented interoperability failures—while the weakest material relies on assertions of importance and necessity without showing why non-standard library approaches cannot meet the need.

- The paper most convincingly establishes that the problem matters and affects a broad, engaged audience, with committee encouragement, BSI’s strong position, and the authors’ dominant library presence all credited as established.
- It also clearly establishes coordination and interoperability problems, including the absence of shared vocabulary and the concrete pound-force seconds versus newton seconds example.
- Prior art and implementation experience are well supported through references to widely used libraries, Compiler Explorer availability, and production feedback.
- The most glaring omission is that the paper does not establish why standardization, rather than a library, is required, nor does it establish that the standard library must contain the feature rather than leaving it to existing or future non-standard libraries.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 18. Replies missing: 0. Sections: 39. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 11.00   accumulate 13.50   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.17  coordination 1.83  insufficiency 1.00  implementation 2.00
sample agreement: 245 of 273 section-criterion pairs unanimous (90%)
single-sample totals would have been: 12.00 / 11.50 / 12.00   (all 3 samples: 11.50)
headings: h2 21 + bold numbered 13
on threshold: audience
splits: motivation[6] 1/0/1  motivation[7] 0/1/0  motivation[12] 1/0/0  motivation[15] 2/1/2
        motivation[20] 1/1/0  motivation[23] 0/1/0  motivation[31] 1/2/1  prior_art[9] 1/0/1
        prior_art[15] 1/2/2  prior_art[18] 0/0/1  prior_art[19] 2/0/2  prior_art[25] 1/0/0
        prior_art[28] 2/0/0  prior_art[31] 1/2/1  vehicle[8] 2/2/0  vehicle[24] 1/0/1
        vehicle[29] 0/1/0  coordination[24] 0/1/0  coordination[25] 1/0/0
        coordination[27] 1/1/0  coordination[29] 2/1/2  insufficiency[14] 0/1/1
        insufficiency[26] 1/0/1  insufficiency[28] 1/0/2  insufficiency[30] 0/0/1
        insufficiency[33] 1/1/0  implementation[8] 1/2/1  implementation[31] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 26 of 39 sections, strong in 13)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/0/1  -> 0.67
  [7] 6 About authors                              0/1/0  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              1/0/0  -> 0.33
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/0/0  -> 0.00
  [15] 14 Systems of quantities and units           2/1/2  -> 1.67
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             2/2/2  -> 2.00
  [20] 15 Text output  (part 1 of 2)                1/1/0  -> 0.67
  [21] 15 Text output  (part 2 of 2)                1/1/1  -> 1.00
  [22] 16 Core Library Framework scope              1/1/1  -> 1.00
  [23] 1. Core library                              0/1/0  -> 0.33
  [24] 2. Quantity kinds                            2/2/2  -> 2.00
  [25] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [26] 4. The affine space                          2/2/2  -> 2.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 1/1/1  -> 1.00
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  1/2/1  -> 1.33
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              2/2/2  -> 2.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): Several groups in the ISO C++ Committee reviewed the “P1935: A C++ Approach to Physical Units” proposal in Belfast 2019 and Prague 2020. All those groups expressed interest in the potential standardization of such a library and encouraged further work.
candidate 2 (found by 3 of 117 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
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
candidate 2 (found by 2 of 117 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 3 (found by 1 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++].

## prior_art - grade 2.00 (fired in 26 of 39 sections, strong in 11)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/1/1  -> 1.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/0/1  -> 0.67
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Usage examples                            1/1/1  -> 1.00
  [14] 13 Why do we need typed quantities?          2/2/2  -> 2.00
  [15] 14 Systems of quantities and units           1/2/2  -> 1.67
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/1  -> 0.33
  [19] 4. No conversion                             2/0/2  -> 1.33
  [20] 15 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [21] 15 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [22] 16 Core Library Framework scope              1/1/1  -> 1.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            1/1/1  -> 1.00
  [25] 3. Various quantities of the same kind       1/0/0  -> 0.33
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    2/0/0  -> 0.67
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  1/2/1  -> 1.33
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              1/1/1  -> 1.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): The features in this chapter are heavily used in the library but are not domain-specific.
candidate 2 (found by 3 of 117 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.
candidate 3 (found by 3 of 117 passes): Units should not be associated with User-Defined Literals (UDLs), as it is the case with `std::chrono::duration`.
candidate 4 (found by 3 of 117 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.

## vehicle - grade 1.17 (fired in 8 of 39 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
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
  [24] 2. Quantity kinds                            1/0/1  -> 0.67
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 0/1/0  -> 0.33
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
candidate 2 (found by 3 of 117 passes): The set of entities required for standardization should be limited to the bare minimum.
candidate 3 (found by 3 of 117 passes): Skipping this feature also means that we will lack very important building block in modeling many problems in engineering.
candidate 4 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.

## coordination - grade 1.83 (fired in 8 of 39 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
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
  [24] 2. Quantity kinds                            0/1/0  -> 0.33
  [25] 3. Various quantities of the same kind       1/0/0  -> 0.33
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               1/1/0  -> 0.67
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 2/1/2  -> 1.67
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
candidate 1 (found by 3 of 117 passes): There is no shared vocabulary between different libraries. User-facing APIs use ad-hoc conventions.
candidate 2 (found by 3 of 117 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 3 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 4 (found by 2 of 117 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds

## insufficiency - grade 1.00 (fired in 6 of 39 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
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
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/1/1  -> 0.67
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
  [26] 4. The affine space                          1/0/1  -> 0.67
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    1/0/2  -> 1.00
  [29] 18 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/1  -> 0.33
  [31] 1. Ordering                                  0/0/0  -> 0.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            1/1/0  -> 0.67
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 2 (found by 2 of 117 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.
candidate 3 (found by 2 of 117 passes): However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.
candidate 4 (found by 2 of 117 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.

## implementation - grade 2.00  [binary: max] (fired in 15 of 39 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              2/2/2  -> 2.00
  [8] 7 Motivation                                 1/2/1  -> 1.33
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
  [19] 4. No conversion                             1/1/1  -> 1.00
  [20] 15 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [21] 15 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            0/0/0  -> 0.00
  [25] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [26] 4. The affine space                          0/0/0  -> 0.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    1/1/1  -> 1.00
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/0/0  -> 0.33
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              1/1/1  -> 1.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): In the following years, the library’s authors focused on getting more feedback from the production about the design and developed version 2 of the [[mp-units]](https://mpusz.github.io/mp-units) library that resolves the issues raised by the users and Committee members.
candidate 2 (found by 3 of 117 passes): He is the creator and lead developer of [[Au]](https://aurora-opensource.github.io/au), a widely-adopted zero-dependency units library with novel features including vector space magnitudes and adaptive overflow protection.
candidate 3 (found by 3 of 117 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 4 (found by 3 of 117 passes): Moreover, from our experience, disallowing such operations and requiring an explicit cast to a common quantity in every single place makes the code so cluttered with casts that it nearly renders the library unusable.

-->
