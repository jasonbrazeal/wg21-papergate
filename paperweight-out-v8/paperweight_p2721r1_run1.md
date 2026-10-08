Verdict: Weak to Adequate (3/14)

The paper offers only a narrow foundation for its standardization case: it establishes that `std::function` has known design problems and has been superseded, but most of the surrounding argument rests on assertion rather than demonstrated need. The thinnest areas are the absence of any implementation experience and the lack of an explanation for why a library-level solution would not suffice.

- The strongest support is the established point that `std::function` has unresolvable API design issues and has been superseded by `copyable_function`.
- The paper claims, but does not establish, that deprecation would unify the standard library and give users clear guidance.
- The paper does not establish why standardization is necessary when a library-level migration or guidance document might address the concern.
- The most glaring omission is the complete lack of implementation experience for the proposed deprecation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 5 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 4.67   accumulate 3.33   max 5.67

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 0.50  vehicle 0.50  coordination 0.50  insufficiency 0.00  implementation 0.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 4.00 / 3.00   (all 3 samples: 3.33)
headings: h2 7
on threshold: motivation
splits: audience[5] 0/2/0
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
candidate 2 (found by 3 of 24 passes): there were serious inconsistencies between the *polymorphic function wrappers* of the standard library.

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

## prior_art - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 24 passes): has been superseded by `copyable_function`
candidate 2 (found by 1 of 24 passes): it has unresolvable API design issues and has been superseded by `copyable_function`.

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

## coordination - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
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
