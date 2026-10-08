Verdict: Adequate (6/14)

The paper offers only a thin evidentiary basis for standardization, relying heavily on assertion and brief references rather than developed argument or demonstrated need. Its strongest concrete support is the existence of prototype implementations, but even that is undercut by the absence of any reported usage, evaluation, or interoperability analysis.

- The clearest support is that the feature has been implemented in GCC and Clang branches and is available on Compiler Explorer.
- The paper gestures toward prior work and a broader contracts plan, but does not show how this proposal fits or interacts with those efforts.
- The most glaring omission is any discussion of coordination and interoperability with existing or planned contract features, leaving the standardization case incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 7.00   accumulate 6.67   max 8.00

## SUMMARY
grades: motivation 1.17  audience 1.17  prior_art 0.83  vehicle 0.50  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 8 + bold numbered 4
on threshold: audience, implementation
splits: motivation[4] 0/2/2  audience[4] 1/0/1  audience[5] 2/1/2  prior_art[2] 1/1/0
        implementation[4] 1/1/0
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/2/2  -> 1.33
  [5] 2 Implementation Experience                  0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 1/1/1  -> 1.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Contract assertions in generic code can often be written for only a subset of the types that a template might support.
candidate 2 (found by 3 of 39 passes): With this small change we improve the ergonomics of writing contract assertions in generic code.
candidate 3 (found by 2 of 39 passes): On function declarations, however, the only way to achieve the same result is to duplicate the function declarations themselves with corresponding constraints (and then duplicate their definitions, or attempt to implement perfect forwarding to a shared implementation).

## audience - grade 1.17 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/0/1  -> 0.67
  [5] 2 Implementation Experience                  2/1/2  -> 1.67
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): In generic code, situations like this come up often, and quite a few examples were explored in [P2755R1].
candidate 2 (found by 2 of 39 passes): Requires clauses on contract assertions have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/oTPGK4zqY`.
candidate 3 (found by 1 of 39 passes): Requires clauses on contract assertions have been implemented in branches of GCC and Clang that are available on Compiler Explorer.

## prior_art - grade 0.83 (fired in 2 of 13 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Implementation Experience                  1/1/1  -> 1.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): They are also available with the flag `-fcontracts-p3850` that enables prototype implementations of many of the papers described in the overall plan in [P3850R1].
candidate 2 (found by 2 of 39 passes): The design of the C++26 Contracts allows for requires clauses on contract assertions to be easily added, and this proposal adds that support.

## vehicle - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Implementation Experience                  0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In the end, this is a simple proposal to add a small feature that has proven to be very useful in practice.

## coordination - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Implementation Experience                  0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Implementation Experience                  0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): On function declarations, however, the only way to achieve the same result is to duplicate the function declarations themselves with corresponding constraints (and then duplicate their definitions, or attempt to implement perfect forwarding to a shared implementation).

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/0  -> 0.67
  [5] 2 Implementation Experience                  2/2/2  -> 2.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Requires clauses on contract assertions have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/oTPGK4zqY`.
candidate 2 (found by 2 of 39 passes): In the end, this is a simple proposal to add a small feature that has proven to be very useful in practice.

-->
