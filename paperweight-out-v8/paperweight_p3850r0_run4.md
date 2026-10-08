Verdict: Adequate (5/14)

The paper offers some useful groundwork for its standardization case, particularly in showing prior art and a considered design path, but it leaves several essential justifications largely unaddressed. The thinnest areas concern who would actually be affected, why the standard itself is the right vehicle, and why a library solution would not suffice.

- The strongest support comes from the paper’s engagement with prior art and alternatives, including references to related proposals and a mature design with wording and a GCC implementation.
- The paper also establishes why the feature matters by pointing to demonstrated needs and the current ill-formedness of contracts on virtual functions.
- The case for coordination and interoperability is only asserted in general terms, without concrete evidence of how the feature would work across large or independently developed codebases.
- The most glaring omissions are the absence of any identified affected audience, any argument for why standardization rather than a library is necessary, and any meaningful implementation experience beyond a single compiler.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 4 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 3.33   accumulate 5.00   max 5.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 3.50 / 5.00 / 5.00   (all 3 samples: 4.50)
headings: h2 4
on threshold: motivation, prior_art
splits: motivation[2] 0/2/2  motivation[3] 0/0/1  prior_art[1] 1/1/2  coordination[1] 0/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] 2 The plan                                   0/2/2  -> 1.33
  [3] 3 Extensions not included in the plan        0/0/1  -> 0.33
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The feature set included in C++26 provides a solid foundation, but lacks a number of extensions needed to support additional use cases for which there is already a demonstrated need.
candidate 2 (found by 2 of 15 passes): Yet, C++26 contract assertions do not integrate with them: placing pre or post on the declaration of a virtual function results in the program being ill-formed.
candidate 3 (found by 1 of 15 passes): A number of other possible extensions to C++26 contract assertions have either significant unresolved design issues, relatively lower impact than those included in the plan, or both.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/2  -> 1.33
  [2] 2 The plan                                   2/2/2  -> 2.00
  [3] 3 Extensions not included in the plan        1/1/1  -> 1.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): These extensions include: * `pre` and `post` on function pointers ([[P3271R1](https://wg21.link/p3271r1)], [[P3327R0](https://wg21.link/p3327r0)])
candidate 2 (found by 2 of 15 passes): This milestone is the result of a sustained effort by the authors of [[P2900R14](https://wg21.link/p2900r14)] and the WG21 subgroups responsible for evaluating the proposal: SG21, EWG, and CWG.
candidate 3 (found by 2 of 15 passes): In [P3097R2], we have a mature and scalable design for adding this functionality.
candidate 4 (found by 1 of 15 passes): This success was made possible in part by the existence of a clear roadmap [[P2695R1](https://wg21.link/p2695r1)] for the C++26 cycle.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): further work is required to make contract assertions truly usable at scale: in very large codebases, across libraries developed and distributed independently, and in specialised environments such as safety-critical systems.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   0/0/0  -> 0.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 The plan                                   1/1/1  -> 1.00
  [3] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [4] Acknowledgements                             0/0/0  -> 0.00
  [5] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): In [P3097R2], we have a mature and scalable design for adding this functionality. It is easy to understand and teach, has complete wording, and has a working implementation in GCC.

-->
