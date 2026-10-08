Verdict: Adequate (4/14)

The paper offers some grounding for its motivation and alternatives, but it leaves most of the case for standardization unargued, particularly around who is affected, why a library solution is insufficient, and how the feature would coordinate with existing practice. The strongest material concerns prior discussion and prior art, while the thinnest areas are the absence of any demonstrated need for a standard rather than a library facility.

- The paper establishes that the design question has real history, citing prior concerns about `affine_on` and the earlier `continues_on` approach.
- It also establishes that alternatives have been considered, including a discontinued related proposal and existing library practice.
- It does not establish who would be affected by the proposed change or what problem they currently face.
- Most glaringly, it never explains why this belongs in the C++ standard rather than remaining a library-level facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 3 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 3.67   accumulate 4.67   max 4.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 5.00 / 4.50 / 4.00   (all 3 samples: 4.17)
headings: h2 4
on threshold: motivation
splits: motivation[1] 1/1/2  motivation[3] 2/2/1  motivation[4] 2/0/2  implementation[4] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/2  -> 1.33
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/1  -> 1.67
  [4] 3 Discussion of Changes                      2/0/2  -> 1.33
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 2 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified:
candidate 3 (found by 1 of 15 passes): One important design of `std::execution::task` is that a coroutine resumes after a `co_await` on the same scheduler as the one it was executing on prior to the `co_await`.
candidate 4 (found by 1 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 3 of 15 passes): [P3718R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3718r0.html) is, however, discontinued (for unrelated reasons) and adding the guarantee to get the current scheduler from a receiver query is proposed here.
candidate 3 (found by 3 of 15 passes): The original proposal for `task` used `continues_on` to schedule the work back on the original scheduler.

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

## implementation - grade 0.67  [binary: max] (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      1/1/0  -> 0.67
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): This functionality was originally included because it is present for, at least, one of the existing libraries, although in a form which was recommended against.

-->
