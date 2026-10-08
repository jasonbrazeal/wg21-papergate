Verdict: Weak to Adequate (3/14)

The paper offers only a narrow basis for its own standardization: it situates the proposed facility alongside existing `std::simd` operations and shows some responsiveness to prior naming feedback, but it does not establish who would be affected, why a library solution is insufficient, or that the feature belongs in the standard rather than in user code. The thinnest support concerns the core justification for standardization itself, with no demonstrated implementation experience, interoperability analysis, or affected-user case.

- The strongest support is the alignment with established `std::simd` functions such as `chunk` and `cat`, which gives the proposal a plausible home within the existing interface.
- The paper also shows some prior-art awareness by noting the standard’s recommendation for conversions to implementation-defined types and by revising its earlier `_indexed` naming proposal.
- The most glaring omission is the absence of any argument for why this cannot be provided as an ordinary library facility outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 3.00   accumulate 3.33   max 3.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.50 / 3.00 / 2.50   (all 3 samples: 2.83)
headings: h2 6
on threshold: none
splits: motivation[5] 2/0/0  prior_art[3] 2/2/1
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Motivation                                0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Background                                2/0/0  -> 0.67
  [6] 4. Description of simd::chunkedinvoke        1/1/1  -> 1.00
  [7] 5. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Proposal to extend `std::simd` with a method of allowing a lambda to be invoked on smaller pieces of a SIMD value in order to make interaction with intrinsics easier.
candidate 2 (found by 3 of 21 passes): Being able to define a different size is useful for two reasons:
candidate 3 (found by 1 of 21 passes): This is now getting verbose, and it only handles `basic_vec` value inputs which are twice the size of a register value.

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

## prior_art - grade 1.83 (fired in 3 of 7 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Motivation                                2/2/1  -> 1.67
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
