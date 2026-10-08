Verdict: Weak (2/14)

The paper offers only a narrow historical argument about naming consistency, and it does not develop that argument into a case for standardization. The support is thinnest around the questions that would matter most to a committee: who is affected, why a library solution is insufficient, and whether there is any implementation experience.

- The strongest support is the paper’s observation that the interface for `std::execution::affine_on` changed from binary to unary, which at least gestures at a rationale for renaming.
- The paper claims some prior art and alternatives by recounting the namespace’s naming history and a remark made during LEWG discussion, but it does not establish that these amount to a standardization need.
- The paper does not establish who is affected by the current name or what practical problem the rename would solve for users.
- The most glaring omission is the absence of any argument for why the standard must act, as opposed to leaving the name alone or addressing the concern through non-standard means.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.00/14)

Provisionally addressed: 2 of 7. Provisional points: 2.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.33

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 2.00 / 2.00 / 2.00   (all 3 samples: 2.00)
headings: h2 6
on threshold: none
splits: motivation[3] 1/0/1  prior_art[3] 1/2/1
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/0/1  -> 0.67
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Rendering `std::execution::affine_on` unary [2] destroys the rationale for including “on” in the name thereof.
candidate 2 (found by 2 of 21 passes): changing the shape of the interface warranted changing the name of the algorithm

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

## prior_art - grade 1.17 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/2/1  -> 1.33
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Before the addition of `std::execution::task` [1] the `std::execution` namespace contained three entities whose name was intended to contain the ordinary English word “on:”
candidate 2 (found by 1 of 21 passes): During LEWG discussion of the above (2026-03-24 in Croydon) it was mentioned (by the author of this paper) that changing the shape of the interface warranted changing the name of the algorithm
candidate 3 (found by 1 of 21 passes): Later [2] it was redesigned to be unary accepting only a sender (the first bullet from above).
candidate 4 (found by 1 of 21 passes): When `std::execution::affine_on` was added [1] it was a binary-invocable object accepting two parameters... Later [2] it was redesigned to be unary accepting only a sender

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
