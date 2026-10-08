Verdict: Weak to Adequate (3/14)

The paper offers a narrow but genuine foundation for its case: it establishes that `span` is an outlier among comparable non-owning reference types, and it points to the earlier inclusion and later removal of comparisons as relevant history. Beyond that, however, the support is thin, with most of the burden of justification left as assertion rather than demonstrated need.

- The strongest support is the established inconsistency between `span` and similar standard library types such as `string_view`, `reference_wrapper`, and `optional<T&>`.
- The paper claims precedent in the original `span` proposal and in the design of other comparison operators, but it does not establish that these amount to a considered alternative or prior art sufficient for standardization.
- The paper asserts that there is no point in omitting comparisons, but it does not establish why this belongs in the standard rather than in a library or user code.
- The most glaring omissions are the complete absence of discussion of who is affected, how the feature would interoperate with existing code or other proposals, and any implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.00   accumulate 4.17   max 4.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.33)
headings: h2 8
on threshold: motivation
splits: motivation[3] 0/0/1  prior_art[3] 0/0/1  prior_art[6] 2/0/2  vehicle[6] 1/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/1  -> 0.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`. All but the first of these support comparisons (both equality and three-way).
candidate 2 (found by 2 of 27 passes): All these concerns are real. What P1085 doesn’t acknowledge is that all but the second concern equally apply to `string_view`, neither does it make a convincing case for why these concerns are in any way alleviated by removing comparisons!
candidate 3 (found by 1 of 27 passes): //NOTE: all of these do „deep value comparisons“
candidate 4 (found by 1 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`. All but the first of these support comparisons (both equality and three-way). This paper aims to fix this inconsistency by adding comparisons to `span`.

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

## prior_art - grade 1.17 (fired in 4 of 9 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   0/0/1  -> 0.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 2/0/2  -> 1.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes comparison operators for `span`, mirroring the design of `string_view`, `optional<T&>`, and `reference_wrapper`.
candidate 2 (found by 3 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`.
candidate 3 (found by 1 of 27 passes): lexicographical_compare_three_way( p0.begin(), p0.end(), p1.begin(), p1.end(), synth-three-way //but that’s exposition-only 😬 );
candidate 4 (found by 1 of 27 passes): The original proposal for `span` [([P0122]) included comparisons, modelling deep value](http://wg21.link/P0122) comparisons. It was adopted in Jacksonville in March 2018. In October of the same year they [were removed in the San Diego meeting by [P1085].](http://wg21.link/p1085)

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 1/2/1  -> 1.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): We therefore see no point in not providing comparisons for `span`.
candidate 2 (found by 1 of 27 passes): All these concerns are real. What P1085 doesn’t acknowledge is that all but the second concern equally apply to `string_view`, neither does it make a convincing case for why these concerns are in any way alleviated by removing comparisons!

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
