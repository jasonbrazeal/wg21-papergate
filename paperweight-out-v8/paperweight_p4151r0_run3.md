Verdict: Weak (2/14)

The paper offers only a narrow, name-focused rationale for its request, and much of that rests on assertions about the history and discussion of another proposal rather than on a demonstrated need for standardization. The support is thinnest around the basic questions of who would be affected, why a library solution would be insufficient, and whether there is any implementation experience to draw on.

- The strongest support is the paper’s observation that a unary `affine_on` no longer matches the “on” in its name, which at least gestures at a consistency problem.
- The paper also points to prior discussion and a redesign as context for why the interface change might warrant a name change.
- The most glaring omission is the absence of any account of who is affected by the current naming or how standardization would address that impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.00/14)

Provisionally addressed: 2 of 7. Provisional points: 2.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.00   corroborated 2.00   accumulate 2.17   max 3.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.00 / 2.00 / 2.00   (all 3 samples: 2.00)
headings: h2 6
on threshold: motivation
splits: prior_art[6] 0/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.

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

## prior_art - grade 1.00 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/1  -> 0.33
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.
candidate 2 (found by 2 of 21 passes): Later [2] it was redesigned to be unary accepting only a sender (the first bullet from above).
candidate 3 (found by 1 of 21 passes): During LEWG discussion of the above (2026-03-24 in Croydon) it was mentioned (by the author of this paper) that changing the shape of the interface warranted changing the name of the algorithm
candidate 4 (found by 1 of 21 passes): An exact diff is difficult/impossible to provide while P3941 [2] is in flight.

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
