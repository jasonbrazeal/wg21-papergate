Verdict: Adequate (6/14)

The paper gives a clear account of why the design goal needs to be settled before the type can be specified, and it situates that concern against existing discussion and prior implementations. Its support is thinnest when it comes to showing who is affected, how standardization would coordinate with other library or language work, and why a non-standard library solution would be insufficient.

- The strongest support is the paper’s explanation that the committee cannot evaluate constructor choices without first knowing what `zstring_view` is meant to enforce.
- The paper also credibly grounds itself in prior art and existing implementation experience, including the observation that many people have already written similar types.
- The most glaring omission is the absence of any established case for why this needs to be in the standard rather than remain a library type.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.33   accumulate 5.67   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.00 / 5.50 / 5.50   (all 3 samples: 5.67)
headings: h2 5
on threshold: motivation, implementation
splits: vehicle[3] 1/0/0  implementation[5] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              1/1/1  -> 1.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Without this LEWG cannot design the type properly. It can only poll who likes which function better.
candidate 2 (found by 2 of 18 passes): Depending on what the goal of `zstring_view` is, a different set of constructors may be optimal. But we will not be able to assess which constructor set is optimal, until we know the design goal.
candidate 3 (found by 1 of 18 passes): If the primary goal of `zstring_view` is to runtime-enforce the C-string contract, then the whole point is to be able to test #3 above.

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

## prior_art - grade 2.00 (fired in 5 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Terminology                                  1/1/1  -> 1.00
  [3] The motivation                               2/2/2  -> 2.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              2/2/2  -> 2.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In this paper, whenever the word 'contract' is used, we *do not* refer to the C++26 feature known as "contract assertions", but instead refer to the methods of Library API specifications.
candidate 2 (found by 3 of 18 passes): While [[P3749R0]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3749r0.html) raises other objections against [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html) our paper focuses solely on defining the goal clearly.
candidate 3 (found by 2 of 18 passes): This paper follows the direction.
candidate 4 (found by 2 of 18 passes): The motivation that we have identified in [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html) is the experience where...

## vehicle - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               1/0/0  -> 0.33
  [4] Design decisions                             0/0/0  -> 0.00
  [5] Recommendations                              0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): To reflect in the type the C-string contract: pointer must not be null, the array shall contain the zero character.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               0/0/0  -> 0.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              1/1/0  -> 0.67
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated. Length is eagerly computed in the constructor, and can be later retrieved in 𝒪(1).
candidate 2 (found by 2 of 18 passes): many people implemented their type called "zstring_view"

-->
