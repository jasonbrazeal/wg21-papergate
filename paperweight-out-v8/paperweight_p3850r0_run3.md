Verdict: Adequate (6/14)

The paper offers solid support in a few important areas, particularly in showing prior art, a clear design path, and implementation experience, but it leaves several foundational questions about the need for standardization largely unaddressed. The thinnest parts concern who is actually affected by the missing feature and why the standard, rather than a library or existing mechanism, is the right place to solve the problem.

- The strongest support comes from the working implementation in GCC and the existence of complete wording, which shows the design is mature enough to evaluate seriously.
- The paper also establishes prior art and alternatives through its references to a roadmap, a comprehensive design analysis, and related proposals for function pointers.
- The most glaring omission is the absence of any established description of who is affected by the current lack of virtual function contract assertions.
- The paper likewise does not establish why this needs to be in the standard rather than addressed through a library or other non-standard means.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 35 of 35 section-criterion pairs unanimous (100%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 4
on threshold: prior_art, implementation
splits: none
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] 2 The plan                                   2/2/2  -> 2.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The feature set included in C++26 provides a solid foundation, but lacks a number of extensions needed to support additional use cases for which there is already a demonstrated need.
candidate 2 (found by 2 of 15 passes): C++26 contract assertions do not integrate with them: placing pre or post on the declaration of a virtual function results in the program being ill-formed.
candidate 3 (found by 1 of 15 passes): Yet, C++26 contract assertions do not integrate with them: placing pre or post on the declaration of a virtual function results in the program being ill-formed.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 The plan                                   2/2/2  -> 2.00
  [3] 3 Extensions not included in the plan        1/1/1  -> 1.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): This success was made possible in part by the existence of a clear roadmap [[P2695R1](https://wg21.link/p2695r1)] for the C++26 cycle.
candidate 2 (found by 2 of 15 passes): In [P3600R0] we have conducted the most comprehensive analysis to date of the use cases, available design space, and trade-offs among the many possible designs for contract assertions on virtual functions.
candidate 3 (found by 2 of 15 passes): These extensions include: * `pre` and `post` on function pointers ([[P3271R1](https://wg21.link/p3271r1)], [[P3327R0](https://wg21.link/p3327r0)])
candidate 4 (found by 1 of 15 passes): This milestone is the result of a sustained effort by the authors of [[P2900R14](https://wg21.link/p2900r14)] and the WG21 subgroups responsible for evaluating the proposal: SG21, EWG, and CWG.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): further work is required to make contract assertions truly usable at scale: in very large codebases, across libraries developed and distributed independently, and in specialised environments such as safety-critical systems.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   2/2/2  -> 2.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): In [P3097R2], we have a mature and scalable design for adding this functionality. It is easy to understand and teach, has complete wording, and has a working implementation in GCC.
candidate 2 (found by 1 of 15 passes): It is easy to understand and teach, has complete wording, and has a working implementation in GCC.

-->
