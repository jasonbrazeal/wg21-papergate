Verdict: Adequate to Strong (6/14)

The paper gives a reasonably clear account of the formatting and encoding problems it wants to solve, and it points to concrete prior work and alternatives, but it does not make a persuasive case that this needs to be in the standard rather than in a library. The thinnest support is around implementation demand and the absence of a viable non-standard solution.

- The strongest part of the paper is its explanation of why current `error_code` output is unreliable and why a formatter would address real encoding and formatting defects.
- The discussion of prior art and alternatives is adequate, particularly in distinguishing this proposal from P2930 and in acknowledging the ABI complications of encoding negotiation.
- The paper only asserts, rather than demonstrates, that users are affected or that standardization is necessary, since it cites no requests for the functionality in {fmt}.
- The paper does not establish why a library cannot provide this, which is a notable omission given that the proposed formatter has apparently already been implemented in {fmt}.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 6 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.33   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.67  vehicle 0.17  coordination 0.67  insufficiency 0.00  implementation 1.33
sample agreement: 105 of 112 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.00 / 7.50 / 5.50   (all 3 samples: 6.00)
headings: h2 15
on threshold: prior_art
splits: audience[11] 1/0/0  prior_art[10] 1/0/0  prior_art[12] 1/2/1  prior_art[14] 1/0/0
        vehicle[11] 0/1/0  coordination[11] 0/2/2  implementation[14] 1/2/1
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
candidate 2 (found by 2 of 48 passes): fixes encoding issues in the underlying API ([LWG4156]).
candidate 3 (found by 2 of 48 passes): the existing inserter has several issues, such as I/O manipulators applying only to the category name rather than the entire error code, resulting in confusing output
candidate 4 (found by 1 of 48 passes): This paper proposes making `std::error_code` formattable using the formatting facility introduced in C++20 (`std::format`) and fixes encoding issues in the underlying API ([LWG4156]).

## audience - grade 0.17 (fired in 1 of 16 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 1 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.

## prior_art - grade 1.67 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
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
  [10] 9. Motivation                                1/0/0  -> 0.33
  [11] 10. Proposal                                 2/2/2  -> 2.00
  [12] 11. Previous work                            1/2/1  -> 1.33
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           1/0/0  -> 0.33
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): An alternative approach could involve communicating the encoding from `error_category`. However, this introduces ABI challenges and complicates usage compared to adopting a single encoding.
candidate 2 (found by 3 of 48 passes): A formatter for `std::error_code` was proposed as part of [P2930] which has more formatting options for the numeric code but doesn’t try to address encoding issues or provide a debug format.
candidate 3 (found by 2 of 48 passes): This paper proposes making `std::error_code` formattable using the formatting facility introduced in C++20 (`std::format`) and fixes encoding issues in the underlying API ([LWG4156]).
candidate 4 (found by 1 of 48 passes): fixes encoding issues in the underlying API ([LWG4156]).

## vehicle - grade 0.17 (fired in 1 of 16 sections, strong in 0)  (SHARED PASSAGE)
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
  [11] 10. Proposal                                 0/1/0  -> 0.33
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.

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
  [11] 10. Proposal                                 0/2/2  -> 1.33
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding.
candidate 2 (found by 1 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding. However, there is significant divergence in message encodings.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
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
  [11] 10. Proposal                                 1/1/1  -> 1.00
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           1/2/1  -> 1.33
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.
candidate 2 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).

-->
