Verdict: Adequate to Strong (7/14)

The paper offers meaningful support for the relevance of the problem and for its engagement with prior work, but it leaves several core justifications asserted rather than demonstrated. The thinnest support concerns why a library solution is insufficient and whether the proposed approach has credible implementation experience behind it.

- The strongest part of the paper is its motivation, which clearly connects undefined behavior to real specification gaps and explains why checkable assumptions would improve on existing practice.
- The discussion of prior art and alternatives is also well grounded, showing awareness of related proposals and deliberate choices about how this work differs.
- The case for why this belongs in the standard is mostly asserted, with benefits described in general terms rather than tied to concrete standardization needs.
- The most glaring omission is the absence of any established argument for why a library cannot address the problem, leaving a central threshold question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 17. Replies missing: 0. Sections: 26. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.00   accumulate 7.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 0.67  insufficiency 0.00  implementation 1.00
sample agreement: 174 of 182 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.00 / 7.50   (all 3 samples: 7.17)
headings: h2 11 + bold numbered 8
on threshold: none
splits: motivation[7] 2/2/0  audience[7] 2/0/0  audience[8] 2/0/2  prior_art[12] 1/0/0
        vehicle[8] 0/2/1  coordination[8] 2/0/2  implementation[8] 0/2/1
        implementation[9] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 26 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/0  -> 1.33
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
candidate 1 (found by 3 of 78 passes): We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard.
candidate 2 (found by 3 of 78 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).
candidate 3 (found by 3 of 78 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.
candidate 4 (found by 2 of 78 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.

## audience - grade 1.00 (fired in 2 of 26 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/0/0  -> 0.67
  [8] 4 Strategy  (part 1 of 2)                    2/0/2  -> 1.33
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
candidate 1 (found by 2 of 78 passes): 77 cases out of 80, or 96.25% of all cases
candidate 2 (found by 1 of 78 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 17 cases of UB (21.25% of all cases).

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
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 6 Basics [basic]                             1/0/0  -> 0.33
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
candidate 2 (found by 3 of 78 passes): unlike earlier revisions of this paper and unlike [P3081R1], which adopted its library API from those earlier revisions, we no longer propose to add new enumerators to the enumeration `detection_mode`
candidate 3 (found by 3 of 78 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]
candidate 4 (found by 2 of 78 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the *entire* C++ language specification

## vehicle - grade 0.50 (fired in 1 of 26 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    0/2/1  -> 1.00
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
candidate 1 (found by 1 of 78 passes): Another benefit is that they will be able to integrate with the same unified standard contract-violation handling facility, significantly increasing the ability to deploy software to production systems that is hardened against entire categories of potential bugs.
candidate 2 (found by 1 of 78 passes): However, bringing them into the scope of the C++ Standard as proposed here has many benefits.

## coordination - grade 0.67 (fired in 1 of 26 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/0/2  -> 1.33
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
candidate 1 (found by 1 of 78 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.
candidate 2 (found by 1 of 78 passes): This API provides not only a user callback in the form of a program-wide replaceable contract-violation handler, but also programmatically accessible information about the defect via the `contract_violation` object passed into the contract-violation handler.

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

## implementation - grade 1.00  [binary: max] (fired in 2 of 26 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    0/2/1  -> 1.00
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
candidate 1 (found by 1 of 78 passes): Checks that can be generated locally by the compiler are often provided via compiler flags, for example the `-ftrapv` flag in GCC that checks for signed integer overflow and terminates the program on failure.
candidate 2 (found by 1 of 78 passes): Implicitly generated runtime checks are widely deployed in the field today.
candidate 3 (found by 1 of 78 passes): The GCC compiler option `-ftrapv`, which aborts the program on signed integer overflow, is a conforming implementation of the *quick-enforce* semantic.

-->
