Verdict: Strong (10/14)

The paper offers solid evidence that `__COUNTER__` is a widely implemented extension with consistent, unsurprising semantics, and it points to real usage such as Google Benchmark as implementation experience. Its case is thinnest where it moves from describing existing practice to justifying standardization itself: the arguments about portability, interoperability, and why a library cannot suffice are asserted rather than demonstrated.

- The strongest support is the established implementation experience, backed by named compilers and a concrete example of real-world use with fallback behavior.
- The paper also clearly establishes why the feature matters and who is affected, citing common metaprogramming uses and broad community reliance.
- The most glaring omission is the lack of an established argument for why the standard, rather than continued compiler extension or a library solution, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 7 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 10.00   accumulate 10.33   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.50  implementation 2.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 10.00 / 10.00 / 10.00   (all 3 samples: 10.00)
headings: h2 10
on threshold: audience, vehicle, coordination
splits: audience[4] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       2/2/2  -> 2.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This is useful for generating unique identifiers, generating unique indices, and other preprocessor metaprogramming uses.
candidate 2 (found by 3 of 33 passes): A brief survey of some uses of `__COUNTER__` in the C and C++ community:
candidate 3 (found by 3 of 33 passes): While `_` covers many uses of `__COUNTER__`, the preprocessor utility continues to be useful due to existing practice, uses outside local identifiers, other preprocessor metaprogramming uses of `__COUNTER__` beyond unique identifiers.
candidate 4 (found by 2 of 33 passes): `__COUNTER__` is a predefined macro provided as a language extension by all major C and C++ implementations.

## audience - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/1  -> 0.67
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             1/1/1  -> 1.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    2/2/2  -> 2.00
  [9] 7. Design Considerations                     0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The `__COUNTER__` predefined macro is a common language extension for C and C++
candidate 2 (found by 2 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard
candidate 3 (found by 2 of 33 passes): `__COUNTER__` has long been supported by all major implementations of C and C++:
candidate 4 (found by 1 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard in order to provide more clear portability and semantic guarantees.

## prior_art - grade 2.00 (fired in 7 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Previous Proposals                        2/2/2  -> 2.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       1/1/1  -> 1.00
  [8] 6. Implementation Support                    1/1/1  -> 1.00
  [9] 7. Design Considerations                     2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper aims to standardize existing practices and match WG14’s adoption of `__COUNTER__` for C2Y.
candidate 2 (found by 3 of 33 passes): The `__COUNTER__` predefined macro is a common language extension for C and C++ which expands to an integer literal that starts at `0` and increments by `1` every time it is expanded in a translation unit.
candidate 3 (found by 3 of 33 passes): Many additional uses include use for static assertions, however, that use case is now covered by built-in static assertion facilities.
candidate 4 (found by 3 of 33 passes): `__COUNTER__` has long been supported by all major implementations of C and C++:

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard in order to provide more clear portability and semantic guarantees.

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Codebases striving for maximum portability must resort to detection and fallback such as this example from google benchmark
candidate 2 (found by 1 of 33 passes): Codebases striving for maximum portability must resort to detection and fallback such as this example from google benchmark.

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             1/1/1  -> 1.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): In the absence of cautious checking and fallback, a developer must consult numerous widely used C++ implementations to convince themselves that `__COUNTER__` exists and does what they want.
candidate 2 (found by 1 of 33 passes): While every major C++ compiler today supports `__COUNTER__`, it’s not always enabled. For example, EDG only provides it outside of standards mode.

## implementation - grade 2.00  [binary: max] (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             1/1/1  -> 1.00
  [7] 5. Motivating Examples                       2/2/2  -> 2.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `__COUNTER__` is a predefined macro provided as a language extension by all major C and C++ implementations.
candidate 2 (found by 3 of 33 passes): Every major implementation supports it with unsurprising semantics.
candidate 3 (found by 3 of 33 passes): Google benchmark uses `__COUNTER__` for [unique identifiers](https://github.com/google/benchmark/blob/c19cfee61e136effb05a7fc8a037b0db3b13bd4c/include/benchmark/benchmark.h#L1531-L1538), falling back to `__LINE__` if `__COUNTER__` isn’t present or doesn’t behave as expected
candidate 4 (found by 3 of 33 passes): This is the current behavior on all compilers tested on Compiler Explorer except Chibicc, which produces `0 1`.

-->
