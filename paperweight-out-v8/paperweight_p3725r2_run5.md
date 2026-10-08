Verdict: Weak to Adequate (3/14)

The paper offers a clear motivation for why the current filter view is unsafe and why a workaround would help ordinary programmers, but it does not build much of a case beyond that. The support is thinnest around the questions that matter most for standardization: who is affected, why the standard is the right place for this, and whether the design has been tested in practice.

- The strongest part of the paper is its explanation that basic filter use cases are broken or risky and that a safer, self-explanatory workaround is needed.
- The discussion of prior art and alternatives gestures toward related proposals and possible names, but it does not establish that the proposed approach is the right one.
- The paper does not establish who is affected by the problem, which leaves the scope and urgency of the need unclear.
- Most glaringly, it offers no evidence on implementation experience, why a library solution would not suffice, or why the standard should adopt this particular design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 3.00   accumulate 3.33   max 3.33

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.50 / 2.50 / 3.00   (all 3 samples: 3.00)
headings: h2 9
on threshold: none
splits: motivation[4] 2/1/2  prior_art[1] 0/0/1  prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 10 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   2/2/2  -> 2.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          2/1/2  -> 1.67
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Several basic use cases of the current filter view are broken or risky.
candidate 2 (found by 3 of 30 passes): Using filter views is both risky and non-intuitive.
candidate 3 (found by 3 of 30 passes): This proposal is what is necessary to give ordinary programmers a workaround top use a safe and self-explanatory filter so that they can simply compose pipelines with filters and it just works for all basic use-cases.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 3 of 10 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] Motivation                                   1/1/1  -> 1.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          2/1/1  -> 1.33
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Note also that as_input is the new name of the to_input view as proposed for C++26 in P3828.
candidate 2 (found by 2 of 30 passes): A new adaptor like safe_filter() or const_filter() might also make sense for different reasons.
candidate 3 (found by 1 of 30 passes): What is proposed here follows the following SG9 vote;
candidate 4 (found by 1 of 30 passes): A new adaptor like safe_filter() or const_filter() might also make sense for different reasons. However, the first step is to have a working workaround because both terminology and constness details might need further discussions.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          0/0/0  -> 0.00
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
