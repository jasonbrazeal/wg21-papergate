Verdict: Strong (11/14)

The paper offers substantial support for the relevance and feasibility of its approach, with particularly strong evidence that the problem is widespread, that runtime checking is already deployed in practice, and that the work builds on existing standardization efforts. The case is thinnest where the paper needs to show why this belongs in the standard rather than in tooling or a library, and how it would coordinate with existing sanitizer and contract mechanisms.

- The paper convincingly establishes that the undefined behavior it targets is pervasive and that most cases can in principle be diagnosed through runtime checks.
- It also demonstrates meaningful implementation experience, citing existing sanitizers, compiler flags, and prototype results across multiple compilers.
- The argument for why standardization is necessary, rather than leaving this to external tools or libraries, is asserted but not developed with concrete evidence.
- The discussion of coordination and interoperability with existing tooling is the most glaring omission, since the paper identifies a limitation in current sanitizer callbacks but does not show how the proposed standard facility would resolve it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 45. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.00   accumulate 11.17   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.17  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 176 of 189 section-criterion pairs unanimous (93%)
single-sample totals would have been: 11.00 / 11.00 / 11.00   (all 3 samples: 10.67)
headings: h2 12 + bold numbered 10
on threshold: audience, vehicle, coordination, insufficiency
splits: motivation[4] 1/0/0  motivation[6] 2/0/1  motivation[7] 0/0/2  motivation[8] 2/0/2
        audience[7] 2/2/0  audience[8] 2/2/1  audience[9] 0/2/2  prior_art[10] 1/1/0
        prior_art[26] 0/1/0  vehicle[8] 0/0/1  implementation[8] 1/1/2  implementation[9] 2/2/1
        implementation[19] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 27 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/0/0  -> 0.33
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/0/1  -> 1.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/2  -> 0.67
  [8] 4 Strategy                                   2/0/2  -> 1.33
  [9] 5 Proposed design                            2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [17] 8 Statements [stmt]                          0/0/0  -> 0.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           0/0/0  -> 0.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          2/2/2  -> 2.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard.
candidate 2 (found by 3 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 3 (found by 3 of 81 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.
candidate 4 (found by 2 of 81 passes): The vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check

## audience - grade 1.50 (fired in 3 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/0  -> 1.33
  [8] 4 Strategy                                   2/2/1  -> 1.67
  [9] 5 Proposed design                            0/2/2  -> 1.33
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [17] 8 Statements [stmt]                          0/0/0  -> 0.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           0/0/0  -> 0.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 2 of 81 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 18 cases of UB (22.0% of all cases).
candidate 2 (found by 2 of 81 passes): the vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 3 (found by 2 of 81 passes): As we saw in Section 3, this is true for 77 cases, that is, 93.9% of all identified cases of explicit core language UB in C++.
candidate 4 (found by 1 of 81 passes): Implicitly generated runtime checks are widely deployed in the field today.

## prior_art - grade 2.00 (fired in 6 of 27 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/0  -> 0.00
  [9] 5 Proposed design                            0/0/0  -> 0.00
  [10] 6 Proposed wording                           1/1/0  -> 0.67
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [17] 8 Statements [stmt]                          0/0/0  -> 0.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           0/0/0  -> 0.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          2/2/2  -> 2.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/1/0  -> 0.33
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): building on the basic framework of Contracts adopted for C++26 via [P2900R14]
candidate 2 (found by 3 of 81 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 3 (found by 2 of 81 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 4 (found by 2 of 81 passes): A companion paper, [P4277R0], contains significant additional commentary on all of the wording changes, along with details on the implementation experience with introducing runtime checks for each of these undefined behaviours.

## vehicle - grade 1.17 (fired in 2 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/1  -> 0.33
  [9] 5 Proposed design                            2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [17] 8 Statements [stmt]                          0/0/0  -> 0.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           0/0/0  -> 0.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 81 passes): Our proposed strategy for removal of explicit core language UB focuses on tools that can be portably specified within the C++ abstract machine.

## coordination - grade 1.00 (fired in 1 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/0  -> 0.00
  [9] 5 Proposed design                            2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [17] 8 Statements [stmt]                          0/0/0  -> 0.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           0/0/0  -> 0.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

## insufficiency - grade 1.00 (fired in 1 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/0  -> 0.00
  [9] 5 Proposed design                            2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [17] 8 Statements [stmt]                          0/0/0  -> 0.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           0/0/0  -> 0.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

## implementation - grade 2.00  [binary: max] (fired in 5 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   1/1/2  -> 1.33
  [9] 5 Proposed design                            2/2/1  -> 1.67
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          2/2/2  -> 2.00
  [17] 8 Statements [stmt]                          2/2/2  -> 2.00
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           2/1/1  -> 1.33
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): For example, for signed integer overflow, the GCC flag `-ftrapv` is a conforming implementation of the *quick-enforce* semantic; sanitisers like ASan and UBSan are conforming implementations of the *enforce* semantic for those cases of UB that they identify.
candidate 2 (found by 3 of 81 passes): exhaustively caught by UBSan’s `return` check, constant evaluation, and the P3850 prototype (all available semantics, both compilers).
candidate 3 (found by 3 of 81 passes): in the P3850 prototype, checkable at run time on both compilers.
candidate 4 (found by 2 of 81 passes): Implicitly generated runtime checks are widely deployed in the field today.

-->
