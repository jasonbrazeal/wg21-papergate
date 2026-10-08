Verdict: Strong (8/14)

The paper offers meaningful support in framing the problem and situating its approach within existing Contracts work, but the case for standardization is uneven: several central claims about affected users, standard-level benefits, and implementation experience are asserted rather than demonstrated, and the absence of any argument against a library solution leaves a significant gap.

- The strongest support is the clear motivation that current sanitizer-style instrumentation is too costly for production and that checkable assumptions would improve on `[[assume]]`.
- The paper also credibly grounds its framework in the Contracts facility adopted for C++26 and in prior enumeration efforts for core language undefined behavior.
- The discussion of coordination and interoperability leans on the existence of a standard contract-violation handler API, but does not establish that tools would actually adopt it or that integration is poor today.
- The most glaring omission is the failure to explain why the proposed behavior cannot be delivered through a library, which leaves the necessity of standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 26. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 7.67   accumulate 7.83   max 10.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.67
sample agreement: 176 of 182 section-criterion pairs unanimous (97%)
single-sample totals would have been: 9.00 / 7.50 / 8.00   (all 3 samples: 7.83)
headings: h2 11 + bold numbered 8
on threshold: audience, vehicle, coordination
splits: motivation[4] 0/0/1  motivation[6] 2/1/2  audience[8] 0/1/0  prior_art[11] 1/1/0
        implementation[8] 2/0/0  implementation[9] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 26 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/1  -> 0.33
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/1/2  -> 1.67
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
candidate 1 (found by 3 of 78 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.
candidate 2 (found by 3 of 78 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).
candidate 3 (found by 3 of 78 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.
candidate 4 (found by 2 of 78 passes): We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard.

## audience - grade 1.17 (fired in 2 of 26 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    0/1/0  -> 0.33
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
candidate 2 (found by 1 of 78 passes): Implicitly generated runtime checks are widely deployed in the field today.

## prior_art - grade 2.00 (fired in 8 of 26 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         1/1/0  -> 0.67
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
  [26] Appendix A: List of language UB  (part 4 ... 1/1/1  -> 1.00
candidate 1 (found by 3 of 78 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 2 (found by 3 of 78 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 3 (found by 3 of 78 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]
candidate 4 (found by 2 of 78 passes): building on the basic framework of Contracts adopted for C++26 via [P2900R14] and giving users complete control over what impact that undefined behaviour has on their programs.

## vehicle - grade 1.00 (fired in 1 of 26 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 78 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 78 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.

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
candidate 1 (found by 1 of 78 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 78 passes): With our proposal, all these tools can instead hook into the standard contract-violationhandling API.
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

## implementation - grade 0.67  [binary: max] (fired in 2 of 26 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/0/0  -> 0.67
  [9] 4 Strategy  (part 2 of 2)                    0/0/1  -> 0.33
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
candidate 1 (found by 1 of 78 passes): An example of such annotations deployed in the field as non-standard vendor extensions is the `__counted_by` attribute introduced in Clang 18.
candidate 2 (found by 1 of 78 passes): The GCC compiler option `-ftrapv`, which aborts the program on signed integer overflow, is a conforming implementation of the *quick-enforce* semantic.

-->
