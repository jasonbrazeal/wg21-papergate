Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates the prevalence and diagnosability of undefined behavior, shows clear implementation experience, and situates its approach against prior work and alternatives. The support is thinnest where the paper needs to show that the problem cannot be solved outside the standard or that the proposed design coordinates cleanly with existing tooling, since those arguments are asserted rather than developed.

- The strongest support comes from the paper’s concrete evidence that the vast majority of core language undefined behavior can be diagnosed with runtime checks and that such checks are already deployed in real implementations.
- The paper also establishes solid prior art and alternatives by building on C++26 Contracts and referencing companion work with implementation details and wording commentary.
- The case for why this belongs in the standard is weaker, resting on a general claim about poor tool integration without showing that non-standard mechanisms are insufficient.
- The most glaring omission is the lack of an established argument for coordination and interoperability, particularly how the proposed facility would work with existing sanitizer callbacks and death-handling mechanisms.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 44. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 10.67   accumulate 10.83   max 13.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 1.33  insufficiency 0.83  implementation 1.67
sample agreement: 174 of 189 section-criterion pairs unanimous (92%)
single-sample totals would have been: 12.00 / 10.50 / 11.00   (all 3 samples: 10.83)
headings: h2 12 + bold numbered 10
on threshold: vehicle, coordination, insufficiency, implementation
splits: motivation[4] 1/0/1  motivation[6] 2/2/0  motivation[7] 2/0/2  audience[6] 0/0/2
        prior_art[10] 1/1/0  prior_art[26] 1/1/0  coordination[23] 2/0/0  insufficiency[9] 2/1/2
        implementation[8] 1/1/2  implementation[9] 1/2/2  implementation[13] 0/2/0
        implementation[16] 0/2/2  implementation[17] 0/2/2  implementation[18] 0/2/0
        implementation[19] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/0/1  -> 0.67
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/0  -> 1.33
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
  [23] 7 Future extensions                          2/2/2  -> 2.00
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard.
candidate 2 (found by 3 of 81 passes): The vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 3 (found by 3 of 81 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 4 (found by 3 of 81 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.

## audience - grade 2.00 (fired in 4 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/2  -> 0.67
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
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
candidate 1 (found by 3 of 81 passes): Overall, as shown in Figure 3, we can define meaningful replacement behaviour for only 18 cases of UB (22.0% of all cases).
candidate 2 (found by 3 of 81 passes): As we saw in Section 3, this is true for 77 cases, that is, 93.9% of all identified cases of explicit core language UB in C++.
candidate 3 (found by 2 of 81 passes): the vast majority of UB (77 cases out of 82, or 93.9% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check
candidate 4 (found by 1 of 81 passes): We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” ... and one instance of explicit language UB introduced with a phrase containing the word “assume”

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
  [26] Appendix A: List of language UB  (part 1 ... 1/1/0  -> 0.67
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 2 (found by 3 of 81 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 3 (found by 2 of 81 passes): A companion paper, [P4277R0], contains significant additional commentary on all of the wording changes, along with details on the implementation experience with introducing runtime checks for each of these undefined behaviours.
candidate 4 (found by 2 of 81 passes): The [P3400R4] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R2] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups.

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

## coordination - grade 1.33 (fired in 2 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
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
  [23] 7 Future extensions                          2/0/0  -> 0.67
  [24] Acknowledgements                             0/0/0  -> 0.00
  [25] References                                   0/0/0  -> 0.00
  [26] Appendix A: List of language UB  (part 1 ... 0/0/0  -> 0.00
  [27] Appendix A: List of language UB  (part 2 ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.
candidate 2 (found by 1 of 81 passes): If we want to have both, we need to specify one in terms of the other to avoid an incoherent and messy design.

## insufficiency - grade 0.83 (fired in 1 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   0/0/0  -> 0.00
  [9] 5 Proposed design                            2/1/2  -> 1.67
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

## implementation - grade 1.67  [binary: max] (fired in 7 of 27 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy                                   1/1/2  -> 1.33
  [9] 5 Proposed design                            1/2/2  -> 1.67
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] 3 Terms and definitions [intro.defs]         0/0/0  -> 0.00
  [12] 4 General principles [intro]                 0/0/0  -> 0.00
  [13] 6 Basics [basic]  (part 1 of 2)              0/2/0  -> 0.67
  [14] 6 Basics [basic]  (part 2 of 2)              0/0/0  -> 0.00
  [15] 7 Expressions [expr]  (part 1 of 2)          0/0/0  -> 0.00
  [16] 7 Expressions [expr]  (part 2 of 2)          0/2/2  -> 1.33
  [17] 8 Statements [stmt]                          0/2/2  -> 1.33
  [18] 9 Declarations [dcl]                         0/2/0  -> 0.67
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
candidate 2 (found by 3 of 81 passes): in the P3850 prototype, checkable at run time on both compilers.
candidate 3 (found by 2 of 81 passes): Implicitly generated runtime checks are widely deployed in the field today.
candidate 4 (found by 2 of 81 passes): caught by UBSan’s `null` check (part of the `undefined` group), which flags the null pointer returned by the non- allocating placement `new`, and by both compilers’ constant evaluators.

-->
