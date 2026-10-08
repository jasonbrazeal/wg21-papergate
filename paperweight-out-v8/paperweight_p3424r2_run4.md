Verdict: Adequate (5/14)

The paper offers only a narrow slice of the case for standardization: it can point to implementation experience in two compilers, but most of the surrounding justification is asserted rather than demonstrated, and several essential questions are left entirely unaddressed. The thinnest areas are the absence of any identified affected users, any argument for why a standard change rather than a non-standard fix is needed, and any explanation of why a library-level or implementation-level remedy would not suffice.

- The strongest support is the implementation experience, since the paper notes that Clang trunk and the EDG compiler follow the existing specification.
- The paper asserts, but does not establish, that the change matters by framing it as removing potential undefined behavior and resolving a contradictory wording concern.
- The paper gestures at prior art and alternatives through references to compiler behavior and CWG2042, but does not develop a comparison of possible approaches.
- The most glaring omission is the complete lack of discussion of who is affected, why the standard is the right venue, or why a library or implementation-level solution would not do.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 4 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.00   accumulate 6.50   max 6.33

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 5.17)
headings: h2 9
on threshold: coordination, implementation
splits: motivation[1] 1/0/0  motivation[4] 0/2/2
## END SUMMARY

## motivation - grade 1.17 (fired in 6 of 10 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/2/2  -> 1.33
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    1/1/1  -> 1.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Throwing from an overloaded `delete` operator is undefined behavior, yet `delete` operators have a non-throwing exception specification by default, leading to a deterministic call to `terminate` before any undefined behavior can occur.
candidate 2 (found by 3 of 30 passes): As the only effect of adding a potentially-throwing exception specification to a deallocation function is to allow undefined behavior, we recommend that construct should be disallowed.
candidate 3 (found by 3 of 30 passes): That issue raises concerns that the current wording is contradictory so needs to be addressed somehow
candidate 4 (found by 3 of 30 passes): Rationale: Removes potential undefined behavior.

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

## prior_art - grade 1.00 (fired in 3 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Proposed resolution                        1/1/1  -> 1.00
  [6] 3 Open Issues                                1/1/1  -> 1.00
  [7] 4 Review History                             0/0/0  -> 0.00
  [8] 5 Wording                                    0/0/0  -> 0.00
  [9] 6 Acknowledgements                           0/0/0  -> 0.00
  [10] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.
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

## coordination - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification. MSVC triggers the `static_assert` because it checks the destructor in this case, even though it should not.

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
candidate 1 (found by 3 of 30 passes): Clang trunk and the EDG compiler follow the Standard specification.

-->
