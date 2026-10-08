Verdict: Weak (1/14)

The paper offers only a narrow, illustrative motivation for the problem it wants to solve, and it leaves nearly the entire case for standardization unaddressed. The thinnest areas are the absence of any audience analysis, prior art, alternative approaches, or evidence that a library solution would be insufficient.

- The strongest support is a single example showing how an exception can leave nested tasks running after a scope and its data have been destroyed.
- The paper does not identify who is affected by the problem or how widely it occurs in practice.
- The paper provides no comparison with existing mechanisms or alternative designs that might address the same lifetime hazard.
- The most glaring omission is the lack of any implementation experience or interoperability discussion to show that the proposed facility is ready for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.00/14)

Provisionally addressed: 1 of 7. Provisional points: 1.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 0.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 42 of 42 section-criterion pairs unanimous (100%)
single-sample totals would have been: 1.00 / 1.00 / 1.00   (all 3 samples: 1.00)
headings: h3 5   <- NOT h2, check the unit list
on threshold: motivation
splits: none
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    2/2/2  -> 2.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Here, if `maybe_throw` throws an exception, then the scope is not joined, and the nested tasks can continue executing asynchronously, potentially accessing both the `scope` and `scoped_data` objects out of lifetime.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

-->
