Verdict: Adequate (4/14)

The paper gives a reasonably clear account of its motivation and its relationship to earlier hardening work, but it leaves several parts of the standardization case almost entirely unargued. The strongest material concerns continuity with prior proposals and the identification of checks that fall outside the earlier criteria, while the discussion of affected users, the need for a standard rather than a library solution, and implementation experience is thin or absent.

- The paper establishes why the proposed checks matter by tying them to the existing hardening paradigm and reporting sanitizer-verified out-of-bounds behavior in major implementations.
- It also establishes prior art and alternatives by positioning itself as a followup to P3471 and P3697 and explaining how it relaxes some of the original selection criteria.
- The paper claims implementation experience through sanitizer verification, but does not establish broader implementation experience with the proposed hardened preconditions.
- It does not establish who is affected, why the standard is the right venue, how the feature coordinates with other specifications, or why a library-only solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 3 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 3.00   accumulate 4.50   max 5.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 42 of 42 section-criterion pairs unanimous (100%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 5
on threshold: motivation, prior_art
splits: none
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              1/1/1  -> 1.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): This paper aims to work towards the goal of making sure the Library is exhaustively covered within the existing hardening paradigm.
candidate 2 (found by 3 of 18 passes): All of these checks were verified when violated to cause an OOB read or write (using Address Sanitizer) in at least one of the major implementations
candidate 3 (found by 2 of 18 passes): This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria (e.g., some of the functions being hardened are not very widely used).
candidate 4 (found by 1 of 18 passes): This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/0/0  -> 0.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              2/2/2  -> 2.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697)
candidate 2 (found by 1 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697) that proposes adding several hardened preconditions across the Library.
candidate 3 (found by 1 of 18 passes): The original hardening paper, [P3471](https://wg21.link/P3471), focused on the checks that satisfied a few criteria: ... This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria
candidate 4 (found by 1 of 18 passes): The original hardening paper, [P3471](https://wg21.link/P3471), focused on the checks that satisfied a few criteria... This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/0/0  -> 0.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/0/0  -> 0.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/0/0  -> 0.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/0/0  -> 0.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): All of these checks were verified when violated to cause an OOB read or write (using Address Sanitizer) in at least one of the major implementations

-->
