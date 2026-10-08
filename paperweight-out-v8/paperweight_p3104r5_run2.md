Verdict: Strong (9/14)

The paper offers a solid foundation for why these operations matter and how they can be implemented, but it leaves several key arguments about the necessity of standardization asserted rather than demonstrated. The thinnest support concerns the case for compiler intrinsics over a library solution and the evidence that the affected population is large enough to justify standardization.

- The strongest support is the demonstration that these operations are non-trivial, common, and already have hardware acceleration, with a working reference implementation across all three major compilers.
- The paper also credibly grounds the proposal in existing practice and prior art, including `std::simd` mask permutations and established bit-manipulation algorithms.
- The argument that only a compiler intrinsic can exploit optimization-time information is stated but not backed by concrete examples or evidence that a library cannot achieve comparable results.
- The most glaring omission is the lack of established evidence about who is affected, since the single GitHub code search figure is treated as sufficient without broader context or corroboration.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.33   accumulate 9.17   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.00  coordination 0.17  insufficiency 1.00  implementation 2.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 9.00 / 9.50 / 9.00   (all 3 samples: 9.17)
headings: h2 11
on threshold: audience, vehicle, insufficiency
splits: prior_art[4] 1/0/0  coordination[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 12 sections, strong in 2)
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
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): However, there are still a few operations which are non-trivial to implement in software and have widely available hardware support.
candidate 2 (found by 3 of 36 passes): The utility functions in `<bit>` are not meant to provide a full bitwise manipulation library, but fundamental operations, especially those that can be accelerated in hardware while still having reasonable software fallbacks.
candidate 3 (found by 2 of 36 passes): They are non-trivial to implement efficiently in software.
candidate 4 (found by 1 of 36 passes): They are common and useful operations.

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

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/0  -> 0.33
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     2/2/2  -> 2.00
  [9] 7. Possible implementation                   1/1/1  -> 1.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The use of `compress` and `expand` is consistent with the mask-based permutations for `std::simd` proposed in [P2664R6].
candidate 2 (found by 3 of 36 passes): [Warren1] presents algorithms which are the basis for [Schultke1].
candidate 3 (found by 2 of 36 passes): Such an intrinsic has been requested from GCC users a number of times in [GNU1].
candidate 4 (found by 1 of 36 passes): The C++ bit manipulation library in `<bit>` is an invaluable abstraction from hardware operations.

## vehicle - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 36 passes): Bullets 2. and 3. suggest that `bit_compress` and `bit_expand` benefit from being implemented directly in the compiler via intrinsic, even if hardware does not directly implement these operations.

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Proposed features                         0/0/0  -> 0.00
  [6] 4. Motivation and scope                      0/1/0  -> 0.33
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Design considerations                     0/0/0  -> 0.00
  [9] 7. Possible implementation                   0/0/0  -> 0.00
  [10] 8. Proposed wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): A GitHub code search for `/(_pdep_u|_pext_u)(32|64)/ AND language:c++` reveals ~1300 files which use the intrinsic wrappers for the x86 instructions.

## insufficiency - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 36 passes): ISO C++ does not offer a mechanism through which all of this information can be utilized. Namely, it is not possible to change strategy based on information that only becomes available during optimization passes.

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
candidate 2 (found by 3 of 36 passes): All proposed functions have been implemented in [Schultke1]. This reference implementation is compatible with all three major compilers, and leverages hardware support from ARM and x86_64 where possible.

-->
