Verdict: Adequate (6/14)

The paper offers some useful grounding for its direction, particularly through prior art and a concrete implementation, but it leaves the central standardization argument largely unaddressed. The thinnest areas are the absence of any established need for a standard facility, any account of who is affected, and any explanation of why a library solution would not suffice.

- The strongest support comes from the cited prior art and the Beman Project implementation, which show that the basic idea has been explored in practice.
- The paper also establishes why the runtime-enforcement question matters for the design discussion, even though that alone does not justify standardization.
- The most glaring omission is the lack of any established case for why this belongs in the standard rather than remaining a library type.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 3 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 5.67   max 6.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.00 / 5.00 / 6.00   (all 3 samples: 5.67)
headings: h2 5
on threshold: motivation, implementation
splits: motivation[5] 2/0/2  prior_art[5] 0/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              2/0/2  -> 1.33
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): If the primary goal of `zstring_view` is to runtime-enforce the C-string contract, then the whole point is to be able to test #3 above.
candidate 2 (found by 2 of 18 passes): Without this LEWG cannot design the type properly. It can only poll who likes which function better.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             0/0/0  -> 0.00
  [5] Recommendations                              0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               2/2/2  -> 2.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              0/2/1  -> 1.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated. Length is eagerly computed in the constructor, and can be later retrieved in 𝒪(1). Middle-zeros are allowed.
candidate 2 (found by 2 of 18 passes): This paper follows the direction.
candidate 3 (found by 2 of 18 passes): Other options that the author has are to either use `const char*` as the function parameter type along with the C-string contract, or introduce a new type that directly reflects the C-string contract.
candidate 4 (found by 1 of 18 passes): During the 2025 Sofia meeting, LEWG declared consensus to spend more time on `zstring_view` ([[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html)). This paper follows the direction.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             0/0/0  -> 0.00
  [5] Recommendations                              0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             0/0/0  -> 0.00
  [5] Recommendations                              0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             0/0/0  -> 0.00
  [5] Recommendations                              0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated. Length is eagerly computed in the constructor, and can be later retrieved in 𝒪(1).
candidate 2 (found by 1 of 18 passes): Beman Project » `cstring_view` ([https://github.com/bemanproject/cstring_view](https://github.com/bemanproject/cstring_view))

-->
