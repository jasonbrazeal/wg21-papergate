Verdict: Adequate (5/14)

The paper offers a partial but uneven case for standardization, with its strongest material concentrated in explaining why existing comparison mechanisms are inadequate and how the proposed operation differs from them. The support becomes thin or absent when the paper turns to the affected audience, coordination with other standards or implementations, and evidence that the facility cannot be provided adequately outside the standard library.

- The paper clearly establishes that current equality and comparison tools fail to provide a padding-independent, read-only value representation check on atomics.
- It also credibly grounds the proposal in the existing `compare_exchange` framework while distinguishing it from `operator==`, `memcmp`, and exchange-based approaches.
- The paper does not establish who is affected by the absence of `compare_load`, leaving the motivating user population unspecified.
- Most glaringly, it offers no implementation experience, coordination evidence, or demonstration that a library solution would be insufficient, leaving the standardization need asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 4 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 5.33   accumulate 4.67   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 4.50 / 4.50 / 5.00   (all 3 samples: 4.67)
headings: h2 10
on threshold: none
splits: insufficiency[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Equality Comparison in the Standard          2/2/2  -> 2.00
  [7] New Capabilities                             2/2/2  -> 2.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Standard C++ currently lacks a mechanism to perform a consistent, read-only, padding-independent value representation equality check on an atomic object.
candidate 2 (found by 3 of 33 passes): These distinct definitions result in behavioral differences when writing concurrent code:
candidate 3 (found by 3 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          0/0/0  -> 0.00
  [7] New Capabilities                             0/0/0  -> 0.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          2/2/2  -> 2.00
  [7] New Capabilities                             2/2/2  -> 2.00
  [8] Relationship to compareexchange              2/2/2  -> 2.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Unlike `operator==` (which relies on semantic logic), `memcmp` (which unsafely evaluates indeterminate padding bits), and `compare_exchange` (which incurs a hardware write), `compare_load` provides a consistent, read-only mechanism to evaluate value representation equality.
candidate 2 (found by 2 of 33 passes): `memcmp` is functionally identical to a value representation comparison only for types *without* padding. For types *with* padding, `memcmp` diverges and becomes an unsafe proxy for value equality due to the potential for indeterminate padding bits.
candidate 3 (found by 2 of 33 passes): The existing `compare_exchange` operations, `compare_exchange_weak` and `compare_exchange_strong`, defined in **[[atomics.types.operations]](https://eel.is/c++draft/atomics#types.operations)** p21–28, provide the semantic basis for the proposed `compare_load` function.
candidate 4 (found by 1 of 33 passes): `memcmp` is functionally identical to a value representation comparison only for types *without* padding.

## vehicle - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          0/0/0  -> 0.00
  [7] New Capabilities                             1/1/1  -> 1.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          0/0/0  -> 0.00
  [7] New Capabilities                             0/0/0  -> 0.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          0/0/0  -> 0.00
  [7] New Capabilities                             0/0/1  -> 0.33
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Unlike a standard atomic `load` followed by a nonatomic `memcmp` comparison, which requires a programmer to commit to a single memory order upfront or navigate complicated standalone fences, `compare_load` allows programmers to express distinct memory orders for success and failure

## implementation - grade 0.00  [binary: max] (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          0/0/0  -> 0.00
  [7] New Capabilities                             0/0/0  -> 0.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

-->
