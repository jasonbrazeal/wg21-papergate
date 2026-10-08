Verdict: Adequate to Strong (7/14)

The paper offers some useful evidence of implementation work, but its broader case for standardization rests mostly on assertions rather than demonstrated need. The thinnest support is in the areas that would justify changing an already-shipped interface: the affected audience, the alternatives, and the reason this must be done in the standard rather than in a library.

- The strongest support is the implementation experience, with a patch series and benchmark details showing the proposed wording changes are workable in practice.
- The paper claims the change matters because it makes the interface more ergonomic and avoids bug-prone computations, but it does not establish who is actually affected or how widespread the problem is.
- The discussion of prior art and alternatives is asserted rather than shown, leaving unclear why the proposed renaming and semantic change is preferable to other possible designs.
- The most glaring omission is the absence of any case for why a library solution would not suffice, which leaves the standardization need itself unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 7.17   max 9.67

## SUMMARY
grades: motivation 1.17  audience 1.00  prior_art 1.33  vehicle 0.33  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.00 / 7.50 / 6.00   (all 3 samples: 6.83)
headings: h2 8
on threshold: audience, prior_art, coordination
splits: motivation[5] 2/2/0  prior_art[2] 0/1/1  prior_art[5] 0/1/1  vehicle[5] 1/1/0
        coordination[4] 0/1/0  coordination[5] 2/1/2
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 2/2/0  -> 1.33
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): it gives `submdspan` a more ergonomic and familiar interface.
candidate 2 (found by 2 of 27 passes): This shows that even for programmers familar with the topic, such computations remain bug-prone.
candidate 3 (found by 1 of 27 passes): This change would be breaking after C++26 is shipped.

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
candidate 1 (found by 2 of 27 passes): Surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 2 (found by 1 of 27 passes): Results from a benchmark similar to one used above show no significant performance difference.

## prior_art - grade 1.33 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/1/1  -> 0.67
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 0/1/1  -> 0.67
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This paper proposes two changes: 1. Rename `strided_slice` to `extent_slice` and adjust the meaning of its `extent` member, to designate the desired number of elements in the range produced by `submdspan`.
candidate 2 (found by 2 of 27 passes): However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 3 (found by 2 of 27 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard.
candidate 4 (found by 1 of 27 passes): One argument for using the *input span* as the value of `stride_slice::extent` was consistency with other programming languages' range slicing interfaces. However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## vehicle - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 1/1/0  -> 0.67
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): As this document explains, the current specification of `strided_slice` fails in both accounts.

## coordination - grade 1.00 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/1/0  -> 0.33
  [5] 4. Ship vehicle, proposed polls, and revi... 2/1/2  -> 1.67
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.
candidate 2 (found by 1 of 27 passes): Based on the inituition built from other languages, `submdspan(md, strided_slice{2, 5, 1})`, should select elements `[2, 5)`, instead of `[2, 7)` as currently specified.

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
