Verdict: Weak (3/14)

The paper offers only a narrow foundation for its own standardization, establishing that the lack of agreed documentation about profiles is a real problem, but leaving nearly every other necessary justification as an unsupported claim or entirely unaddressed. The thinnest areas are the absence of any discussion of coordination, library alternatives, or implementation experience, which leaves the standardization case largely undeveloped.

- The paper does establish that the absence of shared, agreed-on documentation about profiles creates confusion and blocks meaningful contributions.
- The paper claims, but does not demonstrate, that the committee’s polling shows strong support for profiles as the intended safety direction.
- The paper gestures at prior profile-related proposals but does not show how they constitute prior art or alternatives that this work builds upon or supersedes.
- The paper offers no account of coordination and interoperability, why a library solution would be insufficient, or any implementation experience to ground the proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.67   accumulate 2.83   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.00 / 3.00 / 2.50   (all 3 samples: 2.83)
headings: h2 4
on threshold: motivation
splits: audience[3] 0/1/0  vehicle[3] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Motivation                                 2/2/2  -> 2.00
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper proposes a tentative plan for making progress on safety and profiles in C++.
candidate 2 (found by 2 of 15 passes): However, there is insufficient agreed-on documentation available to WG21 to be able to say specifically what profiles can and cannot do, leading to confusion and inability of individuals and groups to make meaningful contributions to profiles.
candidate 3 (found by 1 of 15 passes): This is a bad thing, as we know that C++ has been pushed since at least 2021 to become a more memory safe language, typically being lopped in with C.

## audience - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Motivation                                 0/1/0  -> 0.33
  [4] 3 The plan                                   0/0/0  -> 0.00
  [5] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): In many polls the committee has indicated a strong desire to make C++ a safer language, and that the design intent of profiles are a great way to do it.

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
  [3] 2 Motivation                                 1/0/0  -> 0.33
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
