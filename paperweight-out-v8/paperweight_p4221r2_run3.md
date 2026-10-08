Verdict: Adequate (5/14)

The paper offers a solid conceptual case for why a read-only, padding-independent atomic comparison would fill a gap in the standard library, and it clearly identifies the existing facilities that fall short. However, the support is thin on the practical and procedural side: it does not establish who is affected, how implementations would coordinate, or whether the feature has been tried in practice.

- The strongest support is the clear contrast drawn between `compare_load` and the existing alternatives—`operator==`, `memcmp`, and `compare_exchange`—showing why none of them provides the desired read-only, padding-safe atomic comparison.
- The paper also grounds the proposal in the existing semantics of `compare_exchange`, which gives it a plausible standardization anchor.
- The most glaring omission is the absence of any implementation experience, leaving no evidence that the proposed operation is implementable or useful in real code.
- Equally unestablished is who would be affected by the change, making it hard to judge the proposal’s reach or urgency.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 6.00   accumulate 5.33   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.67  implementation 0.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 5.50 / 5.00   (all 3 samples: 5.33)
headings: h2 10
on threshold: none
splits: motivation[4] 0/1/0  prior_art[6] 1/2/1  vehicle[8] 0/1/0  insufficiency[6] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/1/0  -> 0.33
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Equality Comparison in the Standard          2/2/2  -> 2.00
  [7] New Capabilities                             2/2/2  -> 2.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Standard C++ currently lacks a mechanism to perform a consistent, read-only, padding-independent value representation equality check on an atomic object.
candidate 2 (found by 3 of 33 passes): Currently, `compare_exchange` is the only mechanism in the standard library capable of consistently evaluating value representation equality in the presence of padding, but it couples this evaluation to a mutating memory write.
candidate 3 (found by 2 of 33 passes): Unlike `operator==` (which relies on semantic logic), `memcmp` (which unsafely evaluates indeterminate padding bits), and `compare_exchange` (which incurs a hardware write), `compare_load` provides a consistent, read-only mechanism to evaluate value representation equality.
candidate 4 (found by 1 of 33 passes): This function performs an atomic comparison of the atomic object's value with an expected value, following the same value representation comparison semantics as `compare_exchange_strong`.

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

## prior_art - grade 2.00 (fired in 3 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          1/2/1  -> 1.33
  [7] New Capabilities                             2/2/2  -> 2.00
  [8] Relationship to compareexchange              2/2/2  -> 2.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Unlike `operator==` (which relies on semantic logic), `memcmp` (which unsafely evaluates indeterminate padding bits), and `compare_exchange` (which incurs a hardware write), `compare_load` provides a consistent, read-only mechanism to evaluate value representation equality.
candidate 2 (found by 3 of 33 passes): The existing `compare_exchange` operations, `compare_exchange_weak` and `compare_exchange_strong`, defined in **[[atomics.types.operations]](https://eel.is/c++draft/atomics#types.operations)** p21–28, provide the semantic basis for the proposed `compare_load` function.
candidate 3 (found by 2 of 33 passes): Currently, `compare_exchange` is the only mechanism in the standard library capable of consistently evaluating value representation equality in the presence of padding, but it couples this evaluation to a mutating memory write.
candidate 4 (found by 1 of 33 passes): `memcmp` is functionally identical to a value representation comparison only for types *without* padding. For types *with* padding, `memcmp` diverges and becomes an unsafe proxy for value equality due to the potential for indeterminate padding bits.

## vehicle - grade 0.67 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          0/0/0  -> 0.00
  [7] New Capabilities                             1/1/1  -> 1.00
  [8] Relationship to compareexchange              0/1/0  -> 0.33
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities
candidate 2 (found by 1 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities:
candidate 3 (found by 1 of 33 passes): The design intent is that any future standard modifications regarding pointer provenance or "zap" fixes applied to the specification of `compare_exchange` will apply equally and systematically to `compare_load`.

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

## insufficiency - grade 0.67 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Equality Comparison in the Standard          1/0/0  -> 0.33
  [7] New Capabilities                             1/1/1  -> 1.00
  [8] Relationship to compareexchange              0/0/0  -> 0.00
  [9] Preview                                      0/0/0  -> 0.00
  [10] Usage Examples                               0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities
candidate 2 (found by 1 of 33 passes): Currently, `compare_exchange` is the only mechanism in the standard library capable of consistently evaluating value representation equality in the presence of padding, but it couples this evaluation to a mutating memory write.
candidate 3 (found by 1 of 33 passes): Unlike a standard atomic `load` followed by a nonatomic `memcmp` comparison, which requires a programmer to commit to a single memory order upfront or navigate complicated standalone fences, `compare_load` allows programmers to express distinct memory orders for success and failure

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
