Verdict: Strong (9/14)

The paper offers solid grounding in existing practice and implementation experience, particularly through its connection to the widely used {fmt} library and concrete performance measurements. Its case is thinnest where it needs to show that the problem cannot be solved outside the standard and that the affected audience and interoperability concerns are more than asserted.

- The strongest support comes from the demonstrated implementation experience, including years of use in {fmt} and benchmark results on a real standard library.
- The paper establishes meaningful prior art by tracing the design through Python’s formatting facility and {fmt}, and by noting past experience with output changes.
- The rationale for why the standard must change is asserted rather than shown, leaving the necessity of standardization less supported.
- The most glaring omission is the absence of any argument for why a library-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 6 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 8.00   accumulate 9.83   max 10.67

## SUMMARY
grades: motivation 1.83  audience 1.17  prior_art 1.50  vehicle 1.00  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.50 / 8.50 / 9.00   (all 3 samples: 8.83)
headings: h2 12
on threshold: prior_art, vehicle, coordination, implementation
splits: motivation[2] 2/1/2  audience[8] 2/0/2  audience[11] 0/1/1  vehicle[2] 1/0/0
        vehicle[8] 1/2/2  coordination[8] 2/2/1
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
  [11] 10. Implementation and usage experience      1/1/1  -> 1.00
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The current paper proposes fixing the default floating-point representation in `std::format` (and `std::to_char`) to use exponent range, fixing the issues described above.
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): This is technically a breaking change for users who rely on the exact output that is being changed.
candidate 4 (found by 2 of 39 passes): this introduced a small but undesirable change compared to the design and reference implementation in [FMT], resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages that have similar facilities.

## audience - grade 1.17 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/0/2  -> 1.33
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/1/1  -> 0.67
  [12] 11. Impact on existing code                  1/1/1  -> 1.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 2 (found by 2 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++: ... normal 77.5 ns ... garbage 91.4 ns
candidate 3 (found by 2 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.

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
candidate 1 (found by 3 of 39 passes): When `std::format` was proposed for standardization, floating-point formatting was defined in terms of `std::to_chars` to simplify specification.
candidate 2 (found by 3 of 39 passes): [FMT], which is modeled after Python’s formatting facility, adopted a similar representation based on the exponent range.
candidate 3 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 4 (found by 3 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.

## vehicle - grade 1.00 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/0/0  -> 0.33
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   1/2/2  -> 1.67
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): As a result, an implementation of the default floating-point handling of `std::format` (and `std::to_chars`) cannot just directly rely on these otherwise perfectly appropriate algorithms.
candidate 2 (found by 1 of 39 passes): This paper proposes fixing this issue, bringing the floating-point formatting on par with other languages and in line with the original design intent.

## coordination - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Changes since R3                          0/0/0  -> 0.00
  [4] 3. Changes since R2                          0/0/0  -> 0.00
  [5] 4. Changes since R1                          0/0/0  -> 0.00
  [6] 5. Changes since R0                          0/0/0  -> 0.00
  [7] 6. Polls                                     0/0/0  -> 0.00
  [8] 7. Problem                                   2/2/1  -> 1.67
  [9] 8. Proposal                                  0/0/0  -> 0.00
  [10] 9. Wording                                   0/0/0  -> 0.00
  [11] 10. Implementation and usage experience      0/0/0  -> 0.00
  [12] 11. Impact on existing code                  0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): When `std::format` was proposed for standardization, floating-point formatting was defined in terms of `std::to_chars` to simplify specification with the assumption that the latter follows the industry practice for the default format described above.
candidate 2 (found by 2 of 39 passes): resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages that have similar facilities
candidate 3 (found by 1 of 39 passes): resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages that have similar facilities.

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
candidate 1 (found by 3 of 39 passes): Results on macOS with Apple clang version 16.0.0 (clang-1600.0.26.6) and libc++:
candidate 2 (found by 3 of 39 passes): The current proposal is based on the existing implementation in [FMT] which has been available and widely used for over 6 years.
candidate 3 (found by 3 of 39 passes): In the past we had experience with changing the output format in [FMT], usage of which is currently at least an order of magnitude higher than that of `std::format`.
candidate 4 (found by 2 of 39 passes): resulting in surprising behavior to users, performance regression and an inconsistency with other mainstream programming languages

-->
