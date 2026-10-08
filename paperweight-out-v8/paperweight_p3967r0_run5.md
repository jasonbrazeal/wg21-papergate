Verdict: Adequate (6/14)

The paper offers a narrow but real basis for its standardization, chiefly by showing that the feature would address a genuine problem and that it can be designed to interoperate with existing code. Beyond that, the support is thin: several important claims are asserted rather than demonstrated, and the paper gives no evidence about the affected audience or any implementation experience.

- The strongest support is for why the proposal matters, since the paper identifies a concrete conflict between performance-critical and safety-critical code under the current TU-level contract semantics.
- The paper also establishes coordination and interoperability, particularly through the alternate-name mechanism for calling functions compiled with older compilers and the single-library approach to hardened and unhardened standard libraries.
- The case for prior art and alternatives is only claimed, because the discussion of related proposals and effective evaluation semantics is not backed by enough detail to show how this approach compares.
- The most glaring omission is implementation experience, as the paper provides no evidence that the proposed mechanism has been tried in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 5 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.33   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.67  coordination 2.00  insufficiency 0.17  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 5.50 / 6.50 / 5.00   (all 3 samples: 5.50)
headings: h2 4
on threshold: motivation
splits: prior_art[4] 2/2/0  vehicle[2] 1/2/1  insufficiency[2] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal solves a number of problems related to contracts by generating code both with and without checked contract-assertions with one compilation command.
candidate 2 (found by 3 of 15 passes): With the TU-level evaluation semantic of C++26 contracts based on compiler switches performance critical code can’t reside in the same TU as safety critical code.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/0/0  -> 0.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 3 of 5 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 1/1/1  -> 1.00
  [3] 3 Proposal                                   1/1/1  -> 1.00
  [4] 4 Discussions                                2/2/0  -> 1.33
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): With this proposal calls to inline and template functions that are not inlined always call the checked or unchecked compile depending on whether the calling code is checked or unchecked
candidate 2 (found by 3 of 15 passes): including using in flight proposals such as [[P3400R2](https://wg21.link/p3400r2)] or [P3968R0].
candidate 3 (found by 2 of 15 passes): With [[P3400R2](https://wg21.link/p3400r2)] it becomes possible to individually control the evaluation semantic of each contract-assertion, creating an *effective* *evaluation* *semantic* that may differ from the *initial* *evaluation* *semantic* from the build system.

## vehicle - grade 0.67 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 1/2/1  -> 1.33
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.

## coordination - grade 2.00 (fired in 2 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                2/2/2  -> 2.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): To make sure that both checked and unchecked compiles can call functions compiled with an older C++ compiler an *alternate* *name* for the function to call using the traditionally mangled name for the function is added to each call site.
candidate 2 (found by 2 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.
candidate 3 (found by 1 of 15 passes): This includes the specific problem of linking to a hardened or unhardened standard library as there is only one.

## insufficiency - grade 0.17 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/1/0  -> 0.33
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/0/0  -> 0.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
