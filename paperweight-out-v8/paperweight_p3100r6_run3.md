Verdict: Strong (9/14)

The paper offers meaningful support in some areas, particularly in motivating the problem and showing continuity with existing standardization work, but its case is uneven and leaves several essential questions largely unargued. The thinnest parts concern why library solutions cannot suffice and whether the proposed mechanisms have enough real-world implementation experience to justify standardization.

- The strongest support is for prior art and alternatives, where the paper connects its approach to Contracts, existing sanitizer practice, and independent UB enumeration efforts.
- The motivation is also well established, with clear examples of undefined behavior and the limits of current production instrumentation.
- The paper only claims, without fully establishing, who is affected, why the standard is the right venue, and how the work coordinates with existing tools and implementations.
- The most glaring omission is the absence of any established argument for why a library solution will not do, which is a central requirement for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 26. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 8.33   accumulate 8.50   max 11.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.17  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 180 of 182 section-criterion pairs unanimous (99%)
single-sample totals would have been: 9.00 / 7.50 / 9.00   (all 3 samples: 8.50)
headings: h2 11 + bold numbered 8
on threshold: audience, vehicle, coordination
splits: vehicle[20] 0/1/0  implementation[8] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 26 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
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
candidate 1 (found by 3 of 78 passes): We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard.
candidate 2 (found by 3 of 78 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.
candidate 3 (found by 3 of 78 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).
candidate 4 (found by 3 of 78 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.

## audience - grade 1.00 (fired in 1 of 26 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
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
candidate 1 (found by 3 of 78 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 17 cases of UB (21.25% of all cases).

## prior_art - grade 2.00 (fired in 6 of 26 sections, strong in 3)
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
candidate 2 (found by 3 of 78 passes): For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.
candidate 3 (found by 3 of 78 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 4 (found by 3 of 78 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]

## vehicle - grade 1.17 (fired in 2 of 26 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
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
  [20] 7 Future extensions                          0/1/0  -> 0.33
  [21] Acknowledgements                             0/0/0  -> 0.00
  [22] References                                   0/0/0  -> 0.00
  [23] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [24] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
  [25] Appendix A: List of language UB  (part 3 ... 0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 4 ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 78 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.
candidate 2 (found by 1 of 78 passes): However, bringing them into the scope of the C++ Standard as proposed here has many benefits.
candidate 3 (found by 1 of 78 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 4 (found by 1 of 78 passes): Such a control mechanism for runtime checks (or for other tools in our toolbox such as language subsetting) needs to be designed carefully and take into account the overall strategy (Figure 4).

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
candidate 1 (found by 2 of 78 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 78 passes): Another benefit is that they will be able to integrate with the same unified standard contract-violation handling facility, significantly increasing the ability to deploy software to production systems that is hardened against entire categories of potential bugs.

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 26 sections, strong in 0)
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
candidate 1 (found by 1 of 78 passes): An example of such annotations deployed in the field as non-standard vendor extensions is the `__counted_by` attribute introduced in Clang 18.
candidate 2 (found by 1 of 78 passes): Checks that require additional instrumentation to perform are provided by various flavours of sanitisers such as ASan, UBSan, etc.

-->
