Verdict: Strong (8/14)

The paper offers a workable foundation for its standardization case, with clear motivation, relevant prior art, and some implementation experience, but it leaves several important arguments asserted rather than demonstrated. The thinnest support concerns why a library solution is insufficient and how the feature would coordinate with existing or planned standard facilities.

- The strongest support is the established implementation experience, with LLVM already providing a portable `@llvm.clmul` intrinsic.
- The paper also clearly establishes why carry-less multiplication matters and situates the proposal against prior art and existing widening-operation styles.
- The most glaring omission is the complete absence of any discussion of coordination and interoperability with related standardization efforts or existing interfaces.
- The claims about who is affected, why the standard is the right venue, and why a library will not suffice all rest on a single unelaborated assertion about architecture-dependent optimal implementations and opaque mathematical properties.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.67   accumulate 7.67   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.83  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 8.00 / 7.50   (all 3 samples: 7.67)
headings: h2 8
on threshold: vehicle, implementation
splits: audience[6] 0/2/0  vehicle[6] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     1/1/1  -> 1.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Carry-less multiplication is an important operation in a number of use cases:
candidate 2 (found by 3 of 27 passes): The issue with library implementations is that the optimal implementation for `std::clmul` highly depends on the architecture and has interesting mathematical properties that become opaque in the library.
candidate 3 (found by 3 of 27 passes): Such a widening function is important in a various cryptographic use cases.

## audience - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   0/2/0  -> 0.67
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): I also propose a widening operation in the style of [[P3161R4]](https://wg21%2elink/p3161r4)
candidate 2 (found by 3 of 27 passes): Such a naive implementation is far from optimal though. [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).
candidate 3 (found by 2 of 27 passes): This specific example is taken from [FastHilbertCurves]. [[HackersDelight]](https://doc%2elagout%2eorg/security/Hackers'Delight%2epdf) explains the basis behind this computation of Hilbert curves using bitwise operations.
candidate 4 (found by 2 of 27 passes): The function is named `widening_clmul` to be symmetrical with `std::saturating_mul` from [[P4052R0]](https://wg21%2elink/p4052r0) (merged into C++26).

## vehicle - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   2/1/2  -> 1.67
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The issue with library implementations is that the optimal implementation for `std::clmul` highly depends on the architecture and has interesting mathematical properties that become opaque in the library.

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   0/0/0  -> 0.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   1/1/1  -> 1.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The issue with library implementations is that the optimal implementation for `std::clmul` highly depends on the architecture and has interesting mathematical properties that become opaque in the library.

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Since January 2026, LLVM also provides a portable `@llvm.clmul` intrinsic function ([[LLVMClmul]](https://llvm%2eorg/docs/LangRef%2ehtml#llvm-clmul-intrinsic)).

-->
