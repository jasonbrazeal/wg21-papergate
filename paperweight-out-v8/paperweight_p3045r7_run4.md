Verdict: Excellent (12/14)

The paper offers substantial support for standardizing the proposed library, with its strongest material covering real-world motivation, affected users, prior art, implementation experience, and the need for a standard rather than a standalone library. The thinnest part is the argument that a library alone will not suffice, where the paper asserts the point but does not fully establish it.

- The paper convincingly grounds the proposal in documented production failures and broad committee and industry interest, showing both why the feature matters and who would benefit.
- It demonstrates meaningful implementation experience through a mature library, compiler explorer availability, and feedback from deployed use.
- The case for standardization over a non-standard library is asserted through dissatisfaction with existing approaches and policy constraints, but the paper does not fully establish why those obstacles cannot be addressed outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 39. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 11.00   accumulate 12.83   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.83  insufficiency 0.83  implementation 2.00
sample agreement: 242 of 273 section-criterion pairs unanimous (89%)
single-sample totals would have been: 12.00 / 12.00 / 12.00   (all 3 samples: 11.67)
headings: h2 21 + bold numbered 13
on threshold: audience, vehicle
splits: motivation[6] 1/0/1  motivation[7] 0/0/1  motivation[14] 0/0/2  motivation[15] 2/2/1
        motivation[19] 1/1/2  motivation[20] 1/1/0  motivation[21] 1/1/2  motivation[28] 0/2/2
        motivation[29] 0/0/2  audience[25] 1/0/0  prior_art[3] 0/0/1  prior_art[9] 0/1/1
        prior_art[15] 2/1/1  prior_art[19] 2/0/0  prior_art[20] 2/2/0  prior_art[22] 1/0/1
        prior_art[25] 1/0/1  vehicle[29] 1/0/1  vehicle[31] 1/0/0  vehicle[33] 0/1/0
        coordination[9] 0/1/1  coordination[24] 1/1/0  coordination[27] 1/0/0
        coordination[29] 2/2/1  coordination[31] 1/2/1  insufficiency[8] 0/1/0
        insufficiency[14] 0/0/2  insufficiency[31] 1/0/0  implementation[7] 2/2/0
        implementation[30] 0/2/2  implementation[35] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 26 of 39 sections, strong in 12)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/0/1  -> 0.67
  [7] 6 About authors                              0/0/1  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/0/2  -> 0.67
  [15] 14 Systems of quantities and units           2/2/1  -> 1.67
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             1/1/2  -> 1.33
  [20] 15 Text output  (part 1 of 2)                1/1/0  -> 0.67
  [21] 15 Text output  (part 2 of 2)                1/1/2  -> 1.33
  [22] 16 Core Library Framework scope              1/1/1  -> 1.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            2/2/2  -> 2.00
  [25] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [26] 4. The affine space                          2/2/2  -> 2.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    0/2/2  -> 1.33
  [29] 18 Design details and rationale  (part 1 ... 0/0/2  -> 0.67
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  1/1/1  -> 1.00
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

## audience - grade 1.50 (fired in 3 of 39 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
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
  [25] 3. Various quantities of the same kind       1/0/0  -> 0.33
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
candidate 2 (found by 2 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++].
candidate 3 (found by 1 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them have more than 90% of all the stars on GitHub in the field of physical units libraries for C++.
candidate 4 (found by 1 of 117 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

## prior_art - grade 2.00 (fired in 26 of 39 sections, strong in 10)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/1  -> 0.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/1/1  -> 1.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/1/1  -> 0.67
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Usage examples                            1/1/1  -> 1.00
  [14] 13 Why do we need typed quantities?          2/2/2  -> 2.00
  [15] 14 Systems of quantities and units           2/1/1  -> 1.33
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             2/0/0  -> 0.67
  [20] 15 Text output  (part 1 of 2)                2/2/0  -> 1.33
  [21] 15 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [22] 16 Core Library Framework scope              1/0/1  -> 0.67
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            1/1/1  -> 1.00
  [25] 3. Various quantities of the same kind       1/0/1  -> 0.67
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
candidate 1 (found by 3 of 117 passes): Units should not be associated with User-Defined Literals (UDLs), as it is the case with `std::chrono::duration`.
candidate 2 (found by 3 of 117 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 3 (found by 3 of 117 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 4 (found by 3 of 117 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.

## vehicle - grade 1.50 (fired in 9 of 39 sections, strong in 1)  (ON THRESHOLD)
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
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 1/0/1  -> 0.67
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/0/0  -> 0.33
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            0/1/0  -> 0.33
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 117 passes): Having the physical quantities and units library standardized would solve those issues for many customers, and would allow them to produce safer code for projects on which human life depends every single day.
candidate 3 (found by 3 of 117 passes): Deciding to postpone this feature will block us from providing proper SI definitions, as the units of this system should be properly constrained for specific quantity kinds (possibly of the same dimension).
candidate 4 (found by 3 of 117 passes): if we never decide to standardize it, then all the symbols provided in unit and dimension definitions will be useless.

## coordination - grade 1.83 (fired in 7 of 39 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 8 Common smells when there is no library ... 0/1/1  -> 0.67
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
  [29] 18 Design details and rationale  (part 1 ... 2/2/1  -> 1.67
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/2/1  -> 1.33
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            0/0/0  -> 0.00
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds
candidate 2 (found by 3 of 117 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 3 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 4 (found by 2 of 117 passes): `QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type

## insufficiency - grade 0.83 (fired in 4 of 39 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 0/1/0  -> 0.33
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/0/0  -> 0.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          0/0/2  -> 0.67
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
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/0/0  -> 0.33
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            1/1/1  -> 1.00
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 2 (found by 1 of 117 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 1 of 117 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.
candidate 4 (found by 1 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.

## implementation - grade 2.00  [binary: max] (fired in 15 of 39 sections, strong in 7)  (SHARED PASSAGE)
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
  [28] 17 Safety                                    2/2/2  -> 2.00
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 0/2/2  -> 1.33
  [31] 1. Ordering                                  0/0/0  -> 0.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  0/1/1  -> 0.67
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              1/1/1  -> 1.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): In the following years, the library’s authors focused on getting more feedback from the production about the design and developed version 2 of the [[mp-units]](https://mpusz.github.io/mp-units) library that resolves the issues raised by the users and Committee members.
candidate 2 (found by 3 of 117 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 3 (found by 3 of 117 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.
candidate 4 (found by 3 of 117 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin.

-->
