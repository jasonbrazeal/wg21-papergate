Verdict: Weak (3/14)

The paper offers a clear motivation for fixing the current filter view’s usability problems, but it provides almost no evidence for the broader case that this particular facility belongs in the standard. The strongest support is concentrated in the opening rationale, while the rest of the standardization case—affected users, prior art, need for language or library support, interoperability, and implementation experience—is largely absent.

- The paper establishes that existing filter views are risky and non-intuitive for ordinary programmers, and that a safe workaround is needed.
- The discussion of prior art gestures toward related proposals and possible alternative adaptors, but does not establish how this proposal compares to or improves upon them.
- The paper does not identify who is affected by the problem or provide evidence of real-world impact.
- It never explains why a standard library facility is required, why a non-standard library would not suffice, or how the proposal coordinates with existing standard components.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.00   accumulate 3.67   max 3.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 3.00 / 2.50 / 2.50   (all 3 samples: 2.67)
headings: h2 9
on threshold: motivation
splits: prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   2/2/2  -> 2.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          1/1/1  -> 1.00
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
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] Proposed Changes                             0/0/0  -> 0.00
  [4] FAQ                                          2/1/1  -> 1.33
  [5] Proposed Wording                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Rev2:                                        0/0/0  -> 0.00
  [8] Rev1:                                        0/0/0  -> 0.00
  [9] Rev0:                                        0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): What is proposed here follows the following SG9 vote;
candidate 2 (found by 3 of 30 passes): Note also that as_input is the new name of the to_input view as proposed for C++26 in P3828.
candidate 3 (found by 2 of 30 passes): A new adaptor like safe_filter() or const_filter() might also make sense for different reasons.
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
