Verdict: Adequate (7/14)

The paper offers solid support in a few areas, particularly in identifying concrete problems with the current `error_code` output and in showing that a formatter has already been implemented in {fmt}. However, the case for standardization is thin where it matters most: the paper does not establish why this needs to be in the standard rather than a library, nor does it show that the affected audience is asking for it.

- The strongest support is the implementation experience, since the proposed formatter exists in {fmt} and the paper also notes the absence of user demand for it there.
- The paper clearly establishes the motivating problems, including encoding inconsistencies and confusing inserter behavior.
- The weakest support is the lack of any established reason for standardization itself, leaving the central question unanswered.
- A glaring omission is the failure to establish who is actually affected, since the only evidence offered is that no one has requested the functionality over years of use.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.00/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.33   accumulate 7.00   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 1.67
sample agreement: 108 of 112 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 15
on threshold: coordination, implementation
splits: audience[11] 0/0/2  prior_art[10] 1/1/0  implementation[11] 1/0/1
        implementation[14] 2/2/1
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
candidate 1 (found by 3 of 48 passes): Obviously none of this is usable in a portable way through the generic `error_category` API because encodings can be and often are different.
candidate 2 (found by 2 of 48 passes): This paper proposes making `std::error_code` formattable using the formatting facility introduced in C++20 (`std::format`) and fixes encoding issues in the underlying API ([LWG4156]).
candidate 3 (found by 1 of 48 passes): fixes encoding issues in the underlying API ([LWG4156]).
candidate 4 (found by 1 of 48 passes): the existing inserter has several issues, such as I/O manipulators applying only to the category name rather than the entire error code, resulting in confusing output

## audience - grade 0.33 (fired in 1 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
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
  [11] 10. Proposal                                 0/0/2  -> 0.67
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.

## prior_art - grade 2.00 (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
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
  [10] 9. Motivation                                1/1/0  -> 0.67
  [11] 10. Proposal                                 2/2/2  -> 2.00
  [12] 11. Previous work                            2/2/2  -> 2.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           1/1/1  -> 1.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This paper proposes making `std::error_code` formattable using the formatting facility introduced in C++20 (`std::format`) and fixes encoding issues in the underlying API ([LWG4156]).
candidate 2 (found by 3 of 48 passes): An alternative approach could involve communicating the encoding from `error_category`. However, this introduces ABI challenges and complicates usage compared to adopting a single encoding.
candidate 3 (found by 3 of 48 passes): A formatter for `std::error_code` was proposed as part of [P2930] which has more formatting options for the numeric code but doesn’t try to address encoding issues or provide a debug format.
candidate 4 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).

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

## coordination - grade 1.00 (fired in 1 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
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
  [11] 10. Proposal                                 2/2/2  -> 2.00
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding. However, there is significant divergence in message encodings.
candidate 2 (found by 1 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding.

## insufficiency - grade 0.00 (fired in 0 of 16 sections, strong in 0)
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
  [11] 10. Proposal                                 1/0/1  -> 0.67
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           2/2/1  -> 1.67
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).
candidate 2 (found by 2 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.

-->
