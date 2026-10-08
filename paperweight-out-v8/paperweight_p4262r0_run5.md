Verdict: Adequate (5/14)

The paper offers a reasonably strong opening case for why class invariants are a meaningful and difficult problem, but it does not carry that case through to the specific standardization questions that would justify a proposal. The support is thinnest where it matters most: showing why this work belongs in the C++ standard rather than in a library or a smaller-scope facility, and how it would coordinate with existing or in-flight contract features.

- The paper establishes that class invariants raise genuinely hard design questions and that prior languages have answered them inconsistently, which gives the topic real weight.
- It also establishes that the design space has been explored in prior work, including the author’s own earlier sketch, though this stops short of demonstrating implementation experience.
- The claim that class invariants are commonly requested is asserted rather than supported with evidence from users or committee discussion.
- The paper does not establish why standardization is necessary, how the feature would interoperate with the existing Contracts facility, or why a library-based approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.33   accumulate 4.83   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 4.50 / 5.50 / 4.50   (all 3 samples: 4.83)
headings: h2 9
on threshold: none
splits: motivation[2] 1/2/1  implementation[4] 0/1/0
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

## audience - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): class invariants are one of the most commonly requested extensions to the C++26 Contracts facility.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  2/2/2  -> 2.00
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

## implementation - grade 0.33  [binary: max] (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/1/0  -> 0.33
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/0  -> 0.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): We have been investigating the design space for class invariants in C++ for several years, including an initial sketch of a possible design in [P2755R1].

-->
