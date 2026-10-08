Verdict: Adequate (5/14)

The paper offers meaningful support in a few areas, particularly in showing that the feature matters and that prior design work exists, but it leaves the core standardization rationale largely unaddressed. The thinnest parts are exactly those that would justify taking this work through the committee rather than pursuing it elsewhere: why the standard is the right vehicle, how it coordinates with existing features, and why a library solution is insufficient.

- The strongest support is the established need for virtual function contract assertions, backed by references to prior analyses and a mature design.
- The paper also credibly points to existing implementation experience, though it does not substantiate the claim in enough detail to count as established.
- The most glaring omission is the absence of any established argument for why this belongs in the standard rather than in a library or separate specification.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 4 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.33   accumulate 5.17   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 4.50 / 4.50   (all 3 samples: 4.67)
headings: h2 6
on threshold: prior_art
splits: motivation[5] 0/0/1  audience[3] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 The plan                                   2/2/2  -> 2.00
  [5] 3 Extensions not included in the plan        0/0/1  -> 0.33
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In order to make the feature more usable at scale and across a wider variety of scenarios, key extensions are needed and are needed soon.
candidate 2 (found by 3 of 21 passes): The feature set included in C++26 provides a solid foundation, but lacks a number of extensions needed to support additional use cases for which there is already a demonstrated need.
candidate 3 (found by 2 of 21 passes): Yet, C++26 contract assertions do not integrate with them: placing `pre` or `post` on the declaration of a virtual function results in the program being ill-formed.
candidate 4 (found by 1 of 21 passes): C++26 contract assertions do not integrate with them: placing `pre` or `post` on the declaration of a virtual function results in the program being ill-formed.

## audience - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/0/0  -> 0.33
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): In particular, further work is required to make contract assertions truly usable at scale: in very large codebases, across libraries developed and distributed independently, and in specialised environments such as safety-critical systems.

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 The plan                                   2/2/2  -> 2.00
  [5] 3 Extensions not included in the plan        1/1/1  -> 1.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This milestone is the result of a sustained effort by the authors of [[P2900R14](https://wg21.link/p2900r14)] and the WG21 subgroups responsible for evaluating the proposal: SG21, EWG, and CWG.
candidate 2 (found by 2 of 21 passes): In [[P3600R0](https://wg21.link/p3600r0)] we have conducted the most comprehensive analysis to date of the use cases, available design space, and trade-offs among the many possible designs for contract assertions on virtual functions.
candidate 3 (found by 2 of 21 passes): These extensions include: * `pre` and `post` on function pointers ([[P3271R1](https://wg21.link/p3271r1)], [[P3327R0](https://wg21.link/p3327r0)])
candidate 4 (found by 1 of 21 passes): In [[P3097R3](https://wg21.link/p3097r3)], we have a mature and scalable design for adding this functionality.

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

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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
