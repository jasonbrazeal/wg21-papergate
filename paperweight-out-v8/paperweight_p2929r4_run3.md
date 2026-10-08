Verdict: Weak (3/14)

The paper gives a partial account of its own standardization case, strongest when situating the proposed facility among existing `std::simd` conventions and prior naming choices, but thin or silent on most of the burden a proposal must carry. The most serious gaps concern who would be affected, why a library solution is insufficient, and whether there is any implementation experience behind the design.

- The clearest support comes from the paper’s alignment with established `std::simd` functions and its acknowledgment of earlier naming alternatives.
- The paper gestures at a shared abstraction for intrinsic call handling, but does not actually establish that this coordination problem is widespread or that standardization is the right remedy.
- The discussion of why the feature matters is asserted rather than demonstrated, leaving the motivating difficulty with large `basic_vec` values underdeveloped.
- The paper offers no evidence about affected users, implementation experience, or why the facility could not be provided as an ordinary library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.33   accumulate 3.33   max 3.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 0.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 2.50 / 3.00 / 3.00   (all 3 samples: 2.67)
headings: h2 6
on threshold: prior_art
splits: motivation[5] 0/2/0  prior_art[5] 0/1/1  coordination[5] 0/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/2/0  -> 0.67
  [6] 4. Description of simd::chunkedinvoke        1/1/1  -> 1.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Proposal to extend `std::simd` with a method of allowing a lambda to be invoked on smaller pieces of a SIMD value in order to make interaction with intrinsics easier.
candidate 2 (found by 3 of 21 passes): Being able to define a different size is useful for two reasons:
candidate 3 (found by 1 of 21 passes): Things become more tricky when dealing with `basic_vec` values which are larger than their implementation types.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/0/0  -> 0.00
  [6] 4. Description of simd::chunkedinvoke        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                1/1/1  -> 1.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/1/1  -> 0.67
  [6] 4. Description of simd::chunkedinvoke        2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The function is named `chunked_invoke` and placed in `std::simd` to directly align with related established functions such as `chunk` and `cat`.
candidate 2 (found by 3 of 21 passes): In the first revision of this paper we proposed that the function which invokes a Callable with an explicit offset should be called with a `_indexed` suffix (e.g., `simd::chunked_invoke_indexed`).
candidate 3 (found by 2 of 21 passes): The draft standard of `std::simd` recommends that provision is made for conversions to and from implementation defined types.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/0/0  -> 0.00
  [6] 4. Description of simd::chunkedinvoke        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/0/1  -> 0.33
  [6] 4. Description of simd::chunkedinvoke        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Rather than requiring every user to have to write their own intrinsic call handlers, we can abstract the general mechanism into something that is easily reused.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/0/0  -> 0.00
  [6] 4. Description of simd::chunkedinvoke        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/0/0  -> 0.00
  [6] 4. Description of simd::chunkedinvoke        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidates: (none validated)

-->
