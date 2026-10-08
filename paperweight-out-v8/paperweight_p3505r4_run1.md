Verdict: Strong (8/14)

The paper offers solid support for its standardization case in the areas of practical impact, prior art, and implementation experience, but it leaves the argument for why this must be done in the standard rather than in a library essentially unaddressed. The thinnest parts are the standard-specific rationale and the coordination story, which are asserted more than demonstrated.

- The strongest support comes from the demonstrated performance and behavior problems in the current default formatting, backed by concrete benchmark results and the widespread deployment of the {fmt} implementation.
- The paper also credibly establishes prior art and alternatives by pointing to {fmt}’s long-standing use of exponent-range formatting and the precedent of changing that library’s output format.
- The case for why the standard itself must change is only claimed, resting on alignment with other languages and original design intent without showing what standardization uniquely enables.
- The most glaring omission is the absence of any argument for why a library-level solution would not suffice, leaving the core standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 6 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 6.67   accumulate 9.33   max 10.67

## SUMMARY
grades: motivation 1.67  audience 1.50  prior_art 1.67  vehicle 0.33  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.50 / 7.50 / 8.50   (all 3 samples: 8.17)
headings: h2 12
on threshold: motivation, audience, prior_art, coordination, implementation
splits: motivation[1] 0/1/0  motivation[2] 2/1/1  audience[2] 1/1/0  prior_art[2] 1/1/2
        vehicle[2] 1/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 6 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [2] 1. Introduction                              2/1/1  -> 1.33
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/2  -> 2.00
  [9] 8. Proposal                                  1/1/1  -> 1.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Apart from giving a false sense of accuracy to users it also has negative performance implications.
candidate 2 (found by 3 of 39 passes): The current paper proposes fixing the default floating-point representation in `std::format` (and `std::to_char`) to use exponent range, fixing the issues described above.
candidate 3 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 4 (found by 3 of 39 passes): Also reliance on the exact representation of floating-point numbers is usually discouraged so the impact of this change is likely moderate.

## audience - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/0  -> 0.67
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
candidate 3 (found by 2 of 39 passes): resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages that have similar facilities.
candidate 4 (found by 2 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++: ... normal 77.5 ns 77.5 ns 9040424 garbage 91.4 ns 91.4 ns 7675186

## prior_art - grade 1.67 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/2  -> 1.33
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
candidate 4 (found by 1 of 39 passes): floating-point formatting was defined in terms of `std::to_chars` to simplify specification.

## vehicle - grade 0.33 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/0/1  -> 0.67
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
candidate 1 (found by 2 of 39 passes): bringing the floating-point formatting on par with other languages and in line with the original design intent.

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
candidate 1 (found by 3 of 39 passes): When `std::format` was proposed for standardization, floating-point formatting was defined in terms of `std::to_chars` to simplify specification with the assumption that the latter follows the industry practice for the default format described above.

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
