Verdict: Strong to Excellent (11/14)

The paper offers substantial support for several core parts of its standardization case, particularly in explaining why the problem matters, surveying prior art, and demonstrating implementation experience. The support is thinnest around who is actually affected and why an existing library cannot suffice, where the paper relies more on assertion and indirect evidence than on a fully developed argument.

- The strongest support is the concrete implementation experience, including a live Compiler Explorer link and production reports of critical bugs prevented by the approach.
- The paper also clearly establishes why the feature matters by connecting it to real failures from mixing semantically different values and the need for compile-time verification.
- The case for coordination and interoperability is well grounded in the need for standardized quantity and unit expression across libraries and the cited BSI position.
- The most glaring omission is the failure to establish who is affected beyond the authors’ own libraries and GitHub popularity, leaving the breadth of the user community largely asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 39. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 9.67   accumulate 12.67   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.50  coordination 1.67  insufficiency 0.67  implementation 2.00
sample agreement: 245 of 273 section-criterion pairs unanimous (90%)
single-sample totals would have been: 12.00 / 12.00 / 11.50   (all 3 samples: 11.17)
headings: h2 21 + bold numbered 13
on threshold: audience, vehicle, coordination
splits: motivation[6] 0/0/1  motivation[14] 2/0/2  motivation[19] 2/1/1  motivation[28] 0/2/2
        motivation[29] 2/1/1  motivation[31] 1/2/2  audience[26] 1/0/1  prior_art[6] 2/1/2
        prior_art[19] 2/0/2  prior_art[25] 1/0/1  prior_art[31] 2/1/2  vehicle[3] 0/1/0
        vehicle[10] 0/1/1  vehicle[23] 0/0/1  vehicle[24] 0/1/0  coordination[9] 1/1/0
        coordination[24] 1/0/1  coordination[27] 1/0/0  coordination[29] 2/2/0
        insufficiency[8] 1/0/1  insufficiency[26] 0/1/0  insufficiency[28] 0/2/0
        insufficiency[31] 1/1/0  insufficiency[33] 0/0/1  implementation[7] 0/2/1
        implementation[8] 2/2/1  implementation[21] 0/2/0  implementation[28] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 26 of 39 sections, strong in 14)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/1  -> 0.33
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              2/2/2  -> 2.00
  [13] 12 Usage examples                            0/0/0  -> 0.00
  [14] 13 Why do we need typed quantities?          2/0/2  -> 1.33
  [15] 14 Systems of quantities and units           2/2/2  -> 2.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             2/1/1  -> 1.33
  [20] 15 Text output  (part 1 of 2)                1/1/1  -> 1.00
  [21] 15 Text output  (part 2 of 2)                1/1/1  -> 1.00
  [22] 16 Core Library Framework scope              1/1/1  -> 1.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            2/2/2  -> 2.00
  [25] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [26] 4. The affine space                          2/2/2  -> 2.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    0/2/2  -> 1.33
  [29] 18 Design details and rationale  (part 1 ... 2/1/1  -> 1.33
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  1/2/2  -> 1.67
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              2/2/2  -> 2.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.
candidate 2 (found by 3 of 117 passes): Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.
candidate 3 (found by 3 of 117 passes): The abundance of `double` parameters makes it easy to accidentally switch values and there is no way of noticing such a mistake at compile-time.
candidate 4 (found by 3 of 117 passes): The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.

## audience - grade 1.33 (fired in 2 of 39 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
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
  [26] 4. The affine space                          1/0/1  -> 0.67
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
candidate 1 (found by 2 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 2 (found by 2 of 117 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 3 (found by 1 of 117 passes): The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++].

## prior_art - grade 2.00 (fired in 24 of 39 sections, strong in 13)  (SHARED PASSAGE)
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
  [13] 12 Usage examples                            1/1/1  -> 1.00
  [14] 13 Why do we need typed quantities?          2/2/2  -> 2.00
  [15] 14 Systems of quantities and units           1/1/1  -> 1.00
  [16] 1. Implicit conversions                      0/0/0  -> 0.00
  [17] 2. Explicit conversions                      0/0/0  -> 0.00
  [18] 3. Explicit casts                            0/0/0  -> 0.00
  [19] 4. No conversion                             2/0/2  -> 1.33
  [20] 15 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [21] 15 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            1/1/1  -> 1.00
  [25] 3. Various quantities of the same kind       1/0/1  -> 0.67
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    2/2/2  -> 2.00
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [31] 1. Ordering                                  2/1/2  -> 1.67
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
candidate 4 (found by 3 of 117 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).

## vehicle - grade 1.50 (fired in 9 of 39 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/0  -> 0.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               0/1/1  -> 0.67
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
  [23] 1. Core library                              0/0/1  -> 0.33
  [24] 2. Quantity kinds                            0/1/0  -> 0.33
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               1/1/1  -> 1.00
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 1/1/1  -> 1.00
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
candidate 1 (found by 3 of 117 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 2 (found by 3 of 117 passes): However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.
candidate 3 (found by 3 of 117 passes): If we do not intend to have text output, we should remove symbol text from the core framework class templates.
candidate 4 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.

## coordination - grade 1.67 (fired in 7 of 39 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 1/1/0  -> 0.67
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
  [24] 2. Quantity kinds                            1/0/1  -> 0.67
  [25] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [26] 4. The affine space                          1/1/1  -> 1.00
  [27] 5. Text output                               1/0/0  -> 0.33
  [28] 17 Safety                                    0/0/0  -> 0.00
  [29] 18 Design details and rationale  (part 1 ... 2/2/0  -> 1.33
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
candidate 2 (found by 3 of 117 passes): If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
candidate 3 (found by 2 of 117 passes): We desperately need to be able to express more quantities and units in a standardized way so different libraries get means to communicate with each other.
candidate 4 (found by 2 of 117 passes): It also means that we will be able to pass a quantity of *solid angular measure* to a function that takes `angular measure`.

## insufficiency - grade 0.67 (fired in 5 of 39 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 1.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 1/0/1  -> 0.67
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
  [26] 4. The affine space                          0/1/0  -> 0.33
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    0/2/0  -> 0.67
  [29] 18 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  1/1/0  -> 0.67
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            0/0/1  -> 0.33
  [34] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [35] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [36] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [37] 19 Teachability                              0/0/0  -> 0.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 117 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 2 (found by 2 of 117 passes): As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list.
candidate 3 (found by 1 of 117 passes): the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.
candidate 4 (found by 1 of 117 passes): [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.

## implementation - grade 2.00  [binary: max] (fired in 14 of 39 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/2/1  -> 1.00
  [8] 7 Motivation                                 2/2/1  -> 1.67
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
  [20] 15 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [21] 15 Text output  (part 2 of 2)                0/2/0  -> 0.67
  [22] 16 Core Library Framework scope              0/0/0  -> 0.00
  [23] 1. Core library                              0/0/0  -> 0.00
  [24] 2. Quantity kinds                            0/0/0  -> 0.00
  [25] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [26] 4. The affine space                          0/0/0  -> 0.00
  [27] 5. Text output                               0/0/0  -> 0.00
  [28] 17 Safety                                    1/2/2  -> 1.67
  [29] 18 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [30] 18 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [31] 1. Ordering                                  0/0/0  -> 0.00
  [32] 2. Aggregation                               0/0/0  -> 0.00
  [33] 3. Simplification                            2/2/2  -> 2.00
  [34] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [35] 4. Repacking  (part 2 of 3)                  1/1/1  -> 1.00
  [36] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [37] 19 Teachability                              1/1/1  -> 1.00
  [38] 20 Acknowledgements                          0/0/0  -> 0.00
  [39] 21 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).
candidate 2 (found by 3 of 117 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.
candidate 3 (found by 3 of 117 passes): In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin.
candidate 4 (found by 3 of 117 passes): However, the feedback we got from the production usage was that such an approach is really bad for generic programming.

-->
