Verdict: Weak to Adequate (3/14)

The paper offers only a narrow slice of the case needed for standardization: it can point to prior discussion and an earlier design as evidence that the change responds to real concerns, but it leaves almost every other necessary justification unaddressed. The support is thinnest around the people affected, the need for a standard rather than a library facility, interoperability, and implementation experience.

- The strongest support is the connection to prior concerns about `affine_on` and the earlier use of `continues_on`, which grounds the proposal in existing committee discussion and design history.
- The paper also establishes that alternatives have been considered, at least to the extent of identifying the previous scheduling approach as the thing being replaced.
- The most glaring omission is any account of who is affected by the problem or who would benefit from the change.
- Equally absent is any demonstration that this requires standardization rather than a library solution, or that there is implementation experience to validate the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 34 of 35 section-criterion pairs unanimous (97%)
single-sample totals would have been: 3.00 / 3.00 / 3.50   (all 3 samples: 3.17)
headings: h2 4
on threshold: motivation, prior_art
splits: motivation[3] 1/1/2
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/2  -> 1.33
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 3 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified:
candidate 3 (found by 2 of 15 passes): It isn’t adding any new functionality but removes a problematic way to achieve something which can be better achieved differently.
candidate 4 (found by 1 of 15 passes): The original proposal for `task` used `continues_on` to schedule the work back on the original scheduler.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 3 of 15 passes): The original proposal for `task` used `continues_on` to schedule the work back on the original scheduler.
candidate 3 (found by 3 of 15 passes): [ Editor's note: This wording is relative to [N5032](https://wg21.link/N5032) with the changes from [P3826r3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3826r3.html) applied. ]

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
