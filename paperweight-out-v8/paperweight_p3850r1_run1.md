Verdict: Adequate (4/14)

The paper offers meaningful support in the areas of motivation and prior art, but its case is uneven: several essential justifications are asserted rather than demonstrated, and some are absent entirely. The thinnest parts concern the people affected, the need for a standard rather than another mechanism, and evidence from implementation.

- The strongest support is the paper’s clear explanation of why the feature matters, including the demonstrated need for extensions and the current ill-formedness of contract assertions on virtual functions.
- The prior-art and alternatives discussion is also well supported, anchored in a comprehensive analysis and a documented roadmap through relevant study groups.
- The weakest established support is the absence of any account of who is affected, which leaves the scope and urgency of the problem under-specified.
- The most glaring omissions are the failure to establish why standardization is the right vehicle, why a library solution will not suffice, and the lack of substantiated implementation experience beyond a bare claim.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 4 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 3.33   accumulate 4.83   max 5.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 4.00 / 5.00 / 4.00   (all 3 samples: 4.33)
headings: h2 6
on threshold: motivation, prior_art
splits: motivation[3] 1/2/1  motivation[5] 1/0/0  prior_art[5] 0/1/0  coordination[4] 0/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/2/1  -> 1.33
  [4] 2 The plan                                   2/2/2  -> 2.00
  [5] 3 Extensions not included in the plan        1/0/0  -> 0.33
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In order to make the feature more usable at scale and across a wider variety of scenarios, key extensions are needed and are needed soon.
candidate 2 (found by 3 of 21 passes): The feature set included in C++26 provides a solid foundation, but lacks a number of extensions needed to support additional use cases for which there is already a demonstrated need.
candidate 3 (found by 3 of 21 passes): Yet, C++26 contract assertions do not integrate with them: placing `pre` or `post` on the declaration of a virtual function results in the program being ill-formed.
candidate 4 (found by 1 of 21 passes): While progress on these extensions should continue during the C++29 cycle, we feel that it is too early to commit to any particular shipping vehicle for them.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 The plan                                   2/2/2  -> 2.00
  [5] 3 Extensions not included in the plan        0/1/0  -> 0.33
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In [[P3600R0](https://wg21.link/p3600r0)] we have conducted the most comprehensive analysis to date of the use cases, available design space, and trade-offs among the many possible designs for contract assertions on virtual functions.
candidate 2 (found by 2 of 21 passes): This milestone is the result of a sustained effort by the authors of [[P2900R14](https://wg21.link/p2900r14)] and the WG21 subgroups responsible for evaluating the proposal: SG21, EWG, and CWG.
candidate 3 (found by 1 of 21 passes): This success was made possible in part by the existence of a clear roadmap [[P2695R1](https://wg21.link/p2695r1)] for the C++26 cycle.
candidate 4 (found by 1 of 21 passes): These extensions include: * `pre` and `post` on function pointers ([[P3271R1](https://wg21.link/p3271r1)], [[P3327R0](https://wg21.link/p3327r0)])

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 The plan                                   0/1/0  -> 0.33
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Many libraries and APIs are designed around virtual functions. Yet, C++26 contract assertions do not integrate with them: placing `pre` or `post` on the declaration of a virtual function results in the program being ill-formed.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 The plan                                   1/1/1  -> 1.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): all but two have already been implemented (criterion F)

-->
