Verdict: Adequate to Strong (8/14)

The paper offers solid evidence that the current behavior is a real regression from established practice, with measurable performance costs and a widely deployed reference implementation behind the proposed change. Its support is thinnest when it comes to explaining why this needs to be a standard-library specification change rather than something addressable through implementation choices or library-level fixes.

- The strongest support comes from implementation experience: the proposal is based on a widely used library with years of deployment and documented past format changes.
- The paper clearly establishes who is affected and why the current default produces surprising results and performance regressions for users.
- Prior art and alternatives are well covered, showing that the proposed behavior matches Python-style formatting and the existing {fmt} design.
- The most glaring omission is the lack of an established case for why the standard itself must change, as opposed to leaving room for implementations or libraries to handle the issue.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.33   accumulate 8.67   max 9.33

## SUMMARY
grades: motivation 1.83  audience 1.50  prior_art 1.50  vehicle 0.00  coordination 0.50  insufficiency 0.17  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 8.00 / 8.00   (all 3 samples: 7.50)
headings: h2 12
on threshold: audience, prior_art, implementation
splits: motivation[2] 1/2/2  motivation[9] 1/2/2  coordination[8] 0/1/2  insufficiency[2] 0/1/0
        implementation[2] 0/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 3)  (SHARED PASSAGE)
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
  [9] 8. Proposal                                  1/2/2  -> 1.67
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): this introduced a small but undesirable change compared to the design and reference implementation in [FMT], resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages
candidate 2 (found by 3 of 39 passes): Apart from giving a false sense of accuracy to users it also has negative performance implications.
candidate 3 (found by 3 of 39 passes): The current paper proposes fixing the default floating-point representation in `std::format` (and `std::to_char`) to use exponent range, fixing the issues described above.
candidate 4 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.

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
candidate 3 (found by 2 of 39 passes): usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 4 (found by 1 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.

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
candidate 4 (found by 2 of 39 passes): When `std::format` was proposed for standardization, floating-point formatting was defined in terms of `std::to_chars` to simplify specification.

## vehicle - grade 0.00 (fired in 0 of 13 sections, strong in 0)
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

## coordination - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   0/1/2  -> 1.00
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): When `std::format` was proposed for standardization, floating-point formatting was defined in terms of `std::to_chars` to simplify specification with the assumption that the latter follows the industry practice for the default format described above.

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/1/0  -> 0.33
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
candidate 1 (found by 1 of 39 passes): This introduced a small but undesirable change compared to the design and reference implementation in [FMT], resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages

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
candidate 4 (found by 1 of 39 passes): resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages

-->
