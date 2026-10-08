Verdict: Adequate to Strong (7/14)

The paper offers some concrete support for its standardization case, particularly around implementation experience and the existence of prior art, but it leaves several essential parts of the argument largely unaddressed. The thinnest areas are the failure to identify who is affected and the absence of any discussion of coordination or interoperability.

- The paper establishes implementation experience by pointing to LLVM’s portable `@llvm.clmul` intrinsic, which shows the operation is already being standardized at the compiler level.
- The paper establishes prior art and alternatives by citing a benchmark against NTL and by aligning the proposed naming with an existing C++26 facility.
- The paper does not establish who is affected, offering no description of the user population or the scale of the need.
- The paper does not establish coordination and interoperability, saying nothing about how the proposal would interact with other standards, compilers, or library features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 7.33   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.50 / 7.50 / 7.00   (all 3 samples: 7.33)
headings: h2 8
on threshold: implementation
splits: prior_art[8] 1/2/1  vehicle[6] 1/2/1  insufficiency[6] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Proposed wording                          0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Carry-less multiplication is an important operation in a number of use cases:
candidate 2 (found by 3 of 27 passes): The issue with library implementations is that the optimal implementation for `std::clmul` highly depends on the architecture and has interesting mathematical properties that become opaque in the library.
candidate 3 (found by 3 of 27 passes): Such a widening function is important in a various cryptographic use cases.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## prior_art - grade 2.00 (fired in 5 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Possible implementation                   2/2/2  -> 2.00
  [7] 5. Design considerations                     2/2/2  -> 2.00
  [8] 6. Proposed wording                          1/2/1  -> 1.33
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): I also propose a widening operation in the style of [[P3161R4]](https://wg21%2elink/p3161r4), as follows:
candidate 2 (found by 2 of 27 passes): [[QuickBench]](https://quick-bench%2ecom/q/eG4Q5BR_udnfh4V5f-3d3h3fRHY) shows that a naive `clmul` implementation which computes both the high and the low bits performs 9.2× worse than an efficient implementation taken from [[NTL]](https://github%2ecom/libntl/ntl).
candidate 3 (found by 2 of 27 passes): The function is named `widening_clmul` to be symmetrical with `std::saturating_mul` from [[P4052R0]] (merged into C++26).
candidate 4 (found by 1 of 27 passes): The special form `clmul(x, -1)` can be used to accelerate the computation of Hilbert curves.

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Possible implementation                   1/2/1  -> 1.33
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
  [6] 4. Possible implementation                   2/1/1  -> 1.33
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
