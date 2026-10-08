Verdict: Excellent (12/14)

The paper offers substantial support for its standardization case, with most of the required elements clearly established through production experience, community adoption, and explicit statements of need. The support is thinnest where it must show that a library solution is insufficient, since several of those arguments are asserted rather than demonstrated with evidence.

- The strongest support comes from implementation experience, where the paper points to widely adopted libraries, production feedback, and compiler-verified performance parity with raw arithmetic.
- The paper also clearly establishes why the feature matters and who is affected, citing concrete failure modes and a large existing user base across multiple roles.
- Prior art and alternatives are well covered through references to existing libraries and design discussions, showing the proposal builds on tested approaches.
- The most glaring omission is the case for why a library will not do, where claims about distinguishing units, modeling temperatures, and certification requirements are made without sufficient evidence that standardization is the only viable path.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.33/14)

Provisionally addressed: 7 of 7. Provisional points: 12.33 of 14. Unsupported quotes rejected: 19. Replies missing: 0. Sections: 41. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.33   corroborated 12.00   accumulate 13.50   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 0.83  implementation 2.00
sample agreement: 262 of 287 section-criterion pairs unanimous (91%)
single-sample totals would have been: 12.50 / 12.50 / 12.50   (all 3 samples: 12.33)
headings: h2 23 + bold numbered 13
on threshold: audience
splits: motivation[3] 1/0/1  motivation[13] 0/1/1  motivation[19] 0/1/0  motivation[22] 1/1/0
        motivation[33] 1/2/2  audience[27] 0/0/1  audience[28] 0/1/0  prior_art[3] 0/0/1
        prior_art[6] 0/1/1  prior_art[9] 0/1/1  prior_art[10] 1/2/2  prior_art[21] 2/0/1
        prior_art[26] 0/1/1  prior_art[33] 1/2/1  vehicle[6] 0/1/0  vehicle[39] 1/1/0
        coordination[29] 0/1/1  coordination[32] 2/2/0  coordination[33] 1/1/0
        insufficiency[8] 0/0/1  insufficiency[26] 0/1/1  insufficiency[28] 1/0/1
        insufficiency[30] 0/0/1  insufficiency[35] 0/0/1  implementation[8] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 24 of 41 sections, strong in 15)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Scope of this proposal                     1/1/1  -> 1.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 2/2/2  -> 2.00
  [10] 9 Design goals                               1/1/1  -> 1.00
  [11] 10 Quick domain introduction                 0/0/0  -> 0.00
  [12] 11 API overview                              0/0/0  -> 0.00
  [13] 12 Representation Types                      0/1/1  -> 0.67
  [14] 13 Hello units                               0/0/0  -> 0.00
  [15] 14 Usage examples                            0/0/0  -> 0.00
  [16] 15 Why do we need typed quantities?          0/0/0  -> 0.00
  [17] 16 Systems of quantities and units           2/2/2  -> 2.00
  [18] 1. Implicit conversions                      0/0/0  -> 0.00
  [19] 2. Explicit conversions                      0/1/0  -> 0.33
  [20] 3. Explicit casts                            0/0/0  -> 0.00
  [21] 4. No conversion                             2/2/2  -> 2.00
  [22] 17 Text output  (part 1 of 2)                1/1/0  -> 0.67
  [23] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [24] 18 Core Library Framework scope              1/1/1  -> 1.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            2/2/2  -> 2.00
  [27] 3. Various quantities of the same kind       2/2/2  -> 2.00
  [28] 4. The affine space                          2/2/2  -> 2.00
  [29] 5. Text output                               1/1/1  -> 1.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 1/1/1  -> 1.00
  [33] 1. Ordering                                  1/2/2  -> 1.67
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
candidate 4 (found by 3 of 123 passes): From the engineering point of view, sometimes Unicode text might not be the best solution as terminals of many (especially embedded) devices can output only letters from the basic literal character set only.

## audience - grade 1.50 (fired in 4 of 41 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
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
  [28] 4. The affine space                          0/1/0  -> 0.33
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  0/0/0  -> 0.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).
candidate 2 (found by 3 of 123 passes): Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B).
candidate 3 (found by 1 of 123 passes): Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing forward velocity to sink rate parameters, or kinetic energy substituting for potential energy.
candidate 4 (found by 1 of 123 passes): Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.

## prior_art - grade 2.00 (fired in 27 of 41 sections, strong in 14)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/1  -> 0.33
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/1/1  -> 0.67
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 2/2/2  -> 2.00
  [9] 8 Common smells when there is no library ... 0/1/1  -> 0.67
  [10] 9 Design goals                               1/2/2  -> 1.67
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
  [21] 4. No conversion                             2/0/1  -> 1.00
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [24] 18 Core Library Framework scope              1/1/1  -> 1.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            0/1/1  -> 0.67
  [27] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    2/2/2  -> 2.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/2  -> 2.00
  [33] 1. Ordering                                  1/2/1  -> 1.33
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            2/2/2  -> 2.00
  [36] 4. Repacking  (part 1 of 3)                  2/2/2  -> 2.00
  [37] 4. Repacking  (part 2 of 3)                  2/2/2  -> 2.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              1/1/1  -> 1.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.
