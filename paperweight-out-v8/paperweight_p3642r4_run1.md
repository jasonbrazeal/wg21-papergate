Verdict: Strong (8/14)

The paper offers some meaningful support for standardization, particularly through concrete implementation evidence and a clear account of why the operation matters, but it leaves several central arguments asserted rather than demonstrated. The thinnest parts concern the case that a library solution is insufficient and that standardization is the right remedy, since the paper leans on a single architectural-optimization claim without showing why that cannot be addressed outside the standard.

- The strongest support is the implementation experience, with benchmark data and an LLVM intrinsic showing real-world viability.
- The paper clearly establishes why carry-less multiplication matters across cryptographic and related use cases.
- Prior art and alternatives are grounded in references to related proposals and existing library practice.
- The most glaring omission is the absence of any coordination or interoperability discussion, leaving the standardization landscape unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 6 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 9.00   accumulate 8.33   max 10.67

## SUMMARY
grades: motivation 1.83  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.00 / 7.50 / 9.00   (all 3 samples: 8.17)
headings: h2 8
on threshold: vehicle, implementation
splits: motivation[6] 1/2/2  audience[6] 2/0/2  insufficiency[6] 1/1/2
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   1/2/2  -> 1.67
  [7] 5. Design considerations                     1/1/1  -> 1.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Carry-less multiplication is an important operation in a number of use cases:
candidate 2 (found by 3 of 27 passes): The issue with library implementations is that the optimal implementation for `std::clmul` highly depends on the architecture and has interesting mathematical properties that become opaque in the library.
candidate 3 (found by 3 of 27 passes): Such a widening function is important in a various cryptographic use cases.

## audience - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   2/0/2  -> 1.33
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 27 passes): I also propose a widening operation in the style of [[P3161R4]](https://wg21%2elink/p3161r4), as follows:
candidate 2 (found by 3 of 27 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).
candidate 3 (found by 2 of 27 passes): In the example above, `std::clmul(x, x)` is equivalent to [[P3104R3]](https://wg21%2elink/p3104r3)'s `std::bit_expand(x, 0x55555555u)`.
candidate 4 (found by 2 of 27 passes): Most of the design choices take the design of [[P3161R4]](https://wg21%2elink/p3161r4) into consideration:

## vehicle - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
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

## insufficiency - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   1/1/2  -> 1.33
  [7] 5. Design considerations                     0/0/0  -> 0.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The issue with library implementations is that the optimal implementation for `std::clmul` highly depends on the architecture and has interesting mathematical properties that become opaque in the library.

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).
candidate 2 (found by 1 of 27 passes): Since January 2026, LLVM also provides a portable `@llvm.clmul` intrinsic function ([[LLVMClmul]](https://llvm%2eorg/docs/LangRef%2ehtml#llvm-clmul-intrinsic)).

-->
