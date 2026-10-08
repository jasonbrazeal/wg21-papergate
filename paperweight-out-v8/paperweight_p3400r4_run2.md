Verdict: Strong (10/14)

The paper offers solid support in several areas, particularly in showing prior art, implementation experience, and coordination concerns, but its case is uneven where it needs to connect the feature to concrete users and to explain why standardization is the only viable path. The thinnest support appears around who is affected and why a library solution would be insufficient, both of which are asserted rather than demonstrated.

- The strongest support comes from the implementation experience, with working branches in both GCC and Clang available for inspection.
- The paper also clearly establishes prior art and alternatives by situating the proposal within the existing Contracts framework and ongoing standardization plans.
- The most glaring omission is the lack of established evidence for who is affected, since the paper asserts widespread impact without showing concrete user or domain needs.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 31. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.33   accumulate 9.83   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.17  coordination 1.67  insufficiency 0.17  implementation 2.00
sample agreement: 212 of 217 section-criterion pairs unanimous (98%)
single-sample totals would have been: 10.00 / 9.00 / 9.50   (all 3 samples: 9.50)
headings: h2 20 + bold numbered 5
on threshold: coordination
splits: motivation[27] 1/0/1  vehicle[4] 2/2/0  coordination[6] 2/0/0  coordination[7] 2/0/2
        insufficiency[5] 0/0/1
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
  [27] 8 Conclusion                                 1/0/1  -> 0.67
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

## prior_art - grade 2.00 (fired in 9 of 31 sections, strong in 5)
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
  [9] 4 Future Directions                          2/2/2  -> 2.00
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
candidate 4 (found by 3 of 93 passes): Note that the *assume* semantic might be added by, for example, [P3100R7].

## vehicle - grade 1.17 (fired in 2 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                2/2/0  -> 1.33
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
candidate 2 (found by 2 of 93 passes): With C++26 Contracts, for example, *hardening* some contract assertions but not others would require maintaining supplementary configuration files that are passed with every build to dictate the semantics of specific contract assertions.

## coordination - grade 1.67 (fired in 3 of 31 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                2/0/0  -> 0.67
  [7] 1 Introduction  (part 4 of 5)                2/0/2  -> 1.33
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
candidate 2 (found by 1 of 93 passes): Any interface we provide to information emanating from an assertion-control object must work correctly for all permutations of compiler and Standard Library implementations that might be used in the two TUs.
candidate 3 (found by 1 of 93 passes): Having an always-enforced function-contract assertion on a function is a property that can easily become baked into an ABI.
candidate 4 (found by 1 of 93 passes): As soon as compilers of caller and callee TUs come to an agreement as to which one will evaluate an always-checked contract assertion the *other* compiler can begin to optimize based on the fact that that assertion will be enforced.

## insufficiency - grade 0.17 (fired in 1 of 31 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/1  -> 0.33
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
candidate 1 (found by 1 of 93 passes): The effects of this new operation could be replicated by manually replicating all of the assertioncontrol-using-directives as regular using directives within a block.

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
candidate 2 (found by 2 of 93 passes): a full, compilable version can be found at `https://godbolt.org/z/xjKxfe9sf`
candidate 3 (found by 1 of 93 passes): a full, compilable version can be found at `https://godbolt.org/z/xjKxfe9sf`.

-->
