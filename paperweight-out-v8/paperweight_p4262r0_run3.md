Verdict: Adequate (4/14)

The paper offers a reasonably strong opening case for why class invariants are a meaningful and difficult design problem, and it shows familiarity with prior art, but it stops short of connecting that motivation to a specific need for ISO standardization. The thinnest parts are the absence of any argument for why this belongs in the standard rather than in tooling or libraries, and the lack of implementation experience or interoperability discussion.

- The paper establishes that class invariants raise genuinely hard, language-specific design questions and that existing languages have answered them inconsistently.
- It also establishes awareness of relevant prior work, including prior C++ contract discussions and the constraints around trivial special member functions.
- The most glaring omission is that the paper never establishes why standardization, as opposed to a library or external tool, is necessary for the feature it describes.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 4 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.67   accumulate 4.33   max 4.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 81 of 84 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.00 / 4.50 / 4.50   (all 3 samples: 4.33)
headings: h2 9
on threshold: none
splits: audience[10] 0/1/0  prior_art[5] 0/2/2  insufficiency[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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

## audience - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [10] 5 Conclusion                                 0/1/0  -> 0.33
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Class invariants are an often-requested extension to C++ Contracts that would greatly aid in leveraging existing software engineering practices to validate correctness in C++ software.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  0/2/2  -> 1.33
  [6] 3 Feature Design  (part 1 of 3)              2/2/2  -> 2.00
  [7] 3 Feature Design  (part 2 of 3)              2/2/2  -> 2.00
  [8] 3 Feature Design  (part 3 of 3)              1/1/1  -> 1.00
  [9] 4 Open Questions                             1/1/1  -> 1.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Every language that has attempted class invariants has encountered the same set of challenges — and no two have arrived at the same answers.
candidate 2 (found by 3 of 36 passes): The questions of *when* an invariant should hold, *which* function boundaries trigger checking, and *how* *much* overhead is acceptable have led to fundamentally different answers across Eiffel, D, Spec#, Ada, and others.
candidate 3 (found by 3 of 36 passes): The general interaction between contract assertions and trivial SMFs was explored in [P2932R3], and the result of that discussion was that [P2900R14] proposed that contract assertions cannot be placed on trivial SMFs.
candidate 4 (found by 3 of 36 passes): It is important that labels (as is made clear in [P3400R4]) do not change the meaning of any contract-related construct

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

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Prior Art                                  0/0/0  -> 0.00
  [6] 3 Feature Design  (part 1 of 3)              0/0/0  -> 0.00
  [7] 3 Feature Design  (part 2 of 3)              0/0/1  -> 0.33
  [8] 3 Feature Design  (part 3 of 3)              0/0/0  -> 0.00
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): such a flag is not viable for C++: it requires per-object storage overhead that violates the zero-overhead principle underlying [P2900R14], and it would constitute an ABI change for any type that adds an invariant.

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
