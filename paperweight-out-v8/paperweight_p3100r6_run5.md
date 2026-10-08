Verdict: Adequate to Strong (8/14)

The paper gives a reasonably clear account of the problem it addresses and shows meaningful engagement with existing practice, but its case for standardization rests more on asserted benefits than on demonstrated necessity. The thinnest parts are the absence of a serious argument that a library solution would be insufficient and the lack of concrete implementation experience with the proposed framework itself.

- The strongest support is the paper’s explanation of why undefined behavior matters and why current mitigations are too costly for production use.
- The paper also credibly establishes who is affected by quantifying how much of the language’s undefined behavior can be given replacement semantics.
- Its discussion of prior art is solid, showing awareness of Contracts, existing UB enumeration efforts, and related proposals.
- The most glaring omission is that the paper never establishes why a library cannot provide the proposed functionality, leaving the central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 26. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.33   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.00  implementation 1.33
sample agreement: 174 of 182 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 9.00 / 9.00   (all 3 samples: 8.33)
headings: h2 11 + bold numbered 8
on threshold: audience, vehicle
splits: motivation[4] 0/0/1  motivation[6] 0/2/0  motivation[9] 2/1/1  audience[8] 0/2/2
        prior_art[12] 0/1/0  coordination[8] 2/0/0  implementation[8] 0/2/2
        implementation[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 26 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/1  -> 0.33
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/2/0  -> 0.67
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    2/1/1  -> 1.33
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
candidate 2 (found by 3 of 78 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.
candidate 3 (found by 3 of 78 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).
candidate 4 (found by 3 of 78 passes): if we apply the transformation describe in the previous section and do nothing further, we introduce significant — and in many cases, unacceptable — performance regressions to existing code.

## audience - grade 1.67 (fired in 2 of 26 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    0/2/2  -> 1.33
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
candidate 2 (found by 2 of 78 passes): 77 cases out of 80, or 96.25% of all cases

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
  [12] 6 Basics [basic]                             0/1/0  -> 0.33
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
candidate 2 (found by 3 of 78 passes): building on the basic framework of Contracts adopted for C++26 via [P2900R14]
candidate 3 (found by 3 of 78 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 4 (found by 3 of 78 passes): unlike earlier revisions of this paper and unlike [P3081R1], which adopted its library API from those earlier revisions, we no longer propose to add new enumerators to the enumeration `detection_mode`

## vehicle - grade 1.00 (fired in 1 of 26 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 2 of 78 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.
candidate 2 (found by 1 of 78 passes): Another benefit is that they will be able to integrate with the same unified standard contract-violation handling facility, significantly increasing the ability to deploy software to production systems that is hardened against entire categories of potential bugs.

## coordination - grade 0.33 (fired in 1 of 26 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/0/0  -> 0.67
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
candidate 1 (found by 1 of 78 passes): This API provides not only a user callback in the form of a program-wide replaceable contract-violation handler, but also programmatically accessible information about the defect via the `contract_violation` object passed into the contract-violation handler.

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
  [8] 4 Strategy  (part 1 of 2)                    0/2/2  -> 1.33
  [9] 4 Strategy  (part 2 of 2)                    0/1/0  -> 0.33
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
candidate 2 (found by 1 of 78 passes): The GCC compiler option `-ftrapv`, which aborts the program on signed integer overflow, is a conforming implementation of the *quick-enforce* semantic.

-->
