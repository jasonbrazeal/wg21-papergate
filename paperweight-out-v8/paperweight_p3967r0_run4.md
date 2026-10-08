Verdict: Adequate (5/14)

The paper gives a reasonably clear account of the problem it targets and the existing mechanisms it would build on, but it leaves several parts of the standardization case largely unargued, particularly around affected users, implementability, and why a library solution is insufficient.

- The strongest support is the explanation of how the proposal addresses a real limitation of C++26 contracts by allowing checked and unchecked contract-assertions to be generated from one compilation command.
- The discussion of prior art and alternatives is also well grounded, especially in its use of in-flight proposals to show how the approach relates to evolving contract semantics.
- The case for why this belongs in the standard is asserted mainly through the pre-compiled library distribution point, but that claim is not developed into a full standardization argument.
- The most glaring omissions are the absence of any established discussion of who is affected, why a library cannot solve the problem, and whether there is implementation experience to support the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.67   accumulate 6.17   max 6.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.33  coordination 2.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 5.50 / 5.00   (all 3 samples: 5.33)
headings: h2 4
on threshold: motivation, prior_art
splits: motivation[4] 1/1/0  vehicle[2] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                1/1/0  -> 0.67
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal solves a number of problems related to contracts by generating code both with and without checked contract-assertions with one compilation command.
candidate 2 (found by 3 of 15 passes): With the TU-level evaluation semantic of C++26 contracts based on compiler switches performance critical code can’t reside in the same TU as safety critical code.
candidate 3 (found by 2 of 15 passes): One obvious drawback of this proposal is that the generated code size is larger by something approaching a factor of 2 compared to a C++26 build.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/0/0  -> 0.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 4 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Motivation                                 1/1/1  -> 1.00
  [3] 3 Proposal                                   1/1/1  -> 1.00
  [4] 4 Discussions                                2/2/2  -> 2.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): including using in flight proposals such as [[P3400R2](https://wg21.link/p3400r2)] or [P3968R0].
candidate 2 (found by 3 of 15 passes): With [[P3400R2](https://wg21.link/p3400r2)] it becomes possible to individually control the evaluation semantic of each contract-assertion, creating an *effective* *evaluation* *semantic* that may differ from the *initial* *evaluation* *semantic* from the build system.
candidate 3 (found by 2 of 15 passes): The unchecked compile works like a C++26 contracts build with *ignore* semantic, except for contract-assertions marked as *non-ignorable* by some mechanism applicable to individual assertions.
candidate 4 (found by 2 of 15 passes): With the TU-level evaluation semantic of C++26 contracts based on compiler switches performance critical code can’t reside in the same TU as safety critical code.

## vehicle - grade 0.33 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 1/1/0  -> 0.67
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.

## coordination - grade 2.00 (fired in 2 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                2/2/2  -> 2.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.
candidate 2 (found by 3 of 15 passes): To make sure that both checked and unchecked compiles can call functions compiled with an older C++ compiler an *alternate* *name* for the function to call using the traditionally mangled name for the function is added to each call site.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/0/0  -> 0.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

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
