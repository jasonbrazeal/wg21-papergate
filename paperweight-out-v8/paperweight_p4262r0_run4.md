Verdict: Adequate (5/14)

The paper offers solid grounding for the problem’s importance and for the existence of prior art, but it does not make a direct case for why this work belongs in the C++ standard rather than in a library or separate tool, and it leaves the affected audience and implementation experience more asserted than demonstrated.

- The strongest support is the clear explanation of why class invariants matter and why naive checking would recreate the overhead problems seen in systems such as Midori.
- The paper also credibly establishes that other languages have faced the same design tensions and that prior C++ contract discussions have already touched on related questions.
- The thinnest support is the absence of any argument for why standardization, specifically, is necessary rather than a non-standard solution.
- The paper likewise does not establish coordination with existing contract facilities or interoperability concerns, and its claims about who is affected and about implementation experience remain largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 5 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 5.33   max 5.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.17  implementation 0.33
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.00 / 6.00 / 5.00   (all 3 samples: 5.33)
headings: h2 9
on threshold: none
splits: motivation[5] 0/0/2  motivation[8] 0/1/0  audience[10] 1/1/0  prior_art[4] 2/0/2
        prior_art[5] 2/2/0  prior_art[8] 1/1/0  insufficiency[7] 0/0/1  implementation[4] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Prior Art                                  0/0/2  -> 0.67
  [6] 3 Feature Design  (part 1 of 3)              2/2/2  -> 2.00
  [7] 3 Feature Design  (part 2 of 3)              2/2/2  -> 2.00
  [8] 3 Feature Design  (part 3 of 3)              0/1/0  -> 0.33
  [9] 4 Open Questions                             0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The ability to *check* these invariants at runtime is a powerful tool for identifying bugs, and class invariants are one of the most commonly requested extensions to the C++26 Contracts facility.
candidate 2 (found by 3 of 36 passes): Redundant checking is precisely the overhead explosion that Midori encountered.
candidate 3 (found by 3 of 36 passes): Class invariants are an often-requested extension to C++ Contracts that would greatly aid in leveraging existing software engineering practices to validate correctness in C++ software.
candidate 4 (found by 2 of 36 passes): Class invariants are a natural extension of the C++26 Contracts facility, but specifying them well requires answering fundamental design questions about when invariants should hold, how checking interacts with access control, and how to avoid prohibitive runtime overhead.

## audience - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
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
  [10] 5 Conclusion                                 1/1/0  -> 0.67
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): class invariants are one of the most commonly requested extensions to the C++26 Contracts facility.
candidate 2 (found by 2 of 36 passes): Class invariants are an often-requested extension to C++ Contracts that would greatly aid in leveraging existing software engineering practices to validate correctness in C++ software.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/0/2  -> 1.33
  [5] 2 Prior Art                                  2/2/0  -> 1.33
  [6] 3 Feature Design  (part 1 of 3)              2/2/2  -> 2.00
  [7] 3 Feature Design  (part 2 of 3)              2/2/2  -> 2.00
  [8] 3 Feature Design  (part 3 of 3)              1/1/0  -> 0.67
  [9] 4 Open Questions                             1/1/1  -> 1.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Every language that has attempted class invariants has encountered the same set of challenges — and no two have arrived at the same answers.
candidate 2 (found by 3 of 36 passes): The general interaction between contract assertions and trivial SMFs was explored in [P2932R3], and the result of that discussion was that [P2900R14] proposed that contract assertions cannot be placed on trivial SMFs.
candidate 3 (found by 3 of 36 passes): How does this interact with the assertion-control framework of [P3400R4]?
candidate 4 (found by 2 of 36 passes): The questions of *when* an invariant should hold, *which* function boundaries trigger checking, and *how* *much* overhead is acceptable have led to fundamentally different answers across Eiffel, D, Spec#, Ada, and others.

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
candidate 1 (found by 1 of 36 passes): any stateful thread-local tracking of being “in” the bubble will eventually fail (in addition to being inordinately expensive), and so any approach needs to find a solution that can be determined statically and not dynamically.

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
