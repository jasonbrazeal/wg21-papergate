Verdict: Adequate (5/14)

The paper offers a reasonably clear motivation for extending contract assertions, but its broader case for standardization rests on assertions that are not backed up with concrete evidence, particularly around affected users, alternatives, and implementation experience. The thinnest parts are the absence of any argument for why this belongs in the standard rather than in a library, and the lack of demonstrated implementation or interoperability support beyond a few passing references.

- The strongest support is the paper’s explanation of why the feature matters, especially the concrete ill-formedness of virtual function contract assertions in C++26.
- The paper gestures toward affected populations and coordination needs, but does not establish who specifically is affected or how the proposed extensions interoperate with existing practice.
- The most glaring omission is the failure to address why a library solution would not suffice, leaving a central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 5 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.33   accumulate 5.17   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 1.00  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 1.33
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 6.00 / 4.00 / 5.00   (all 3 samples: 4.83)
headings: h2 6
on threshold: none
splits: motivation[5] 0/0/1  audience[3] 1/0/1  prior_art[4] 0/0/2  coordination[3] 1/0/0
        implementation[4] 2/1/1
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

## audience - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/0/1  -> 0.67
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): In particular, further work is required to make contract assertions truly usable at scale: in very large codebases, across libraries developed and distributed independently, and in specialised environments such as safety-critical systems.

## prior_art - grade 1.00 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 The plan                                   0/0/2  -> 0.67
  [5] 3 Extensions not included in the plan        1/1/1  -> 1.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): These extensions include: * `pre` and `post` on function pointers ([[P3271R1](https://wg21.link/p3271r1)], [[P3327R0](https://wg21.link/p3327r0)])
candidate 2 (found by 2 of 21 passes): This milestone is the result of a sustained effort by the authors of [[P2900R14](https://wg21.link/p2900r14)] and the WG21 subgroups responsible for evaluating the proposal: SG21, EWG, and CWG.
candidate 3 (found by 1 of 21 passes): This success was made possible in part by the existence of a clear roadmap [[P2695R1](https://wg21.link/p2695r1)] for the C++26 cycle.
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

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/0/0  -> 0.33
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): further work is required to make contract assertions truly usable at scale: in very large codebases, across libraries developed and distributed independently, and in specialised environments such as safety-critical systems.

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 The plan                                   2/1/1  -> 1.33
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): all but two have already been implemented (criterion F)
candidate 2 (found by 1 of 21 passes): It is easy to understand and teach, has complete wording, and has a working implementation in GCC.

-->
