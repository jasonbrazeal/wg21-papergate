Verdict: Adequate to Strong (7/14)

The paper gives solid support for the formatting problem it targets, including prior implementation experience and a clear account of existing API defects, but it leaves several parts of the standardization case largely unargued, particularly around affected users and why a library solution would be insufficient. The strongest material concerns what is broken and what has already been tried; the thinnest concerns the actual need for a standard-language facility rather than a portable library.

- The paper clearly establishes why the current behavior matters by tying the proposal to concrete encoding defects and confusing inserter output.
- It offers credible prior art and alternatives, including LWG4156, P2930, and an existing {fmt} implementation.
- The discussion of why this belongs in the standard rests mainly on an asserted preference for the C locale encoding rather than a demonstrated need for standardization.
- The paper does not establish who is affected or why a library cannot adequately provide the proposed formatting support.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 6.67   accumulate 7.33   max 8.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 109 of 112 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 15
on threshold: motivation, coordination, implementation
splits: motivation[10] 2/2/0  vehicle[11] 1/0/1  implementation[11] 0/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)
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
  [10] 9. Motivation                                2/2/0  -> 1.33
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
  [10] 9. Motivation                                1/1/1  -> 1.00
  [11] 10. Proposal                                 2/2/2  -> 2.00
  [12] 11. Previous work                            2/2/2  -> 2.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           1/1/1  -> 1.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): fixes encoding issues in the underlying API ([LWG4156])
candidate 2 (found by 3 of 48 passes): An alternative approach could involve communicating the encoding from `error_category`. However, this introduces ABI challenges and complicates usage compared to adopting a single encoding.
candidate 3 (found by 3 of 48 passes): A formatter for `std::error_code` was proposed as part of [P2930] which has more formatting options for the numeric code but doesn’t try to address encoding issues or provide a debug format.
candidate 4 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).

## vehicle - grade 0.33 (fired in 1 of 16 sections, strong in 0)
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
  [11] 10. Proposal                                 1/0/1  -> 0.67
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           0/0/0  -> 0.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): To address this, the proposal suggests using the C locale encoding (execution character set), which is already employed in most cases and aligns with underlying system APIs.

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
candidate 1 (found by 1 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding.
candidate 2 (found by 1 of 48 passes): In practice, implementations typically define category names as string literals, meaning they are in the ordinary literal encoding. However, there is significant divergence in message encodings.
candidate 3 (found by 1 of 48 passes): libstdc++ uses the Active Code Page (ACP) while libc++ again uses `strerror` / C locale on Windows.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
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
  [11] 10. Proposal                                 0/1/1  -> 0.67
  [12] 11. Previous work                            0/0/0  -> 0.00
  [13] 12. Wording                                  0/0/0  -> 0.00
  [14] 13. Implementation                           2/2/2  -> 2.00
  [15] 14. Acknowledgements                         0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The proposed `formatter` for `std::error_code` has been implemented in the open-source {fmt} library ([FMT]).
candidate 2 (found by 2 of 48 passes): This functionality is not currently provided by {fmt}, and over several years of usage, there have been no requests to add it.

-->
