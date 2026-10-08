Verdict: Adequate (5/14)

The paper offers a narrow but real foundation for its standardization case: it clearly explains why a read-only, padding-independent atomic comparison would matter and situates the idea against existing operations and `memcmp`. Beyond that, however, the support thins considerably, with several essential arguments asserted rather than demonstrated and others absent entirely.

- The strongest support is the motivation, which identifies a genuine gap in current atomic operations and contrasts the proposed facility with `operator==`, `memcmp`, and `compare_exchange`.
- The discussion of prior art and alternatives is also well grounded, particularly in showing how `memcmp` fails for types with padding and how existing compare-exchange operations provide a semantic basis.
- The weakest established area is the claim that the capability cannot be achieved by combining existing facilities, which is repeated but not substantiated.
- The most glaring omissions are any account of who is affected, implementation experience, and coordination or interoperability considerations, leaving the practical need and readiness for standardization largely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 6.00   accumulate 5.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.50  implementation 0.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h2 10
on threshold: none
splits: motivation[10] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
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
  [10] Usage Examples                               1/0/0  -> 0.33
  [11] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Standard C++ currently lacks a mechanism to perform a consistent, read-only, padding-independent value representation equality check on an atomic object.
candidate 2 (found by 3 of 33 passes): These distinct definitions result in behavioral differences when writing concurrent code:
candidate 3 (found by 3 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities
candidate 4 (found by 1 of 33 passes): The following table shows code snippets using the current standard C++ (on the left) and using the proposed atomic `compare_load` function (on the right).

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
candidate 2 (found by 3 of 33 passes): The existing `compare_exchange` operations, `compare_exchange_weak` and `compare_exchange_strong`, defined in **[[atomics.types.operations]](https://eel.is/c++draft/atomics#types.operations)** p21–28, provide the semantic basis for the proposed `compare_load` function.
candidate 3 (found by 2 of 33 passes): `memcmp` is functionally identical to a value representation comparison only for types *without* padding. For types *with* padding, `memcmp` diverges and becomes an unsafe proxy for value equality due to the potential for indeterminate padding bits.
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
candidate 1 (found by 2 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities
candidate 2 (found by 1 of 33 passes): The introduction of `compare_load` provides fundamental concurrency capabilities that cannot be achieved by combining existing standard library facilities:

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

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
