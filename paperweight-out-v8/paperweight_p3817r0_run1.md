Verdict: Adequate (5/14)

The paper offers a clear and well-supported motivation for the feature, particularly as a library-free replacement for `std::tie`, and it credibly establishes the prior-art gap. The case thins considerably around the standard’s role, interoperability, and implementation experience, where the paper provides no evidence at all, and the claims about affected users and why a library will not suffice remain asserted rather than demonstrated.

- The strongest support is the motivation, which is concrete and tied to a recognizable gap in structured bindings and `std::tie`.
- The prior-art discussion is also well grounded, with explicit alternatives and a stated advantage over the existing idiom.
- The most glaring omission is the absence of any argument for why this belongs in the standard rather than remaining a library or language-extension concern.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.67   accumulate 5.50   max 6.67

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.50  implementation 0.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h3 9   <- NOT h2, check the unit list
on threshold: motivation, audience
splits: motivation[7] 1/0/0  insufficiency[4] 0/1/0  insufficiency[5] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Proposal                                     1/1/1  -> 1.00
  [6] Examples                                     1/1/1  -> 1.00
  [7] Alternative Syntaxes Considered              1/0/0  -> 0.33
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This proposal introduces an extension to C++ structured bindings, allowing assignment to existing variables.
candidate 2 (found by 3 of 30 passes): Structured bindings (`auto [x, y] = foo();`) can only declare new variables. Assigning to pre-existing variables requires `std::tie` from `<tuple>`. There is no single construct that does both.
candidate 3 (found by 2 of 30 passes): This provides a complete, library-free replacement for `std::tie` with `std::ignore`:
candidate 4 (found by 2 of 30 passes): This enables tracking state across iterations without a separate assignment in the loop body

## audience - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Examples                                     2/2/2  -> 2.00
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): #### 1. [llvm PassBuilder](https://github.com/llvm/llvm-project/blob/00062ed982256651a28187e865d6ae14e21d8395/llvm/lib/Passes/PassBuilder.cpp#L766)

## prior_art - grade 2.00 (fired in 3 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Proposal                                     2/2/2  -> 2.00
  [6] Examples                                     0/0/0  -> 0.00
  [7] Alternative Syntaxes Considered              2/2/2  -> 2.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This proposal closes that gap, with several advantages over std::tie::
candidate 2 (found by 3 of 30 passes): This provides a complete, library-free replacement for `std::tie` with `std::ignore`:
candidate 3 (found by 3 of 30 passes): **`tie x`** — Overly verbose; confusingly evokes `std::tie` even though it does not use it.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Examples                                     0/0/0  -> 0.00
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Examples                                     0/0/0  -> 0.00
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 2 of 10 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Proposal                                     1/0/1  -> 0.67
  [6] Examples                                     0/0/0  -> 0.00
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Assigning from a tuple-like type to a pack of existing variables without P3817 requires either the standard library or significant boilerplate
candidate 2 (found by 1 of 30 passes): `std::tie` requires `<tuple>`, which is unavailable in many constrained environments (embedded systems, bare-metal, OS kernels).

## implementation - grade 0.00  [binary: max] (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Examples                                     0/0/0  -> 0.00
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
