Verdict: Weak (3/14)

The paper offers only a thin, mostly asserted case for its own standardization, with most of the necessary justification left implicit or framed as a response to an NB comment rather than developed independently. The strongest material concerns the motivation and the proposed return-type change, but even those points are stated as conclusions rather than demonstrated through affected users, alternatives, or implementation experience.

- The paper’s clearest support is its explanation that returning `void*` is intended to address the NB comment about unsafe direct access.
- The discussion of prior art gestures toward P2738R1 and C++26 constant evaluation, but does not establish how that context justifies this change.
- The paper does not identify who is affected, what coordination or interoperability concerns exist, or what implementation experience informs the proposal.
- The most glaring omission is the absence of any established case for why a library solution would be insufficient, beyond a passing remark about a “slightly more complicated return type.”


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 3.00   accumulate 2.50   max 5.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.17  coordination 0.00  insufficiency 0.33  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 2.50 / 2.50 / 2.50   (all 3 samples: 2.50)
headings: h2 6
on threshold: motivation, prior_art
splits: vehicle[4] 1/0/0  insufficiency[4] 0/1/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): However, it is generally unsafe to access the object at `address` directly, and so, the NB comment argues that `address` is maybe too convenient.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): cast from `void*` to `T*` are now supported in constant evaluation. This feature was added by [P2738R1](https://wg21.link/P2738R1) [2] in C++26.

## vehicle - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   1/0/0  -> 0.33
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Therefore, we think using `void*` as the return type of `address` addresses the NB comment in a satisfactory manner.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/1/1  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): The only downsize of using `void*` is then a slightly more complicated return type.

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
