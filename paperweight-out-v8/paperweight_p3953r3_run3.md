Verdict: Weak (3/14)

The paper offers only a narrow slice of the case needed for standardization: it explains why the existing name has become misleading, but it does not establish who is affected, why this belongs in the standard, or that the change is implementable and coordinated. The thinnest support is around the core standardization questions, where the paper is largely silent.

- The strongest support is the explanation that `std::runtime_format` is now misleading because formatting can occur at compile time.
- The paper claims some alignment with existing terminology and prior proposals, but does not establish that those precedents support this renaming.
- The paper does not establish who is affected by the current name or the proposed change.
- The most glaring omission is the absence of any case for why the standard should make this change rather than leaving it to library-level guidance or documentation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.00   accumulate 3.33   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 3.00 / 2.50 / 3.00   (all 3 samples: 2.83)
headings: h2 9
on threshold: motivation, prior_art
splits: prior_art[2] 2/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/1  -> 1.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                2/2/2  -> 2.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 3 of 30 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/1/2  -> 1.67
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                1/1/1  -> 1.00
  [7] 6. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 30 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 30 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr`contexts.
candidate 4 (found by 1 of 30 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
