Verdict: Strong (10/14)

The paper gives solid evidence that `__COUNTER__` is a widely implemented, widely used extension with consistent semantics, and it makes a reasonable case that standardizing it would align C++ with existing practice and with WG14’s direction. The support is thinnest where the paper needs to explain why standardization—rather than continued reliance on the de facto extension—is necessary, and why a library-level or alternative preprocessor mechanism cannot serve the same purpose.

- The strongest support is the demonstration of broad, consistent implementation experience across major compilers and real-world use such as google benchmark.
- The paper also clearly establishes why the feature matters for unique identifiers and preprocessor metaprogramming, and who is affected by its absence from the standard.
- The case for why the standard specifically must adopt it, beyond matching C2Y, is asserted but not developed.
- The most glaring omission is the lack of any real argument for why a library or other existing language facility cannot adequately cover the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 7 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 11.00   accumulate 10.17   max 12.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.17  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.50 / 10.00 / 10.00   (all 3 samples: 10.17)
headings: h2 10
on threshold: vehicle
splits: audience[4] 1/0/1  prior_art[4] 1/1/0  vehicle[2] 1/0/0  implementation[2] 0/1/0
        implementation[6] 2/2/1
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
candidate 1 (found by 3 of 33 passes): This paper aims to standardize existing practices and match WG14’s adoption of `__COUNTER__` for C2Y.
candidate 2 (found by 3 of 33 passes): This is useful for generating unique identifiers, generating unique indices, and other preprocessor metaprogramming uses.
candidate 3 (found by 3 of 33 passes): A brief survey of some uses of `__COUNTER__` in the C and C++ community:
candidate 4 (found by 3 of 33 passes): While `_` covers many uses of `__COUNTER__`, the preprocessor utility continues to be useful due to existing practice, uses outside local identifiers, other preprocessor metaprogramming uses of `__COUNTER__` beyond unique identifiers.

## audience - grade 2.00 (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/1  -> 0.67
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/2  -> 2.00
  [7] 5. Motivating Examples                       0/0/0  -> 0.00
  [8] 6. Implementation Support                    2/2/2  -> 2.00
  [9] 7. Design Considerations                     2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `__COUNTER__` has long been supported by all major implementations of C and C++:
candidate 2 (found by 3 of 33 passes): As an example of use of `__COUNTER__` beyond local identifiers google benchmark uses uniquely-named identifiers at namespace-scope to register benchmark functions:
candidate 3 (found by 2 of 33 passes): The `__COUNTER__` predefined macro is a common language extension for C and C++
candidate 4 (found by 2 of 33 passes): Every major implementation supports it with unsurprising semantics.

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

## vehicle - grade 1.17 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
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
candidate 2 (found by 1 of 33 passes): This paper aims to standardize existing practices and match WG14’s adoption of `__COUNTER__` for C2Y.

## coordination - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard in order to provide more clear portability and semantic guarantees.

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
candidate 1 (found by 3 of 33 passes): Due to fairly widespread use, both in C and C++, it would be useful to incorporate the existing practice of `__COUNTER__` into the official standard in order to provide more clear portability and semantic guarantees.

## implementation - grade 2.00  [binary: max] (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Previous Proposals                        0/0/0  -> 0.00
  [6] 4. Rationale for Standardization             2/2/1  -> 1.67
  [7] 5. Motivating Examples                       2/2/2  -> 2.00
  [8] 6. Implementation Support                    0/0/0  -> 0.00
  [9] 7. Design Considerations                     2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Every major implementation supports it with unsurprising semantics.
candidate 2 (found by 3 of 33 passes): Google benchmark uses `__COUNTER__` for [unique identifiers](https://github.com/google/benchmark/blob/c19cfee61e136effb05a7fc8a037b0db3b13bd4c/include/benchmark/benchmark.h#L1531-L1538), falling back to `__LINE__` if `__COUNTER__` isn’t present or doesn’t behave as expected
candidate 3 (found by 3 of 33 passes): This is the current behavior on all compilers tested on Compiler Explorer except Chibicc, which produces `0 1`.
candidate 4 (found by 1 of 33 passes): This paper aims to standardize existing practices and match WG14’s adoption of `__COUNTER__` for C2Y.

-->
