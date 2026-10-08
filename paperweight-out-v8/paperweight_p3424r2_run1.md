Verdict: Adequate (5/14)

The paper offers only a narrow foundation for its standardization case: it establishes that the current wording around throwing `delete` operators is contradictory and worth resolving, but it does little to show who is affected, why the standard is the right venue, or why a library-level solution would not suffice. The supporting evidence is thinnest where the paper relies on implementation observations that are themselves marked as unestablished or contingent on a compiler bug being fixed.

- The strongest support is the established point that the existing specification is contradictory and therefore needs some form of corrective action.
- The paper claims some implementation divergence and prior discussion, but does not establish those claims as reliable evidence for standardization.
- The paper does not establish who is affected by the problem or why the standard is the necessary place to address it.
- The most glaring omission is the absence of any established case for implementation experience, coordination, or why a library solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 4 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.00   accumulate 5.50   max 5.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 1.33
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 4.00 / 3.50 / 6.00   (all 3 samples: 4.50)
headings: h2 9
on threshold: motivation, prior_art
splits: motivation[8] 1/1/0  prior_art[4] 2/1/2  coordination[4] 0/0/2  implementation[4] 1/1/2
        implementation[5] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    1/1/0  -> 0.67
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Throwing from an overloaded `delete` operator is undefined behavior, yet `delete` operators have a non-throwing exception specification by default, leading to a deterministic call to `terminate` before any undefined behavior can occur.
candidate 2 (found by 3 of 30 passes): Unfortunately, the destroying delete test reveals implementation divergence.
candidate 3 (found by 3 of 30 passes): As the only effect of adding a potentially-throwing exception specification to a deallocation function is to allow undefined behavior, we recommend that construct should be disallowed.
candidate 4 (found by 3 of 30 passes): That issue raises concerns that the current wording is contradictory so needs to be addressed somehow

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

## prior_art - grade 1.33 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/1/2  -> 1.67
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This risks expose the gcc bug of not supplying the implicitly nonthrowing exception to any implementation of a destroying delete function
candidate 2 (found by 3 of 30 passes): This paper would resolve [CWG2042] filed in November 2014.
candidate 3 (found by 2 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification. MSVC triggers the `static_assert` because it checks the destructor in this case, even though it should not.
candidate 4 (found by 1 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.

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

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/2  -> 0.67
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Testing against the current trunk for gcc, we see the `static_assert` fires because it does not implement the implicitly non-throwing exception specification for destroying delete.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/2  -> 1.33
  [5] 2 Proposed resolution                        0/0/1  -> 0.33
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Testing against the current trunk for gcc, we see the `static_assert` fires because it does not implement the implicitly non-throwing exception specification for destroying delete.
candidate 2 (found by 1 of 30 passes): Our hope is that gcc resolve this bug before it becomes an issue, but the timeline is tight if we were to consider this change for C++26.

-->
