Verdict: Adequate (6/14)

The paper offers a narrow but concrete basis for standardization, centered on a genuine wording contradiction and some observed compiler divergence. Its support is strongest where it documents existing implementation behavior and connects the issue to a long-open core issue, but it leaves the affected audience, the need for a standard rather than another remedy, and interoperability consequences largely unstated.

- The clearest support comes from the demonstration that Clang and EDG follow the current specification while GCC and MSVC diverge, showing that the problematic construct is already being interpreted inconsistently.
- The paper also establishes that the issue has prior standing through CWG2042 and that the current wording can lead directly to undefined behavior despite a default non-throwing specification.
- The thinnest part of the case is the absence of any discussion of who is affected or why a standard change, rather than guidance or a non-normative fix, is the necessary response.
- Most glaringly, the paper does not establish that a library-level or implementation-level resolution would be insufficient, nor does it substantiate its interoperability claims beyond a single compiler test.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 5.00 / 6.00   (all 3 samples: 5.67)
headings: h2 9
on threshold: motivation, prior_art, implementation
splits: motivation[8] 1/0/0  coordination[4] 2/0/2
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    1/0/0  -> 0.33
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Throwing from an overloaded `delete` operator is undefined behavior, yet `delete` operators have a non-throwing exception specification by default, leading to a deterministic call to `terminate` before any undefined behavior can occur.
candidate 2 (found by 3 of 30 passes): Unfortunately, the destroying delete test reveals implementation divergence.
candidate 3 (found by 3 of 30 passes): As the only effect of adding a potentially-throwing exception specification to a deallocation function is to allow undefined behavior, we recommend that construct should be disallowed.
candidate 4 (found by 2 of 30 passes): That issue raises concerns that the current wording is contradictory so needs to be addressed somehow

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification. MSVC triggers the `static_assert` because it checks the destructor in this case, even though it should not.
candidate 2 (found by 3 of 30 passes): This risks expose the gcc bug of not supplying the implicitly nonthrowing exception to any implementation of a destroying delete function
candidate 3 (found by 3 of 30 passes): This paper would resolve [CWG2042] filed in November 2014.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.67 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/0/2  -> 1.33
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Testing against the current trunk for gcc, we see the `static_assert` fires because it does not implement the implicitly non-throwing exception specification for destroying delete.
candidate 2 (found by 1 of 30 passes): Unfortunately, the destroying delete test reveals implementation divergence.

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.

-->
