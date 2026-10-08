Verdict: Weak (2/14)

The paper offers only a thin, largely rhetorical case for its own standardization, leaning on general assertions about confusion and the need for progress rather than concrete evidence. The thinnest areas are the complete absence of discussion about who is affected, implementation experience, interoperability, and why a library solution would be insufficient.

- The strongest support is the paper’s recognition that prior profiles-related proposals have failed and that agreed-on documentation is lacking, though even this is asserted rather than demonstrated.
- The claim that profiles are “the best way we know” to achieve safety is presented without comparison to alternatives or explanation of why standardization is the right venue.
- The paper does not identify any affected users, implementers, or constituencies, leaving the practical stakes unexamined.
- Most glaringly, it offers no implementation experience, no coordination or interoperability analysis, and no argument for why a library approach could not address the stated confusion.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 2.33   accumulate 2.50   max 3.33

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 2.00 / 2.50 / 3.00   (all 3 samples: 2.50)
headings: h2 4
on threshold: motivation
splits: motivation[2] 0/1/1  vehicle[3] 0/0/1
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/1  -> 0.67
  [3] 2 Motivation                                 2/2/2  -> 2.00
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): However, there is insufficient agreed-on documentation available to WG21 to be able to say specifically what profiles can and cannot do, leading to confusion and inability of individuals and groups to make meaningful contributions to profiles.
candidate 2 (found by 2 of 15 passes): This paper proposes a tentative plan for making progress on safety and profiles in C++.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 0/0/0  -> 0.00
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 1/1/1  -> 1.00
  [4] 3 The plan                                   1/1/1  -> 1.00
  [5] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Over the past few years we have seen multiple papers pass by that attempt to move profiles forward in some way ([P3081R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3081r2.pdf), [P3589R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3589r2.pdf), [P3700R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3700r0.html), [P3984R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3984r0.pdf)), so far none successful.
candidate 2 (found by 3 of 15 passes): We have had many proposals in the past that have large amounts of what we need - up to the level of wording in some cases.

## vehicle - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 0/0/1  -> 0.33
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): Profiles is the best way we know to do this.

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 0/0/0  -> 0.00
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 0/0/0  -> 0.00
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 0/0/0  -> 0.00
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
