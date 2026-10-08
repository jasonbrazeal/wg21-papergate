Verdict: Weak (2/14)

The paper offers only a narrow, name-focused argument for its standardization, and that argument rests on claims attributed to discussion rather than on demonstrated need. The thinnest support is in the areas that would show a real constituency, a standards-shaped problem, or a reason the work cannot live outside the standard.

- The strongest support is the assertion that a unary `affine_on` makes the existing “on” suffix misleading, which at least gestures at a rationale tied to interface shape.
- The paper claims some prior discussion in LEWG about renaming when the interface changes, but it does not establish that this discussion represents broader prior art or a considered alternative.
- The paper does not identify who is affected by the current name or by the proposed change.
- Most glaringly, it offers no case for why the standard should address this, why a library-level or editorial remedy would not suffice, or what implementation experience supports the change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.00/14)

Provisionally addressed: 2 of 7. Provisional points: 2.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.00   corroborated 2.00   accumulate 2.17   max 2.33

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 2.00 / 2.00 / 2.00   (all 3 samples: 2.00)
headings: h2 6
on threshold: none
splits: motivation[3] 0/1/1  prior_art[4] 2/1/1  prior_art[6] 0/1/0
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/1/1  -> 0.67
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.
candidate 2 (found by 2 of 21 passes): it was mentioned (by the author of this paper) that changing the shape of the interface warranted changing the name of the algorithm

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/1/1  -> 1.33
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/1/0  -> 0.33
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): During LEWG discussion of the above (2026-03-24 in Croydon) it was mentioned (by the author of this paper) that changing the shape of the interface warranted changing the name of the algorithm
candidate 2 (found by 3 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.
candidate 3 (found by 1 of 21 passes): An exact diff is difficult/impossible to provide while P3941 [2] is in flight.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
