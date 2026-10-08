Verdict: Adequate to Strong (7/14)

The paper gives a reasonably concrete account of the performance benefit and existing production use of batched hazard pointers, but it leaves the central standardization rationale largely implicit. The strongest material concerns implementation experience and the affected audience, while the argument for why this belongs in the standard rather than in a library is essentially absent.

- The paper’s strongest support is its concrete latency comparison and citation of Folly’s `hazptr_array`, which has been used in production since 2017.
- The discussion of prior art is thinner, since it identifies the current C++26 interface and Folly’s design but does not really establish that the proposed batch interface is the right standardization shape.
- The paper does not establish why the standard should provide this facility, as opposed to leaving batched construction and destruction to libraries.
- The most glaring omission is the absence of any case for why a library implementation would be insufficient for the proposed functionality.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.67   accumulate 7.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 1.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 7.50 / 7.50   (all 3 samples: 7.17)
headings: h2 8
on threshold: implementation
splits: audience[5] 1/2/2  prior_art[7] 0/0/1  coordination[5] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Batches of Hazard Pointers                   2/2/2  -> 2.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 3 (found by 3 of 27 passes): The construction and destruction of a nonempty `hazard_pointer` object typically involves access to thread-local storage and has low but non-negligible latency (low single digit nanoseconds).

## audience - grade 1.83 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation and Use Experience            1/2/2  -> 1.67
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.

## prior_art - grade 1.00 (fired in 4 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Batches of Hazard Pointers                   1/1/1  -> 1.00
  [7] Proposed Wording                             0/0/1  -> 0.33
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 2 (found by 3 of 27 passes): The P2530R3 C++26 hazard pointer interface supports only the construction and destruction of nonempty hazard pointers individually.
candidate 3 (found by 2 of 27 passes): This paper proposes extending the C++26 hazard pointer interface to support creation and destruction of batches of nonempty hazard pointers.
candidate 4 (found by 1 of 27 passes): This revision P3428R4 revises R3 by following LWG Brno 2026 feedback.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/1/1  -> 0.67
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            2/2/2  -> 2.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.

-->
