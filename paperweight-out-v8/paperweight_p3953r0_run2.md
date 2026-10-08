Verdict: Weak to Adequate (3/14)

The paper gives a clear and well-supported rationale for why the existing name is misleading, but it offers almost no evidence about the practical scope of the change, the affected users, or the standardization path. The strongest material concerns terminology and consistency with existing wording, while the case for acting through the standard is largely absent.

- The paper establishes that the name `std::runtime_format` no longer matches its behavior now that compile-time evaluation is possible, and that the real distinction lies in how the format string is supplied and validated.
- The paper grounds its proposed name in existing terminology such as dynamic format specifiers and explains the historical accuracy of the original name.
- The paper does not identify who is affected by the rename or what the migration or compatibility burden would be.
- The paper does not explain why the standard is the right venue, why a library-level solution would not suffice, or how the change would coordinate with existing implementations and other proposals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.00   accumulate 3.67   max 4.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 3.00 / 3.50   (all 3 samples: 3.17)
headings: h2 5
on threshold: motivation, prior_art
splits: motivation[2] 1/1/2
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
candidate 2 (found by 2 of 18 passes): The real distinction is not when formatting occurs, but how the format string is provided and validated. The term runtime conflates it with evaluation time.
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

## prior_art - grade 1.50 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  2/2/2  -> 2.00
  [3] 2. Motivation                                1/1/1  -> 1.00
  [4] 3. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This paper proposes renaming `std::runtime_format` to `std::dynamic_format` to better reflect its semantics and avoid confusion in `constexpr`contexts.
candidate 2 (found by 3 of 18 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 3 (found by 3 of 18 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).

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
