Verdict: Weak (3/14)

The paper offers only a narrow historical observation about why the existing name has become misleading, but it does not build a case that this naming problem requires a standards change. The support is thinnest around the basic questions of who is harmed, what alternatives were considered, and why the issue cannot be addressed outside the standard.

- The strongest support is the established point that `std::runtime_format` was accurate when introduced but has become misleading now that format strings work in constant evaluation.
- The paper claims some prior art and alternative framing around existing terminology, but does not establish that these alternatives were actually examined or rejected.
- The paper does not establish who is affected by the misleading name or what practical problem they encounter.
- The most glaring omission is the absence of any argument for why the standard must change, as opposed to documentation, guidance, or a library-level remedy.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.00   accumulate 3.33   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 2.50 / 3.00   (all 3 samples: 2.83)
headings: h2 6
on threshold: motivation, prior_art
splits: prior_art[4] 2/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 2 (found by 2 of 21 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated.
candidate 3 (found by 1 of 21 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.

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

## prior_art - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/1  -> 1.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/1/2  -> 1.67
  [5] 4. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [6] 5. Impact on existing code                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 21 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 21 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.
candidate 4 (found by 1 of 21 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`.

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
