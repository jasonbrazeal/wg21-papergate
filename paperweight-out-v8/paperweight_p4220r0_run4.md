Verdict: Adequate (6/14)

The paper offers some useful groundwork by explaining why a clear design goal matters and by pointing to prior art and implementation experience, but it leaves the central case for standardization largely unaddressed. The support is thinnest around who would be affected, why the standard is the right venue, and how the proposed type would coordinate with existing library facilities.

- The strongest support is the paper’s explanation that the design of `zstring_view` cannot be evaluated without first settling its intended purpose.
- The paper also credibly grounds itself in prior discussions and an existing implementation with eager length computation and zero-termination assumptions.
- The most glaring omission is any account of who is affected by the absence of such a type or how standardization would serve those users.
- The paper likewise does not establish why a library solution would be insufficient or how the type would interoperate with the rest of the standard library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 3 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 5
on threshold: implementation
splits: motivation[5] 1/1/2  prior_art[2] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Terminology                                  0/0/0  -> 0.00
  [3] The motivation                               2/2/2  -> 2.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              1/1/2  -> 1.33
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Such setup "compiles" and could work, but the callers would need to be informed and then disciplined to only create `string_view` objects that happen to be zero-terminated.
candidate 2 (found by 3 of 18 passes): Depending on what the goal of `zstring_view` is, a different set of constructors may be optimal. But we will not be able to assess which constructor set is optimal, until we know the design goal.
candidate 3 (found by 3 of 18 passes): Without this LEWG cannot design the type properly. It can only poll who likes which function better.

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
  [2] Terminology                                  0/0/1  -> 0.33
  [3] The motivation                               2/2/2  -> 2.00
  [4] Design decisions                             2/2/2  -> 2.00
  [5] Recommendations                              2/2/2  -> 2.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The motivation that we have identified in [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html) is the experience where...
candidate 2 (found by 3 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated. Length is eagerly computed in the constructor, and can be later retrieved in 𝒪(1). Middle-zeros are allowed.
candidate 3 (found by 3 of 18 passes): While [[P3749R0]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3749r0.html) raises other objections against [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html) our paper focuses solely on defining the goal clearly.
candidate 4 (found by 2 of 18 passes): This paper follows the direction.

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
candidate 1 (found by 3 of 18 passes): The library offers a conversion from `const char*` with UB if the `char` array is not zero-terminated. Length is eagerly computed in the constructor, and can be later retrieved in 𝒪(1).

-->
