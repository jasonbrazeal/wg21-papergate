Verdict: Adequate (4/14)

The paper offers a reasonably grounded case that class invariants are a meaningful and contested design area, but it stops well short of showing why this particular proposal should be standardized. The strongest material concerns prior art and the difficulty of the problem, while the argument for standardization itself is almost entirely absent.

- The paper establishes that class invariants are widely requested and that prior languages have produced genuinely different answers to the core design questions.
- It also shows that the interaction between invariants and C++’s existing contract and special-member-function rules has already received some committee attention.
- The paper does not establish who would be affected by the proposed feature or what practical problem in existing C++ code it would solve.
- Most glaringly, it never explains why the standard is the right venue, why a library cannot suffice, or what implementation experience supports the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 2 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 4.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 9
on threshold: none
splits: motivation[2] 1/2/1  prior_art[5] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  2/2/2  -> 2.00
  [6] 3 Feature Design  (part 1 of 3)              2/2/2  -> 2.00
  [7] 3 Feature Design  (part 2 of 3)              2/2/2  -> 2.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Every language that has attempted class invariants has encountered the same set of challenges — and no two have arrived at the same answers.
candidate 2 (found by 3 of 36 passes): The ability to *check* these invariants at runtime is a powerful tool for identifying bugs, and class invariants are one of the most commonly requested extensions to the C++26 Contracts facility.
candidate 3 (found by 3 of 36 passes): The lesson for C++ is that we must identify a principled rule for *when* invariants should hold that avoids both the unsoundness of Eiffel’s approach and the impracticality of brute-force checking, while remaining expressible within C++’s compilation and access-control model.
candidate 4 (found by 3 of 36 passes): We have seen a few potential motivations for invariants expressed, and each one leads to a different set of requirements for the feature:

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  0/2/0  -> 0.67
  [6] 3 Feature Design  (part 1 of 3)              2/2/2  -> 2.00
  [7] 3 Feature Design  (part 2 of 3)              2/2/2  -> 2.00
  [8] 3 Feature Design  (part 3 of 3)              1/1/1  -> 1.00
  [9] 4 Open Questions                             1/1/1  -> 1.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Every language that has attempted class invariants has encountered the same set of challenges — and no two have arrived at the same answers.
candidate 2 (found by 3 of 36 passes): The questions of *when* an invariant should hold, *which* function boundaries trigger checking, and *how* *much* overhead is acceptable have led to fundamentally different answers across Eiffel, D, Spec#, Ada, and others.
candidate 3 (found by 3 of 36 passes): D takes this approach, prohibiting public method calls in invariants entirely.
candidate 4 (found by 3 of 36 passes): The general interaction between contract assertions and trivial SMFs was explored in [P2932R3], and the result of that discussion was that [P2900R14] proposed that contract assertions cannot be placed on trivial SMFs.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

-->
