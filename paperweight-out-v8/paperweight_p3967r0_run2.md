Verdict: Adequate (6/14)

The paper gives a partial account of why its approach might be useful, but it leaves several essential parts of the standardization case unaddressed, particularly around who is affected, why a library solution is insufficient, and whether anyone has actually implemented or used the technique. The strongest material concerns the problem of TU-level contract semantics and the interaction with existing proposals and legacy linking, while the weakest areas are almost entirely silent.

- The paper clearly establishes the core motivation: performance-critical and safety-critical code cannot currently share a translation unit under C++26’s TU-level contract evaluation semantics.
- It also establishes meaningful prior art and alternatives by situating the proposal against P3400R2 and describing how the unchecked compile would behave relative to existing contract modes.
- The discussion of coordination and interoperability is supported by concrete claims about alternate names, legacy mangling, and compatibility with older compilers and standard libraries.
- The most glaring omission is the absence of any established case for who is affected, why a library cannot solve the problem, or what implementation experience exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.67  coordination 2.00  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 5.00 / 6.00 / 6.00   (all 3 samples: 5.67)
headings: h2 4
on threshold: motivation, prior_art
splits: prior_art[1] 1/1/0  vehicle[2] 0/2/2  coordination[1] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                1/1/1  -> 1.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal solves a number of problems related to contracts by generating code both with and without checked contract-assertions with one compilation command.
candidate 2 (found by 3 of 15 passes): With the TU-level evaluation semantic of C++26 contracts based on compiler switches performance critical code can’t reside in the same TU as safety critical code.
candidate 3 (found by 2 of 15 passes): This proposal solves that issue and also makes the idea of being able to turn off library hardening less important.
candidate 4 (found by 1 of 15 passes): One obvious drawback of this proposal is that the generated code size is larger by something approaching a factor of 2 compared to a C++26 build.

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
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] 2 Motivation                                 1/1/1  -> 1.00
  [3] 3 Proposal                                   1/1/1  -> 1.00
  [4] 4 Discussions                                2/2/2  -> 2.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): With the TU-level evaluation semantic of C++26 contracts based on compiler switches performance critical code can’t reside in the same TU as safety critical code.
candidate 2 (found by 3 of 15 passes): including using in flight proposals such as [[P3400R2](https://wg21.link/p3400r2)] or [P3968R0].
candidate 3 (found by 3 of 15 passes): With [[P3400R2](https://wg21.link/p3400r2)] it becomes possible to individually control the evaluation semantic of each contract-assertion, creating an *effective* *evaluation* *semantic* that may differ from the *initial* *evaluation* *semantic* from the build system.
candidate 4 (found by 1 of 15 passes): The unchecked compile works like a C++26 contracts build with *ignore* semantic, except for contract-assertions marked as *non-ignorable* by some mechanism applicable to individual assertions.

## vehicle - grade 0.67 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/2/2  -> 1.33
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.

## coordination - grade 2.00 (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                2/2/2  -> 2.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): To make sure that both checked and unchecked compiles can call functions compiled with an older C++ compiler an *alternate* *name* for the function to call using the traditionally mangled name for the function is added to each call site.
candidate 2 (found by 2 of 15 passes): This includes the specific problem of linking to a hardened or unhardened standard library as there is only one.
candidate 3 (found by 1 of 15 passes): By virtue of its legacy name mangling the thunk will also be called by code compiled with an older compiler.
candidate 4 (found by 1 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.

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