candidate 2 (found by 3 of 123 passes): The next example serves as a showcase of various features available in the [[mp-units]](https://mpusz.github.io/mp-units) library.
candidate 3 (found by 3 of 123 passes): Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety.
candidate 4 (found by 3 of 123 passes): The above grammar for `unit-symbol-solidus` is consistent with the current state of [[mp-units]](https://mpusz.github.io/mp-units). However, a few aternatives are possible:

## vehicle - grade 2.00 (fired in 8 of 41 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/1/0  -> 0.33
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
  [39] 21 Teachability                              1/1/0  -> 0.67
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library.
candidate 2 (found by 3 of 123 passes): Companies often have a policy that the software they use must obey all the rules MISRA provides.
candidate 3 (found by 3 of 123 passes): if we never decide to standardize it, then all the symbols provided in unit and dimension definitions will be useless.
candidate 4 (found by 3 of 123 passes): The primary motivation is **error message quality**: when a type mismatch occurs, the compiler reports the full qualified name of every type involved.

## coordination - grade 2.00 (fired in 8 of 41 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 8 Common smells when there is no library ... 1/1/1  -> 1.00
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
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/1/1  -> 1.00
  [29] 5. Text output                               0/1/1  -> 0.67
  [30] 19 Safety                                    0/0/0  -> 0.00
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 2/2/0  -> 1.33
  [33] 1. Ordering                                  1/1/0  -> 0.67
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/0  -> 0.00
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  2/2/2  -> 2.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 123 passes): the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.
candidate 2 (found by 2 of 123 passes): There is no shared vocabulary between different libraries. User-facing APIs use ad-hoc conventions.
candidate 3 (found by 2 of 123 passes): Users will also not be able to model their own distinct abstractions like we showed in the case of the audio example (samples, beats, etc.).
candidate 4 (found by 2 of 123 passes): if we never decide to standardize it, then all the symbols provided in unit and dimension definitions will be useless.

## insufficiency - grade 0.83 (fired in 6 of 41 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              0/0/0  -> 0.00
  [8] 7 Motivation                                 0/0/1  -> 0.33
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
  [26] 2. Quantity kinds                            0/1/1  -> 0.67
  [27] 3. Various quantities of the same kind       0/0/0  -> 0.00
  [28] 4. The affine space                          1/0/1  -> 0.67
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    0/0/1  -> 0.33
  [31] 20 Design details and rationale  (part 1 ... 0/0/0  -> 0.00
  [32] 20 Design details and rationale  (part 2 ... 0/0/0  -> 0.00
  [33] 1. Ordering                                  1/1/1  -> 1.00
  [34] 2. Aggregation                               0/0/0  -> 0.00
  [35] 3. Simplification                            0/0/1  -> 0.33
  [36] 4. Repacking  (part 1 of 3)                  0/0/0  -> 0.00
  [37] 4. Repacking  (part 2 of 3)                  0/0/0  -> 0.00
  [38] 4. Repacking  (part 3 of 3)                  0/0/0  -> 0.00
  [39] 21 Teachability                              0/0/0  -> 0.00
  [40] 22 Acknowledgements                          0/0/0  -> 0.00
  [41] 23 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 123 passes): If we remove this feature, we would not be able to make a distinction between `Hz`, `Bq`, and `Bd`, or `rad`, `sr` and `bit`, or `Gy` and `Sv` as the quantities associated with those units have the same dimensions.
candidate 2 (found by 2 of 123 passes): However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin.
candidate 3 (found by 2 of 123 passes): As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list.
candidate 4 (found by 1 of 123 passes): Such certification requires a specification to be certified against, and those tools often do not have one.

## implementation - grade 2.00  [binary: max] (fired in 16 of 41 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope of this proposal                     0/0/0  -> 0.00
  [5] 4 Terms and definitions                      0/0/0  -> 0.00
  [6] 5 Impact on the C++ standard                 0/0/0  -> 0.00
  [7] 6 About authors                              2/2/2  -> 2.00
  [8] 7 Motivation                                 1/2/2  -> 1.67
  [9] 8 Common smells when there is no library ... 0/0/0  -> 0.00
  [10] 9 Design goals                               1/1/1  -> 1.00
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
  [21] 4. No conversion                             1/1/1  -> 1.00
  [22] 17 Text output  (part 1 of 2)                2/2/2  -> 2.00
  [23] 17 Text output  (part 2 of 2)                2/2/2  -> 2.00
  [24] 18 Core Library Framework scope              0/0/0  -> 0.00
  [25] 1. Core library                              0/0/0  -> 0.00
  [26] 2. Quantity kinds                            0/0/0  -> 0.00
  [27] 3. Various quantities of the same kind       1/1/1  -> 1.00
  [28] 4. The affine space                          0/0/0  -> 0.00
  [29] 5. Text output                               0/0/0  -> 0.00
  [30] 19 Safety                                    2/2/2  -> 2.00
  [31] 20 Design details and rationale  (part 1 ... 2/2/2  -> 2.00
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
candidate 1 (found by 3 of 123 passes): In the following years, the library’s authors focused on getting more feedback from the production about the design and developed version 2 of the [[mp-units]](https://mpusz.github.io/mp-units) library that resolves the issues raised by the users and Committee members.
candidate 2 (found by 3 of 123 passes): He is the creator and lead developer of [[Au]](https://aurora-opensource.github.io/au), a widely-adopted zero-dependency units library with novel features including vector space magnitudes and adaptive overflow protection.
candidate 3 (found by 3 of 123 passes): In practice, the [[mp-units]](https://mpusz.github.io/mp-units) implementation compiles to identical or faster assembly as equivalent code using raw `double` arithmetic — this can be verified via the Compiler Explorer links provided in the Usage examples chapter.
candidate 4 (found by 3 of 123 passes): Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).

-->
