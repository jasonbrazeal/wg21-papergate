Verdict: Adequate (6/14)

The paper offers a narrow but genuine foundation for its standardization argument: it explains why the design question matters, situates itself against prior proposals, and points to existing implementations. The support is thinnest around the basic case for ISO action—who is affected, why the standard is the right venue, and why a library solution is insufficient are left unaddressed.

- The strongest support is the paper’s clear explanation of why the contract-enforcement goal must be settled before the type can be designed.
- The paper also credibly establishes prior art and alternatives by distinguishing its direction from `const char*` parameters and rejecting the unverifiable conversion in P3655R4.
- Implementation experience is established through the Beman Project’s `cstring_view`, including its UB conversion and eager length computation.
- The most glaring omission is the absence of any established case for why this needs to be in the C++ standard rather than remain a library facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 5.67   accumulate 6.00   max 6.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 5
on threshold: motivation, implementation
splits: motivation[5] 2/1/1  prior_art[5] 2/2/1  coordination[5] 0/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              2/1/1  -> 1.33
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): If the primary goal of `zstring_view` is to runtime-enforce the C-string contract, then the whole point is to be able to test #3 above.
candidate 2 (found by 2 of 18 passes): Without this LEWG cannot design the type properly. It can only poll who likes which function better.
candidate 3 (found by 1 of 18 passes): The observation that many people demand to have a type called "zstring_view" and that many people implemented their type called "zstring_view" is misleading.

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

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               2/2/2  -> 2.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              2/2/1  -> 1.67
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This paper follows the direction.
candidate 2 (found by 3 of 18 passes): Other options that the author has are to either use `const char*` as the function parameter type along with the C-string contract, or introduce a new type that directly reflects the C-string contract.
candidate 3 (found by 3 of 18 passes): But we definitely cannot accept `zstring_view(const char*)`, as proposed in [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html), because we will not be able to verify the contract.
candidate 4 (found by 3 of 18 passes): While [[P3749R0]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3749r0.html) raises other objections against [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html) our paper focuses solely on defining the goal clearly.

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

## coordination - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             0/0/0  -> 0.00
  [5] Recommendations                              0/1/1  -> 0.67
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): These implementations by different parties have different semantics and serve different goals.

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
candidate 1 (found by 1 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated.
candidate 2 (found by 1 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated. Length is eagerly computed in the constructor, and can be later retrieved in 𝒪(1).
candidate 3 (found by 1 of 18 passes): Beman Project » `cstring_view` ([https://github.com/bemanproject/cstring_view](https://github.com/bemanproject/cstring_view))

-->
