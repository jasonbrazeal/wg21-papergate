Verdict: Weak to Adequate (3/14)

The paper offers a narrow but real foundation for its case, centered on the historical accuracy and present misleadingness of the name `std::runtime_format`, yet it leaves most of the burden of justifying standardization unaddressed. The support is thinnest where a proposal normally needs to show who is harmed, what alternatives were weighed, why the standard is the right venue, and that the change is implementable.

- The strongest support is the established point that `std::runtime_format` can now be evaluated at compile time, so its name no longer matches its actual semantics.
- The paper claims some prior art and alternative framing through references to P2918, P3391, and existing `std::format` terminology, but does not establish that these were examined as alternatives to the proposed rename.
- The most glaring omission is the absence of any established discussion of who is affected by the current name or why a standard change, rather than documentation or library-level mitigation, is needed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 3.00   accumulate 3.50   max 3.33

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.50 / 3.00 / 2.50   (all 3 samples: 3.00)
headings: h2 6
on threshold: none
splits: motivation[2] 2/2/1  prior_art[2] 2/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 2 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/2/1  -> 1.67
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposed Naming: std::dynamicformat       0/0/0  -> 0.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): As a result, `std::runtime_format` can now be evaluated at compile time, making its name misleading.
candidate 2 (found by 1 of 21 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.
candidate 3 (found by 1 of 21 passes): Despite its name, `std::runtime_format` can be evaluated at compile time.
candidate 4 (found by 1 of 21 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.

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

## prior_art - grade 1.17 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/1/1  -> 1.33
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                1/1/1  -> 1.00
  [5] 4. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 21 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 21 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.
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
