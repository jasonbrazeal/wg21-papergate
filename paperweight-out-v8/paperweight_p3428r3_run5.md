Verdict: Adequate (7/14)

The paper offers solid evidence that the feature has real performance value and production backing, but it does not make a complete case for why this needs to be in the C++ standard rather than remaining a library facility. The strongest support concerns implementation experience and the affected audience, while the argument thins considerably around standardization rationale, interoperability, and why existing library approaches are insufficient.

- The paper clearly establishes implementation experience through years of production use in Folly and concrete latency measurements showing a meaningful improvement over individual construction and destruction.
- The affected audience is well supported by the same production evidence and the observation that nonempty hazard pointer operations already incur low but non-negligible thread-local storage costs.
- The paper only claims, rather than establishes, prior art and alternatives, since it points to Folly and the existing P2530R3 interface but does not fully develop the comparison or the design space.
- The most glaring omission is the absence of any established argument for why the standard is the right home for this facility, how it coordinates with existing or future hazard pointer interfaces, or why a library implementation would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.00   accumulate 7.83   max 7.00

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 6.50 / 6.50   (all 3 samples: 6.67)
headings: h2 9
on threshold: audience, implementation
splits: audience[5] 2/1/1  audience[6] 1/0/1  prior_art[8] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Batches of Hazard Pointers                   2/2/2  -> 2.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 30 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 3 (found by 3 of 30 passes): The construction and destruction of a nonempty `hazard_pointer` object typically involves access to thread-local storage and has low but non-negligible latency (low single digit nanoseconds).

## audience - grade 1.67 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation and Use Experience            2/1/1  -> 1.33
  [6] Batches of Hazard Pointers                   1/0/1  -> 0.67
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 2 (found by 2 of 30 passes): e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 3 (found by 2 of 30 passes): The construction and destruction of a nonempty `hazard_pointer` object typically involves access to thread-local storage and has low but non-negligible latency (low single digit nanoseconds).
candidate 4 (found by 1 of 30 passes): 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.

## prior_art - grade 1.00 (fired in 4 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Batches of Hazard Pointers                   1/1/1  -> 1.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                1/1/0  -> 0.67
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 2 (found by 3 of 30 passes): The P2530R3 C++26 hazard pointer interface supports only the construction and destruction of nonempty hazard pointers individually.
candidate 3 (found by 2 of 30 passes): This revision P3428R3 revises R2 by following LEWG Croydon 2026 feedback.
candidate 4 (found by 2 of 30 passes): The following table shows two functionally-equivalent code snippets using the P2530R3 C++26 hazard pointer interface and using hazard pointer batches.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            2/2/2  -> 2.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Usage Example                                0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 30 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.

-->
