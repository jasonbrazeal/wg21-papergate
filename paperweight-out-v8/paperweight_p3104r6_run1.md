Verdict: Strong (10/14)

The paper offers a mixed case for standardization, with its strongest grounding in prior art, implementation experience, and the argument that compiler integration can exploit information unavailable to ordinary library code. The support is thinnest where the paper needs to show who is concretely affected, why a library cannot suffice, and how the proposal coordinates with adjacent standardization efforts.

- The paper’s implementation experience is well supported by a reference implementation that works across major compilers and leverages ARM and x86_64 hardware where available.
- The argument for standardization is most convincing when it points to compiler-level strategy changes that become possible only during optimization, which a library cannot access.
- The paper does not adequately establish who is affected beyond a single code-search count, leaving the user base and its needs largely asserted rather than demonstrated.
- The most glaring omission is the failure to substantiate why a library will not do, since the paper itself concedes that more general forms can be built on the proposed operations with relative ease and little overhead.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.33   accumulate 10.00   max 11.00

## SUMMARY
grades: motivation 1.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 0.17  insufficiency 1.33  implementation 2.00
sample agreement: 79 of 84 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.00 / 9.50 / 9.50   (all 3 samples: 9.50)
headings: h2 11
on threshold: audience, insufficiency
splits: motivation[6] 2/0/0  vehicle[4] 0/1/0  coordination[8] 1/0/0  insufficiency[6] 1/2/2
        insufficiency[8] 0/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/0/0  -> 0.67
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     1/1/1  -> 1.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): However, there are still a few operations which are non-trivial to implement in software and have widely available hardware support.
candidate 2 (found by 2 of 36 passes): The utility functions in `<bit>` are not meant to provide a full bitwise manipulation library, but fundamental operations, especially those that can be accelerated in hardware while still having reasonable software fallbacks.
candidate 3 (found by 1 of 36 passes): They are non-trivial to implement efficiently in software.
candidate 4 (found by 1 of 36 passes): The generality falsely suggests hardware support for all forms, despite the function only being accelerated for specific inputs.

## audience - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     2/2/2  -> 2.00
  [9] 7. Possible implementation                   1/1/1  -> 1.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The C++ bit manipulation library in `<bit>` is an invaluable abstraction from hardware operations.
candidate 2 (found by 3 of 36 passes): [Warren1] presents an O(log n) algorithm which operates by swapping lower and upper `N / 2`, ..., `16`, `8`, `4`, `2`, and `1` bits in parallel.
candidate 3 (found by 3 of 36 passes): [Warren1] presents algorithms which are the basis for [Schultke1].
candidate 4 (found by 2 of 36 passes): The use of `compress` and `expand` is consistent with the mask-based permutations for `std::simd` proposed in [P2664R6].

## vehicle - grade 2.00 (fired in 3 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     2/2/2  -> 2.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Bullets 2. and 3. suggest that `bit_compress` and `bit_expand` benefit from being implemented directly in the compiler via intrinsic, even if hardware does not directly implement these operations.
candidate 2 (found by 3 of 36 passes): The utility functions in `<bit>` are not meant to provide a full bitwise manipulation library, but fundamental operations, especially those that can be accelerated in hardware while still having reasonable software fallbacks.
candidate 3 (found by 1 of 36 passes): Even without hardware support, these functions provide great utility and/or help the developer write more expressive code.

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     1/0/0  -> 0.33
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The use of `compress` and `expand` is consistent with the mask-based permutations for `std::simd` proposed in [P2664R6].

## insufficiency - grade 1.33 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      1/2/2  -> 1.67
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     0/0/1  -> 0.33
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): However, there are still a few operations which are non-trivial to implement in software and have widely available hardware support.
candidate 2 (found by 2 of 36 passes): ISO C++ does not offer a mechanism through which all of this information can be utilized. Namely, it is not possible to change strategy based on information that only becomes available during optimization passes.
candidate 3 (found by 1 of 36 passes): ISO C++ does not offer a mechanism through which all of this information can be utilized.
candidate 4 (found by 1 of 36 passes): These more general form can be built on top of the proposed hardware-oriented versions. This can be done with relative ease and with little to no overhead.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 2)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 36 passes): A GitHub code search for `/(_pdep_u|_pext_u)(32|64)/ AND language:c++` reveals ~1300 files which use the intrinsic wrappers for the x86 instructions.
candidate 2 (found by 2 of 36 passes): All proposed functions have been implemented in [Schultke1].
candidate 3 (found by 1 of 36 passes): All proposed functions have been implemented in [Schultke1]. This reference implementation is compatible with all three major compilers, and leverages hardware support from ARM and x86_64 where possible.

-->
