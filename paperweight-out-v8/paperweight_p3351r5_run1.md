Verdict: Adequate (6/14)

The paper offers a solid starting point for why a lazy scan view is useful and that it has real implementation precedent, but it leaves several essential standardization questions essentially unaddressed. The strongest material concerns motivation and existing practice, while the case for putting this in the standard rather than a library is almost entirely absent.

- The paper clearly establishes that stateful transformation is a common need and that scan already exists in eager STL algorithms and in range-v3.
- It shows credible implementation experience through both range-v3 and the Beman Project implementation.
- It gestures at affected users by citing the Ranges plan, but does not actually demonstrate who needs this in the standard or how widely they would be affected.
- The paper does not establish why the standard is the right home, how this would coordinate with related facilities, or why a library implementation would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 5.50 / 6.00   (all 3 samples: 5.67)
headings: h2 8
on threshold: prior_art, implementation
splits: motivation[5] 2/0/0  audience[1] 0/0/1  prior_art[7] 1/1/0  implementation[4] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                2/2/2  -> 2.00
  [4] 3. Design  (part 1 of 2)                     2/2/2  -> 2.00
  [5] 3. Design  (part 2 of 2)                     2/0/0  -> 0.67
  [6] 4. Implementation Experience                 0/0/0  -> 0.00
  [7] 5. Questions To Resolve                      0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Basically, `views::scan` is a lazy view version of `std::inclusive_scan`, or `views::transform` with a stateful function.
candidate 2 (found by 3 of 30 passes): But there are many cases where you need a `transform` to that is stateful.
candidate 3 (found by 2 of 30 passes): Scan is a pretty common operation in functional programming.
candidate 4 (found by 1 of 30 passes): C++ STL provides `std::partial_sum` and `std::inclusive_scan` (latter since C++17) with the inclusive semantics, and `std::exclusive_scan` (since C++17) with the exclusive semantics.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Design  (part 1 of 2)                     0/0/0  -> 0.00
  [5] 3. Design  (part 2 of 2)                     0/0/0  -> 0.00
  [6] 4. Implementation Experience                 0/0/0  -> 0.00
  [7] 5. Questions To Resolve                      0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): The `views::scan` adaptor is classified as a Tier 1 item in the Ranges plan for C++26 ([P2760R1]).

## prior_art - grade 1.50 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Design  (part 1 of 2)                     0/0/0  -> 0.00
  [5] 3. Design  (part 2 of 2)                     2/2/2  -> 2.00
  [6] 4. Implementation Experience                 0/0/0  -> 0.00
  [7] 5. Questions To Resolve                      1/1/0  -> 0.67
  [8] 6. Wording                                   1/1/1  -> 1.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The `views::scan` adaptor is classified as a Tier 1 item in the Ranges plan for C++26 ([P2760R1]).
candidate 2 (found by 3 of 30 passes): Existing third-party parallel libraries like OpenMP and oneTBB also nearly always require random access iterators in their algorithms.
candidate 3 (found by 3 of 30 passes): The wording below is based on [N5054].
candidate 4 (found by 2 of 30 passes): Currently the wording uses the latter (following range-v3), but `transform_view` used the former.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Design  (part 1 of 2)                     0/0/0  -> 0.00
  [5] 3. Design  (part 2 of 2)                     0/0/0  -> 0.00
  [6] 4. Implementation Experience                 0/0/0  -> 0.00
  [7] 5. Questions To Resolve                      0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Design  (part 1 of 2)                     0/0/0  -> 0.00
  [5] 3. Design  (part 2 of 2)                     0/0/0  -> 0.00
  [6] 4. Implementation Experience                 0/0/0  -> 0.00
  [7] 5. Questions To Resolve                      0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Design  (part 1 of 2)                     0/0/0  -> 0.00
  [5] 3. Design  (part 2 of 2)                     0/0/0  -> 0.00
  [6] 4. Implementation Experience                 0/0/0  -> 0.00
  [7] 5. Questions To Resolve                      0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Motivation                                1/1/1  -> 1.00
  [4] 3. Design  (part 1 of 2)                     2/0/2  -> 1.33
  [5] 3. Design  (part 2 of 2)                     0/0/0  -> 0.00
  [6] 4. Implementation Experience                 2/2/2  -> 2.00
  [7] 5. Questions To Resolve                      0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Poll Results                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This adaptor is also present in ranges-v3, where it is called `views::partial_sum` with the function parameter defaulted to `std::plus{}`.
candidate 2 (found by 3 of 30 passes): The author implemented this proposal in [beman.scan_view](https://github.com/bemanproject/scan_view) as part of Beman Project.
candidate 3 (found by 2 of 30 passes): range-v3 has a [`views::partial_sum` adaptor](https://ericniebler.github.io/range-v3/structranges_1_1partial__sum__view.html) that don’t take initial seeds, but takes arbitrary function parameter (defaults to `+`).

-->
