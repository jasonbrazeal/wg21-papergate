Verdict: Adequate (6/14)

The paper gives a reasonably concrete account of the performance benefit and existing production use of hazard pointer batches, but it leaves several core standardization questions essentially unaddressed. The thinnest parts concern why this needs to be in the standard library rather than remain a library facility, and how the proposed interface would coordinate with the existing C++26 hazard pointer design.

- The strongest support is the demonstrated latency improvement and the long production history of the equivalent Folly facility.
- The paper also clearly identifies the affected audience as users of the C++26 hazard pointer interface who need lower-overhead batch construction and destruction.
- Prior art is asserted through the Folly example and a comparison table, but the paper does not establish how thoroughly alternatives were considered.
- The most glaring omission is the absence of any argument for why a library implementation outside the standard would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.67   accumulate 7.00   max 5.67

## SUMMARY
grades: motivation 1.67  audience 2.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 6.00 / 5.50   (all 3 samples: 5.67)
headings: h2 8
on threshold: none
splits: motivation[4] 1/2/2  motivation[5] 1/2/1  motivation[6] 2/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/2/2  -> 1.67
  [5] Implementation and Use Experience            1/2/1  -> 1.33
  [6] Batches of Hazard Pointers                   2/2/1  -> 1.67
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 3 (found by 3 of 27 passes): The construction and destruction of a nonempty `hazard_pointer` object typically involves access to thread-local storage and has low but non-negligible latency (low single digit nanoseconds).

## audience - grade 2.00 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation and Use Experience            2/2/2  -> 2.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 2 (found by 2 of 27 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 3 (found by 1 of 27 passes): e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.

## prior_art - grade 1.00 (fired in 4 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Batches of Hazard Pointers                   1/1/1  -> 1.00
  [7] Proposed Wording                             1/1/1  -> 1.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.
candidate 2 (found by 3 of 27 passes): The P2530R3 C++26 hazard pointer interface supports only the construction and destruction of nonempty hazard pointers individually.
candidate 3 (found by 3 of 27 passes): The following table shows two functionally-equivalent code snippets using the P2530R3 C++26 hazard pointer interface and using hazard pointer batches.
candidate 4 (found by 2 of 27 passes): This paper proposes extending the C++26 hazard pointer interface to support creation and destruction of batches of nonempty hazard pointers.

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

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## implementation - grade 1.00  [binary: max] (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Batches of Hazard Pointers                   0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] History                                      0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The construction and destruction of multiple nonempty `hazard_pointer` objects in one batch has lower latency than their construction and destruction separately, e.g., 2 ns vs 6 ns for the construction/destruction of 3 nonempty hazard pointers.
candidate 2 (found by 3 of 27 passes): Batches of hazard pointers have been part of the Folly open-source library (under the name `hazptr_array` as a distinct class) and in heavy use in production since 2017.

-->
