Verdict: Weak (3/14)

The paper offers only a narrow foundation for its own standardization: it explains why the current name has become misleading, but leaves nearly every other part of the case unstated. The thinnest areas are the absence of any identified affected users, any argument for why the standard is the right venue, and any evidence of implementation experience or coordination.

- The strongest support is the established point that `std::runtime_format` can now be evaluated at compile time, making its name genuinely misleading.
- The discussion of prior art and alternatives is present but only claimed, relying on references to P2918 and P3391 without fully establishing how they support the rename.
- The paper does not establish who is affected by the current name or why the standard, rather than a library or documentation change, is needed.
- The most glaring omissions are the complete lack of coordination, interoperability, and implementation experience, leaving the standardization case largely unbuilt.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.00   accumulate 3.50   max 3.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 5
on threshold: motivation, prior_art
splits: motivation[2] 1/1/2  prior_art[2] 2/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/2  -> 1.33
  [3] 2. Motivation                                2/2/2  -> 2.00
  [4] 3. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 2 of 18 passes): Despite its name, `std::runtime_format` can be evaluated at compile time.
candidate 3 (found by 1 of 18 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.

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

## prior_art - grade 1.33 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/2/1  -> 1.67
  [3] 2. Motivation                                1/1/1  -> 1.00
  [4] 3. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 18 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 18 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr`contexts.
candidate 4 (found by 1 of 18 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.

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
