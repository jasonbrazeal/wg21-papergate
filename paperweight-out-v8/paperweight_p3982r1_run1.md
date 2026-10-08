Verdict: Adequate to Strong (8/14)

The paper offers solid support in a few areas, particularly implementation experience and the existence of prior art, but it leaves several important parts of its standardization case asserted rather than demonstrated. The thinnest support concerns why a library solution would be insufficient, which is not addressed at all.

- The paper’s strongest support is its implementation experience, with a patch series and detailed discussion showing the proposed wording changes have been worked through in libstdc++.
- The paper also establishes prior art and alternatives by showing how common languages use `first, last` rather than `offset, length`, and by explaining the proposed rename and reinterpretation of `strided_slice`.
- The case for who is affected is only claimed, since the paper asserts broad relevance and comparable performance but does not establish the scope or significance of the affected user population.
- The most glaring omission is the absence of any argument for why a library cannot provide the same functionality, leaving the need for standardization itself unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.00   accumulate 7.83   max 10.33

## SUMMARY
grades: motivation 1.50  audience 0.83  prior_art 1.50  vehicle 0.83  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.50 / 7.00 / 7.50   (all 3 samples: 7.50)
headings: h2 8
on threshold: motivation, audience, prior_art, coordination
splits: motivation[4] 2/0/0  audience[4] 2/2/1  vehicle[4] 1/0/1  coordination[5] 2/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/0/0  -> 0.67
  [5] 4. Ship vehicle, proposed polls, and revi... 2/2/2  -> 2.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): it gives `submdspan` a more ergonomic and familiar interface.
candidate 2 (found by 3 of 27 passes): This shows that even for programmers familar with the topic, such computations remain bug-prone.
candidate 3 (found by 1 of 27 passes): As mentioned before, the current *input span* specification does not give users a way to select a statically sized subset of elements with dynamic stride.

## audience - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/1  -> 1.67
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Results from a benchmark similar to one used above show no significant performance difference.
candidate 2 (found by 1 of 27 passes): We illustrate this by including benchmark results below.
candidate 3 (found by 1 of 27 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## prior_art - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes two changes: 1. Rename `strided_slice` to `extent_slice` and adjust the meaning of its `extent` member, to designate the desired number of elements in the range produced by `submdspan`.
candidate 2 (found by 3 of 27 passes): However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## vehicle - grade 0.83 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/0/1  -> 0.67
  [5] 4. Ship vehicle, proposed polls, and revi... 1/1/1  -> 1.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As this document explains, the current specification of `strided_slice` fails in both accounts.
candidate 2 (found by 2 of 27 passes): In contrast, with this paper's proposed changes, the members of `strided_slice` directly represent values used by `submdspan` creation.

## coordination - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 2/1/2  -> 1.67
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
