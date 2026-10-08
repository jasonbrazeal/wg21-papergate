Verdict: Strong (10/14)

The paper offers a mixed case for its own standardization, with the strongest support coming from its prior art, implementation experience, and the general argument that these operations belong in a fundamental bit-manipulation library. The thinnest areas are the failure to establish who is concretely affected, how the proposal coordinates with existing practice, and why a library solution is genuinely insufficient.

- The paper’s prior art and implementation experience are well grounded, with references to existing algorithms, compiler builtins, and a working implementation.
- The argument for why the standard library is the right home is reasonably supported by the claim that these are fundamental operations with hardware acceleration and reasonable software fallbacks.
- The paper does not establish coordination and interoperability with existing standards or implementations, leaving that requirement unaddressed.
- The case for why a library cannot suffice is only claimed, not established, and the evidence for who is affected rests on a single code-search figure without further context.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 9.83   max 11.67

## SUMMARY
grades: motivation 1.33  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 0.00  insufficiency 1.17  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.50 / 9.50 / 10.00   (all 3 samples: 9.50)
headings: h2 11
on threshold: motivation, audience, insufficiency
splits: motivation[6] 0/0/2  motivation[8] 2/1/2  prior_art[4] 1/0/1  prior_art[5] 0/0/1
        vehicle[4] 1/1/0  insufficiency[4] 0/1/0
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      0/0/2  -> 0.67
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     2/1/2  -> 1.67
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): However, there are still a few operations which are non-trivial to implement in software and have widely available hardware support.
candidate 2 (found by 1 of 36 passes): Bit-reversal, repetition, compression, and expansion are fundamental operations that meet multiple criteria which make them suitable for standardization: 1. They are common and useful operations. 2. They can be used to implement numerous other operations.
candidate 3 (found by 1 of 36 passes): Both operations can be described with `extract` and `deposit` terminology, making it virtually useless for keeping the operations apart.
candidate 4 (found by 1 of 36 passes): The utility functions in `<bit>` are not meant to provide a full bitwise manipulation library, but fundamental operations, especially those that can be accelerated in hardware while still having reasonable software fallbacks.

## audience - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     0/0/0  -> 0.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A GitHub code search for `/(_pdep_u|_pext_u)(32|64)/ AND language:c++` reveals ~1300 files which use the intrinsic wrappers for the x86 instructions.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/1  -> 0.67
  [5] 3. Proposed features                         0/0/1  -> 0.33
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     2/2/2  -> 2.00
  [9] 7. Possible implementation                   1/1/1  -> 1.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The use of `compress` and `expand` is consistent with the mask-based permutations for `std::simd` proposed in [P2664R6].
candidate 2 (found by 3 of 36 passes): [Warren1] presents algorithms which are the basis for [Schultke1].
candidate 3 (found by 2 of 36 passes): The C++ bit manipulation library in `<bit>` is an invaluable abstraction from hardware operations.
candidate 4 (found by 2 of 36 passes): It is worth noting that clang provides a cross-platform family of intrinsics. [`__builtin_bitreverse`](https://clang.llvm.org/docs/LanguageExtensions.html#builtin-bitreverse) uses byte-swapping or bit-reversal instructions if possible.

## vehicle - grade 2.00 (fired in 3 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/0  -> 0.67
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     2/2/2  -> 2.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): All in all, there are multiple factors that strongly suggest a standard library implementation:
candidate 2 (found by 3 of 36 passes): The utility functions in `<bit>` are not meant to provide a full bitwise manipulation library, but fundamental operations, especially those that can be accelerated in hardware while still having reasonable software fallbacks.
candidate 3 (found by 2 of 36 passes): However, there are still a few operations which are non-trivial to implement in software and have widely available hardware support.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     0/0/0  -> 0.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.17 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     0/0/0  -> 0.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): ISO C++ does not offer a mechanism through which all of this information can be utilized. Namely, it is not possible to change strategy based on information that only becomes available during optimization passes.
candidate 2 (found by 1 of 36 passes): However, there are still a few operations which are non-trivial to implement in software and have widely available hardware support.
candidate 3 (found by 1 of 36 passes): ISO C++ does not offer a mechanism through which all of this information can be utilized.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     0/0/0  -> 0.00
  [9] 7. Possible implementation                   2/2/2  -> 2.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Clang 18 emits the following (and GCC virtually the same); see [CompilerExplorer1]:
candidate 2 (found by 3 of 36 passes): All proposed functions have been implemented in [Schultke1].

-->
