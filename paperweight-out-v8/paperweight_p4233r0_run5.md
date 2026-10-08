Verdict: Adequate (4/14)

The paper offers a narrow, internally consistent rationale for extending existing hardening coverage, but it leans almost entirely on continuity with prior proposals rather than making a fresh case for why these particular additions belong in the standard. The thinnest areas are the absence of any discussion of why standardization is necessary, how the changes interact with existing implementations or other hardening modes, and why a library-level solution would be insufficient.

- The strongest support is the paper’s positioning as a follow-up to already-adopted hardening work, which gives its motivation some context even if the new checks themselves are only asserted to matter.
- The claim that the identified checks produce out-of-bounds accesses in at least one major implementation offers a concrete, if limited, form of implementation experience.
- The paper does not establish why the standard is the right venue, leaving unaddressed whether these checks could be delivered through vendor libraries or implementation-specific extensions.
- The most glaring omission is the complete lack of coordination and interoperability discussion, particularly how these new preconditions would behave across different hardening levels or alongside existing contracts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.33   accumulate 4.17   max 4.33

## SUMMARY
grades: motivation 1.33  audience 0.17  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 4.00 / 3.50 / 3.50   (all 3 samples: 3.67)
headings: h2 5
on threshold: motivation
splits: motivation[6] 2/1/2  audience[4] 0/1/0  prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              1/1/1  -> 1.00
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             2/1/2  -> 1.67
candidate 1 (found by 3 of 18 passes): This paper aims to work towards the goal of making sure the Library is exhaustively covered within the existing hardening paradigm.
candidate 2 (found by 3 of 18 passes): This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria
candidate 3 (found by 2 of 18 passes): All of these checks were verified when violated to cause an OOB read or write (using Address Sanitizer) in at least one of the major implementations
candidate 4 (found by 1 of 18 passes): As the name implies, these would attempt to add an element even if the underlying buffer has no capacity, resulting in an OOB write.

## audience - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            0/0/0  -> 0.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              0/1/0  -> 0.33
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): some of the functions being hardened are not very widely used

## prior_art - grade 1.17 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction §                            1/1/1  -> 1.00
  [3] 2 Revision history §                        0/0/0  -> 0.00
  [4] 3 Motivation §                              2/1/1  -> 1.33
  [5] 4 A note on scope §                         0/0/0  -> 0.00
  [6] 5 Summary of proposed changes §             0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697)
candidate 2 (found by 2 of 18 passes): The original hardening paper, [P3471](https://wg21.link/P3471), focused on the checks that satisfied a few criteria
candidate 3 (found by 1 of 18 passes): This paper is a small followup to [P3471R4 “Standard Library Hardening”](https://wg21.link/P3471R4) and [P3697R1 “Minor additions to C++26 standard library hardening”](https://wg21.link/P3697) that proposes adding several hardened preconditions across the Library.
candidate 4 (found by 1 of 18 passes): This paper aims to identify checks that “fell between the cracks” and sometimes somewhat relaxes the latter two criteria

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
