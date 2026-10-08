Verdict: Strong (8/14)

The paper offers solid evidence that the proposed change addresses a real, user-visible inconsistency and has substantial implementation backing, but it is much thinner when it comes to showing why this needs to be done in the standard itself rather than through existing library mechanisms. The strongest material concerns practical experience and measurable impact, while the weakest areas are the absence of any argument that a library solution is insufficient and only cursory treatment of standardization-specific justification and coordination.

- The paper clearly establishes that the change matters by connecting it to surprising behavior, performance regressions, and divergence from widely used formatting practice.
- It provides credible implementation experience through benchmark results and the long deployment history of the {fmt} library.
- The discussion of prior art and alternatives is well supported by references to Python-style formatting and other mainstream languages.
- The paper does not establish why a library cannot address the problem, leaving a central standardization rationale unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 7.33   accumulate 9.17   max 10.33

## SUMMARY
grades: motivation 1.83  audience 1.50  prior_art 1.50  vehicle 0.17  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.00 / 8.00 / 8.50   (all 3 samples: 8.00)
headings: h2 12
on threshold: audience, prior_art, coordination, implementation
splits: motivation[2] 1/2/2  motivation[9] 2/1/1  vehicle[2] 0/0/1  implementation[2] 0/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/2/2  -> 1.67
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  2/1/1  -> 1.33
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The current paper proposes fixing the default floating-point representation in `std::format` (and `std::to_char`) to use exponent range, fixing the issues described above.
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): This is technically a breaking change for users who rely on the exact output that is being changed.
candidate 4 (found by 2 of 39 passes): this introduced a small but undesirable change compared to the design and reference implementation in [FMT], resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages

## audience - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++: ... normal 77.5 ns 77.5 ns 9040424 garbage 91.4 ns 91.4 ns 7675186
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): usage of which is currently at least an order of magnitude higher than that of `std::format`.

## prior_art - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): [FMT], which is modeled after Python’s formatting facility, adopted a similar representation based on the exponent range.
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 4 (found by 2 of 39 passes): This paper proposes fixing this issue, bringing the floating-point formatting on par with other languages and in line with the original design intent.

## vehicle - grade 0.17 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/1  -> 0.33
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   0/0/0  -> 0.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): This paper proposes fixing this issue, bringing the floating-point formatting on par with other languages and in line with the original design intent.

## coordination - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): As a result, an implementation of the default floating-point handling of `std::format` (and `std::to_chars`) cannot just directly rely on these otherwise perfectly appropriate algorithms.

## insufficiency - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   0/0/0  -> 0.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/1  -> 0.33
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++:
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 4 (found by 1 of 39 passes): bringing the floating-point formatting on par with other languages and in line with the original design intent.

-->
