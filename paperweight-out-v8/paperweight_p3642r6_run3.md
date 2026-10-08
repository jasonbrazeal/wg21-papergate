Verdict: Strong (8/14)

The paper offers some useful grounding for its proposal, particularly through concrete prior art and a benchmark suggesting meaningful performance gains, but it leaves several core justifications for standardization largely unaddressed. The thinnest support concerns who would be affected by the change and how it would coordinate with existing practice or adjacent language features.

- The strongest support comes from the cited prior art and the QuickBench comparison showing a naive implementation performing 9.2× worse than an efficient one.
- The paper establishes that carry-less multiplication matters in cryptographic and other use cases, though it does so only in general terms.
- The argument that a pure library implementation misses optimization opportunities is asserted but not substantiated, leaving both the “why the standard” and “why a library will not do” cases weak.
- The paper offers no account of who is affected or how the proposal would coordinate with existing implementations, language features, or interoperability concerns.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 8.00   max 10.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.50 / 8.00 / 7.50   (all 3 samples: 7.67)
headings: h2 11
on threshold: motivation, vehicle, insufficiency, implementation
splits: motivation[6] 0/1/1  motivation[7] 1/2/1  motivation[8] 0/1/0  prior_art[6] 0/2/2
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   0/1/1  -> 0.67
  [7] 5. Design considerations                     1/2/1  -> 1.33
  [8] 6. Potential design changes following LWG... 0/1/0  -> 0.33
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Carry-less multiplication is an important operation in a number of use cases:
candidate 2 (found by 3 of 36 passes): Such a widening function is important in a various cryptographic use cases.
candidate 3 (found by 2 of 36 passes): While a pure library implementation of `std::clmul` is possible, it misses out on many optimization opportunities.
candidate 4 (found by 1 of 36 passes): A notable problem is that this permits structured bindings and list initialization, and the low bits first order was perceived as more surprising than the other way around.

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

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   0/2/2  -> 1.33
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Potential design changes following LWG... 2/2/2  -> 2.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Optional wording changes A                0/0/0  -> 0.00
  [11] 9. Optional wording changes B                0/0/0  -> 0.00
  [12] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): I also propose a widening operation in the style of [[P3161R4]](https://wg21%2elink/p3161r4), as follows:
candidate 2 (found by 3 of 36 passes): This specific example is taken from [FastHilbertCurves]. [[HackersDelight]](https://doc%2elagout%2eorg/security/Hackers'Delight%2epdf) explains the basis behind this computation of Hilbert curves using bitwise operations.
candidate 3 (found by 3 of 36 passes): This would be consistent with `__int128` but inconsistent with `_BitInt(128)`; the latter is only aligned to 64 bits.
candidate 4 (found by 2 of 36 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).

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
