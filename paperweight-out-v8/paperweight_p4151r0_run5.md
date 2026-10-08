Verdict: Weak (2/14)

The paper offers only a narrow, name-focused rationale for its change, and it does not build a broader case for why this belongs in the standard. The support is thinnest around the practical consequences of the rename and around any evidence that the change has been tried or coordinated with the surrounding ecosystem.

- The strongest support is the internal consistency argument that a unary interface no longer matches the “on” suffix in `affine_on`.
- The paper gestures at prior discussion and the history of “on” names, but it does not establish that these amount to meaningful prior art or considered alternatives.
- It never identifies who would be affected by the rename or what the real-world cost and benefit would be.
- Most glaringly, the paper offers no implementation experience, no interoperability analysis, and no reason a library-level migration or deprecation approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.67/14)

Provisionally addressed: 2 of 7. Provisional points: 1.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.67   corroborated 2.00   accumulate 1.83   max 2.00

## SUMMARY
grades: motivation 0.67  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 1.50 / 2.00 / 1.50   (all 3 samples: 1.67)
headings: h2 6
on threshold: none
splits: motivation[3] 0/1/0  motivation[5] 0/1/0
## END SUMMARY

## motivation - grade 0.67 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/1/0  -> 0.33
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/1/0  -> 0.33
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.
candidate 2 (found by 1 of 21 passes): changing the shape of the interface warranted changing the name of the algorithm
candidate 3 (found by 1 of 21 passes): Remove “on” from the name of `std::execution::affine_on` as it no longer makes sense.

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

## prior_art - grade 1.00 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): During LEWG discussion of the above (2026-03-24 in Croydon) it was mentioned (by the author of this paper) that changing the shape of the interface warranted changing the name of the algorithm
candidate 2 (found by 2 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.
candidate 3 (found by 1 of 21 passes): When `std::execution::affine_on` was added [1] it was a binary-invocable object accepting two parameters, respectively:
candidate 4 (found by 1 of 21 passes): Before the addition of `std::execution::task` [1] the `std::execution` namespace contained three entities whose name was intended to contain the ordinary English word “on:”

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
