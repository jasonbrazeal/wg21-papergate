Verdict: Strong (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates the prevalence and diagnosability of undefined behavior, identifies the affected population, situates its approach against prior and ongoing work, and points to concrete implementation experience. The support is thinnest where the argument needs to move from technical feasibility to institutional necessity, particularly in explaining why the standard, rather than a library or existing tooling conventions, is the right vehicle.

- The strongest support comes from the implementation experience, where existing compiler flags, sanitizers, constant evaluators, and deployed annotations show that the proposed semantics are already being realized in practice.
- The paper also establishes why the problem matters and who is affected by quantifying the share of core language undefined behavior that can be diagnosed and the smaller share for which meaningful replacement behavior can be defined.
- The prior art and alternatives section is well grounded, tying the work to existing UB inventories, Contracts, and recent status reports.
- The most glaring omission is the lack of an established case for why standardization is required, since the paper claims poor integration between tools and user code but does not demonstrate that this cannot be addressed through library interfaces or vendor conventions.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 44. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 11.00   accumulate 11.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 181 of 189 section-criterion pairs unanimous (96%)
single-sample totals would have been: 11.00 / 11.00 / 11.00   (all 3 samples: 11.00)
headings: h2 12 + bold numbered 10
on threshold: vehicle, coordination, insufficiency
splits: motivation[6] 0/2/2  motivation[7] 2/2/0  audience[7] 2/0/2  implementation[8] 1/2/2
        implementation[10] 1/0/0  implementation[13] 0/2/0  implementation[17] 0/0/2
        implementation[19] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/2/2  -> 1.33
  [7] 3 Analysis  (part 2 of 2)                    2/2/0  -> 1.33
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
candidate 2 (found by 3 of 81 passes): Eliminating or at least meaningfully reducing the amount of undefined behaviour (UB) is an important objective for the future evolution of C++.
candidate 3 (found by 3 of 81 passes): The vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 4 (found by 3 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.

## audience - grade 2.00 (fired in 3 of 27 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    2/0/2  -> 1.33
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
candidate 1 (found by 3 of 81 passes): the vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 2 (found by 3 of 81 passes): As we saw in Section 3, this is true for 77 cases, that is, 93.9% of all identified cases of explicit core language UB in C++.
candidate 3 (found by 2 of 81 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 18 cases of UB (22.0% of all cases).

## prior_art - grade 2.00 (fired in 5 of 27 sections, strong in 2)
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
  [26] Appendix A: List of language UB  (part 1 ... 1/1/1  -> 1.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 2 (found by 3 of 81 passes): All identifiers are consistent with those listed in [P3596R3] and [P4284R0].
candidate 3 (found by 2 of 81 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 4 (found by 2 of 81 passes): For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.

## vehicle - grade 1.00 (fired in 1 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.

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

## implementation - grade 2.00  [binary: max] (fired in 7 of 27 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   1/2/2  -> 1.67
  [9] 5 Proposed design                            1/1/1  -> 1.00
  [10] 6 Proposed wording                           1/0/0  -> 0.33
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/2/0  -> 0.67
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          2/2/2  -> 2.00
  [17] 8 Statements [stmt]                          0/0/2  -> 0.67
  [18] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [19] 11 Classes [class]                           2/2/1  -> 1.67
  [20] 13 Templates [temp]                          0/0/0  -> 0.00
  [21] 14 Exception handling [except]               0/0/0  -> 0.00
  [22] 17 Language support library [support]        0/0/0  -> 0.00
  [23] 7 Future extensions                          0/0/0  -> 0.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): For example, for signed integer overflow, the GCC flag `-ftrapv` is a conforming implementation of the *quick-enforce* semantic; sanitisers like ASan and UBSan are conforming implementations of the *enforce* semantic for those cases of UB that they identify.
candidate 2 (found by 3 of 81 passes): caught by UBSan’s `null` check (part of the `undefined` group), which flags the null pointer returned by the non- allocating placement `new`, and by both compilers’ constant evaluators.
candidate 3 (found by 3 of 81 passes): in the P3850 prototype, checkable at run time on both compilers.
candidate 4 (found by 2 of 81 passes): An example of such annotations deployed in the field as non-standard vendor extensions is the `__counted_by` attribute introduced in Clang 18.

-->
