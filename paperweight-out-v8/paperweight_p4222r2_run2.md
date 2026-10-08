Verdict: Adequate (7/14)

The paper gives a partial account of why a standardization effort might be warranted, with its strongest material concentrated in the problem description and the survey of existing techniques. The case becomes noticeably thinner when it moves from motivating the general issue to showing that this specific mechanism belongs in the standard, and it offers almost nothing on why a library solution would be inadequate.

- The paper clearly establishes that static initialization order is a real problem and that a way to express intentional lack of initialization would address a genuine need.
- It also establishes that the proposed techniques have substantial prior art and that existing C++26 facilities such as **[[indeterminate]]** are not intended to fill this exact role.
- The claim that a large affected codebase exists is asserted through a brief reference to operating systems but is not substantiated with concrete examples or evidence.
- The most glaring omission is the complete absence of a case for why a library facility could not provide the intended behavior, which leaves a central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.67   accumulate 6.67   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.50  coordination 0.67  insufficiency 0.00  implementation 1.00
sample agreement: 124 of 133 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.00 / 6.50 / 6.50   (all 3 samples: 6.67)
headings: h2 18
on threshold: none
splits: motivation[7] 2/1/1  motivation[8] 0/1/0  motivation[10] 1/1/0  prior_art[9] 0/1/1
        prior_art[13] 0/0/1  vehicle[3] 1/0/0  vehicle[5] 1/1/0  coordination[7] 0/0/1
        implementation[5] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 12 of 19 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            2/2/2  -> 2.00
  [6] 4. We need a way to say “leave uninitia... 2/2/2  -> 2.00
  [7] 5. Class objects                             2/1/1  -> 1.33
  [8] X arr3[20];                                  0/1/0  -> 0.33
  [9] X arr4[20] [[uninit]];                       1/1/1  -> 1.00
  [10] 6. What is initialization?                   1/1/0  -> 0.67
  [11] X aar8 [[uninit]] [10];                      1/1/1  -> 1.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      1/1/1  -> 1.00
  [14] 7. Code that does not obey profiles::unin... 2/2/2  -> 2.00
  [15] 8. How to specify this in the standard?      1/1/1  -> 1.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This note emphasizes the rationale of the initialization profile, considers a few alternatives, and suggests simplifications.
candidate 2 (found by 3 of 57 passes): The order of initialization of static objects in different translation units is implementation defined and can lead to an object being accessed before it is initialized.
candidate 3 (found by 3 of 57 passes): We need a way to say “not initialized” because we often pass uninitialized memory around (e.g. to initialize it; see §1.1) and in rare cases initialization of class members must be postponed.
candidate 4 (found by 3 of 57 passes): This is an example of the problem of determining what an initialization is and whether it is complete.

## audience - grade 0.50 (fired in 1 of 19 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            0/0/0  -> 0.00
  [6] 4. We need a way to say “leave uninitia... 0/0/0  -> 0.00
  [7] 5. Class objects                             0/0/0  -> 0.00
  [8] X arr3[20];                                  0/0/0  -> 0.00
  [9] X arr4[20] [[uninit]];                       0/0/0  -> 0.00
  [10] 6. What is initialization?                   0/0/0  -> 0.00
  [11] X aar8 [[uninit]] [10];                      0/0/0  -> 0.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      0/0/0  -> 0.00
  [14] 7. Code that does not obey profiles::unin... 1/1/1  -> 1.00
  [15] 8. How to specify this in the standard?      0/0/0  -> 0.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): There is a lot of such code, e.g., some operating systems.

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            1/1/1  -> 1.00
  [6] 4. We need a way to say “leave uninitia... 2/2/2  -> 2.00
  [7] 5. Class objects                             1/1/1  -> 1.00
  [8] X arr3[20];                                  0/0/0  -> 0.00
  [9] X arr4[20] [[uninit]];                       0/1/1  -> 0.67
  [10] 6. What is initialization?                   1/1/1  -> 1.00
  [11] X aar8 [[uninit]] [10];                      1/1/1  -> 1.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      0/0/1  -> 0.33
  [14] 7. Code that does not obey profiles::unin... 1/1/1  -> 1.00
  [15] 8. How to specify this in the standard?      0/0/0  -> 0.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                2/2/2  -> 2.00
