Verdict: Adequate (5/14)

The paper offers some useful groundwork by situating itself within prior efforts and showing that draft wording has been developed collaboratively, but it leaves several core justifications for standardization largely unargued. The thinnest areas are the absence of any account of who is affected, why the standard is the right vehicle, or why a library or other non-normative artifact would not suffice.

- The strongest support is the implementation experience, since the annex wording exists as a branch of the C++ working draft and has been developed collaboratively.
- The paper also establishes prior art and alternatives by connecting its approach to earlier UB/IFNDR cataloging efforts and existing groupings.
- The paper only claims, rather than establishes, why the problem matters, resting on general statements about IFNDR and undefined behavior being problematic without tying that to a concrete need for standardization.
- The most glaring omission is the lack of any established case for why the standard is the appropriate place for this work, or why a library or separate reference document would not do.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 39. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.33   accumulate 5.50   max 5.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 269 of 273 section-criterion pairs unanimous (99%)
single-sample totals would have been: 4.50 / 5.00 / 5.50   (all 3 samples: 5.00)
headings: h2 22 + bold numbered 11
on threshold: implementation
splits: motivation[5] 1/0/1  prior_art[4] 1/2/2  prior_art[24] 1/0/0  coordination[4] 0/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 39 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Organization                               1/0/1  -> 0.67
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
candidate 3 (found by 2 of 117 passes): Overall, the categorization-based structure seems to be more beneficial for readers and for maintainers, however with the significant time investment needed to settle on a categorization we suggest postponing exploring that option to a future paper.

## audience - grade 0.00 (fired in 0 of 39 sections, strong in 0)
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

## prior_art - grade 1.83 (fired in 3 of 39 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/2/2  -> 1.67
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
  [24] 7 Expressions [expr]                         1/0/0  -> 0.33
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
candidate 2 (found by 2 of 117 passes): An earlier attempt at gathering this information was made in [P1705R1]. Calls to formalize this data into an annex within the C++ Standard itself were made in [P2234R0] and later [P3075R0].
candidate 3 (found by 1 of 117 passes): An earlier attempt at gathering this information was made in [P1705R1].
candidate 4 (found by 1 of 117 passes): In C, an entire object of structure type can be accessed, e.g., using assignment. By contrast, C++ has no notion of accessing an object of class type through an lvalue of class type.

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
  [4] 1 Introduction                               0/0/1  -> 0.33
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
