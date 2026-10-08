Verdict: Adequate (5/14)

The paper offers meaningful support for the timeliness and practical motivation of its proposed extensions, particularly around virtual functions and large-scale use, but much of that support remains asserted rather than demonstrated. The thinnest areas are the absence of a case for why standardization is the right vehicle, why a library solution cannot suffice, and any real implementation experience beyond a single compiler.

- The strongest support is for why the work matters now, with the paper clearly situating the proposed extensions as necessary follow-ons to the C++26 contracts foundation.
- The paper claims broad affected audiences and prior design analysis, but does not substantiate those claims with evidence or detail.
- The paper asserts coordination and interoperability needs around virtual functions, yet does not establish how standardization would resolve them in practice.
- The most glaring omission is the lack of any argument for why the standard is needed or why a library-based approach would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 5 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.00   accumulate 5.17   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.17  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 1.33
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.50 / 5.50 / 3.50   (all 3 samples: 4.83)
headings: h2 6
on threshold: none
splits: audience[3] 0/1/0  prior_art[4] 2/2/0  prior_art[5] 1/1/0  coordination[4] 0/1/0
        implementation[4] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 The plan                                   2/2/2  -> 2.00
  [5] 3 Extensions not included in the plan        1/1/1  -> 1.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In order to make the feature more usable at scale and across a wider variety of scenarios, key extensions are needed and are needed soon.
candidate 2 (found by 3 of 21 passes): The feature set included in C++26 provides a solid foundation, but lacks a number of extensions needed to support additional use cases for which there is already a demonstrated need.
candidate 3 (found by 3 of 21 passes): Yet, C++26 contract assertions do not integrate with them: placing `pre` or `post` on the declaration of a virtual function results in the program being ill-formed.
candidate 4 (found by 3 of 21 passes): While progress on these extensions should continue during the C++29 cycle, we feel that it is too early to commit to any particular shipping vehicle for them.

## audience - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/1/0  -> 0.33
  [4] 2 The plan                                   0/0/0  -> 0.00
  [5] 3 Extensions not included in the plan        0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): In particular, further work is required to make contract assertions truly usable at scale: in very large codebases, across libraries developed and distributed independently, and in specialised environments such as safety-critical systems.

## prior_art - grade 1.17 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 The plan                                   2/2/0  -> 1.33
  [5] 3 Extensions not included in the plan        1/1/0  -> 0.67
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This milestone is the result of a sustained effort by the authors of [[P2900R14](https://wg21.link/p2900r14)] and the WG21 subgroups responsible for evaluating the proposal: SG21, EWG, and CWG.
candidate 2 (found by 2 of 21 passes): In [[P3600R0](https://wg21.link/p3600r0)] we have conducted the most comprehensive analysis to date of the use cases, available design space, and trade-offs among the many possible designs for contract assertions on virtual functions.
candidate 3 (found by 1 of 21 passes): This success was made possible in part by the existence of a clear roadmap [[P2695R1](https://wg21.link/p2695r1)] for the C++26 cycle.
candidate 4 (found by 1 of 21 passes): A number of other possible extensions to C++26 contract assertions have either significant unresolved design issues, relatively lower impact than those included in the plan, or both.

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
