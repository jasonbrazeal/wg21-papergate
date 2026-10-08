Verdict: Adequate (4/14)

The paper offers a narrow but concrete basis for its standardization case: it clearly explains why the identified checks matter within the existing hardening framework and points to prior work and some implementation verification. The support is thinnest around the standard-specific justifications, with no established case for why this belongs in the standard, who is affected, how it coordinates with existing practice, or why a library solution would not suffice.

- The strongest support is the established motivation, which ties the proposed checks to the existing hardening paradigm and confirms they can cause out-of-bounds reads or writes in major implementations.
- The paper also gestures toward prior art by linking itself to earlier hardening proposals, though that connection is only claimed rather than fully established.
- The most glaring omission is the absence of any established argument for why the standard is the right venue, leaving the core standardization rationale unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 3 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 3.00   accumulate 4.50   max 4.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 4.00 / 4.00 / 3.50   (all 3 samples: 3.83)
headings: h2 5
on threshold: motivation
splits: motivation[4] 2/1/1  prior_art[4] 1/2/1  prior_art[6] 0/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              2/1/1  -> 1.33
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): This paper aims to work towards the goal of making sure the Library is exhaustively covered within the existing hardening paradigm.
candidate 2 (found by 3 of 18 passes): This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria
candidate 3 (found by 3 of 18 passes): All of these checks were verified when violated to cause an OOB read or write (using Address Sanitizer) in at least one of the major implementations

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

## prior_art - grade 1.17 (fired in 3 of 6 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              1/2/1  -> 1.33
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/1/1  -> 0.67
candidate 1 (found by 3 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697)
candidate 2 (found by 2 of 18 passes): The original hardening paper, [P3471](https://wg21.link/P3471), focused on the checks that satisfied a few criteria
candidate 3 (found by 2 of 18 passes): As the name implies, these would attempt to add an element even if the underlying buffer has no capacity, resulting in an OOB write.
candidate 4 (found by 1 of 18 passes): The original hardening paper, [P3471](https://wg21.link/P3471), focused on the checks that satisfied a few criteria: ... This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria.

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
