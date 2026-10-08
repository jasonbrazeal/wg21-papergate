Verdict: Weak (3/14)

The paper offers only a thin, mostly asserted case for its own standardization, with the strongest material concentrated in its discussion of prior art and alternatives, while several foundational questions are left entirely unaddressed. The most conspicuous gaps concern who would be affected by the change and whether any implementation experience exists to validate the approach.

- The paper’s clearest support comes from its account of prior art, where it explains why earlier options such as mandating `uintptr_t` were rejected and why `void*` became viable after P2738R1.
- The rationale for why the standard must change rests mainly on the assertion that returning `void*` addresses the NB comment, but the paper does not demonstrate that the current behavior causes concrete problems for users.
- The paper does not identify any affected audience, leaving it unclear whose code or workflows would benefit from or be disrupted by the proposed change.
- The absence of any implementation experience is the most glaring omission, since the proposal offers no evidence that the suggested return type has been tried in practice or that it behaves as expected.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 3.33   accumulate 3.00   max 6.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.83  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 6
on threshold: motivation, prior_art, vehicle
splits: vehicle[4] 2/1/2  insufficiency[4] 0/1/0
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
candidate 1 (found by 1 of 21 passes): FR-030-310 proposes to mandate `uintptr_t`. However, EWG had no appetite to do it in the C++26 time frame (over concernns that there might exist architectures in which pointers can be larger than the largest integer type).
candidate 2 (found by 1 of 21 passes): But... as it turns out, `void*` is now a suitable option. Indeed cast from `void*` to `T*` are now supported in constant evaluation. This feature was added by [P2738R1](https://wg21.link/P2738R1) [2] in C++26.
candidate 3 (found by 1 of 21 passes): However, of the options explored at the time, none seemed compelling.

## vehicle - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   2/1/2  -> 1.67
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): However, it is generally unsafe to access the object at `address` directly, and so, the NB comment argues that `address` is maybe too convenient.
candidate 2 (found by 1 of 21 passes): Therefore, we think using `void*` as the return type of `address` addresses the NB comment in a satisfactory manner.
candidate 3 (found by 1 of 21 passes): The only downsize of using `void*` is then a slightly more complicated return type. However, that return type is really just copying the CV qualifiers, which is not exactly novel.

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

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Wording                                      0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): However, it is generally unsafe to access the object at `address` directly, and so, the NB comment argues that `address` is maybe too convenient.

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
