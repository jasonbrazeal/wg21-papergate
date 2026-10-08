Verdict: Strong (9/14)

The paper gives a reasonably solid account of why the problem matters, who is affected, and what prior work exists, but it is much thinner when it comes to showing that the solution belongs in the standard rather than in a library or existing tooling. The weakest parts concern the necessity of standardization and the evidence of real implementation experience.

- The strongest support is for prior art and alternatives, where the paper engages with related efforts and positions its approach against them.
- The paper also establishes clearly that the affected population is broad, with most undefined behavior cases being diagnosable in principle.
- The case for why the standard is the right venue is asserted mainly through general benefits rather than demonstrated through concrete interoperability or coordination needs.
- The most glaring omission is the failure to establish why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 6 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 26. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 9.33   accumulate 8.83   max 10.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.50  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 175 of 182 section-criterion pairs unanimous (96%)
single-sample totals would have been: 10.00 / 8.50 / 9.00   (all 3 samples: 8.83)
headings: h2 11 + bold numbered 8
on threshold: coordination
splits: motivation[4] 1/0/0  prior_art[4] 1/1/2  prior_art[11] 1/0/1  prior_art[12] 0/1/1
        vehicle[8] 2/1/0  implementation[8] 2/0/2  implementation[9] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 26 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/0/0  -> 0.33
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    1/1/1  -> 1.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 6 Basics [basic]                             0/0/0  -> 0.00
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          2/2/2  -> 2.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 78 passes): Much of the ongoing work around how to “make C++ safe” is focused on these categories (see [P3081R2], [P3700R0], and references therein).
candidate 2 (found by 3 of 78 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.
candidate 3 (found by 3 of 78 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).
candidate 4 (found by 3 of 78 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.

## audience - grade 2.00 (fired in 2 of 26 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 6 Basics [basic]                             0/0/0  -> 0.00
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          0/0/0  -> 0.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 78 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 17 cases of UB (21.25% of all cases).
candidate 2 (found by 2 of 78 passes): As we saw in Section 3.3, the vast majority of UB (77 cases out of 80, or 96.25% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 3 (found by 1 of 78 passes): 77 cases out of 80, or 96.25% of all cases

## prior_art - grade 2.00 (fired in 8 of 26 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/2  -> 1.33
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    0/0/0  -> 0.00
  [9] 4 Strategy  (part 2 of 2)                    2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         1/0/1  -> 0.67
  [12] 6 Basics [basic]                             0/1/1  -> 0.67
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          2/2/2  -> 2.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 1/1/1  -> 1.00
candidate 1 (found by 3 of 78 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 2 (found by 3 of 78 passes): Notably, the [P3400R3] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R1] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups.
candidate 3 (found by 3 of 78 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]
candidate 4 (found by 2 of 78 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification

## vehicle - grade 0.50 (fired in 1 of 26 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/1/0  -> 1.00
  [9] 4 Strategy  (part 2 of 2)                    0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 6 Basics [basic]                             0/0/0  -> 0.00
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          0/0/0  -> 0.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 78 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 78 passes): However, bringing them into the scope of the C++ Standard as proposed here has many benefits.

## coordination - grade 1.00 (fired in 1 of 26 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [12] 6 Basics [basic]                             0/0/0  -> 0.00
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          0/0/0  -> 0.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 78 passes): All Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.
candidate 2 (found by 1 of 78 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 3 (found by 1 of 78 passes): This API provides not only a user callback in the form of a program-wide replaceable contract-violation handler, but also programmatically accessible information about the defect via the `contract_violation` object passed into the contract-violation handler.

## insufficiency - grade 0.00 (fired in 0 of 26 sections, strong in 0)
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
  [12] 6 Basics [basic]                             0/0/0  -> 0.00
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          0/0/0  -> 0.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 2 of 26 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/0/2  -> 1.33
  [9] 4 Strategy  (part 2 of 2)                    1/1/0  -> 0.67
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 6 Basics [basic]                             0/0/0  -> 0.00
  [13] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [14] 7 Expressions [expr]  (part 2 of 2)          0/0/0  -> 0.00
  [15] 8 Statements [stmt]                          0/0/0  -> 0.00
  [16] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [17] 11 Classes [class]                           0/0/0  -> 0.00
  [18] 14 Exception handling [except]               0/0/0  -> 0.00
  [19] 17 Language support library [support]        0/0/0  -> 0.00
  [20] 7 Future extensions                          0/0/0  -> 0.00
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 2 of 78 passes): An example of such annotations deployed in the field as non-standard vendor extensions is the `__counted_by` attribute introduced in Clang 18.
candidate 2 (found by 2 of 78 passes): The GCC compiler option `-ftrapv`, which aborts the program on signed integer overflow, is a conforming implementation of the *quick-enforce* semantic.

-->
