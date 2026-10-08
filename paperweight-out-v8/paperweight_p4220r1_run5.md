Verdict: Adequate to Strong (7/14)

The paper offers some useful grounding for its standardization case, particularly through its discussion of prior art and implementation experience, but it leaves several essential questions unanswered. The thinnest areas are the absence of a clear account of who is affected, why a standard facility is needed rather than a library solution, and why the standard itself is the right venue.

- The paper establishes that the problem is real and that differing assumptions about `zstring_view`’s purpose have caused confusion among experts.
- The paper points to existing practice, including the {fmt} library’s `basic_cstring_view`, as evidence that implementations exist and vary in semantics.
- The paper does not establish who is affected by the lack of a standardized type or what concrete user populations would benefit.
- The paper does not establish why a library cannot adequately address the need, nor why standardization is required rather than continued use of existing implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 6.83   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 7.50 / 6.00   (all 3 samples: 6.83)
headings: h2 6
on threshold: implementation
splits: motivation[4] 2/0/0  prior_art[5] 2/0/2  coordination[5] 2/2/0  coordination[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               2/0/0  -> 0.67
  [5] Design decisions                             2/2/2  -> 2.00
  [6] Recommendations                              2/2/2  -> 2.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Avoiding the unfortunate copy in (3) is actually part of the goal "`string_view` with `c_str()`". But if we changed the type of `filename` from `string_view` to `zstring_view` we haven't solved the problem.
candidate 2 (found by 3 of 21 passes): Discussions among the experts in the reflector revealed that they work with different implicit assumptions as to what the goal of `zstring_view` is.
candidate 3 (found by 1 of 21 passes): Such setup "compiles" and could work, but the callers would need to be informed and then disciplined to only create `string_view` objects that happen to be zero-terminated.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Recommendations                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               2/2/2  -> 2.00
  [5] Design decisions                             2/0/2  -> 1.33
  [6] Recommendations                              2/2/2  -> 2.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper follows the direction.
candidate 2 (found by 3 of 21 passes): The motivation that we have identified in [[P3655R4]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3655r4.html) is the experience where:
candidate 3 (found by 3 of 21 passes): [[P4227R0]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4227r0.pdf) argues that zero characters in the middle shall be considered a bug and ideally prevented. This position is correct for a type whose goal is "C-string with runtime contract enforcement".
candidate 4 (found by 2 of 21 passes): The {fmt} library ([https://github.com/fmtlib/fmt](https://github.com/fmtlib/fmt)) defines type `basic_cstring_view` (and the accompanying `cstring_view` alias) with only three non-defaulted member functions:

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Recommendations                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.83 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             2/2/0  -> 1.33
  [6] Recommendations                              0/1/0  -> 0.33
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Implementations of "something like `zstring_view`" exist in quantity, but they do not necessarily agree on their primary goal, often they state no goal.
candidate 2 (found by 1 of 21 passes): These implementations by different parties have different semantics and serve different goals.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Recommendations                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             2/2/2  -> 2.00
  [6] Recommendations                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): The {fmt} library ([https://github.com/fmtlib/fmt](https://github.com/fmtlib/fmt)) defines type `basic_cstring_view` (and the accompanying `cstring_view` alias) with only three non-defaulted member functions:
candidate 2 (found by 1 of 21 passes): The {fmt} library ([https://github.com/fmtlib/fmt](https://github.com/fmtlib/fmt)) defines type `basic_cstring_view` (and the accompanying `cstring_view` alias) with only three non-defaulted member functions.

-->
