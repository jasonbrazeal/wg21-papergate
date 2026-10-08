Verdict: Adequate (6/14)

The paper offers some useful groundwork by acknowledging prior efforts and by developing draft wording collaboratively, but it does not build a persuasive case that this material belongs in the C++ Standard. The support is thinnest where the paper needs to show why standardization is the right vehicle and why a non-normative library or reference document would not suffice.

- The strongest support is the implementation experience, since the annex wording has already been developed as a branch of the C++ working draft.
- The paper also establishes prior art and alternatives by connecting its approach to earlier undefined behavior groupings and prior collection efforts.
- The case for who is affected remains only a claim, with the paper offering little beyond the observation that some totals would be useful.
- The most glaring omission is the absence of any established reason why this needs to be in the standard, rather than in a separate catalog, guide, or other non-normative resource.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 5 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 39. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.33   accumulate 5.83   max 6.67

## SUMMARY
grades: motivation 1.00  audience 0.67  prior_art 1.67  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 269 of 273 section-criterion pairs unanimous (99%)
single-sample totals would have been: 5.50 / 6.50 / 4.50   (all 3 samples: 5.50)
headings: h2 22 + bold numbered 11
on threshold: prior_art, implementation
splits: motivation[5] 0/1/1  audience[5] 2/2/0  prior_art[4] 1/2/1  coordination[4] 0/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 39 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Organization                               0/1/1  -> 0.67
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): Programs that are ill-formed, no diagnostic required (IFNDR) or that exhibit Undefined Behavior are always potentially problematic, and so it is good to be aware of the full scope of potential places where these issues might arise.
candidate 2 (found by 3 of 117 passes): Cataloging all undefined and IFNDR behavior has been identified as a useful task for quite a while.
candidate 3 (found by 1 of 117 passes): Overall, the categorization-based structure seems to be more beneficial for readers and for maintainers, however with the significant time investment needed to settle on a categorization we suggest postponing exploring that option to a future paper.
candidate 4 (found by 1 of 117 passes): Overall, the categorization-based structure seems to be more beneficial for readers and for maintainers

## audience - grade 0.67 (fired in 1 of 39 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization                               2/2/0  -> 1.33
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 117 passes): Some totals to aid in the decision are useful:

## prior_art - grade 1.67 (fired in 2 of 39 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/2/1  -> 1.33
  [5] 2 Organization                               2/2/2  -> 2.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): Groupings have already been identified for undefined behavior in [P3100R6], and we can identify similar groupings for IFNDR entries.
candidate 2 (found by 2 of 117 passes): An earlier attempt at gathering this information was made in [P1705R1].
candidate 3 (found by 1 of 117 passes): An earlier attempt at gathering this information was made in [P1705R1]. Calls to formalize this data into an annex within the C++ Standard itself were made in [P2234R0] and later [P3075R0].

## vehicle - grade 0.00 (fired in 0 of 39 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization                               0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 39 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/1/0  -> 0.33
  [5] 2 Organization                               0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 117 passes): We hope that these stable names will be fruitful to use as a common vocabulary for any efforts to modify or mitigate specific classes of problems.

## insufficiency - grade 0.00 (fired in 0 of 39 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Organization                               0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 39 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Organization                               0/0/0  -> 0.00
  [6] 3 Wording Changes                            0/0/0  -> 0.00
  [7] 5 Lexical conventions [lex] 12               0/0/0  -> 0.00
  [8] 6 Basics [basic] 13                          0/0/0  -> 0.00
  [9] 7 Expressions [expr] 25                      0/0/0  -> 0.00
  [10] 8 Statements [stmt] 35                       0/0/0  -> 0.00
  [11] 9 Declarations [dcl] 37                      0/0/0  -> 0.00
  [12] 10 Modules [module] 42                       0/0/0  -> 0.00
  [13] 11 Classes [class] 43                        0/0/0  -> 0.00
  [14] 12 Overloading [over] 48                     0/0/0  -> 0.00
  [15] 13 Templates [temp] 48                       0/0/0  -> 0.00
  [16] 14 Exception handling [except] 56            0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 56         0/0/0  -> 0.00
  [18] D+a Enumeration of Core Undefined Behavio... 0/0/0  -> 0.00
  [19] D+b Enumeration of Ill-formed, No Diagnos... 0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [23] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [24] 7 Expressions [expr]                         0/0/0  -> 0.00
  [25] 8 Statements [stmt]                          0/0/0  -> 0.00
  [26] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [27] 10 Modules [module]                          0/0/0  -> 0.00
  [28] 11 Classes [class]                           0/0/0  -> 0.00
  [29] 12 Overloading [over]                        0/0/0  -> 0.00
  [30] 13 Templates [temp]                          0/0/0  -> 0.00
  [31] 14 Exception handling [except]               0/0/0  -> 0.00
  [32] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [33] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [34] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [35] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [36] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [37] 4 Conclusion                                 0/0/0  -> 0.00
  [38] Acknowledgments                              0/0/0  -> 0.00
  [39] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 117 passes): The wording in this annex has been developed collaboratively as a branch of the C++ working draft, which can be found [here](https://github.com/cplusplus/draft/tree/ub-ifndr).

-->
