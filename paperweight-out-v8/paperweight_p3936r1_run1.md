Verdict: Weak (2/14)

The paper offers only a thin, mostly asserted case for its own standardization. The strongest material appears in the discussion of why the proposed change matters and why the standard is the right venue, but even those points are stated rather than demonstrated. The remaining categories—affected users, prior art, coordination, library feasibility, and implementation experience—are essentially unaddressed.

- The paper at least gestures toward the safety concern that motivates the change, though it does not establish the significance of that concern.
- The claim that standardization is the appropriate response rests on an assertion that the proposed return type addresses the comment satisfactorily, without supporting argument.
- The paper does not identify who would be affected by the change or what the practical consequences would be.
- Most notably, it offers no implementation experience, no interoperability analysis, and no explanation of why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.67   accumulate 2.33   max 4.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.00 / 2.50   (all 3 samples: 2.33)
headings: h2 6
on threshold: motivation, prior_art
splits: vehicle[4] 1/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 2 of 21 passes): However, of the options explored at the time, none seemed compelling.
candidate 2 (found by 1 of 21 passes): cast from `void*` to `T*` are now supported in constant evaluation. This feature was added by [P2738R1](https://wg21.link/P2738R1) [2] in C++26.

## vehicle - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   1/0/1  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Therefore, we think using `void*` as the return type of `address` addresses the NB comment in a satisfactory manner.

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
