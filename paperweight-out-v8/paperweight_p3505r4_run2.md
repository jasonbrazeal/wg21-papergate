Verdict: Strong (9/14)

The paper offers solid support in the areas that matter most for motivating the change and showing it is practical, but it leaves the standardization-specific justification comparatively thin. The strongest material concerns real-world impact, prior art, and implementation experience, while the case for why this must be done in the standard rather than in a library is essentially absent.

- The paper convincingly establishes that the current behavior causes surprising output, performance regressions, and divergence from widely used formatting libraries and other languages.
- It shows meaningful implementation experience through the long-standing {fmt} behavior and includes concrete benchmark results from a standard library implementation.
- The discussion of why existing algorithms cannot simply be reused by implementations gestures at a standardization need but does not fully connect that limitation to a requirement for normative change.
- The paper does not establish why a library-level solution would be insufficient, leaving the most fundamental question about standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 8.67   accumulate 9.33   max 10.67

## SUMMARY
grades: motivation 1.83  audience 1.50  prior_art 1.83  vehicle 1.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.00 / 8.00 / 9.50   (all 3 samples: 8.50)
headings: h2 12
on threshold: audience, vehicle, implementation
splits: motivation[2] 2/1/2  motivation[11] 1/1/0  prior_art[2] 1/2/2  coordination[8] 0/0/2
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/1/2  -> 1.67
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  1/1/1  -> 1.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/0  -> 0.67
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): this introduced a small but undesirable change compared to the design and reference implementation in [FMT], resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages
candidate 2 (found by 3 of 39 passes): The current paper proposes fixing the default floating-point representation in `std::format` (and `std::to_char`) to use exponent range, fixing the issues described above.
candidate 3 (found by 3 of 39 passes): Also reliance on the exact representation of floating-point numbers is usually discouraged so the impact of this change is likely moderate.
candidate 4 (found by 2 of 39 passes): This problem is that `std::to_chars` defines "shortness" in terms of the number of characters in the output which is different from the "shortness" of decimal significand normally used both in the literature and in the industry.

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
candidate 1 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 2 (found by 3 of 39 passes): usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 3 (found by 2 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++: ... normal 77.5 ns ... garbage 91.4 ns
candidate 4 (found by 1 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++: ... normal 77.5 ns 77.5 ns 9040424 garbage 91.4 ns 91.4 ns 7675186

## prior_art - grade 1.83 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 2 (found by 3 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 3 (found by 2 of 39 passes): [FMT], which is modeled after Python’s formatting facility, adopted a similar representation based on the exponent range.
candidate 4 (found by 1 of 39 passes): bringing the floating-point formatting on par with other languages and in line with the original design intent.

## vehicle - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
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

## coordination - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   0/0/2  -> 0.67
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): This problem is that `std::to_chars` defines "shortness" in terms of the number of characters in the output which is different from the "shortness" of decimal significand normally used both in the literature and in the industry.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
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
candidate 1 (found by 3 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++:
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.

-->
