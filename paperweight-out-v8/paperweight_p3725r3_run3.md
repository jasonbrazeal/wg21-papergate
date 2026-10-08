Verdict: Weak (3/14)

The paper offers a clear motivation for why the current filter view is unsafe and unintuitive, but it provides little beyond that assertion to justify standardization. The case is thinnest around who is affected, how the feature would coordinate with existing library components, and whether there is any implementation experience.

- The strongest support is the established claim that existing filter views are broken or risky in basic use cases, which gives the proposal a concrete problem to solve.
- The paper gestures at prior art and alternatives, but those references are only claimed and not substantiated enough to show the proposed direction is well grounded.
- The most glaring omission is the absence of any established evidence about who is affected, how the proposal interoperates with the existing standard, or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.33   accumulate 3.67   max 3.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 2.50 / 3.00 / 2.50   (all 3 samples: 2.67)
headings: h2 10
on threshold: motivation
splits: vehicle[4] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   2/2/2  -> 2.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          1/1/1  -> 1.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Several basic use cases of the current filter view are broken or risky or non-intuitive.
candidate 2 (found by 3 of 33 passes): Using filter views is both risky and non-intuitive.
candidate 3 (found by 3 of 33 passes): This proposal is what is necessary to give ordinary programmers a workaround top use a safe and self-explanatory filter so that they can simply compose pipelines with filters and it just works for all basic use-cases.

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          1/1/1  -> 1.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): What is proposed here follows the following SG9 vote;
candidate 2 (found by 3 of 33 passes): Note also that as_input is the new name of the to_input view as proposed for C++26 in P3828.
candidate 3 (found by 3 of 33 passes): A new adaptor like safe_filter() or const_filter() might also make sense for different reasons.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/1/0  -> 0.33
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): This proposal is what is necessary to give ordinary programmers a workaround top use a safe and self-explanatory filter so that they can simply compose pipelines with filters and it just works for all basic use-cases.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev3:                                        0/0/0  -> 0.00
  [8] Rev2:                                        0/0/0  -> 0.00
  [9] Rev1:                                        0/0/0  -> 0.00
  [10] Rev0:                                        0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
