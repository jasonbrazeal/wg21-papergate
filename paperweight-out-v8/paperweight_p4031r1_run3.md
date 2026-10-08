Verdict: Weak (2/14)

The paper offers only a narrow, largely rhetorical case for its naming concern, and it does not build out the broader justification that a standardization proposal would need. The support is thinnest where the paper should be most concrete: in showing why the standard must act, how the change fits with existing facilities, and what implementation experience suggests.

- The strongest support is the observation that adding a `system_context_replaceability` name would create confusion because `system_context` does not exist in the current working draft.
- The paper gestures at prior discussion and alternatives, but it does not turn those references into a developed comparison or a clear rationale for the proposed direction.
- The paper leaves unestablished the core standardization questions of why the standard is the right venue, how the change coordinates with related work, and why a library solution would not suffice.
- The most glaring omission is the absence of any implementation experience or evidence that would ground the naming choice in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.67   accumulate 2.33   max 4.67

## SUMMARY
grades: motivation 1.00  audience 0.33  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.00 / 2.50   (all 3 samples: 2.33)
headings: h2 7
on threshold: motivation, prior_art
splits: audience[3] 1/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Adding `system_context_replaceability` namespace name to C++26 will cause a lot of confusion because `system_context` does not even exist in the current working draft.

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 1/0/1  -> 0.67
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): The poll below taken in Kona meeting (2025) shows that:

## prior_art - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): [[P3804R1]](https://wg21.link/p3804r1) proposed several options favoring `replacement` and `replacement_functions`.
candidate 2 (found by 1 of 24 passes): [[P3804R1]](https://wg21.link/p3804r1) proposed several options favoring `replacement` and `replacement_functions`. As people pointed out, those names are probably also not great because they don’t give any sense of what developers try to replace.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Proposal                                   0/0/0  -> 0.00
  [5] 3 Outcome                                    0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 Revision History                           0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
