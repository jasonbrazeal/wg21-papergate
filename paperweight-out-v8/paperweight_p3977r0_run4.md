Verdict: Adequate (6/14)

The paper offers a partial foundation for its standardization case, with its conceptual motivation and survey of related work reasonably developed, but it leaves several essential justifications largely unaddressed. The thinnest support concerns the practical necessity of standardization itself, the absence of implementation experience, and the lack of evidence that a library solution would be insufficient.

- The paper establishes that the existing contract taxonomy is incomplete and that the proposed distinctions address real conceptual gaps in reasoning about incorrect programs.
- It credibly situates the work against prior art, including P2861R0, P2899R1, erroneous behaviour, and P2900 Contracts.
- The claim that the proposed behaviour is fundamentally different from other implementation decisions is asserted without being demonstrated as a standardization need.
- The paper does not establish who is affected, why a library cannot solve the problem, or that there is any implementation experience supporting the proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 4 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 6.00   accumulate 6.00   max 8.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 137 of 140 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 5.50 / 6.00   (all 3 samples: 5.83)
headings: h2 19
on threshold: vehicle, coordination
splits: motivation[4] 2/1/2  motivation[6] 2/1/2  prior_art[17] 0/0/2
## END SUMMARY

## motivation - grade 1.83 (fired in 6 of 20 sections, strong in 3)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] I. INTRODUCTION                              2/2/2  -> 2.00
  [4] II. INCORRECT PROGRAMS                       2/1/2  -> 1.67
  [5] Definition 2.1. Contractually Incorrect B... 1/1/1  -> 1.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        2/1/2  -> 1.67
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
  [18] VI. CONCLUSION                               1/1/1  -> 1.00
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

## prior_art - grade 2.00 (fired in 7 of 20 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] I. INTRODUCTION                              2/2/2  -> 2.00
  [4] II. INCORRECT PROGRAMS                       1/1/1  -> 1.00
  [5] Definition 2.1. Contractually Incorrect B... 2/2/2  -> 2.00
  [6] III. IMPLEMENTATION FREEDOM & THE ABI        2/2/2  -> 2.00
  [7] Example 4.4.a. The primary domain of void    0/0/0  -> 0.00
  [8] Example 4.4.c. The primary domain of float   0/0/0  -> 0.00
  [9] Example 4.5.a. The secondary domain of void  0/0/0  -> 0.00
  [10] Example 4.5.c. The secondary domain of float 0/0/0  -> 0.00
  [11] Example                                      0/0/0  -> 0.00
  [12] Example 4.6.d. Consider a version of float   1/1/1  -> 1.00
  [13] Example                                      0/0/0  -> 0.00
  [14] Example                                      0/0/0  -> 0.00
  [15] Example                                      0/0/0  -> 0.00
  [16] Example                                      0/0/0  -> 0.00
  [17] Example                                      0/0/2  -> 0.67
  [18] VI. CONCLUSION                               2/2/2  -> 2.00
  [19] ACKNOWLEDGMENTS                              0/0/0  -> 0.00
  [20] REFERENCES                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): This distinguishes primary behaviour from essential behaviour as defined in [P2861R0, P2899R1]: essential behaviour follows from a function being invoked in-contract.
candidate 2 (found by 3 of 60 passes): Since C++26, the standard [N5014] has another way to categorize programming errors: [erroneous](https://eel.is/c++draft/defns.erroneous) behaviour [P2795R5].
candidate 3 (found by 3 of 60 passes): The non-wide categories include the remaining three cases, two of which—unconditionally hardened and pathological— have no analogue in the wide/narrow scheme of [N3248].
candidate 4 (found by 3 of 60 passes): Similarly, P2900 Contracts [P2900R14] are designed so that an implementer can introduce ... without fear of ABI breakage.

## vehicle - grade 1.00 (fired in 1 of 20 sections, strong in 1)  (ON THRESHOLD)
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

## coordination - grade 1.00 (fired in 1 of 20 sections, strong in 1)  (ON THRESHOLD)
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
candidate 2 (found by 1 of 60 passes): This implies that unconditionally hardened preconditions should be emitted callee side (this conclusion can also be reached by considering indirect calls [P3912R0]).

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
