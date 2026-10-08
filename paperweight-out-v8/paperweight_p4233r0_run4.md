Verdict: Weak to Adequate (3/14)

The paper offers a narrow but concrete justification for its existence: it positions itself as filling gaps left by prior hardening work and provides some evidence that the proposed checks correspond to real memory-safety violations in major implementations. The support is thinnest where the paper needs to show why this belongs in the standard rather than in implementation-specific hardening or a library-level solution, and it does not establish who is concretely affected beyond a general claim of wide use.

- The strongest support is the verification that each proposed check, when violated, causes an out-of-bounds read or write under Address Sanitizer in at least one major implementation.
- The paper clearly situates itself as a follow-up to earlier standard library hardening proposals and explains the criteria it relaxes to catch checks that previously fell between the cracks.
- The claim that the affected facilities are widely used is asserted but not backed by evidence about actual usage or impact.
- The most glaring omission is the absence of any case for why standardization, rather than implementation or library action, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.00   accumulate 4.00   max 4.33

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h2 5
on threshold: motivation
splits: audience[4] 0/1/0  prior_art[4] 1/2/1  implementation[6] 1/0/1
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
candidate 2 (found by 3 of 18 passes): This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria
candidate 3 (found by 3 of 18 passes): All of these checks were verified when violated to cause an OOB read or write (using Address Sanitizer) in at least one of the major implementations

## audience - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/1/0  -> 0.33
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): Widely used (so that the benefit from hardening is clear)

## prior_art - grade 1.17 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              1/2/1  -> 1.33
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697)
candidate 2 (found by 2 of 18 passes): The original hardening paper, [P3471](https://wg21.link/P3471), focused on the checks that satisfied a few criteria
candidate 3 (found by 1 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697) that proposes adding several hardened preconditions across the Library.
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

## implementation - grade 0.67  [binary: max] (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/0/0  -> 0.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             1/0/1  -> 0.67
candidate 1 (found by 2 of 18 passes): All of these checks were verified when violated to cause an OOB read or write (using Address Sanitizer) in at least one of the major implementations

-->
