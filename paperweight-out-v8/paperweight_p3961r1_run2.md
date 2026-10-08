Verdict: Adequate (5/14)

The paper offers a narrow but real basis for its standardization, chiefly through a concrete implementation and a recognized connection to existing library issues, but it leaves several essential parts of the case largely unargued. The support is thinnest around the actual need for a standard change rather than a library solution, and around who would be affected or how the change would interoperate with existing practice.

- The strongest support is the existence of an implementation and a compiler-visible example showing behavior that the paper ties to its proposed change.
- The paper also grounds itself in prior discussion and an existing LWG issue, which gives the proposal some historical and procedural context.
- The most glaring omission is the absence of any established argument for why this cannot be handled by a library or why standardization is required at all.
- The paper likewise does not establish who is affected or how the change would coordinate with existing codebases and library specifications.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h3 7   <- NOT h2, check the unit list
on threshold: motivation, prior_art, implementation
splits: implementation[4] 2/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): RU-220 calls for allowing skipping indirections when constructing `function_ref` to improve codegen.
candidate 2 (found by 3 of 24 passes): Without this paper, `r1 = r2` doesn't compile.
candidate 3 (found by 3 of 24 passes): The users shouldn't expect `function_ref` to exhibit a "reference to reference" behavior.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): However, because unwrapping `reference_wrapper` is a discussed matter about 8 years ago, the author wants to see more evidence in real-world code to justify this change.
candidate 2 (found by 2 of 24 passes): This paper (P3961) suggests that, in addition to the change, a subset of the "optimized" cases should be mandated.
candidate 3 (found by 2 of 24 passes): Without this paper, `r1 = r2` doesn't compile.
candidate 4 (found by 1 of 24 passes): The proposed change in LWG 4264<sup>[1]</sup> is not strictly an optimization because certain behaviors with and without the change are visible, therefore, need to be made unspecified.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Discussion                                   2/0/0  -> 0.67
  [5] Implementation                               2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The paper has been implemented in [zhihaoy/nontype_functional@p3961r1](https://github.com/zhihaoy/nontype_functional/tree/p3961r1).
candidate 2 (found by 1 of 24 passes): Note that *without* unwrapping `reference_wrapper`, a user can call a non-const member `operator()` from a `function_ref` with a const signature: [eP11Kh6es](https://godbolt.org/z/eP11Kh6es)Compiler Explorer.

-->
