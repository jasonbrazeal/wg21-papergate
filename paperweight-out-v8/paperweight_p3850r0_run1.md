Verdict: Adequate (5/14)

The paper offers meaningful support in a few areas, particularly in showing prior art and a deliberate design path, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest support concerns who is affected, why the standard is the right venue, and why a library solution would not suffice.

- The strongest support is the paper’s account of prior art and alternatives, including its reference to a comprehensive design analysis and a clear roadmap.
- The paper also establishes why the feature matters by pointing to demonstrated needs and the current ill-formedness of contract assertions on virtual functions.
- The most glaring omission is the absence of any established case for who is affected by the problem or would benefit from the proposed change.
- Equally unestablished are the arguments for why this requires a standard rather than a library solution, and what implementation experience actually demonstrates beyond a single compiler claim.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.33   accumulate 5.67   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 1.33
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.00 / 6.00 / 5.00   (all 3 samples: 5.33)
headings: h2 4
on threshold: prior_art
splits: prior_art[3] 1/1/0  implementation[2] 1/2/1
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
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 The plan                                   2/2/2  -> 2.00
  [3] 3 Extensions not included in the plan        1/1/0  -> 0.67
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): This success was made possible in part by the existence of a clear roadmap [[P2695R1](https://wg21.link/p2695r1)] for the C++26 cycle.
candidate 2 (found by 2 of 15 passes): In [P3600R0] we have conducted the most comprehensive analysis to date of the use cases, available design space, and trade-offs among the many possible designs for contract assertions on virtual functions.
candidate 3 (found by 2 of 15 passes): A number of other possible extensions to C++26 contract assertions have either significant unresolved design issues, relatively lower impact than those included in the plan, or both.
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

## implementation - grade 1.33  [binary: max] (fired in 1 of 5 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   1/2/1  -> 1.33
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): It is easy to understand and teach, has complete wording, and has a working implementation in GCC.
candidate 2 (found by 1 of 15 passes): In [P3097R2], we have a mature and scalable design for adding this functionality. It is easy to understand and teach, has complete wording, and has a working implementation in GCC.
candidate 3 (found by 1 of 15 passes): has a working implementation in GCC.

-->
