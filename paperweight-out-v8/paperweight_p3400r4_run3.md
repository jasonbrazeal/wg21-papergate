Verdict: Strong (10/14)

The paper offers solid support in several areas, particularly in motivating the need for contract assertion control, surveying prior art, addressing ABI coordination, and demonstrating implementation experience. Its thinnest support lies in showing who is affected, why the standard is the right venue, and why a library solution cannot suffice, where the evidence is asserted rather than demonstrated.

- The strongest support comes from the implementation experience, with working branches in both GCC and Clang covering the full design and available for direct inspection.
- The paper also establishes prior art and alternatives clearly, situating the proposal against C++26 Contracts and explaining why other operators or mechanisms would be less suitable.
- Coordination and interoperability are well supported through discussion of ABI implications and the need to avoid Standard Library dependencies.
- The most glaring omission is the lack of concrete evidence for who is affected and why a library will not do, since the paper only claims these points without showing specific user populations or demonstrating why library-level replication is insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 7 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 31. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 10.33   accumulate 10.33   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.33  coordination 2.00  insufficiency 0.17  implementation 2.00
sample agreement: 211 of 217 section-criterion pairs unanimous (97%)
single-sample totals would have been: 9.50 / 10.50 / 10.50   (all 3 samples: 10.17)
headings: h2 20 + bold numbered 5
on threshold: vehicle
splits: motivation[27] 1/0/1  audience[10] 0/0/1  vehicle[4] 1/2/2  vehicle[5] 0/0/1
        coordination[6] 0/1/0  insufficiency[5] 0/1/0
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

## audience - grade 0.67 (fired in 2 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
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
  [10] 6 Implementation Experience                  0/0/1  -> 0.33
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
candidate 2 (found by 1 of 93 passes): Both implementations cover the full design: the `pre<`*label*`>(...)` syntax on all three contract kinds, the `contract_control` keyword with its scoped name lookup, `operator|` combining of labels, and every facet that requires compiler involvement

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
candidate 3 (found by 3 of 93 passes): Other possibilities that we might consider are the comma operator (which is always confusing when overloaded) or bitwise `and` (which has less precedent for use in chaining behavior in the Standard).
candidate 4 (found by 3 of 93 passes): The string message introduced in [P3099R2] can also be considered as implicitly adding another label to the start of the assertion-control expression that is implemented by `fixed_message_label_t` above.

## vehicle - grade 1.33 (fired in 3 of 31 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                1/2/2  -> 1.67
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
candidate 1 (found by 3 of 93 passes): The functionality enabled by this proposal is essential to the unhindered and widespread adoption of Contracts across the many domains in which C++ is used.
candidate 2 (found by 3 of 93 passes): With C++26 Contracts, for example, *hardening* some contract assertions but not others would require maintaining supplementary configuration files that are passed with every build to dictate the semantics of specific contract assertions.
candidate 3 (found by 1 of 93 passes): The effects of this new operation could be replicated by manually replicating all of the assertioncontrol-using-directives as regular using directives within a block.

## coordination - grade 2.00 (fired in 3 of 31 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/0/0  -> 0.00
  [6] 1 Introduction  (part 3 of 5)                0/1/0  -> 0.33
  [7] 1 Introduction  (part 4 of 5)                2/2/2  -> 2.00
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
candidate 1 (found by 3 of 93 passes): Having an always-enforced function-contract assertion on a function is a property that can easily become baked into an ABI.
candidate 2 (found by 3 of 93 passes): All of these changes are part of the shared ABI that is implemented in both compiler branches; that ABI will be proposed later as part of the Itanium ABI.
candidate 3 (found by 1 of 93 passes): Because we can’t depend on using the same Standard Library, we can’t depend on using a polymorphic class and virtual functions to access information.

## insufficiency - grade 0.17 (fired in 1 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 5)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 5)                0/1/0  -> 0.33
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
candidate 2 (found by 3 of 93 passes): a full, compilable version can be found at `https://godbolt.org/z/xjKxfe9sf`

-->
