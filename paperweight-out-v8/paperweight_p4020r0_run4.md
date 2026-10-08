Verdict: Adequate (6/14)

The paper offers a partial case for its own standardization, with its strongest material going to the existence of prior work and the general motivation for formalizing parts of a contract. The support becomes much thinner when the paper turns to the specific need for a standard mechanism, the affected parties, and interoperability, where assertions are made but not backed by evidence or argument. The absence of any case against a library solution is the most conspicuous gap.

- The paper does establish that contract assertions have a long history and that current in-body assertion experience does not transfer directly to declarations.
- The paper’s motivation is credited as established, particularly the desire to formally communicate parts of a contract.
- The paper claims but does not establish that a standardized uniform mechanism for recording contract violations is needed.
- The paper offers no established argument for why a library approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 6 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 6.00   accumulate 5.67   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 1.50  vehicle 0.50  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 25 of 28 section-criterion pairs unanimous (89%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 3
on threshold: prior_art
splits: audience[3] 1/0/1  prior_art[2] 0/1/0  coordination[2] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 4 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Contracts in general                         2/2/2  -> 2.00
  [3] P2900 contract assertions                    2/2/2  -> 2.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): To provide one more means of formally communicating at least parts of the contract.
candidate 2 (found by 2 of 12 passes): With contract assertions ([[P2900R14]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2900r14.pdf)) voted into the [[CD]](https://www.iso.org/standard/91179.html), a number of concerns have been risen.
candidate 3 (found by 1 of 12 passes): a number of concerns have been risen.
candidate 4 (found by 1 of 12 passes): There is a lot of experience with configurable assertions inside function bodies. There is little experience with assertions in function declarations.

## audience - grade 0.33 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         0/0/0  -> 0.00
  [3] P2900 contract assertions                    1/0/1  -> 0.67
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): The representatives of two compiler vendors — Microsoft and EDG — have objected to standardizing contract assertions as in P2900.

## prior_art - grade 1.50 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Contracts in general                         0/1/0  -> 0.33
  [3] P2900 contract assertions                    2/2/2  -> 2.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): With contract assertions ([[P2900R14]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2900r14.pdf)) voted into the [[CD]](https://www.iso.org/standard/91179.html), a number of concerns have been risen.
candidate 2 (found by 2 of 12 passes): Things proposed in [[P3911R2]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3911r2.html) and other considered papers (P4005R0, P4009R0) are new features, features proposed on top of P2900 for C++26.
candidate 3 (found by 1 of 12 passes): So why have we been working to add precondition and postcondition declarations to the language for over two decades?
candidate 4 (found by 1 of 12 passes): The declared experience is with using *statements* inside function bodies. There, it is the function's implementation detail whether a check is performed or not.

## vehicle - grade 0.50 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         1/1/1  -> 1.00
  [3] P2900 contract assertions                    0/0/0  -> 0.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): To have a standardized, uniform mechanism of recording any act of contract violation in the program.

## coordination - grade 0.17 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         0/1/0  -> 0.33
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

## implementation - grade 1.00  [binary: max] (fired in 1 of 4 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Contracts in general                         0/0/0  -> 0.00
  [3] P2900 contract assertions                    1/1/1  -> 1.00
  [4] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): We have seen reports that ever since P2900 has been implemented as an experiment in GCC and Clang, experiments have been performed with rewriting some libraries using assertion statements into a variant using precondition and postcondition assertions.

-->
