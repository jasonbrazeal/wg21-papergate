Verdict: Strong (9/14)

The paper offers meaningful support in the areas of motivation, prior art, and implementation experience, but its case for standardization is uneven: several points central to why this work belongs in the standard are asserted rather than demonstrated, and the question of why a library solution would be insufficient is left entirely unaddressed.

- The strongest support comes from implementation experience, where the paper shows that similar runtime checks and annotations are already deployed in real compilers and toolchains.
- The paper also establishes why the problem matters by connecting undefined behavior to ongoing safety efforts and the practical limits of existing sanitizers.
- The case for why this needs to be in the standard, rather than handled through existing tooling or user-level integration, is only claimed and not backed by sufficient evidence.
- The most glaring omission is the absence of any established argument for why a library approach would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 28. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 8.67   accumulate 9.00   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 1.67
sample agreement: 192 of 196 section-criterion pairs unanimous (98%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 11 + bold numbered 9
on threshold: audience, vehicle, coordination, implementation
splits: motivation[4] 0/1/0  audience[8] 2/0/0  implementation[8] 1/2/2  implementation[9] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 28 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/1/0  -> 0.33
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    2/2/2  -> 2.00
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          2/2/2  -> 2.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 84 passes): We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard.
candidate 2 (found by 3 of 84 passes): Much of the ongoing work around how to “make C++ safe” is focused on these categories (see [P3081R2], [P3700R0], and references therein).
candidate 3 (found by 3 of 84 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.
candidate 4 (found by 3 of 84 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).

## audience - grade 1.33 (fired in 2 of 28 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    2/0/0  -> 0.67
  [9] 4 Strategy  (part 2 of 2)                    0/0/0  -> 0.00
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          0/0/0  -> 0.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 84 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 17 cases of UB (21.25% of all cases).
candidate 2 (found by 1 of 84 passes): As we saw in Section 3.3, the vast majority of UB (77 cases out of 80, or 96.25% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check.

## prior_art - grade 2.00 (fired in 6 of 28 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    0/0/0  -> 0.00
  [9] 4 Strategy  (part 2 of 2)                    2/2/2  -> 2.00
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          2/2/2  -> 2.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 1/1/1  -> 1.00
candidate 1 (found by 3 of 84 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 2 (found by 3 of 84 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 3 (found by 3 of 84 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]
candidate 4 (found by 2 of 84 passes): For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.

## vehicle - grade 1.00 (fired in 1 of 28 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    0/0/0  -> 0.00
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          0/0/0  -> 0.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 84 passes): This is significant because today, the integration between such tools and user code tends to be poor.

## coordination - grade 1.00 (fired in 1 of 28 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    0/0/0  -> 0.00
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          0/0/0  -> 0.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 84 passes): For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.
candidate 2 (found by 1 of 84 passes): This API provides not only a user callback in the form of a program-wide replaceable contract-violation handler, but also programmatically accessible information about the defect via the `contract_violation` object passed into the contract-violation handler.
candidate 3 (found by 1 of 84 passes): This is significant because today, the integration between such tools and user code tends to be poor.

## insufficiency - grade 0.00 (fired in 0 of 28 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    0/0/0  -> 0.00
  [9] 4 Strategy  (part 2 of 2)                    0/0/0  -> 0.00
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          0/0/0  -> 0.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.67  [binary: max] (fired in 2 of 28 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    1/2/2  -> 1.67
  [9] 4 Strategy  (part 2 of 2)                    1/0/0  -> 0.33
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
  [20] 14 Exception handling [except]               0/0/0  -> 0.00
  [21] 17 Language support library [support]        0/0/0  -> 0.00
  [22] 7 Future extensions                          0/0/0  -> 0.00
  [23] Acknowledgements                             0/0/0  -> 0.00
  [24] References                                   0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [28] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 84 passes): Implicitly generated runtime checks are widely deployed in the field today.
candidate 2 (found by 1 of 84 passes): Checks that can be generated locally by the compiler are often provided via compiler flags, for example the `-ftrapv` flag in GCC that checks for signed integer overflow and terminates the program on failure.
candidate 3 (found by 1 of 84 passes): An example of such annotations deployed in the field as non-standard vendor extensions is the `__counted_by` attribute introduced in Clang 18.
candidate 4 (found by 1 of 84 passes): The GCC compiler option `-ftrapv`, which aborts the program on signed integer overflow, is a conforming implementation of the *quick-enforce* semantic.

-->
