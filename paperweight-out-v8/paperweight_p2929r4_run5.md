Verdict: Weak to Adequate (3/14)

The paper gives a partial account of why the proposed facility would be useful and how it relates to existing practice, but it leaves most of the case for standardization unstated. The strongest material concerns motivation and naming, while the discussion of affected users, the need for a standard rather than a library, interoperability, and implementation experience is essentially absent.

- The paper establishes a concrete motivation by showing that interacting with intrinsics through smaller SIMD chunks becomes verbose and awkward.
- It grounds the design in prior art by aligning the proposed name and placement with existing `std::simd` operations and by noting the standard’s own recommendation about implementation-defined conversions.
- The most glaring omission is the lack of any discussion of who would use this facility, how widely the need arises, or what implementation experience supports it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 3.50 / 3.00   (all 3 samples: 3.17)
headings: h2 6
on threshold: motivation, prior_art
splits: motivation[6] 1/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                2/2/2  -> 2.00
  [6] 4. Description of simd::chunkedinvoke        1/2/1  -> 1.33
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Proposal to extend `std::simd` with a method of allowing a lambda to be invoked on smaller pieces of a SIMD value in order to make interaction with intrinsics easier.
candidate 2 (found by 2 of 21 passes): Being able to define a different size is useful for two reasons:
candidate 3 (found by 1 of 21 passes): make interaction with intrinsics easier
candidate 4 (found by 1 of 21 passes): This is now getting verbose, and it only handles `basic_vec` value inputs which are twice the size of a register value.

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
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                1/1/1  -> 1.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                1/1/1  -> 1.00
  [6] 4. Description of simd::chunkedinvoke        2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The function is named `chunked_invoke` and placed in `std::simd` to directly align with related established functions such as `chunk` and `cat`.
candidate 2 (found by 3 of 21 passes): The draft standard of `std::simd` recommends that provision is made for conversions to and from implementation defined types.
candidate 3 (found by 3 of 21 passes): In the first revision of this paper we proposed that the function which invokes a Callable with an explicit offset should be called with a `_indexed` suffix (e.g., `simd::chunked_invoke_indexed`).

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
