Verdict: Adequate (6/14)

The paper offers a solid conceptual motivation for its taxonomy and shows familiarity with relevant prior work, but it does not build a complete case that this vocabulary belongs in the standard. The thinnest parts are the absence of any demonstrated user population, implementation experience, or argument for why a library or ordinary technical report would be insufficient.

- The strongest support is the established motivation, which clearly explains why existing contract classifications are incomplete and why the proposed terms address real conceptual gaps.
- The paper also credibly establishes prior art by connecting its ideas to existing standards, erroneous behavior, and current contract proposals.
- The most glaring omission is the lack of any established evidence about who is affected, leaving the practical need for standardization ungrounded.
- Equally missing is any implementation experience or argument that a library cannot provide the same vocabulary, so the case for standardization rather than documentation remains unproven.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 137 of 140 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 19
on threshold: vehicle, coordination
splits: motivation[18] 1/2/2  prior_art[4] 2/2/1  prior_art[18] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 20 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] I. INTRODUCTION                              2/2/2  -> 2.00
  [4] II. INCORRECT PROGRAMS                       1/1/1  -> 1.00
  [5] Definition 2.1. Contractually Incorrect B... 1/1/1  -> 1.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        2/2/2  -> 2.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   0/0/0  -> 0.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               1/2/2  -> 1.67
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): However, there are circumstances in which this categorization may be counterintuitive or even inapplicable, as has been brought into sharp focus by the current discussions around non-ignorable contracts.
candidate 2 (found by 3 of 60 passes): The premise of this paper is that, previously, we have not had the right words to describe situations such as this and others: the existing classification of contracts is incomplete.
candidate 3 (found by 3 of 60 passes): One of the things which, in my opinion, makes contracts so difficult to understand deeply is that we are forced to reason about incorrect programs, which can be very counterintuitive.
candidate 4 (found by 3 of 60 passes): As mentioned above, this may be counterintuitive which is part of the motivation for the taxonomy proposed by this paper: we call a wide contract of this type disconnecting.

## audience - grade 0.00 (fired in 0 of 20 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              0/0/0  -> 0.00
  [4] II. INCORRECT PROGRAMS                       0/0/0  -> 0.00
  [5] Definition 2.1. Contractually Incorrect B... 0/0/0  -> 0.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        0/0/0  -> 0.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   0/0/0  -> 0.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               0/0/0  -> 0.00
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 20 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              2/2/2  -> 2.00
  [4] II. INCORRECT PROGRAMS                       2/2/1  -> 1.67
  [5] Definition 2.1. Contractually Incorrect B... 2/2/2  -> 2.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        2/2/2  -> 2.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   2/2/2  -> 2.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               1/2/1  -> 1.33
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): To understand why it is useful to define primary behaviour differently from essential behaviour, return to the case of what `float` `sqrt(float)` does for negative inputs.
candidate 2 (found by 3 of 60 passes): Since C++26, the standard [N5014] has another way to categorize programming errors: [erroneous](https://eel.is/c++draft/defns.erroneous) behaviour [P2795R5].
candidate 3 (found by 3 of 60 passes): The non-wide categories include the remaining three cases, two of which—unconditionally hardened and pathological— have no analogue in the wide/narrow scheme of [N3248].
candidate 4 (found by 3 of 60 passes): Similarly, P2900 Contracts [P2900R14] are designed so that an implementer can introduce `void foo(int x) pre(x >= 0);` without fear of ABI breakage.

## vehicle - grade 1.00 (fired in 1 of 20 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              0/0/0  -> 0.00
  [4] II. INCORRECT PROGRAMS                       0/0/0  -> 0.00
  [5] Definition 2.1. Contractually Incorrect B... 0/0/0  -> 0.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        2/2/2  -> 2.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   0/0/0  -> 0.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               0/0/0  -> 0.00
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): This is fundamentally different from any other implementation decision for the contractually incorrect behaviour of `foo`.

## coordination - grade 1.00 (fired in 1 of 20 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              0/0/0  -> 0.00
  [4] II. INCORRECT PROGRAMS                       0/0/0  -> 0.00
  [5] Definition 2.1. Contractually Incorrect B... 0/0/0  -> 0.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        2/2/2  -> 2.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   0/0/0  -> 0.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               0/0/0  -> 0.00
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 60 passes): The problem here is that, by design, `quick` `enforce` cannot be ignored. Therefore, as pointed out by Lisa Lippincott, it becomes part of the ABI and removing it constitutes an ABI break.
candidate 2 (found by 1 of 60 passes): This is fundamentally different from any other implementation decision for the contractually incorrect behaviour of `foo`.

## insufficiency - grade 0.00 (fired in 0 of 20 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              0/0/0  -> 0.00
  [4] II. INCORRECT PROGRAMS                       0/0/0  -> 0.00
  [5] Definition 2.1. Contractually Incorrect B... 0/0/0  -> 0.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        0/0/0  -> 0.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   0/0/0  -> 0.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               0/0/0  -> 0.00
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 20 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              0/0/0  -> 0.00
  [4] II. INCORRECT PROGRAMS                       0/0/0  -> 0.00
  [5] Definition 2.1. Contractually Incorrect B... 0/0/0  -> 0.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        0/0/0  -> 0.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   0/0/0  -> 0.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/0  -> 0.00
  [18] VI. CONCLUSION                               0/0/0  -> 0.00
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidates: (none validated)

-->