candidate 1 (found by 3 of 57 passes): Variations of all four techniques have been used for decades.
candidate 2 (found by 3 of 57 passes): In C++26, we have **[[indeterminate]].** However, this is not meant to be “misused to document intentional lack of initialization” [TK24], so I suggest something slightly different for that.
candidate 3 (found by 3 of 57 passes): The issue of differing profiles for different TU and modules is dealt with in the Profiles framework [GDR’26], rather than in an individual profile.
candidate 4 (found by 3 of 57 passes): Suppressing the initialization and using a recognized initialization method (e.g. **uninitialized_fill())** can be used to delay initialization without suppressing the profile.

## vehicle - grade 0.50 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/0  -> 0.33
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            1/1/0  -> 0.67
  [6] 4. We need a way to say “leave uninitia... 0/0/0  -> 0.00
  [7] 5. Class objects                             0/0/0  -> 0.00
  [8] X arr3[20];                                  0/0/0  -> 0.00
  [9] X arr4[20] [[uninit]];                       0/0/0  -> 0.00
  [10] 6. What is initialization?                   0/0/0  -> 0.00
  [11] X aar8 [[uninit]] [10];                      0/0/0  -> 0.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      0/0/0  -> 0.00
  [14] 7. Code that does not obey profiles::unin... 0/0/0  -> 0.00
  [15] 8. How to specify this in the standard?      0/0/0  -> 0.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): This rule seems Draconian, but it conforms to common practice and has language support.
candidate 2 (found by 1 of 57 passes): The initialization profile offers a stronger guarantee at the cost of imposing stricter rules of use.

## coordination - grade 0.67 (fired in 2 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            0/0/0  -> 0.00
  [6] 4. We need a way to say “leave uninitia... 0/0/0  -> 0.00
  [7] 5. Class objects                             0/0/1  -> 0.33
  [8] X arr3[20];                                  0/0/0  -> 0.00
  [9] X arr4[20] [[uninit]];                       0/0/0  -> 0.00
  [10] 6. What is initialization?                   0/0/0  -> 0.00
  [11] X aar8 [[uninit]] [10];                      0/0/0  -> 0.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      0/0/0  -> 0.00
  [14] 7. Code that does not obey profiles::unin... 1/1/1  -> 1.00
  [15] 8. How to specify this in the standard?      0/0/0  -> 0.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): system headers and much other foundational C style code is controlled by organizations that (at least in the short term) will not accept C++ attributes.
candidate 2 (found by 1 of 57 passes): The issue of differing profiles for different TU and modules is dealt with in the Profiles framework [GDR’26], rather than in an individual profile.

## insufficiency - grade 0.00 (fired in 0 of 19 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            0/0/0  -> 0.00
  [6] 4. We need a way to say “leave uninitia... 0/0/0  -> 0.00
  [7] 5. Class objects                             0/0/0  -> 0.00
  [8] X arr3[20];                                  0/0/0  -> 0.00
  [9] X arr4[20] [[uninit]];                       0/0/0  -> 0.00
  [10] 6. What is initialization?                   0/0/0  -> 0.00
  [11] X aar8 [[uninit]] [10];                      0/0/0  -> 0.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      0/0/0  -> 0.00
  [14] 7. Code that does not obey profiles::unin... 0/0/0  -> 0.00
  [15] 8. How to specify this in the standard?      0/0/0  -> 0.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Implicit initialization is initialization 0/0/0  -> 0.00
  [5] 3. Static objects                            0/1/0  -> 0.33
  [6] 4. We need a way to say “leave uninitia... 0/0/0  -> 0.00
  [7] 5. Class objects                             0/0/0  -> 0.00
  [8] X arr3[20];                                  0/0/0  -> 0.00
  [9] X arr4[20] [[uninit]];                       0/0/0  -> 0.00
  [10] 6. What is initialization?                   0/0/0  -> 0.00
  [11] X aar8 [[uninit]] [10];                      0/0/0  -> 0.00
  [12] X arr9 [[uninit]] [20];                      0/0/0  -> 0.00
  [13] X arr10[[uninit]] [20];                      0/0/0  -> 0.00
  [14] 7. Code that does not obey profiles::unin... 0/0/0  -> 0.00
  [15] 8. How to specify this in the standard?      0/0/0  -> 0.00
  [16] 9. Early draft standard text                 0/0/0  -> 0.00
  [17] References                                   0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] Appendix: Attribute placement                1/1/1  -> 1.00
candidate 1 (found by 3 of 57 passes): With the exception of the overloading described in §4.8 and some notational details to match the latest specification, an implementation exists.
candidate 2 (found by 3 of 57 passes): Implementers point out that embedding attributes in types is distinctly nontrivial, that the implications of doing so are not completely specified in the standard, and that the existing implementations don’t completely cover these cases.
candidate 3 (found by 1 of 57 passes): Variations of all four techniques have been used for decades.

-->
