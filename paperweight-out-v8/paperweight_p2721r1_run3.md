Verdict: Weak to Adequate (3/14)

The paper offers some support for standardizing its proposal, particularly in explaining why the issue matters, but much of the case remains asserted rather than demonstrated. The thinnest areas are coordination, implementation experience, and any argument for why a library solution would be insufficient.

- The paper clearly establishes that the proposal addresses a real design problem, citing unresolvable API issues and the existence of a replacement.
- The claim that users are affected rests on a single poll, but the paper does not connect that sentiment to concrete usage or migration burdens.
- The paper repeatedly asserts that `copyable_function` supersedes `function` and that deprecation would unify the library, but it does not establish alternatives or why standardization is necessary.
- The paper offers no evidence of implementation experience, coordination with other proposals, or why a library-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 3.67   accumulate 3.17   max 4.67

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 0.50  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.00 / 2.50 / 4.00   (all 3 samples: 3.17)
headings: h2 7
on threshold: motivation
splits: audience[5] 0/0/2  vehicle[3] 1/0/1
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
candidate 2 (found by 2 of 24 passes): Deprecating `function` would lead to a more unified standard library design and would send a clear guidance to users which types to use in new codes.
candidate 3 (found by 1 of 24 passes): there were serious inconsistencies between the *polymorphic function wrappers* of the standard library.

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/2  -> 0.67
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The following two polls were taken: **Poll:** We are interested in deprecating std::function at some future point. | SF | F | N | A | SA | | 10 | 5 | 3 | 2 | 2 |

## prior_art - grade 0.50 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): has been superseded by `copyable_function`.
candidate 2 (found by 1 of 24 passes): has been superseded by `copyable_function`

## vehicle - grade 0.83 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Deprecating function in C++29                0/0/0  -> 0.00
  [3] Abstract                                     1/0/1  -> 0.67
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Impact on the Standard                       0/0/0  -> 0.00
  [7] Proposed Wording                             0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Deprecating `function` would lead to a more unified standard library design and would send a clear guidance to users which types to use in new codes.
candidate 2 (found by 2 of 24 passes): deprecating `function` (and associated entities) as it has unresolvable API design issues and has been superseded by `copyable_function`.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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
