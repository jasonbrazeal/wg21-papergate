Verdict: Adequate (6/14)

The paper offers some concrete support for its standardization, chiefly through implementation experience and a clear statement of the ergonomic problem it addresses, but much of the surrounding case is asserted rather than demonstrated. The thinnest areas are the lack of any established coordination or interoperability discussion and the reliance on claims about frequency, prior art, and the inadequacy of library solutions without supporting evidence.

- The strongest support is the implementation experience, with the feature available in GCC and Clang branches on Compiler Explorer.
- The paper clearly establishes why the feature matters by describing the duplication and forwarding burden that contract assertions in generic code currently impose.
- The case for why a library solution will not suffice is only claimed, since the paper asserts the need for duplication but does not show that alternative library-based approaches fail.
- The most glaring omission is the absence of any coordination and interoperability discussion, leaving the proposal’s relationship to other Contracts work and existing practice unexamined.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 7.00   accumulate 6.67   max 8.00

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 0.67  vehicle 0.50  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 5.50 / 7.00   (all 3 samples: 6.17)
headings: h2 8 + bold numbered 4
on threshold: motivation, implementation
splits: audience[5] 1/0/2  prior_art[2] 0/0/1  implementation[4] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
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
candidate 2 (found by 3 of 39 passes): On function declarations, however, the only way to achieve the same result is to duplicate the function declarations themselves with corresponding constraints (and then duplicate their definitions, or attempt to implement perfect forwarding to a shared implementation).
candidate 3 (found by 2 of 39 passes): This improvement reduces barriers to writing correctness checks in generic code, allowing for more unfettered use of Contracts in general.
candidate 4 (found by 1 of 39 passes): With this small change we improve the ergonomics of writing contract assertions in generic code.

## audience - grade 1.00 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Implementation Experience                  1/0/2  -> 1.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 6 Basics [basic]                             0/0/0  -> 0.00
  [8] 8 Statements [stmt]                          0/0/0  -> 0.00
  [9] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [10] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [11] 4 Conclusion                                 0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In generic code, situations like this come up often, and quite a few examples were explored in [P2755R1].
candidate 2 (found by 2 of 39 passes): Requires clauses on contract assertions have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/oTPGK4zqY`.

## prior_art - grade 0.67 (fired in 2 of 13 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
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
candidate 2 (found by 1 of 39 passes): The design of the C++26 Contracts allows for requires clauses on contract assertions to be easily added, and this proposal adds that support.

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
