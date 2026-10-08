Verdict: Adequate (6/14)

The paper offers some useful grounding for its motivation and shows relevant implementation experience, but it leaves several essential parts of the standardization case unaddressed, particularly around who is affected, why the standard is the right venue, and why a library would not suffice.

- The strongest support is the concrete implementation experience from the {fmt} library, which demonstrates that the proposed type has been built and used outside the standard.
- The paper also establishes prior art and alternatives by engaging with related proposals and identifying differing goals among existing designs.
- The thinnest support is the absence of any established case for who is affected, why standardization is necessary, or why a library solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 6
on threshold: implementation
splits: coordination[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             2/2/2  -> 2.00
  [6] Recommendations                              2/2/2  -> 2.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Avoiding the unfortunate copy in (3) is actually part of the goal "`string_view` with `c_str()`". But if we changed the type of `filename` from `string_view` to `zstring_view` we haven't solved the problem.
candidate 2 (found by 3 of 21 passes): Discussions among the experts in the reflector revealed that they work with different implicit assumptions as to what the goal of `zstring_view` is.

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

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               2/2/2  -> 2.00
  [5] Design decisions                             2/2/2  -> 2.00
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

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Terminology                                  0/0/0  -> 0.00
  [4] The motivation                               0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Recommendations                              0/0/1  -> 0.33
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): These implementations by different parties have different semantics and serve different goals.

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
candidate 1 (found by 3 of 21 passes): The {fmt} library ([https://github.com/fmtlib/fmt](https://github.com/fmtlib/fmt)) defines type `basic_cstring_view` (and the accompanying `cstring_view` alias) with only three non-defaulted member functions:

-->
