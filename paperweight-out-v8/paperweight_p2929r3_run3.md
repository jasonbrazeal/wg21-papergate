Verdict: Weak (2/14)

The paper offers only a narrow, aspirational case for its own standardization, centered on a plausible motivation and a naming alignment with existing `std::simd` facilities. Most of the burden of proof is simply absent, leaving the proposal without evidence about its audience, feasibility, or necessity in the standard.

- The strongest support is the stated rationale that target-specific intrinsics will inevitably require a way to break SIMD values into smaller pieces and reassemble them.
- The paper gestures toward prior art by linking the proposed `chunked_invoke` to existing `chunk` and `cat` functions, but does not develop that comparison into a real alternatives analysis.
- The paper does not identify who would use this facility or what codebases or platforms would benefit.
- The most glaring omission is the complete lack of implementation experience, library-only feasibility, or coordination with existing practice, leaving no evidence that standardization is warranted.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.00   accumulate 2.83   max 2.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.00 / 2.50 / 2.50   (all 3 samples: 2.33)
headings: h2 6
on threshold: motivation
splits: motivation[3] 1/2/2
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Motivation                                1/2/2  -> 1.67
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                0/0/0  -> 0.00
  [6] 4. Description of simd::chunkedinvoke        1/1/1  -> 1.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Proposal to extend `std::simd` with a method of allowing a lambda to be invoked on smaller pieces of a SIMD value in order to make interaction with intrinsics easier.
candidate 2 (found by 3 of 21 passes): Being able to define a different size is useful for two reasons:
candidate 3 (found by 2 of 21 passes): However, it is inevitable that the programmer will want to make some use of target-specific intrinsics in order to unlock some of the more unusual features of those specific platforms.
candidate 4 (found by 1 of 21 passes): This requires that the programmer is able to allow a `basic_vec` value to be used in a call to a target intrinsic, and that the result of the intrinsic call can be used to generate a new `basic_vec` value.

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

## prior_art - grade 1.00 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                1/1/1  -> 1.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                1/1/1  -> 1.00
  [6] 4. Description of simd::chunkedinvoke        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The function is named `chunked_invoke` and placed in `std::simd` to directly align with related established functions such as `chunk` and `cat`.
candidate 2 (found by 3 of 21 passes): The draft standard of `std::simd` recommends that provision is made for conversions to and from implementation defined types.

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

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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
