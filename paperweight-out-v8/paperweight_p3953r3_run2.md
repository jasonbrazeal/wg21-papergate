Verdict: Weak (3/14)

The paper offers a narrow but genuine rationale for renaming `std::runtime_format`, grounded in the changed meaning of “runtime” after compile-time formatting became possible. Beyond that motivation, however, it provides almost no support for the standardization case: it does not identify affected users, justify why a standard change is needed, or show that the problem cannot be addressed outside the standard. The thinnest areas are the complete absence of implementation experience and any discussion of coordination or interoperability.

- The strongest support is the established point that the name `std::runtime_format` became misleading once format strings could be evaluated at compile time.
- The paper claims some relevant prior art and terminology alignment, but does not establish that these alternatives were seriously considered or compared.
- The paper does not establish who is affected by the current name or why the standard is the right place to fix it.
- The most glaring omission is the lack of any implementation experience, leaving the proposal without evidence that the change is practical or tested.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.00   accumulate 3.33   max 3.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 3.00 / 2.50 / 3.00   (all 3 samples: 2.83)
headings: h2 9
on threshold: motivation
splits: motivation[2] 2/1/1  prior_art[2] 1/1/2
## END SUMMARY

## motivation - grade 1.67 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/1/1  -> 1.33
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                2/2/2  -> 2.00
  [7] 6. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 1 of 30 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated. The term runtime conflates it with evaluation time.
candidate 3 (found by 1 of 30 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 4 (found by 1 of 30 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.

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

## prior_art - grade 1.17 (fired in 3 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/2  -> 1.33
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                1/1/1  -> 1.00
  [7] 6. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [8] 7. Impact on existing code                   0/0/0  -> 0.00
  [9] 8. Wording                                   0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.
candidate 2 (found by 3 of 30 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 3 (found by 3 of 30 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).

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
