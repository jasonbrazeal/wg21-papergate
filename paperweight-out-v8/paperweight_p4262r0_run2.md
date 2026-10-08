Verdict: Adequate (4/14)

The paper offers some useful framing for why class invariants are a recurring and difficult design question, but it does not build a case that this particular proposal belongs in the C++ standard. The strongest material concerns prior art and the range of unresolved design choices; the thinnest concerns the core standardization questions of why a language feature, rather than a library, is needed and how the feature would coordinate with the existing Contracts framework.

- The paper establishes that class invariants are a widely discussed problem with genuinely divergent answers across Eiffel, D, Spec#, Ada, and others.
- It establishes that the proposal engages with prior art by noting, for example, D’s prohibition on public method calls in invariants and by asking how the feature interacts with P3400R4.
- It claims, but does not establish, that class invariants are among the most commonly requested extensions to C++26 Contracts and that the feature would aid existing software engineering practice.
- It does not establish why the standard is the right venue, why a library solution is insufficient, how the feature would coordinate with existing Contracts machinery, or that there is implementation experience to support the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 3 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.33   accumulate 4.33   max 4.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 81 of 84 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.50 / 4.50 / 4.00   (all 3 samples: 4.33)
headings: h2 9
on threshold: none
splits: audience[4] 0/1/0  audience[10] 1/0/0  prior_art[5] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              2/2/2  -> 2.00
  [7] 3 Feature Design  (part 2 of 3)              2/2/2  -> 2.00
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The ability to *check* these invariants at runtime is a powerful tool for identifying bugs, and class invariants are one of the most commonly requested extensions to the C++26 Contracts facility.
candidate 2 (found by 3 of 36 passes): We have seen a few potential motivations for invariants expressed, and each one leads to a different set of requirements for the feature:
candidate 3 (found by 3 of 36 passes): Class invariants are an often-requested extension to C++ Contracts that would greatly aid in leveraging existing software engineering practices to validate correctness in C++ software.
candidate 4 (found by 2 of 36 passes): Every language that has attempted class invariants has encountered the same set of challenges — and no two have arrived at the same answers.

## audience - grade 0.33 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] 5 Conclusion                                 1/0/0  -> 0.33
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): class invariants are one of the most commonly requested extensions to the C++26 Contracts facility.
candidate 2 (found by 1 of 36 passes): Class invariants are an often-requested extension to C++ Contracts that would greatly aid in leveraging existing software engineering practices to validate correctness in C++ software.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  2/0/0  -> 0.67
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
candidate 4 (found by 3 of 36 passes): How does this interact with the assertion-control framework of [P3400R4]?

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
