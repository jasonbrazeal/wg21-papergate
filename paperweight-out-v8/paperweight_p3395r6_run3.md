Verdict: Adequate (6/14)

The paper offers solid support in a few important areas, particularly the motivation from existing encoding problems and the availability of implementation experience in {fmt}, but it leaves several parts of the standardization case largely unargued. The thinnest support concerns who is affected and why the work belongs in the standard rather than in a library, which makes the overall case feel narrower than the proposal itself.

- The strongest support is the concrete demonstration that the proposed formatter has already been implemented in {fmt}, alongside the observation that a related debug-formatting feature has seen no demand over years of use.
- The paper also clearly establishes why the current inserter behavior is confusing and why encoding issues in the underlying API need attention.
- The discussion of alternatives is useful in rejecting an encoding-communication approach and in distinguishing this work from P2930, though it does not fully establish why standardization is the right venue.
- The most glaring omission is any account of who is affected by the problem, and the paper likewise does not establish why a library solution would be insufficient in a portable setting.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 5 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.00   accumulate 6.50   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.67  insufficiency 0.17  implementation 1.67
sample agreement: 105 of 112 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 6.00 / 5.50   (all 3 samples: 6.17)
headings: h2 15
on threshold: prior_art, implementation
splits: prior_art[2] 0/1/1  prior_art[10] 1/0/1  prior_art[12] 1/2/1  coordination[11] 2/2/0
        insufficiency[11] 1/0/0  implementation[11] 0/0/1  implementation[14] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                2/2/2  -> 2.00
  [11] 10. Proposal                                 2/2/2  -> 2.00
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): the existing inserter has several issues, such as I/O manipulators applying only to the category name rather than the entire error code, resulting in confusing output
candidate 2 (found by 2 of 48 passes): This paper proposes making `std::error_code` formattable using the formatting facility introduced in C++20 (`std::format`) and fixes encoding issues in the underlying API ([LWG4156]).
candidate 3 (found by 2 of 48 passes): Obviously none of this is usable in a portable way through the generic `error_category` API because encodings can be and often are different.
candidate 4 (found by 1 of 48 passes): fixes encoding issues in the underlying API ([LWG4156]).

## audience - grade 0.00 (fired in 0 of 16 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                0/0/0  -> 0.00
  [11] 10. Proposal                                 0/0/0  -> 0.00
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/1/1  -> 0.67
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                1/0/1  -> 0.67
  [11] 10. Proposal                                 2/2/2  -> 2.00
  [12] 11. Previous work                            1/2/1  -> 1.33
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           1/1/1  -> 1.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): An alternative approach could involve communicating the encoding from `error_category`. However, this introduces ABI challenges and complicates usage compared to adopting a single encoding.
candidate 2 (found by 3 of 48 passes): A formatter for `std::error_code` was proposed as part of [P2930] which has more formatting options for the numeric code but doesn’t try to address encoding issues or provide a debug format.
candidate 3 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).
candidate 4 (found by 1 of 48 passes): fixes encoding issues in the underlying API ([LWG4156]).

## vehicle - grade 0.00 (fired in 0 of 16 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                0/0/0  -> 0.00
  [11] 10. Proposal                                 0/0/0  -> 0.00
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.67 (fired in 1 of 16 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                0/0/0  -> 0.00
  [11] 10. Proposal                                 2/2/0  -> 1.33
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding. However, there is significant divergence in message encodings.

## insufficiency - grade 0.17 (fired in 1 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                0/0/0  -> 0.00
  [11] 10. Proposal                                 1/0/0  -> 0.33
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): Obviously none of this is usable in a portable way through the generic `error_category` API because encodings can be and often are different.

## implementation - grade 1.67  [binary: max] (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R5                          0/0/0  -> 0.00
  [4] 3. Changes since R4                          0/0/0  -> 0.00
  [5] 4. Changes since R3                          0/0/0  -> 0.00
  [6] 5. Changes since R2                          0/0/0  -> 0.00
  [7] 6. Changes since R1                          0/0/0  -> 0.00
  [8] 7. Changes since R0                          0/0/0  -> 0.00
  [9] 8. Polls                                     0/0/0  -> 0.00
  [10] 9. Motivation                                0/0/0  -> 0.00
  [11] 10. Proposal                                 0/0/1  -> 0.33
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           2/1/2  -> 1.67
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).
candidate 2 (found by 1 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.

-->
