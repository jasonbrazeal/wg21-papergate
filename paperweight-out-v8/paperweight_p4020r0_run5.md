Verdict: Adequate (6/14)

The paper offers some grounding for why contract violation recording matters and shows awareness of existing work, but much of its case for standardization rests on assertions rather than demonstrated need. The thinnest areas are the absence of a library-only alternative analysis and the lack of direct implementation experience with the proposed mechanism itself.

- The strongest support is the recognition that P2900 has already been implemented experimentally and prompted library rewriting efforts, showing the surrounding problem is live.
- The paper clearly identifies that existing practice and prior proposals already cover much of the space, which frames the need for something new.
- The argument for why this must be in the standard, rather than handled by existing or library-level mechanisms, is asserted but not substantiated.
- The most glaring omission is the complete lack of a case for why a library solution cannot address the stated goals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 6 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.67   accumulate 6.17   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 1.50  vehicle 0.67  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 24 of 28 section-criterion pairs unanimous (86%)
single-sample totals would have been: 5.50 / 6.00 / 5.50   (all 3 samples: 5.67)
headings: h2 3
on threshold: prior_art
splits: audience[2] 0/1/0  audience[3] 0/0/1  vehicle[2] 1/2/1  coordination[2] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 4 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         2/2/2  -> 2.00
  [3] P2900 contract assertions                    2/2/2  -> 2.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): To enable (or guarantee) that parts of these contracts are "enforced", that is, as in sanitizers, an instrumentation code is injected to kill the program that is observed to violate the declared preconditions (and postconditions).
candidate 2 (found by 1 of 12 passes): To provide one more means of formally communicating at least parts of the contract.
candidate 3 (found by 1 of 12 passes): To communicate, at least parts of the contract, also to machines.
candidate 4 (found by 1 of 12 passes): We have seen reports that ever since P2900 has been implemented as an experiment in GCC and Clang, experiments have been performed with rewriting some libraries using assertion statements into a variant using precondition and postcondition assertions.

## audience - grade 0.33 (fired in 2 of 4 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         0/1/0  -> 0.33
  [3] P2900 contract assertions                    0/0/1  -> 0.33
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): Serious C++ programmers have to and do deal with contracts: they recognize them, they communicate them, and they will continue to do so with or without a dedicated language feature.
candidate 2 (found by 1 of 12 passes): It is evident that this model is not adopted by a significant portion of WG21.

## prior_art - grade 1.50 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Contracts in general                         1/1/1  -> 1.00
  [3] P2900 contract assertions                    2/2/2  -> 2.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): With contract assertions ([[P2900R14]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2900r14.pdf)) voted into the [[CD]](https://www.iso.org/standard/91179.html), a number of concerns have been risen.
candidate 2 (found by 3 of 12 passes): C++ doesn't need a new feature for this to continue.
candidate 3 (found by 3 of 12 passes): Things proposed in [[P3911R2]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3911r2.html) and other considered papers (P4005R0, P4009R0) are new features, features proposed on top of P2900 for C++26.

## vehicle - grade 0.67 (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         1/2/1  -> 1.33
  [3] P2900 contract assertions                    0/0/0  -> 0.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): To have a standardized, uniform mechanism of recording any act of contract violation in the program.
candidate 2 (found by 1 of 12 passes): To enable (or guarantee) that parts of these contracts are "enforced", that is, as in sanitizers, an instrumentation code is injected to kill the program that is observed to violate the declared preconditions (and postconditions).
candidate 3 (found by 1 of 12 passes): To provide one more means of formally communicating at least parts of the contract.

## coordination - grade 0.17 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         1/0/0  -> 0.33
  [3] P2900 contract assertions                    0/0/0  -> 0.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): If one person creates a component and another uses it, in order for this cöopertion to work both parties need to have the same understanding on what this component does.

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         0/0/0  -> 0.00
  [3] P2900 contract assertions                    0/0/0  -> 0.00
  [4] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         0/0/0  -> 0.00
  [3] P2900 contract assertions                    1/1/1  -> 1.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): We have seen reports that ever since P2900 has been implemented as an experiment in GCC and Clang, experiments have been performed with rewriting some libraries using assertion statements into a variant using precondition and postcondition assertions.

-->
