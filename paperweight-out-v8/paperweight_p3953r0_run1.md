Verdict: Weak (3/14)

The paper offers a narrow but genuine rationale for why the existing name has become misleading, but it does little to establish that standardization is the necessary or appropriate remedy. The strongest material concerns the semantic mismatch introduced by later constexpr changes, while the case for affected users, standardization need, and practical alternatives is essentially absent.

- The paper establishes that `std::runtime_format` can now be evaluated at compile time, making its name misleading in a way that matters for clarity.
- The paper claims some alignment with existing terminology and prior proposals, but does not substantiate that the rename reflects established usage or a considered design direction.
- The paper does not identify who is affected by the current name or what practical problem the rename would solve for them.
- The paper offers no argument for why the standard must change rather than leaving the name alone or addressing confusion through documentation or library-level guidance.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.00   accumulate 3.17   max 3.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.50 / 3.00   (all 3 samples: 2.67)
headings: h2 5
on threshold: motivation
splits: prior_art[2] 1/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/1  -> 1.00
  [3] 2. Motivation                                2/2/2  -> 2.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 2 of 18 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.
candidate 3 (found by 1 of 18 passes): Despite its name, `std::runtime_format` can be evaluated at compile time.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 3 of 6 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/2  -> 1.33
  [3] 2. Motivation                                1/1/1  -> 1.00
  [4] 3. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 18 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 18 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.
candidate 4 (found by 1 of 18 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr`contexts.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Motivation                                0/0/0  -> 0.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
