Verdict: Strong to Excellent (11/14)

The paper offers solid support for standardizing `__COUNTER__` on the grounds of existing practice, widespread implementation, and clear utility, though its case is thinner when it comes to showing why standardization—rather than continued reliance on the extension—is necessary, and it does not convincingly rule out a library-level or other non-core-language solution.

- The strongest support comes from the paper’s demonstration that every major implementation already provides `__COUNTER__` with consistent, unsurprising semantics, backed by concrete compiler evidence and real-world usage such as google benchmark.
- The paper also clearly establishes why the feature matters and who is affected, citing common metaprogramming needs and the portability burden created by the current extension-only status.
- The most notable gap is the claim that a library cannot address the need, which is asserted but not substantiated with any argument or example showing why the preprocessor-level behavior is irreplaceable outside the core language.
- A further weakness is the coordination and interoperability discussion, where the paper points to existing divergence and fallback code but does not establish how standardization would resolve those issues or align implementations beyond what already exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 11.00   accumulate 11.33   max 13.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.50  coordination 1.33  insufficiency 0.50  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 12.00 / 11.00 / 11.00   (all 3 samples: 11.33)
headings: h2 10
on threshold: vehicle, coordination
splits: audience[2] 0/1/1  audience[4] 0/0/1  audience[9] 2/0/2  prior_art[4] 1/1/0
        coordination[9] 2/0/0
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

## audience - grade 2.00 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/1  -> 0.33
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    2/2/2  -> 2.00
  [9] 7. Design Considerations                     2/0/2  -> 1.33
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Every major implementation supports it with unsurprising semantics.
candidate 2 (found by 2 of 33 passes): `__COUNTER__` is a predefined macro provided as a language extension by all major C and C++ implementations.
candidate 3 (found by 2 of 33 passes): `__COUNTER__` has long been supported by all major implementations of C and C++: | Compiler | Earliest Version On Compiler Explorer |
candidate 4 (found by 1 of 33 passes): The `__COUNTER__` predefined macro is a common language extension for C and C++

## prior_art - grade 2.00 (fired in 7 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/0  -> 0.67
  [5] 3. Previous Proposals                        2/2/2  -> 2.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       1/1/1  -> 1.00
  [8] 6. Implementation Support                    1/1/1  -> 1.00
  [9] 7. Design Considerations                     2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper aims to standardize existing practices and match WG14’s adoption of `__COUNTER__` for C2Y.
candidate 2 (found by 3 of 33 passes): In the case of google benchmark, `__LINE__` is an adequate fallback due to how `BENCHMARK` macros are typically used. However, this is not an adequate general-purpose replacement due to it not being unique in the general case.
candidate 3 (found by 3 of 33 passes): Many additional uses include use for static assertions, however, that use case is now covered by built-in static assertion facilities.
candidate 4 (found by 3 of 33 passes): `__COUNTER__` has long been supported by all major implementations of C and C++:

## vehicle - grade 1.50 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper aims to standardize existing practices and match WG14’s adoption of `__COUNTER__` for C2Y.
candidate 2 (found by 3 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard in order to provide more clear portability and semantic guarantees.

## coordination - grade 1.33 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     2/0/0  -> 0.67
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Codebases striving for maximum portability must resort to detection and fallback such as this example from google benchmark
candidate 2 (found by 1 of 33 passes): Codebases striving for maximum portability must resort to detection and fallback such as this example from google benchmark.
candidate 3 (found by 1 of 33 passes): Currently, Clang diverges from MSVC and GCC in the following example. It produces `0` while the others produce `1`

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard in order to provide more clear portability and semantic guarantees.
candidate 2 (found by 1 of 33 passes): In the absence of cautious checking and fallback, a developer must consult numerous widely used C++ implementations to convince themselves that `__COUNTER__` exists and does what they want.

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
