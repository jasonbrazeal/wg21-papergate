Verdict: Strong (9/14)

The paper offers solid support in the areas of prior art, implementation experience, and coordination, but its case is much thinner when it comes to showing who is concretely affected, why the standard is the right venue, and especially why a library solution would be insufficient.

- The strongest support comes from the demonstrated implementation experience in both GCC and Clang, along with a compilable example.
- The paper also establishes meaningful prior art and a clear coordination story around ABI and cross-implementation concerns.
- The weakest part of the case is the absence of any established argument for why a library cannot provide the proposed functionality.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 31. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.67   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.83  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 210 of 217 section-criterion pairs unanimous (97%)
single-sample totals would have been: 10.00 / 8.50 / 10.00   (all 3 samples: 9.00)
headings: h2 20 + bold numbered 5
on threshold: coordination
splits: motivation[27] 0/1/1  prior_art[9] 2/2/0  prior_art[10] 1/1/2  vehicle[4] 1/1/0
        vehicle[5] 0/0/2  vehicle[7] 2/0/0  coordination[6] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 31 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                2/2/2  -> 2.00
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
  [27] 8 Conclusion                                 0/1/1  -> 0.67
  [28] A Glossary                                   0/0/0  -> 0.00
  [29] B Example Implementation                     0/0/0  -> 0.00
  [30] Acknowledgments                              0/0/0  -> 0.00
  [31] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): The functionality enabled by this proposal is essential to the unhindered and widespread adoption of Contracts across the many domains in which C++ is used.
candidate 2 (found by 3 of 93 passes): With C++26 Contracts, however, the behavior of the program when a contract assertion is evaluated is controlled entirely in an implementation-defined manner, i.e., through command line options and build configurations outside of the source code.
candidate 3 (found by 3 of 93 passes): Three absolutely needed use cases arise where contract assertions must restrict the range of semantics that might be applied to a contract assertion.
candidate 4 (found by 3 of 93 passes): Customizing contract-violation handling for specific contexts and specific contract assertions is an oft-requested feature that arises in several distinct situations:

## audience - grade 0.50 (fired in 1 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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
candidate 1 (found by 3 of 93 passes): The functionality enabled by this proposal is essential to the unhindered and widespread adoption of Contracts across the many domains in which C++ is used.

## prior_art - grade 2.00 (fired in 9 of 31 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 5)                2/2/2  -> 2.00
  [6] 1 Introduction  (part 3 of 5)                2/2/2  -> 2.00
  [7] 1 Introduction  (part 4 of 5)                2/2/2  -> 2.00
  [8] 1 Introduction  (part 5 of 5)                1/1/1  -> 1.00
  [9] 4 Future Directions                          2/2/0  -> 1.33
  [10] 6 Implementation Experience                  1/1/2  -> 1.33
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
candidate 3 (found by 3 of 93 passes): An additional property on `contract_violation`, `message`, has been proposed by [P3099R2].
candidate 4 (found by 3 of 93 passes): In [P3850R1], we propose a plan for prioritizing the features that are most needed for C++26.

## vehicle - grade 0.83 (fired in 4 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                1/1/0  -> 0.67
  [5] 1 Introduction  (part 2 of 5)                0/0/2  -> 0.67
  [6] 1 Introduction  (part 3 of 5)                0/0/0  -> 0.00
  [7] 1 Introduction  (part 4 of 5)                2/0/0  -> 0.67
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
candidate 2 (found by 2 of 93 passes): With C++26 Contracts, however, the behavior of the program when a contract assertion is evaluated is controlled entirely in an implementation-defined manner, i.e., through command line options and build configurations outside of the source code.
candidate 3 (found by 1 of 93 passes): The effects of this new operation could be replicated by manually replicating all of the assertioncontrol-using-directives as regular using directives within a block.
candidate 4 (found by 1 of 93 passes): Any feature that might *implicitly* make use of labels must also consider whether such implicit use should depend on having included `&lt;contracts>` before such use.

## coordination - grade 1.67 (fired in 2 of 31 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                2/0/2  -> 1.33
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
candidate 1 (found by 3 of 93 passes): All of these changes are part of the shared ABI that is implemented in both compiler branches; that ABI will be proposed later as part of the Itanium ABI.
candidate 2 (found by 2 of 93 passes): Any interface we provide to information emanating from an assertion-control object must work correctly for all permutations of compiler and Standard Library implementations that might be used in the two TUs.

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
