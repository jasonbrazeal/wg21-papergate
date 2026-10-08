Verdict: Weak (1/14)

The paper offers only a thin case for its own standardization, resting almost entirely on a single motivating example and a brief reference to committee discussion. Most of the necessary groundwork—audience, alternatives, interaction with the standard, library feasibility, and implementation experience—is simply absent, leaving the proposal’s standardization rationale largely unexamined.

- The strongest support is the concrete failure scenario involving `maybe_throw`, which at least gestures at a lifetime and correctness problem worth solving.
- The paper claims a connection to prior LEWG concerns about joining a `counting_scope`, but does not develop that history or show how this proposal answers it.
- The most glaring omission is the complete lack of evidence about who is affected, how the feature would interact with existing standard facilities, or whether a library-only approach has been ruled out.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.33/14)

Provisionally addressed: 2 of 7. Provisional points: 1.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.33   corroborated 1.67   accumulate 1.33   max 2.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 0.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 1.50 / 1.50 / 1.00   (all 3 samples: 1.33)
headings: h3 5   <- NOT h2, check the unit list
on threshold: motivation
splits: prior_art[2] 1/1/0
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

## prior_art - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Background and motivation                    1/1/0  -> 0.67
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Wording                                      0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This is intended to address concerns raised in LEWG about ensuring that a `counting_scope` is joined

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
