Verdict: Adequate (4/14)

The paper offers only a narrow basis for its own standardization, centered on the fact that draft wording has been developed in a working-draft branch. Most of the surrounding case—why the problem matters, what prior work exists, and why the standard is the right vehicle—is asserted rather than demonstrated, while the affected audience, coordination concerns, and the impossibility of a library solution are left unaddressed.

- The strongest support is the implementation experience, since the annex wording exists as a collaborative branch of the C++ working draft.
- The paper gestures at prior art and alternatives, but does not establish how those earlier efforts inform or justify this proposal.
- The motivation is only claimed in general terms, without showing concrete consequences for users or implementers.
- The most glaring omission is the absence of any argument for why this belongs in the standard rather than in a separate reference or library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 3 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 36. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 4.00   accumulate 4.17   max 4.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 251 of 252 section-criterion pairs unanimous (100%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 19 + bold numbered 11
on threshold: implementation
splits: prior_art[5] 0/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 36 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Organization  (part 1 of 3)                0/0/0  -> 0.00
  [6] 2 Organization  (part 2 of 3)                0/0/0  -> 0.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 108 passes): Programs that are ill-formed, no diagnostic required (IFNDR) or that exhibit Undefined Behavior are always potentially problematic, and so it is good to be aware of the full scope of potential places where these issues might arise.
candidate 2 (found by 3 of 108 passes): Cataloging all undefined and IFNDR behavior has been identified as a useful task for quite a while.

## audience - grade 0.00 (fired in 0 of 36 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization  (part 1 of 3)                0/0/0  -> 0.00
  [6] 2 Organization  (part 2 of 3)                0/0/0  -> 0.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 3 of 36 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Organization  (part 1 of 3)                0/1/0  -> 0.33
  [6] 2 Organization  (part 2 of 3)                1/1/1  -> 1.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 108 passes): Groupings have already been identified for undefined behavior in [P3100R5], and we can identify similar groupings for IFNDR entries.
candidate 2 (found by 2 of 108 passes): An earlier attempt at gathering this information was made in [P1705R1].
candidate 3 (found by 1 of 108 passes): An earlier attempt at gathering this information was made in [P1705R1]. Calls to formalize this data into an annex within the C++ Standard itself was made in [P2234R0] and later [P3075R0].
candidate 4 (found by 1 of 108 passes): There are two potential options we can consider for organization of the entries in the annexes.

## vehicle - grade 0.00 (fired in 0 of 36 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization  (part 1 of 3)                0/0/0  -> 0.00
  [6] 2 Organization  (part 2 of 3)                0/0/0  -> 0.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 36 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization  (part 1 of 3)                0/0/0  -> 0.00
  [6] 2 Organization  (part 2 of 3)                0/0/0  -> 0.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 36 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization  (part 1 of 3)                0/0/0  -> 0.00
  [6] 2 Organization  (part 2 of 3)                0/0/0  -> 0.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 36 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Organization  (part 1 of 3)                0/0/0  -> 0.00
  [6] 2 Organization  (part 2 of 3)                0/0/0  -> 0.00
  [7] 2 Organization  (part 3 of 3)                0/0/0  -> 0.00
  [8] 5 Lexical conventions [lex] 17               0/0/0  -> 0.00
  [9] 6 Basics [basic] 17                          0/0/0  -> 0.00
  [10] 7 Expressions [expr] 28                      0/0/0  -> 0.00
  [11] 8 Statements [stmt] 38                       0/0/0  -> 0.00
  [12] 9 Declarations [dcl] 39                      0/0/0  -> 0.00
  [13] 10 Modules [module] 45                       0/0/0  -> 0.00
  [14] 11 Classes [class] 46                        0/0/0  -> 0.00
  [15] 12 Overloading [over] 51                     0/0/0  -> 0.00
  [16] 13 Templates [temp] 51                       0/0/0  -> 0.00
  [17] 14 Exception handling [except] 58            0/0/0  -> 0.00
  [18] 15 Preprocessing directives [cpp] 59         0/0/0  -> 0.00
  [19] Modifications                                0/0/0  -> 0.00
  [20] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [21] 6 Basics [basic]                             0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 10 Modules [module]                          0/0/0  -> 0.00
  [26] 11 Classes [class]                           0/0/0  -> 0.00
  [27] 12 Overloading [over]                        0/0/0  -> 0.00
  [28] 13 Templates [temp]                          0/0/0  -> 0.00
  [29] 14 Exception handling [except]               0/0/0  -> 0.00
  [30] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [31] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 4 Conclusion                                 0/0/0  -> 0.00
  [35] Acknowledgments                              0/0/0  -> 0.00
  [36] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 108 passes): The wording in this annex has been developed collaboratively as a branch of the C++ working draft, which can be found [here](https://github.com/cplusplus/draft/tree/ub-ifndr).

-->
