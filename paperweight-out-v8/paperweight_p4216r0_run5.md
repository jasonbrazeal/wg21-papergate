Verdict: Adequate (4/14)

The paper gives a partial account of why `span` comparisons would be useful, chiefly by pointing to comparable standard library types and the history of their removal, but it leaves the standardization case largely unbuilt in several important respects. The strongest material concerns motivation and precedent, while the discussion of affected users, interoperability, implementation experience, and why a library solution is insufficient is essentially absent.

- The paper establishes that comparisons for `span` would mirror existing behavior in `string_view`, `optional<T&>`, and `reference_wrapper`, and that such comparisons were originally adopted before being removed.
- The paper claims a standard-library solution is warranted mainly by asserting there is no point in omitting comparisons, but it does not develop that claim into a standardization argument.
- The paper does not identify who would be affected by the change or how it would coordinate with existing practice and related proposals.
- The paper offers no implementation experience and no explanation of why a library-provided comparison facility would not satisfy the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 3 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 3.00   accumulate 4.67   max 5.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 4.50 / 3.50 / 3.50   (all 3 samples: 3.83)
headings: h2 8
on threshold: motivation, prior_art
splits: motivation[5] 2/1/1  vehicle[6] 2/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/1/1  -> 1.33
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): NOTE: all of these do „deep value comparisons“
candidate 2 (found by 3 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`. All but the first of these support comparisons (both equality and three-way).
candidate 3 (found by 1 of 27 passes): The concerns of P1085 can be summarised as: `span` … has „reference semantics“, therefore it’s value can change transparently. … does not enforce deep const … rebinds on assignment.
candidate 4 (found by 1 of 27 passes): The concerns of P1085 can be summarised as: `span` … has „reference semantics“, therefore it’s value can change transparently.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes comparison operators for `span`, mirroring the design of `string_view`, `optional<T&>`, and `reference_wrapper`.
candidate 2 (found by 3 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`.
candidate 3 (found by 2 of 27 passes): The original proposal for `span` [([P0122]) included comparisons, modelling deep value comparisons. It was adopted in Jacksonville in March 2018. In October of the same year they [were removed in the San Diego meeting by [P1085].](http://wg21.link/p1085)
candidate 4 (found by 1 of 27 passes): The original proposal for `span` [([P0122]) included comparisons, modelling deep value](http://wg21.link/P0122) comparisons. It was adopted in Jacksonville in March 2018. In October of the same year they [were removed in the San Diego meeting by [P1085].](http://wg21.link/p1085)

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 2/1/1  -> 1.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): We therefore see no point in not providing comparisons for `span`.
candidate 2 (found by 1 of 27 passes): The original proposal for `span` [([P0122]) included comparisons, modelling deep value comparisons. It was adopted in Jacksonville in March 2018. In October of the same year they [were removed in the San Diego meeting by [P1085].](http://wg21.link/p1085)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

-->
