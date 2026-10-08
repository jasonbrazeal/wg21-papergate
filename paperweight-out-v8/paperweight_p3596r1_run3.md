Verdict: Adequate (4/14)

The paper offers only a narrow foundation for its own standardization: it demonstrates that the proposed annex wording has been developed in the working draft, but it does little to establish who is affected, why the standard is the right home, or why a library solution would be inadequate. The thinnest support concerns the basic rationale for standardization, where the paper relies on general statements about undefined behavior rather than a concrete case for normative inclusion.

- The strongest support is the implementation experience, since the annex wording exists as a collaborative branch of the C++ working draft.
- The paper gestures at prior art and a hoped-for common vocabulary, but these are asserted rather than shown to justify standardization.
- The paper does not establish who would use the annex or what problem they would solve in practice.
- The most glaring omission is the absence of any argument for why this belongs in the standard rather than in a separate reference or library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 4 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 43. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 5.00   accumulate 4.00   max 5.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 0.50  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 301 of 301 section-criterion pairs unanimous (100%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 28 + bold numbered 11
on threshold: implementation
splits: none
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 43 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 129 passes): Programs that are ill-formed, no diagnostic required (IFNDR) or that exhibit Undefined Behavior are always potentially problematic, and so it is good to be aware of the full scope of potential places where these issues might arise.
candidate 2 (found by 3 of 129 passes): Cataloging all undefined and IFNDR behavior has been identified as a useful task for quite a while.

## audience - grade 0.00 (fired in 0 of 43 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.50 (fired in 1 of 43 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 129 passes): An earlier attempt at gathering this information was made in [P1705R1].
candidate 2 (found by 1 of 129 passes): An earlier attempt at gathering this information was made in [P1705R1]. Calls to formalize this data into an annex within the C++ Standard itself was made in [P2234R0] and later [P3075R0].

## vehicle - grade 0.00 (fired in 0 of 43 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 1 of 43 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 129 passes): We hope that these stable names will be fruitful to use as a common vocabulary for any efforts to modify or mitigate specific classes of problems.

## insufficiency - grade 0.00 (fired in 0 of 43 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 43 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Wording Changes                            0/0/0  -> 0.00
  [6] 5 Lexical conventions [lex] 10               0/0/0  -> 0.00
  [7] 6 Basics [basic] 10                          0/0/0  -> 0.00
  [8] 7 Expressions [expr] 21                      0/0/0  -> 0.00
  [9] 8 Statements [stmt] 31                       0/0/0  -> 0.00
  [10] 9 Declarations [dcl] 32                      0/0/0  -> 0.00
  [11] 10 Modules [module] 38                       0/0/0  -> 0.00
  [12] 11 Classes [class] 39                        0/0/0  -> 0.00
  [13] 12 Overloading [over] 43                     0/0/0  -> 0.00
  [14] 13 Templates [temp] 44                       0/0/0  -> 0.00
  [15] 14 Exception handling [except] 51            0/0/0  -> 0.00
  [16] 15 Preprocessing directives [cpp] 52         0/0/0  -> 0.00
  [17] Modifications                                0/0/0  -> 0.00
  [18] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [19] 6 Basics [basic]                             0/0/0  -> 0.00
  [20] Foonotes                                     0/0/0  -> 0.00
  [21] Foonotes                                     0/0/0  -> 0.00
  [22] Foonotes                                     0/0/0  -> 0.00
  [23] Foonotes                                     0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] Foonotes                                     0/0/0  -> 0.00
  [26] Foonotes                                     0/0/0  -> 0.00
  [27] Foonotes                                     0/0/0  -> 0.00
  [28] Foonotes                                     0/0/0  -> 0.00
  [29] Foonotes                                     0/0/0  -> 0.00
  [30] 8 Statements [stmt]                          0/0/0  -> 0.00
  [31] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [32] 10 Modules [module]                          0/0/0  -> 0.00
  [33] 11 Classes [class]                           0/0/0  -> 0.00
  [34] 12 Overloading [over]                        0/0/0  -> 0.00
  [35] 13 Templates [temp]                          0/0/0  -> 0.00
  [36] 14 Exception handling [except]               0/0/0  -> 0.00
  [37] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [38] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [39] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [40] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [41] 3 Conclusion                                 0/0/0  -> 0.00
  [42] Acknowledgments                              0/0/0  -> 0.00
  [43] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 129 passes): The wording in this annex has been developed collaboratively as a branch of the C++ working draft, which can be found [here](https://github.com/cplusplus/draft/tree/ub-ifndr).

-->
