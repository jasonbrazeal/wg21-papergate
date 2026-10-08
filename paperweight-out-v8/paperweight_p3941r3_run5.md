Verdict: Adequate (4/14)

The paper offers some support for its standardization case by explaining the motivation and showing that the change responds to prior discussion and supersedes an earlier approach, but it leaves most of the burden of justification unaddressed. The thinnest areas are the absence of any account of who is affected, why the standard is the right venue, or how the feature would work with existing practice.

- The strongest support is the explanation of why the change matters, tied to concerns raised about `affine_on` and the earlier `continues_on` approach.
- The paper also establishes some prior art and alternatives by referencing P3796R1, the discontinued P3718R0, and the original `task` scheduling strategy.
- The most glaring omission is the lack of any implementation experience or evidence that the proposed guarantee is workable in practice.
- Equally unestablished are the arguments for why this belongs in the standard rather than a library, and how it coordinates with existing schedulers and receiver queries.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 2 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 4.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 4.00 / 4.00   (all 3 samples: 3.83)
headings: h2 4
on threshold: none
splits: motivation[3] 1/2/2  prior_art[5] 0/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/2/2  -> 1.67
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

## prior_art - grade 2.00 (fired in 4 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            0/0/1  -> 0.33
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 3 of 15 passes): [P3718R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3718r0.html) is, however, discontinued (for unrelated reasons) and adding the guarantee to get the current scheduler from a receiver query is proposed here.
candidate 3 (found by 3 of 15 passes): The original proposal for `task` used `continues_on` to schedule the work back on the original scheduler.
candidate 4 (found by 1 of 15 passes): [ Editor's note: This wording is relative to [N5032](https://wg21.link/N5032) with the changes from [P3826r3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3826r3.html) applied. ]

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
