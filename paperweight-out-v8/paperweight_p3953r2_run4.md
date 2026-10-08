Verdict: Weak (3/14)

The paper offers only a narrow justification for its proposed change: it establishes that the existing name has become misleading in light of later constexpr support, but it does little to show who is affected, why standardization is the right venue, or how the change would fit with existing practice. The strongest support is conceptual, while the practical and procedural case is largely absent.

- The paper clearly establishes the motivating semantic shift: `std::runtime_format` can now appear in constant evaluation, so the name no longer reflects its actual distinction.
- The paper gestures toward prior art and alternative naming, but does not substantiate the claim that `dynamic_format` aligns with established terminology or that the rename is the best available option.
- The paper does not identify any affected users or codebases, leaving the practical impact of the rename unexamined.
- The paper offers no argument for why this requires standardization rather than a library-level or documentation-level response, and no implementation experience to support the change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.00   accumulate 3.33   max 3.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 3.00 / 3.00 / 2.50   (all 3 samples: 2.83)
headings: h2 8
on threshold: motivation
splits: motivation[2] 2/1/1  prior_art[2] 1/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/1/1  -> 1.33
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 3 of 27 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 3 of 9 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/2/1  -> 1.33
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                1/1/1  -> 1.00
  [6] 5. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 27 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 27 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.
candidate 4 (found by 1 of 27 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr`contexts.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [7] 6. Impact on existing code                   0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
