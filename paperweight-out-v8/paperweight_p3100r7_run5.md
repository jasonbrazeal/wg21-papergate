Verdict: Adequate to Strong (8/14)

The paper offers meaningful support for standardization in its framing of the problem and its engagement with prior work, but the case is uneven: several central claims about who benefits, why the standard is the right venue, and how the feature would interoperate are asserted rather than demonstrated, and the absence of a library-only alternative is left unaddressed.

- The strongest support comes from the paper’s grounding in existing practice and prior art, including compiler flags and sanitizer mechanisms that already perform related checks.
- The motivation is clearly tied to ongoing safety efforts and the practical limits of current instrumentation in production.
- The paper asserts broad applicability and benefits from standardization, but does not substantiate those claims with concrete evidence or scenarios.
- The most glaring omission is the failure to establish why a library solution would be insufficient, leaving a key threshold question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 28. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.67   accumulate 8.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 193 of 196 section-criterion pairs unanimous (98%)
single-sample totals would have been: 8.00 / 7.00 / 9.00   (all 3 samples: 8.00)
headings: h2 11 + bold numbered 9
on threshold: vehicle, implementation
splits: audience[8] 0/0/2  prior_art[8] 2/0/2  coordination[8] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 28 sections, strong in 5)
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

## audience - grade 0.33 (fired in 1 of 28 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    0/0/2  -> 0.67
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
candidate 1 (found by 1 of 84 passes): As we saw in Section 3.3, the vast majority of UB (77 cases out of 80, or 96.25% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check

## prior_art - grade 2.00 (fired in 7 of 28 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    2/2/2  -> 2.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/0/2  -> 1.33
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
candidate 1 (found by 3 of 84 passes): For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.
candidate 2 (found by 3 of 84 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 3 (found by 3 of 84 passes): Notably, the [P3400R3] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R1] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups.
candidate 4 (found by 3 of 84 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]

## vehicle - grade 1.00 (fired in 1 of 28 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 2 of 84 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.
candidate 2 (found by 1 of 84 passes): However, bringing them into the scope of the C++ Standard as proposed here has many benefits.

## coordination - grade 0.67 (fired in 1 of 28 sections, strong in 0)
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
candidate 1 (found by 1 of 84 passes): This is significant because today, the integration between such tools and user code tends to be poor.
candidate 2 (found by 1 of 84 passes): All Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 28 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
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
candidate 1 (found by 3 of 84 passes): Checks that can be generated locally by the compiler are often provided via compiler flags, for example the `-ftrapv` flag in GCC that checks for signed integer overflow and terminates the program on failure.

-->
