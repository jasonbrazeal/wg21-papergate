Verdict: Weak (3/14)

The paper offers only a thin account of why its change belongs in the standard, resting most of its case on a single design preference and leaving the broader rationale largely implicit. The strongest material concerns the motivation for changing `address`’s return type, but even that is asserted rather than demonstrated, and the surrounding case for standardization is largely absent.

- The paper at least gestures toward a concrete problem by citing the NB comment’s concern that `address` is “maybe too convenient” for unsafe direct access.
- Its discussion of prior art is limited to noting that `void*`-to-`T*` casts are now usable in constant evaluation, without showing how that resolves the design question or what alternatives were seriously weighed.
- The paper does not establish who would be affected by the change, how it would interoperate with existing code or other proposals, or why a library-level solution would be inadequate.
- It offers no implementation experience or evidence from practice to support standardizing the proposed behavior.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 3.00   accumulate 2.67   max 5.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.50 / 3.00   (all 3 samples: 2.67)
headings: h2 6
on threshold: motivation, prior_art
splits: vehicle[4] 1/1/2
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): However, it is generally unsafe to access the object at `address` directly, and so, the NB comment argues that `address` is maybe too convenient.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): cast from `void*` to `T*` are now supported in constant evaluation. This feature was added by [P2738R1](https://wg21.link/P2738R1) [2] in C++26.
candidate 2 (found by 1 of 21 passes): However, of the options explored at the time, none seemed compelling.

## vehicle - grade 0.67 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   1/1/2  -> 1.33
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Therefore, we think using `void*` as the return type of `address` addresses the NB comment in a satisfactory manner.
candidate 2 (found by 1 of 21 passes): However, it is generally unsafe to access the object at `address` directly, and so, the NB comment argues that `address` is maybe too convenient.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
