Verdict: Strong (10/14)

The paper offers solid support in several areas, particularly in showing prior art, implementation experience, and interoperability considerations, but it leaves the central question of why a library solution is insufficient entirely unaddressed. The case for who is affected and why the standard itself is needed rests mostly on broad assertions rather than concrete demonstration, making those parts of the argument feel thin.

- The strongest support comes from the implementation experience, with working branches in both GCC and Clang and a compilable example available for inspection.
- The paper also does well in establishing prior art and alternatives, grounding its approach in C++26 Contracts and existing proposals while explaining the choice of `operator|`.
- Coordination and interoperability are credibly addressed through discussion of cross-TU behavior and shared ABI concerns.
- The most glaring omission is the absence of any established argument for why a library cannot provide the proposed functionality, leaving a core requirement for standardization unmet.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 6 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 31. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 9.67   accumulate 10.17   max 10.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.33  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 209 of 217 section-criterion pairs unanimous (96%)
single-sample totals would have been: 10.00 / 10.50 / 9.50   (all 3 samples: 10.00)
headings: h2 20 + bold numbered 5
on threshold: vehicle
splits: motivation[4] 2/2/0  motivation[27] 1/0/1  audience[2] 1/1/0  audience[27] 1/1/0
        prior_art[7] 2/2/0  prior_art[9] 0/2/2  vehicle[4] 1/2/2  vehicle[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 31 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                2/2/0  -> 1.33
  [5] 1 Introduction  (part 2 of 5)                2/2/2  -> 2.00
  [6] 1 Introduction  (part 3 of 5)                2/2/2  -> 2.00
  [7] 1 Introduction  (part 4 of 5)                2/2/2  -> 2.00
  [8] 1 Introduction  (part 5 of 5)                0/0/0  -> 0.00
  [9] 4 Future Directions                          2/2/2  -> 2.00
  [10] 6 Implementation Experience                  0/0/0  -> 0.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 1/0/1  -> 0.67
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): The functionality enabled by this proposal is essential to the unhindered and widespread adoption of Contracts across the many domains in which C++ is used.
candidate 2 (found by 3 of 93 passes): Three absolutely needed use cases arise where contract assertions must restrict the range of semantics that might be applied to a contract assertion.
candidate 3 (found by 3 of 93 passes): Customizing contract-violation handling for specific contexts and specific contract assertions is an oft-requested feature that arises in several distinct situations:
candidate 4 (found by 3 of 93 passes): On some platforms (such as Windows), function parameters are destroyed by the callee before control is returned to the caller, which means that caller-side checking of postconditions that refer to a function parameter is nonviable.

## audience - grade 0.67 (fired in 2 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                0/0/0  -> 0.00
  [7] 1 Introduction  (part 4 of 5)                0/0/0  -> 0.00
  [8] 1 Introduction  (part 5 of 5)                0/0/0  -> 0.00
  [9] 4 Future Directions                          0/0/0  -> 0.00
  [10] 6 Implementation Experience                  0/0/0  -> 0.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 1/1/0  -> 0.67
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 93 passes): The functionality enabled by this proposal is essential to the unhindered and widespread adoption of Contracts across the many domains in which C++ is used.
candidate 2 (found by 1 of 93 passes): a programming language used by millions — to write software that is used by billions
candidate 3 (found by 1 of 93 passes): a programming language used by millions — to write software that is used by billions — demands.

## prior_art - grade 2.00 (fired in 9 of 31 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 5)                2/2/2  -> 2.00
  [6] 1 Introduction  (part 3 of 5)                2/2/2  -> 2.00
  [7] 1 Introduction  (part 4 of 5)                2/2/0  -> 1.33
  [8] 1 Introduction  (part 5 of 5)                1/1/1  -> 1.00
  [9] 4 Future Directions                          0/2/2  -> 1.33
  [10] 6 Implementation Experience                  1/1/1  -> 1.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 1/1/1  -> 1.00
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): C++26 Contracts, adopted with [P2900R14], provides a framework for specifying and checking contract assertions whose behavior is controlled through implementation-defined build configurations.
candidate 2 (found by 3 of 93 passes): In [P3850R1] a plan for that set of features is being proposed, and those features that fully enable the control of evaluation semantics are a core part of that plan.
candidate 3 (found by 3 of 93 passes): Because of the existing use of `operator|` with ranges to chain together multiple objects, we will continue to propose `operator|` as our default mechanism for combining assertion-control objects.
candidate 4 (found by 3 of 93 passes): An additional property on `contract_violation`, `message`, has been proposed by [P3099R2].

