Verdict: Adequate (5/14)

The paper offers a clear rationale for the feature and a credible account of the gap it fills relative to `std::tie`, but it does not carry that case through to the standardization-specific questions that would justify committee action. The strongest material concerns the expressive limitation and the prior-art comparison, while the discussion of affected users, implementability, and interoperability remains largely asserted rather than demonstrated.

- The paper establishes why the feature matters by identifying a concrete, recurring limitation in structured bindings and the absence of a single construct for both declaration and assignment.
- The prior-art and alternatives section is well supported, particularly the comparison with `std::tie` and the explanation of why existing mechanisms cannot mix new and pre-existing variables.
- The claim that real-world code is affected is only asserted through a single LLVM reference, without enough surrounding evidence to show the scope or frequency of the need.
- The paper does not establish why the standard, rather than a library or existing language machinery, is the necessary venue, nor does it address coordination, interoperability, or implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.00   accumulate 5.33   max 7.00

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.50  implementation 0.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 4.50 / 5.00   (all 3 samples: 5.00)
headings: h3 9   <- NOT h2, check the unit list
on threshold: motivation, audience
splits: motivation[3] 1/0/0  motivation[6] 0/0/1  insufficiency[5] 2/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     1/0/0  -> 0.33
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Proposal                                     1/1/1  -> 1.00
  [6] Examples                                     0/0/1  -> 0.33
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Structured bindings (`auto [x, y] = foo();`) can only declare new variables. Assigning to pre-existing variables requires `std::tie` from `<tuple>`. There is no single construct that does both.
candidate 2 (found by 2 of 30 passes): This provides a complete, library-free replacement for `std::tie` with `std::ignore`:
candidate 3 (found by 1 of 30 passes): This proposal introduces an extension to C++ structured bindings, allowing assignment to existing variables.
candidate 4 (found by 1 of 30 passes): Assigning from a tuple-like type to a pack of existing variables without P3817 requires either the standard library or significant boilerplate

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
candidate 1 (found by 2 of 30 passes): #### 1. [llvm PassBuilder](https://github.com/llvm/llvm-project/blob/00062ed982256651a28187e865d6ae14e21d8395/llvm/lib/Passes/PassBuilder.cpp#L766)
candidate 2 (found by 1 of 30 passes): 1. [llvm PassBuilder](https://github.com/llvm/llvm-project/blob/00062ed982256651a28187e865d6ae14e21d8395/llvm/lib/Passes/PassBuilder.cpp#L766)

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
candidate 1 (found by 3 of 30 passes): This provides a complete, library-free replacement for `std::tie` with `std::ignore`:
candidate 2 (found by 2 of 30 passes): This proposal closes that gap, with several advantages over std::tie::
candidate 3 (found by 2 of 30 passes): **`=x`** — Conflicts with lambda capture-by-value intuition (`[=]`).
candidate 4 (found by 1 of 30 passes): Neither `std::tie` nor structured bindings alone allow some elements to be new variables and others pre-existing in the same statement. P3817 uniquely enables this

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

## insufficiency - grade 0.50 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Proposal                                     2/0/1  -> 1.00
  [6] Examples                                     0/0/0  -> 0.00
  [7] Alternative Syntaxes Considered              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] Previous Papers                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Assigning from a tuple-like type to a pack of existing variables without P3817 requires either the standard library or significant boilerplate
candidate 2 (found by 1 of 30 passes): This provides a complete, library-free replacement for `std::tie` with `std::ignore`:

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
