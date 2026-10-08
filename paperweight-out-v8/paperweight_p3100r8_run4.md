Verdict: Strong (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates the breadth of the problem, shows that the vast majority of undefined behavior is diagnosable, and provides concrete implementation experience. The support is thinnest where the paper needs to show that standardization—rather than a library or existing tooling—is the right vehicle, and that the proposed mechanisms will coordinate cleanly with the ecosystem.

- The paper’s strongest support comes from its implementation experience, with prototype checks working across compilers and existing sanitizer flags serving as conforming implementations of the proposed semantics.
- The paper clearly establishes who is affected by quantifying that 93.9% of explicit core language undefined behavior cases can in principle be diagnosed at runtime.
- The paper’s case for why the standard is necessary remains thin, relying on general claims about poor tool integration without showing that a non-standard approach could not achieve the same result.
- The most glaring omission is a convincing argument for coordination and interoperability, since the paper asserts that tools can hook into a standard API but does not establish that this will work cleanly across the existing ecosystem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.50/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.50 of 14. Unsupported quotes rejected: 49. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.50   corroborated 10.67   accumulate 10.50   max 12.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.17  coordination 1.00  insufficiency 0.33  implementation 2.00
sample agreement: 177 of 189 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.00 / 11.00 / 10.50   (all 3 samples: 10.50)
headings: h2 12 + bold numbered 10
on threshold: vehicle, coordination, implementation
splits: motivation[6] 0/2/1  motivation[7] 0/0/2  audience[7] 0/2/0  prior_art[7] 0/0/2
        prior_art[8] 2/0/0  prior_art[26] 1/0/0  vehicle[8] 0/0/1  insufficiency[9] 0/2/0
        implementation[8] 0/0/1  implementation[9] 1/1/2  implementation[10] 0/1/0
        implementation[17] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/2/1  -> 1.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/2  -> 0.67
  [8] 4 Strategy                                   2/2/2  -> 2.00
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
candidate 2 (found by 3 of 81 passes): The vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check.
candidate 3 (found by 3 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 4 (found by 3 of 81 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.

## audience - grade 2.00 (fired in 3 of 27 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/2/0  -> 0.67
  [8] 4 Strategy                                   2/2/2  -> 2.00
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
candidate 1 (found by 3 of 81 passes): As we saw in Section 3, this is true for 77 cases, that is, 93.9% of all identified cases of explicit core language UB in C++.
candidate 2 (found by 2 of 81 passes): As we saw in Section 3.3, the vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 3 (found by 1 of 81 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 18 cases of UB (22.0% of all cases).
candidate 4 (found by 1 of 81 passes): the vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check

## prior_art - grade 2.00 (fired in 7 of 27 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/2  -> 0.67
  [8] 4 Strategy                                   2/0/0  -> 0.67
  [9] 5 Proposed design                            0/0/0  -> 0.00
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
  [26] Appendix A: List of language UB  (part 1 ... 1/0/0  -> 0.33
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 2 (found by 3 of 81 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 3 (found by 3 of 81 passes): Notably, the [P3400R4] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R2] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups.
candidate 4 (found by 2 of 81 passes): For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.

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
candidate 1 (found by 2 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 81 passes): Our proposed strategy for removal of explicit core language UB focuses on tools that can be portably specified within the C++ abstract machine.
candidate 3 (found by 1 of 81 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.

## coordination - grade 1.00 (fired in 1 of 27 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 2 of 81 passes): With our proposal, all these tools can instead hook into the standard contract-violationhandling API.
candidate 2 (found by 1 of 81 passes): This API provides not only a user callback in the form of a program-wide replaceable contract-violation handler, but also programmatically accessible information about the defect via the `contract_violation` object passed into the contract-violation handler.

## insufficiency - grade 0.33 (fired in 1 of 27 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/0  -> 0.00
  [9] 5 Proposed design                            0/2/0  -> 0.67
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
candidate 1 (found by 1 of 81 passes): For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

## implementation - grade 2.00  [binary: max] (fired in 6 of 27 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/1  -> 0.33
  [9] 5 Proposed design                            1/1/2  -> 1.33
  [10] 6 Proposed wording                           0/1/0  -> 0.33
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/0/0  -> 0.00
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          2/2/2  -> 2.00
  [17] 8 Statements [stmt]                          2/0/2  -> 1.33
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           1/1/1  -> 1.00
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): in the P3850 prototype, checkable at run time on both compilers.
candidate 2 (found by 2 of 81 passes): For example, for signed integer overflow, the GCC flag `-ftrapv` is a conforming implementation of the *quick-enforce* semantic; sanitisers like ASan and UBSan are conforming implementations of the *enforce* semantic for those cases of UB that they identify.
candidate 3 (found by 2 of 81 passes): `.nullptr` caught by a native P3850 check (all available semantics on Clang; four non-throwing semantics on GCC) and constant evaluation, both compilers;
candidate 4 (found by 2 of 81 passes): exhaustively caught by UBSan’s `return` check, constant evaluation, and the P3850 prototype (all available semantics, both compilers).

-->
