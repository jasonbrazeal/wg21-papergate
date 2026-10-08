Verdict: Adequate (5/14)

The paper offers a solid rationale for the change and useful evidence that it can be implemented, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest areas concern who is actually affected, why the core language rather than a library solution is required, and how the proposal fits with existing or neighboring specifications.

- The strongest support comes from the concrete motivation and the demonstrated implementation experience.
- The discussion of prior art and alternatives is substantive, particularly in relating the behavior to existing `noexcept` function type rules and identifying related problems in `move_only_function`.
- The most glaring omission is the absence of any established audience or user impact, leaving the affected community unspecified.
- The paper also does not establish why standardization is necessary or why a library-only approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.00   accumulate 5.83   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h3 7   <- NOT h2, check the unit list
on threshold: motivation, prior_art, implementation
splits: motivation[4] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Discussion                                   1/1/0  -> 0.67
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
candidate 1 (found by 3 of 24 passes): This paper (P3961) suggests that, in addition to the change, a subset of the "optimized" cases should be mandated.
candidate 2 (found by 3 of 24 passes): Closely matching the behavior of `noexcept` function types in the core language
candidate 3 (found by 2 of 24 passes): Note that *without* unwrapping `reference_wrapper`, a user can call a non-const member `operator()` from a `function_ref` with a const signature: [eP11Kh6es](https://godbolt.org/z/eP11Kh6es)Compiler Explorer. `move_only_function` has the same problem.
candidate 4 (found by 1 of 24 passes): Although a pointer to non-const member function cannot store a value of a pointer to const member function in the core language, the interactions between the `noexcept` and non-`noexcept` could be generalized to cover `function_ref` with const and non-const signatures.

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
candidate 1 (found by 3 of 24 passes): The paper has been implemented in [zhihaoy/nontype_functional@p3961r1](https://github.com/zhihaoy/nontype_functional/tree/p3961r1).

-->
