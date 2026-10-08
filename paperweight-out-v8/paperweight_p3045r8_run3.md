Verdict: Excellent (13/14)

The paper makes a strong overall case for standardizing its proposed library, with particularly solid evidence of real-world importance, affected communities, prior art, implementation experience, and the need for a standard rather than a standalone library. The thinnest part of the argument is the claim that a library alone will not suffice, which is asserted with conviction but not backed by concrete demonstration or evidence.

- The strongest support comes from the documented real-world failures and the breadth of affected developers, combined with the authors’ demonstrated track record and implementation experience.
- The case for why standardization is necessary—especially around error message quality and interoperability—is well supported by concrete technical motivations and external institutional interest.
- The paper clearly establishes prior art and alternatives, showing how existing libraries and standards inform the design without making the proposal redundant.
- The most glaring omission is the lack of established evidence for the claim that a library will not do, since the paper asserts certification and policy constraints without showing that these actually block non-standardized library use.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.67/14)

Provisionally addressed: 7 of 7. Provisional points: 12.67 of 14. Unsupported quotes rejected: 22. Replies missing: 0. Sections: 41. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.67   corroborated 12.00   accumulate 14.00   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.17  implementation 2.00
sample agreement: 257 of 287 section-criterion pairs unanimous (90%)
single-sample totals would have been: 12.50 / 13.00 / 13.00   (all 3 samples: 12.67)
headings: h2 23 + bold numbered 13
on threshold: audience
splits: motivation[6] 1/0/0  motivation[7] 0/0/1  motivation[13] 2/0/0  motivation[16] 0/2/0
        motivation[22] 1/0/0  motivation[23] 2/1/1  motivation[32] 0/1/1  motivation[33] 2/1/2
        audience[3] 1/0/1  audience[26] 1/0/0  audience[37] 1/0/0  audience[39] 0/0/1
        prior_art[9] 0/1/0  prior_art[24] 1/0/0  prior_art[30] 0/2/2  prior_art[33] 1/1/2
        prior_art[37] 2/2/0  vehicle[3] 1/0/1  vehicle[39] 1/0/0  coordination[26] 0/0/1
        coordination[32] 0/2/2  insufficiency[8] 1/1/0  insufficiency[16] 1/0/0
        insufficiency[30] 0/2/2  insufficiency[32] 0/0/1  insufficiency[33] 1/1/0
        implementation[8] 2/1/1  implementation[10] 2/1/1  implementation[30] 1/1/2
        implementation[32] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 26 of 41 sections, strong in 13)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 1/0/0  -> 0.33
  [7] 6 About authors                              0/0/1  -> 0.33
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types                      2/0/0  -> 0.67
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          0/2/0  -> 0.67
  [17] 16 Systems of quantities and units           2/2/2  -> 2.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             1/1/1  -> 1.00
  [22] 17 Text output  (part 1 of 2)                1/0/0  -> 0.33
  [23] 17 Text output  (part 2 of 2)                2/1/1  -> 1.33
  [24] 18 Core Library Framework scope              1/1/1  -> 1.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            2/2/2  -> 2.00
  [27] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [28] 4. The affine space                          2/2/2  -> 2.00
  [29] 5. Text output                               1/1/1  -> 1.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 0/1/1  -> 0.67
  [33] 1. Ordering                                  2/1/2  -> 1.67
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
candidate 3 (found by 3 of 123 passes): The abundance of `double` parameters makes it easy to accidentally switch values and there is no way of noticing such a mistake at compile-time.
candidate 4 (found by 3 of 123 passes): The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.

## audience - grade 1.50 (fired in 6 of 41 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
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
  [26] 2. Quantity kinds                            1/0/0  -> 0.33
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
  [37] 4. Repacking  (part 2 of 3)                  1/0/0  -> 0.33
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/1  -> 0.33
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 2 of 123 passes): Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 3 (found by 2 of 123 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 4 (found by 1 of 123 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them have more than 90% of all the stars on GitHub in the field of physical units libraries for C++.

## prior_art - grade 2.00 (fired in 24 of 41 sections, strong in 11)
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
  [9] 8 Common smells when there is no library ... 0/1/0  -> 0.33
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 1/1/1  -> 1.00
  [12] 11 API overview                              1/1/1  -> 1.00
  [13] 12 Representation Types                      2/2/2  -> 2.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            1/1/1  -> 1.00
  [16] 15 Why do we need typed quantities?          2/2/2  -> 2.00
  [17] 16 Systems of quantities and units           2/2/2  -> 2.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/0/0  -> 0.00
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             0/0/0  -> 0.00
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [24] 18 Core Library Framework scope              1/0/0  -> 0.33
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            1/1/1  -> 1.00
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/2/2  -> 1.33
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [33] 1. Ordering                                  1/1/2  -> 1.33
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  2/2/0  -> 1.33
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): The features in this chapter are heavily used in the library but are not domain-specific.
candidate 2 (found by 3 of 123 passes): Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.
candidate 3 (found by 3 of 123 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 4 (found by 3 of 123 passes): The library follows these established conventions rather than imposing a single unified name (e.g., `abs()`).

## vehicle - grade 2.00 (fired in 7 of 41 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
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
  [39] 21 Teachability                              1/0/0  -> 0.33
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): The primary motivation is **error message quality**: when a type mismatch occurs, the compiler reports the full qualified name of every type involved.
candidate 2 (found by 3 of 123 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 3 (found by 2 of 123 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 4 (found by 2 of 123 passes): Having the physical quantities and units library standardized would solve those issues for many customers, and would allow them to produce safer code for projects on which human life depends every single day.

## coordination - grade 2.00 (fired in 6 of 41 sections, strong in 2)  (SHARED PASSAGE)
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
  [26] 2. Quantity kinds                            0/0/1  -> 0.33
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/2/2  -> 1.33
  [33] 1. Ordering                                  1/1/1  -> 1.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 3 of 123 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 3 (found by 3 of 123 passes): This library comes with built-in interoperability with those types thanks to: specializations of `quantity_like_traits` and `quantity_point_like_traits` that provide support for implicit conversions between types in both directions
candidate 4 (found by 2 of 123 passes): `QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type

## insufficiency - grade 1.17 (fired in 6 of 41 sections, strong in 0)
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
  [13] 12 Representation Types                      0/0/0  -> 0.00
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          1/0/0  -> 0.33
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
  [30] 19 Safety                                    0/2/2  -> 1.33
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/1  -> 0.33
  [33] 1. Ordering                                  1/1/0  -> 0.67
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            1/1/1  -> 1.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results.
candidate 2 (found by 2 of 123 passes): [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.
candidate 3 (found by 1 of 123 passes): Such certification requires a specification to be certified against, and those tools often do not have one.
candidate 4 (found by 1 of 123 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.

## implementation - grade 2.00  [binary: max] (fired in 14 of 41 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              2/2/2  -> 2.00
  [8] 7 Motivation                                 2/1/1  -> 1.33
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               2/1/1  -> 1.33
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
  [21] 4. No conversion                             0/0/0  -> 0.00
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                0/0/0  -> 0.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            0/0/0  -> 0.00
  [27] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [28] 4. The affine space                          0/0/0  -> 0.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    1/1/2  -> 1.33
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/2/0  -> 0.67
  [33] 1. Ordering                                  0/0/0  -> 0.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): He is the creator and lead developer of [[Au]](https://aurora-opensource.github.io/au), a widely-adopted zero-dependency units library with novel features including vector space magnitudes and adaptive overflow protection.
candidate 2 (found by 3 of 123 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 3 (found by 3 of 123 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.
candidate 4 (found by 3 of 123 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin.

-->
