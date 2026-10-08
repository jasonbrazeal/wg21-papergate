Verdict: Adequate (6/14)

The paper offers only a narrow basis for its own standardization: it demonstrates some current implementation behavior, but leaves most of the case for necessity, affected users, alternatives, and interoperability asserted rather than substantiated. The thinnest support is in the areas that would justify committee action beyond a defect report, particularly who is harmed and why a non-standard remedy would be inadequate.

- The strongest support is the concrete implementation experience, with specific compiler behavior reported for Clang, EDG, GCC, and MSVC.
- The paper claims a contradiction in the current wording and points to an existing core issue, but does not establish why that contradiction matters in practice.
- The paper asserts implementation divergence and a possible GCC bug, but does not show who is affected or how widespread the problem is.
- The most glaring omission is the absence of any discussion of why a library-level or non-standard solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 5 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.33   accumulate 6.67   max 7.00

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.17  vehicle 0.17  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.00 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 9
on threshold: coordination, implementation
splits: motivation[4] 2/0/2  motivation[8] 1/0/1  prior_art[4] 1/2/1  prior_art[6] 1/0/1
        vehicle[6] 1/0/0
## END SUMMARY

## motivation - grade 1.17 (fired in 5 of 10 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/0/2  -> 1.33
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    1/0/1  -> 0.67
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Throwing from an overloaded `delete` operator is undefined behavior, yet `delete` operators have a non-throwing exception specification by default, leading to a deterministic call to `terminate` before any undefined behavior can occur.
candidate 2 (found by 3 of 30 passes): As the only effect of adding a potentially-throwing exception specification to a deallocation function is to allow undefined behavior, we recommend that construct should be disallowed.
candidate 3 (found by 3 of 30 passes): That issue raises concerns that the current wording is contradictory so needs to be addressed somehow
candidate 4 (found by 2 of 30 passes): Whatever else the user intended by allowing an exception to propagate from their deallocation function, the standard is very clear that once you leave that function you proceed straight to undefined behavior

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

## prior_art - grade 1.17 (fired in 3 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/2/1  -> 1.33
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/0/1  -> 0.67
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.
candidate 2 (found by 2 of 30 passes): This risks expose the gcc bug of not supplying the implicitly nonthrowing exception to any implementation of a destroying delete function
candidate 3 (found by 2 of 30 passes): This paper would resolve [CWG2042] filed in November 2014.
candidate 4 (found by 1 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification. MSVC triggers the `static_assert` because it checks the destructor in this case, even though it should not.

## vehicle - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                1/0/0  -> 0.33
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): That issue raises concerns that the current wording is contradictory so needs to be addressed somehow, and this proposal removes that contradiction by removing the possibility to reach the contradictory undefined behavior.

## coordination - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
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
candidate 1 (found by 2 of 30 passes): Unfortunately, the destroying delete test reveals implementation divergence.
candidate 2 (found by 1 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification. MSVC triggers the `static_assert` because it checks the destructor in this case, even though it should not.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.
candidate 2 (found by 1 of 30 passes): Testing against the current trunk for gcc, we see the `static_assert` fires because it does not implement the implicitly non-throwing exception specification for destroying delete.

-->