## vehicle - grade 1.33 (fired in 3 of 31 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                1/2/2  -> 1.67
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                0/0/0  -> 0.00
  [7] 1 Introduction  (part 4 of 5)                0/1/0  -> 0.33
  [8] 1 Introduction  (part 5 of 5)                0/0/0  -> 0.00
  [9] 4 Future Directions                          0/0/0  -> 0.00
  [10] 6 Implementation Experience                  0/0/0  -> 0.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 0/0/0  -> 0.00
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): The functionality enabled by this proposal is essential to the unhindered and widespread adoption of Contracts across the many domains in which C++ is used.
candidate 2 (found by 2 of 93 passes): With C++26 Contracts, for example, *hardening* some contract assertions but not others would require maintaining supplementary configuration files that are passed with every build to dictate the semantics of specific contract assertions.
candidate 3 (found by 1 of 93 passes): With C++26 Contracts, however, the behavior of the program when a contract assertion is evaluated is controlled entirely in an implementation-defined manner, i.e., through command line options and build configurations outside of the source code.
candidate 4 (found by 1 of 93 passes): Some or all of the above facilities can be adopted in order to ease the use of labels in different situations, though they all build on core-language functionality and could be written by users themselves.

## coordination - grade 2.00 (fired in 2 of 31 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                2/2/2  -> 2.00
  [7] 1 Introduction  (part 4 of 5)                0/0/0  -> 0.00
  [8] 1 Introduction  (part 5 of 5)                0/0/0  -> 0.00
  [9] 4 Future Directions                          0/0/0  -> 0.00
  [10] 6 Implementation Experience                  2/2/2  -> 2.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 0/0/0  -> 0.00
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): Any interface we provide to information emanating from an assertion-control object must work correctly for all permutations of compiler and Standard Library implementations that might be used in the two TUs.
candidate 2 (found by 3 of 93 passes): All of these changes are part of the shared ABI that is implemented in both compiler branches; that ABI will be proposed later as part of the Itanium ABI.

## insufficiency - grade 0.00 (fired in 0 of 31 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                0/0/0  -> 0.00
  [7] 1 Introduction  (part 4 of 5)                0/0/0  -> 0.00
  [8] 1 Introduction  (part 5 of 5)                0/0/0  -> 0.00
  [9] 4 Future Directions                          0/0/0  -> 0.00
  [10] 6 Implementation Experience                  0/0/0  -> 0.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 0/0/0  -> 0.00
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 31 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                0/0/0  -> 0.00
  [7] 1 Introduction  (part 4 of 5)                0/0/0  -> 0.00
  [8] 1 Introduction  (part 5 of 5)                0/0/0  -> 0.00
  [9] 4 Future Directions                          0/0/0  -> 0.00
  [10] 6 Implementation Experience                  2/2/2  -> 2.00
  [11] 7 Wording                                    0/0/0  -> 0.00
  [12] 5 Lexical conventions [lex] 61               0/0/0  -> 0.00
  [13] 6 Basics [basic] 62                          0/0/0  -> 0.00
  [14] 7 Expressions [expr] 66                      0/0/0  -> 0.00
  [15] 8 Statements [stmt] 66                       0/0/0  -> 0.00
  [16] 9 Declarations [dcl] 67                      0/0/0  -> 0.00
  [17] 15 Preprocessing directives [cpp] 68         0/0/0  -> 0.00
  [18] 17 Language support library [support] 69     0/0/0  -> 0.00
  [19] C Compatibility [diff] 85                    0/0/0  -> 0.00
  [20] Modifications                                0/0/0  -> 0.00
  [21] 5 Lexical conventions [lex]                  0/0/0  -> 0.00
  [22] 7 Expressions [expr]                         0/0/0  -> 0.00
  [23] 8 Statements [stmt]                          0/0/0  -> 0.00
  [24] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [25] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [26] 15 Preprocessing directives [cpp]  (part ... 0/0/0  -> 0.00
  [27] 8 Conclusion                                 0/0/0  -> 0.00
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     2/2/2  -> 2.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): Assertion-control objects have been implemented in branches of both GCC and Clang that are available on Compiler Explorer:
candidate 2 (found by 3 of 93 passes): A full, compilable version can be found at `https://godbolt.org/z/xjKxfe9sf`.

-->
