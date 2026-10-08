Verdict: Weak (3/14)

The paper offers only a narrow foundation for its own standardization: it explains why the existing name has become misleading, but it does little to establish who is affected, what alternatives were seriously weighed, or why a library-level solution would be inadequate. The strongest material is historical and terminological, while the case for standardizing the proposed change remains largely undeveloped.

- The paper clearly establishes that `std::runtime_format` no longer reliably signals runtime-only behavior now that format strings can be evaluated at compile time.
- The discussion of prior art gestures toward relevant history and existing terminology, but it does not demonstrate that alternatives were evaluated or that the proposed direction is the right one.
- The paper provides no evidence about affected users, implementation experience, or coordination with other features, leaving the practical need for standardization unsubstantiated.
- Most glaringly, the paper never explains why a library-level remedy would not suffice, which is a central requirement for bringing the change into the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.00   accumulate 3.17   max 3.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.50 / 3.00   (all 3 samples: 2.67)
headings: h2 5
on threshold: motivation
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
candidate 2 (found by 3 of 18 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation. However, with the adoption of `constexpr` `std::format`, the term runtime no longer reliably describes the behavior of `std::runtime_format`.

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

## prior_art - grade 1.00 (fired in 3 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Abstract                                  1/1/1  -> 1.00
  [3] 2. Motivation                                1/1/1  -> 1.00
  [4] 3. Proposed Naming: std::dynamicformat       1/1/1  -> 1.00
  [5] 4. Impact on existing code                   0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The name `std::runtime_format` was accurate when introduced in [P2918], as format strings were not usable in constant evaluation.
candidate 2 (found by 3 of 18 passes): This aligns with existing terminology `std::format` such as dynamic format specifiers (`check_dynamic_spec`).
candidate 3 (found by 2 of 18 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`. Subsequently, [P3391] made `std::format` usable in constant evaluation.
candidate 4 (found by 1 of 18 passes): [P2918] introduced `std::runtime_format` to allow opting out of compile-time format string checks in `std::format`.

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
