Verdict: Weak (2/14)

The paper offers only a thin, largely conversational case for standardization, resting on a single assertion that a policy would improve on the status quo and on informal recollections of committee discussion. Most of the necessary support—who is affected, why the standard is the right venue, interoperability, why a library cannot suffice, and implementation experience—is simply absent.

- The strongest support is the claim that having a policy is clearly better than having none, though even this is asserted rather than argued.
- The paper gestures at prior art by noting that other policy proposals mark wide-contract non-throwing functions `noexcept`, but it does not establish that this represents a settled or viable alternative.
- The most glaring omission is the complete lack of evidence about who would be affected by the proposed standardization or what implementation experience exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.50/14)

Provisionally addressed: 2 of 7. Provisional points: 1.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.50   corroborated 2.00   accumulate 1.50   max 3.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 42 of 42 section-criterion pairs unanimous (100%)
single-sample totals would have been: 1.50 / 1.50 / 1.50   (all 3 samples: 1.50)
headings: h2 5
on threshold: prior_art
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
candidate 1 (found by 3 of 18 passes): This is clearly better than the status quo of having no policy.

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

## prior_art - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       2/2/2  -> 2.00
  [4] 3 Policy Proposal                            0/0/0  -> 0.00
  [5] 4 Acknowledgements                           0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): In the discussions since then, it seems that all of the policy proposals have marking wide contract (no preconditions) non-throwing functions `noexcept`.
candidate 2 (found by 1 of 18 passes): In Varna, we discovered that the Lakos Rule was never voted on as a policy past C++11.

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
