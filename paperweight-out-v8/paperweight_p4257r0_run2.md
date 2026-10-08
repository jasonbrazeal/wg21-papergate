Verdict: Weak (1/14)

The paper offers very little support for its own standardization, resting almost entirely on assertions that a policy would be better than none and that prior discussions leaned toward marking wide-contract non-throwing functions `noexcept`. The thinnest areas are the complete absence of discussion about who is affected, why a library solution is insufficient, implementation experience, and the need for a standard rather than guidance.

- The strongest support is the claim that the proposal improves on the status quo of having no policy.
- The paper also gestures toward prior art by asserting that earlier policy proposals favored marking wide-contract non-throwing functions `noexcept`.
- The most glaring omission is the lack of any implementation experience or evidence of how the policy would work in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.00/14)

Provisionally addressed: 2 of 7. Provisional points: 1.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.00   corroborated 2.00   accumulate 1.00   max 2.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 0.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 42 of 42 section-criterion pairs unanimous (100%)
single-sample totals would have been: 1.00 / 1.00 / 1.00   (all 3 samples: 1.00)
headings: h2 5
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       1/1/1  -> 1.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This is clearly better than the status quo of having no policy.
candidate 2 (found by 1 of 18 passes): Since then, there has been no policy regarding `noexcept` in the standard library.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.50 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       1/1/1  -> 1.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In the discussions since then, it seems that all of the policy proposals have marking wide contract (no preconditions) non-throwing functions `noexcept`.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
