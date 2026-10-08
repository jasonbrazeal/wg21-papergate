Verdict: Strong (8/14)

The paper offers some concrete support for the usefulness and performance motivation behind carry-less multiplication, but it leaves several essential parts of the standardization case largely unaddressed. The strongest material concerns prior art and implementation experience, while the thinnest areas are the absence of any identified affected audience and the lack of evidence for coordination or interoperability concerns.

- The paper establishes meaningful prior art and implementation experience by citing a benchmark showing a 9.2× performance gap between a naive implementation and an efficient one from NTL.
- The motivation for standardization rests almost entirely on the claim that a pure library implementation misses optimization opportunities, but the paper does not substantiate why that requires a standard facility rather than a compiler intrinsic or vendor extension.
- The paper does not identify who is affected by the lack of a standardized `clmul`, leaving the urgency and breadth of the need unclear.
- The paper offers no discussion of coordination with existing practice, other proposals, or interoperability constraints, which is a notable omission for a proposal touching low-level arithmetic.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 84 of 84 section-criterion pairs unanimous (100%)
single-sample totals would have been: 8.00 / 8.00 / 8.00   (all 3 samples: 8.00)
headings: h2 11
on threshold: vehicle, insufficiency, implementation
splits: none
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Potential design changes following LWG... 1/1/1  -> 1.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Carry-less multiplication is an important operation in a number of use cases:
candidate 2 (found by 3 of 36 passes): Such a widening function is important in a various cryptographic use cases.
candidate 3 (found by 3 of 36 passes): A notable problem is that this permits structured bindings and list initialization, and the low bits first order was perceived as more surprising than the other way around.
candidate 4 (found by 1 of 36 passes): While a pure library implementation of `std::clmul` is possible, it misses out on many optimization opportunities.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   0/0/0  -> 0.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Potential design changes following LWG... 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Potential design changes following LWG... 2/2/2  -> 2.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).
candidate 2 (found by 3 of 36 passes): The function is named `widening_clmul` to be symmetrical with `std::saturating_mul` from [[P4052R0]](https://wg21%2elink/p4052r0) (merged into C++26).
candidate 3 (found by 3 of 36 passes): This would be consistent with `__int128` but inconsistent with `_BitInt(128)`; the latter is only aligned to 64 bits.
candidate 4 (found by 2 of 36 passes): I also propose a widening operation in the style of [[P3161R4]](https://wg21%2elink/p3161r4), as follows:

## vehicle - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Potential design changes following LWG... 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): While a pure library implementation of `std::clmul` is possible, it misses out on many optimization opportunities.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   0/0/0  -> 0.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Potential design changes following LWG... 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Potential design changes following LWG... 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): While a pure library implementation of `std::clmul` is possible, it misses out on many optimization opportunities.

## implementation - grade 2.00  [binary: max] (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Potential design changes following LWG... 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).

-->
