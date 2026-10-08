Verdict: Adequate (5/14)

The paper offers concrete evidence for the core language inconsistency it targets and for the existence of implementation divergence, but it leaves several essential parts of the standardization case unaddressed. The thinnest support concerns who is affected, why a standard change is the right remedy, and why a library-level solution would not suffice.

- The paper clearly establishes why the current wording matters by identifying a contradiction that leads to undefined behavior and by showing that the proposed change removes the path to that behavior.
- It provides credible implementation experience, citing specific compiler behavior in gcc, Clang, EDG, and MSVC, and it connects the issue to an existing CWG item.
- The discussion of prior art and alternatives is grounded in observed compiler differences, though it does not develop a broader comparison of possible approaches.
- The most glaring omission is the absence of any established case for who is affected, why the standard is the necessary venue, or why a library solution cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.67   accumulate 6.33   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 6.00 / 4.50   (all 3 samples: 5.33)
headings: h2 9
on threshold: motivation, prior_art, implementation
splits: motivation[8] 1/0/0  prior_art[4] 2/2/1  prior_art[6] 2/1/1  coordination[4] 0/2/0
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
candidate 4 (found by 3 of 30 passes): That issue raises concerns that the current wording is contradictory so needs to be addressed somehow, and this proposal removes that contradiction by removing the possibility to reach the contradictory undefined behavior.

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

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/1  -> 1.67
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                2/1/1  -> 1.33
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This risks expose the gcc bug of not supplying the implicitly nonthrowing exception to any implementation of a destroying delete function
candidate 2 (found by 2 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification. MSVC triggers the `static_assert` because it checks the destructor in this case, even though it should not.
candidate 3 (found by 2 of 30 passes): This paper would resolve [CWG2042] filed in November 2014.
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
  [4] 1 Introduction                               0/2/0  -> 0.67
  [5] 2 Proposed resolution                        0/0/0  -> 0.00
  [6] 3 Open Issues                                0/0/0  -> 0.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Unfortunately, the destroying delete test reveals implementation divergence.

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
candidate 1 (found by 2 of 30 passes): Testing against the current trunk for gcc, we see the `static_assert` fires because it does not implement the implicitly non-throwing exception specification for destroying delete.
candidate 2 (found by 1 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.

-->
