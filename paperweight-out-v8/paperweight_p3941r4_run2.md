Verdict: Adequate (4/14)

The paper offers some useful context about prior discussion and alternatives, but it leaves most of the case for standardization unstated. The strongest material concerns why the design question matters and what has been tried before, while the argument for putting this in the standard is essentially absent.

- The paper establishes that the issue has real design significance by pointing to concerns raised about `affine_on` and the resulting reconsideration of the approach.
- It also shows awareness of prior work and alternatives, including the discontinued P3718R0 and the earlier use of `continues_on`.
- The paper does not establish who is affected by the proposal or what implementation experience supports it.
- Most glaringly, it never explains why this needs to be in the standard rather than in a library, nor how it would coordinate with existing standard facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.00   accumulate 4.00   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 4.00 / 3.50   (all 3 samples: 3.50)
headings: h2 4
on threshold: motivation
splits: motivation[3] 2/2/1  motivation[4] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/1  -> 1.67
  [4] 3 Discussion of Changes                      0/2/2  -> 1.33
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 2 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified:
candidate 3 (found by 1 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified.
candidate 4 (found by 1 of 15 passes): If there were no way to change the scheduler it would still be possible to execute using a different scheduler, although not as direct

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 3 of 15 passes): [P3718R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3718r0.html) is, however, discontinued (for unrelated reasons) and adding the guarantee to get the current scheduler from a receiver query is proposed here.
candidate 3 (found by 3 of 15 passes): The original proposal for `task` used `continues_on` to schedule the work back on the original scheduler.
candidate 4 (found by 3 of 15 passes): [ Editor's note: This wording is relative to [N5032](https://wg21.link/N5032) with the changes from [P3826r3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3826r3.html) applied. ]

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

-->
