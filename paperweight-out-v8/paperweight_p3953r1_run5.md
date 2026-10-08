Verdict: Weak (3/14)

The paper offers a narrow but genuine foundation for its case by explaining why the current name has become misleading in light of constexpr formatting, but it leaves most of the standardization burden unaddressed. The support is thinnest around the practical and procedural questions that would justify a standards change rather than a naming preference.

- The paper establishes that the distinction between `runtime_format` and `dynamic_format` concerns how the format string is provided and validated, not when formatting occurs.
- The paper gestures toward prior terminology and the historical accuracy of the old name, but does not substantiate alternatives or prior art beyond assertion.
- The paper does not establish who is affected, why the standard is the right venue, how the change would coordinate with existing practice, or why a library-level solution would be insufficient.
- The paper offers no implementation experience or evidence of real-world confusion that would demonstrate the need for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.00   accumulate 3.33   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 3.00 / 2.50   (all 3 samples: 2.83)
headings: h2 6
on threshold: motivation, prior_art
splits: prior_art[2] 2/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/1  -> 1.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 2 of 21 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated. The term runtime conflates it with evaluation time.
candidate 3 (found by 1 of 21 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/2/1  -> 1.67
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                1/1/1  -> 1.00
  [5] 4. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 21 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 1 of 21 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr` contexts.
candidate 4 (found by 1 of 21 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr`contexts.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
