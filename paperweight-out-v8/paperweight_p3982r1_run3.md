Verdict: Strong (8/14)

The paper offers solid support in a few areas, particularly in explaining the ergonomic problem with the current `strided_slice` interface and in showing implementation experience through a libstdc++ patch series. However, the case for standardization is much thinner when it comes to showing who is affected, why the standard is the right venue, and how the change coordinates with existing components, and the paper does not establish why a library solution would be insufficient.

- The strongest support is the implementation experience, with a concrete patch series and linked benchmark details demonstrating that the proposed wording changes are workable in practice.
- The paper also clearly establishes the motivation and prior art by contrasting the current `offset, length` approach with the `first, last` convention used in common languages and by explaining the ergonomic and layout limitations of the current design.
- The weakest part of the case is the absence of any argument for why a library-only solution cannot provide the proposed interface, leaving the need for a standard change largely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 8.33   max 11.00

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.50  vehicle 0.67  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.00 / 7.50 / 8.00   (all 3 samples: 7.67)
headings: h2 8
on threshold: motivation, audience, prior_art, coordination
splits: motivation[4] 0/0/2  prior_art[2] 1/1/0  vehicle[4] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/2  -> 0.67
  [5] 4. Ship vehicle, proposed polls, and revi... 2/2/2  -> 2.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): it gives `submdspan` a more ergonomic and familiar interface.
candidate 2 (found by 3 of 27 passes): It incurs the cost of division, and it cannot be used for non-unique layouts.
candidate 3 (found by 1 of 27 passes): As mentioned before, the current *input span* specification does not give users a way to select a statically sized subset of elements with dynamic stride.

## audience - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Results from a benchmark similar to one used above show no significant performance difference.
candidate 2 (found by 1 of 27 passes): We illustrate this by including benchmark results below.

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/0  -> 0.67
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 1/1/1  -> 1.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This paper proposes two changes: 1. Rename `strided_slice` to `extent_slice` and adjust the meaning of its `extent` member, to designate the desired number of elements in the range produced by `submdspan`.
candidate 2 (found by 2 of 27 passes): However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 3 (found by 2 of 27 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard.
candidate 4 (found by 1 of 27 passes): Surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## vehicle - grade 0.67 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/0/0  -> 0.33
  [5] 4. Ship vehicle, proposed polls, and revi... 1/1/1  -> 1.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As this document explains, the current specification of `strided_slice` fails in both accounts.
candidate 2 (found by 1 of 27 passes): In contrast, with this paper's proposed changes, the members of `strided_slice` directly represent values used by `submdspan` creation.

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 2/2/2  -> 2.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               2/2/2  -> 2.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): More details about above results may be found [here](https://gcc.gnu.org/pipermail/libstdc++/2026-January/065129.html).
candidate 2 (found by 3 of 27 passes): Here is a [patch series](https://gcc.gnu.org/pipermail/libstdc++/2026-March/065843.html) implementing the proposed wording changes to `submdspan` in libstdc++.

-->
