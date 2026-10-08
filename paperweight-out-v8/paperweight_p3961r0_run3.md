Verdict: Adequate (5/14)

The paper gives a partial account of why the change matters and what alternatives were considered, but it leaves several core justifications for standardization essentially unaddressed. The strongest material concerns motivation and prior discussion, while the case for affected users, the need for a standard rather than a library solution, and interoperability is largely absent.

- The paper establishes a clear motivation by tying the change to a specific codegen concern and a currently ill-formed assignment case.
- It engages meaningfully with prior art, including the older `reference_wrapper` discussion and the visible-behavior implications of LWG 4264.
- It offers implementation experience through a linked implementation of the proposed direction.
- The most glaring omission is any account of who is affected or why the desired behavior cannot be achieved through a library facility outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.00   accumulate 5.67   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h3 7   <- NOT h2, check the unit list
on threshold: motivation, prior_art, implementation
splits: motivation[4] 1/0/1  prior_art[3] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Discussion                                   1/0/1  -> 0.67
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): RU-220 calls for allowing skipping indirections when constructing `function_ref` to improve codegen.
candidate 2 (found by 3 of 24 passes): Without this paper, `r1 = r2` doesn't compile.
candidate 3 (found by 2 of 24 passes): The users shouldn't expect `function_ref` to exhibit a "reference to reference" behavior.

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

## prior_art - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivation                                   1/1/0  -> 0.67
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): because unwrapping `reference_wrapper` is a discussed matter about 8 years ago, the author wants to see more evidence in real-world code to justify this change.
candidate 2 (found by 2 of 24 passes): The proposed change in LWG 4264<sup>[1]</sup> is not strictly an optimization because certain behaviors with and without the change are visible, therefore, need to be made unspecified.
candidate 3 (found by 2 of 24 passes): Replacing `auto` with `function_ref` CTAD, the assignment behaviors between `noexcept` and non-`noexcept` function objects should stay the same.
candidate 4 (found by 1 of 24 passes): This paper (P3961) suggests that, in addition to the change, a subset of the "optimized" cases should be mandated.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Implementation                               2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The paper has been implemented in [zhihaoy/nontype_functional@p3961r0](https://github.com/zhihaoy/nontype_functional/tree/p3961r0).

-->
