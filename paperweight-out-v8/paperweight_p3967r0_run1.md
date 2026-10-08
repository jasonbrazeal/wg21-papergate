Verdict: Adequate (5/14)

The paper offers only a narrow basis for its standardization case, with the strongest support concentrated in coordination and interoperability, while most other necessary justifications remain asserted rather than demonstrated. The thinnest areas are the absence of any implementation experience and any account of who would be affected by the proposed change.

- The paper does establish that the approach addresses distribution of pre-compiled libraries and provides an alternate name for calls into older compilers, which is a concrete interoperability point.
- The discussion of prior art and alternatives gestures at existing proposals and the checked/unchecked split, but does not show how this proposal meaningfully improves on or differs from those alternatives.
- The paper never identifies the affected users, codebases, or ecosystems, leaving the scope and practical relevance of the problem unclear.
- There is no implementation experience presented, so the proposal offers no evidence that the mechanism is feasible, usable, or beneficial in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 5 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.33   accumulate 5.83   max 5.67

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.00  vehicle 0.50  coordination 1.67  insufficiency 0.17  implementation 0.00
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 5.50 / 5.00 / 4.00   (all 3 samples: 4.50)
headings: h2 4
on threshold: coordination
splits: motivation[2] 2/0/2  prior_art[4] 2/0/0  coordination[4] 2/2/0  insufficiency[2] 0/1/0
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Motivation                                 2/0/2  -> 1.33
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                1/1/1  -> 1.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal solves a number of problems related to contracts by generating code both with and without checked contract-assertions with one compilation command.
candidate 2 (found by 2 of 15 passes): This proposal solves that issue and also makes the idea of being able to turn off library hardening less important.
candidate 3 (found by 1 of 15 passes): This forces unnatural subdivision of code such as `setup` and `run` functions in the same classes into different TUs just to get contract checks on the `setup` parts without getting unacceptable performance degradation in the `run` parts.
candidate 4 (found by 1 of 15 passes): With the TU-level evaluation semantic of C++26 contracts based on compiler switches performance critical code can’t reside in the same TU as safety critical code.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/0/0  -> 0.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 4 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Motivation                                 1/1/1  -> 1.00
  [3] 3 Proposal                                   1/1/1  -> 1.00
  [4] 4 Discussions                                2/0/0  -> 0.67
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): With this proposal calls to inline and template functions that are not inlined always call the checked or unchecked compile depending on whether the calling code is checked or unchecked
candidate 2 (found by 3 of 15 passes): including using in flight proposals such as [[P3400R2](https://wg21.link/p3400r2)] or [P3968R0].
candidate 3 (found by 2 of 15 passes): The unchecked compile works like a C++26 contracts build with *ignore* semantic, except for contract-assertions marked as *non-ignorable* by some mechanism applicable to individual assertions.
candidate 4 (found by 1 of 15 passes): This proposal solves a number of problems related to contracts by generating code both with and without checked contract-assertions with one compilation command.

## vehicle - grade 0.50 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 1/1/1  -> 1.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.

## coordination - grade 1.67 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 2/2/2  -> 2.00
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                2/2/0  -> 1.33
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This proposal also solves the problem of distributing pre-compiled libraries as the same library file contains both the checked and unchecked compiles.
candidate 2 (found by 2 of 15 passes): To make sure that both checked and unchecked compiles can call functions compiled with an older C++ compiler an *alternate* *name* for the function to call using the traditionally mangled name for the function is added to each call site.

## insufficiency - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Motivation                                 0/1/0  -> 0.33
  [3] 3 Proposal                                   0/0/0  -> 0.00
  [4] 4 Discussions                                0/0/0  -> 0.00
  [5] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): Furthermore the lack of name mangling difference between functions with different evaluation semantics in C++26 allows the linker to randomly select implementations of outlined inline and template functions, which is a big problem for instance for the standard library.

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
