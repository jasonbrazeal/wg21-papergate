Verdict: Strong (8/14)

The paper offers meaningful support in a few areas, particularly in showing that carry-less multiplication is a recognized operation with relevant use cases and that efficient implementations already exist outside the standard. However, the case for standardization is uneven: the paper does not establish who is affected in a concrete way, nor does it demonstrate why a library solution is insufficient or how the proposal would coordinate with existing practice.

- The strongest support is the implementation experience, where a benchmark is cited to show that a naive implementation is substantially slower than an efficient existing one.
- The paper also establishes prior art and alternatives by connecting the proposed operation to related proposals and existing library implementations.
- The thinnest support is in coordination and interoperability, where the paper offers nothing to show how the feature would fit with existing or planned standard facilities.
- The claim that a library implementation misses optimization opportunities is asserted but not substantiated, leaving the central argument for standardization unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.67   accumulate 8.33   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 8.00 / 8.00 / 9.00   (all 3 samples: 8.33)
headings: h2 11
on threshold: vehicle, insufficiency, implementation
splits: motivation[6] 1/2/0  audience[6] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   1/2/0  -> 1.00
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Potential design changes following LWG... 1/1/1  -> 1.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Such a widening function is important in a various cryptographic use cases.
candidate 2 (found by 3 of 36 passes): A notable problem is that this permits structured bindings and list initialization, and the low bits first order was perceived as more surprising than the other way around.
candidate 3 (found by 2 of 36 passes): Carry-less multiplication is an important operation in a number of use cases: CRC Computation, Cryptography, Bit manipulation.
candidate 4 (found by 1 of 36 passes): Carry-less multiplication is an important operation in a number of use cases:

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   0/0/2  -> 0.67
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Potential design changes following LWG... 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)
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
candidate 1 (found by 3 of 36 passes): In the example above, `std::clmul(x, x)` is equivalent to [[P3104R3]](https://wg21%2elink/p3104r3)'s `std::bit_expand(x, 0x55555555u)`.
candidate 2 (found by 3 of 36 passes): Such a naive implementation is far from optimal though. [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).
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
