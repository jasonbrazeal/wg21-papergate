Verdict: Weak to Adequate (4/14)

The paper offers a narrow but real basis for its central claim that `std::function` has been superseded, but it does not build out the broader case that standardization action is warranted. The support is thinnest where the paper relies on assertion rather than evidence: affected users, alternatives, and the need for a standard rather than a library-level remedy are all left largely unsubstantiated.

- The strongest support is the established point that `std::function` has unresolvable API design issues and has been superseded by `copyable_function`.
- The paper claims a poll and a desire for unified standard library design, but does not establish who is actually affected or how widespread the problem is.
- The case for why deprecation requires standardization, rather than guidance or a library-level migration, is asserted but not demonstrated.
- The most glaring omission is the complete absence of implementation experience or any evidence that a library-only approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 5 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 4.00   accumulate 3.67   max 5.33

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 1.17  vehicle 0.50  coordination 0.17  insufficiency 0.00  implementation 0.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.50 / 5.00 / 2.50   (all 3 samples: 3.67)
headings: h2 7
on threshold: motivation
splits: audience[5] 0/2/0  prior_art[5] 2/2/0  coordination[5] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): it has unresolvable API design issues and has been superseded by `copyable_function`.
candidate 2 (found by 3 of 24 passes): Deprecating `function` would lead to a more unified standard library design and would send a clear guidance to users which types to use in new codes.

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/2/0  -> 0.67
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The following two polls were taken: **Poll:** We are interested in deprecating std::function at some future point. | SF | F | N | A | SA | | 10 | 5 | 3 | 2 | 2 |

## prior_art - grade 1.17 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/0  -> 1.33
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): As `function` was incompatible (and could not be made compatible) with *non-copyable* functors, [[P0288] introduced](https://wg21.link/P0288) `move_only_function`.
candidate 2 (found by 1 of 24 passes): has been superseded by `copyable_function`.
candidate 3 (found by 1 of 24 passes): it has unresolvable API design issues and has been superseded by `copyable_function`.
candidate 4 (found by 1 of 24 passes): has been superseded by `copyable_function`

## vehicle - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Deprecating `function` would lead to a more unified standard library design and would send a clear guidance to users which types to use in new codes.

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/1/0  -> 0.33
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): Deprecating `function` would lead to a more unified standard library design and would send a clear guidance to users which types to use in new codes.

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

-->
