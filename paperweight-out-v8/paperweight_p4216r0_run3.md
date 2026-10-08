Verdict: Adequate (4/14)

The paper offers some grounding for its proposal by situating `span` comparisons among existing non-owning reference types and by citing the earlier inclusion and later removal of comparisons, but it leaves several essential parts of the standardization case unaddressed. The thinnest areas are the absence of any demonstrated affected audience, implementation experience, or argument for why this cannot be provided as a library.

- The strongest support is the established prior art, including the original `span` proposal with comparisons and the parallel design of `string_view`, `optional<T&>`, and `reference_wrapper`.
- The paper also establishes why the issue matters by identifying a real inconsistency among standard non-owning reference types.
- The most glaring omission is the lack of any implementation experience or evidence about who is affected by the absence of `span` comparisons.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 3 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 4.00   accumulate 4.50   max 5.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.50  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.00 / 3.50 / 4.00   (all 3 samples: 3.83)
headings: h2 8
on threshold: prior_art
splits: motivation[2] 1/0/0  motivation[5] 2/1/2  prior_art[3] 1/0/0
## END SUMMARY

## motivation - grade 1.83 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Tony Table                                   1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/1/2  -> 1.67
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`. All but the first of these support comparisons (both equality and three-way).
candidate 2 (found by 2 of 27 passes): NOTE: all of these do „deep value comparisons“
candidate 3 (found by 2 of 27 passes): All these concerns are real. What P1085 doesn’t acknowledge is that all but the second concern equally apply to `string_view`, neither does it make a convincing case for why these concerns are in any way alleviated by removing comparisons!
candidate 4 (found by 1 of 27 passes): This paper proposes comparison operators for `span`, mirroring the design of `string_view`, `optional<T&>`, and `reference_wrapper`.

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

## prior_art - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   1/0/0  -> 0.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes comparison operators for `span`, mirroring the design of `string_view`, `optional<T&>`, and `reference_wrapper`.
candidate 2 (found by 3 of 27 passes): The standard library has several types that represent non-owning references to data: `span`, `string_view`, `reference_wrapper`, `optional<T&>`.
candidate 3 (found by 2 of 27 passes): The original proposal for `span` [([P0122]) included comparisons, modelling deep value comparisons. It was adopted in Jacksonville in March 2018. In October of the same year they were removed in the San Diego meeting by [P1085].
candidate 4 (found by 1 of 27 passes): lexicographical_compare_three_way( p0.begin(), p0.end(), p1.begin(), p1.end(), synth-three-way //but that’s exposition-only 😬 );

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): We therefore see no point in not providing comparisons for `span`.

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
