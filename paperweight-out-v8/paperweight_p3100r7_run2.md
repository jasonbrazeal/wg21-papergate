Verdict: Strong (9/14)

The paper gives a reasonably strong account of why reducing undefined behavior matters and who would be affected, and it situates itself credibly against prior efforts and existing tooling. The case becomes much thinner when it turns to what standardization itself would uniquely provide, how the feature would coordinate with existing implementations, and whether any of this could be done outside the standard.

- The strongest support is the demonstration that undefined behavior is widespread, diagnosable in principle, and largely untouched by current production-safe tooling.
- The paper also establishes meaningful prior art, including independent enumeration efforts and connections to Contracts and existing sanitizer practice.
- The weakest established area is the rationale for standardization itself, where the paper asserts shared terminology and paradigm benefits without showing why those require a standard rather than convention or library-level coordination.
- The most glaring omission is the absence of any established argument for why a library or non-standard implementation would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 6 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 28. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.33   accumulate 9.17   max 11.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.83  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 190 of 196 section-criterion pairs unanimous (97%)
single-sample totals would have been: 9.00 / 9.50 / 9.00   (all 3 samples: 9.17)
headings: h2 11 + bold numbered 9
on threshold: vehicle, coordination
splits: motivation[6] 0/0/2  motivation[9] 1/2/2  prior_art[8] 0/2/2  vehicle[8] 2/1/2
        implementation[8] 1/2/1  implementation[9] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 28 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/2  -> 0.67
  [7] 3 Analysis  (part 2 of 2)                    2/2/2  -> 2.00
  [8] 4 Strategy  (part 1 of 2)                    2/2/2  -> 2.00
  [9] 4 Strategy  (part 2 of 2)                    1/2/2  -> 1.67
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
candidate 1 (found by 3 of 84 passes): Eliminating or at least meaningfully reducing the amount of *undefined* *behaviour* (UB) is an important objective for the future evolution of C++.
candidate 2 (found by 3 of 84 passes): As we know from existing sanitisers, such instrumentation is expensive enough that it is almost never affordable in production.
candidate 3 (found by 3 of 84 passes): In C++ today, the behaviour of this program is undefined if the value of `i` is not smaller than 10 ({expr.add.out.of.bounds}).
candidate 4 (found by 3 of 84 passes): Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.

## audience - grade 2.00 (fired in 2 of 28 sections, strong in 2)
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
candidate 2 (found by 3 of 84 passes): As we saw in Section 3.3, the vast majority of UB (77 cases out of 80, or 96.25% of all cases) can in principle be diagnosed by inserting and performing a suitable runtime check

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
  [8] 4 Strategy  (part 1 of 2)                    0/2/2  -> 1.33
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
candidate 1 (found by 3 of 84 passes): Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]).
candidate 2 (found by 3 of 84 passes): Assertion in a catch handler if not made ill-formed by [P3424R0]
candidate 3 (found by 2 of 84 passes): Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification
candidate 4 (found by 2 of 84 passes): For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.

## vehicle - grade 0.83 (fired in 1 of 28 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    2/1/2  -> 1.67
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
candidate 1 (found by 3 of 84 passes): One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.

## coordination - grade 1.00 (fired in 1 of 28 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 84 passes): All Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 28 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 History and polls                          0/0/0  -> 0.00
  [6] 3 Analysis  (part 1 of 2)                    0/0/0  -> 0.00
  [7] 3 Analysis  (part 2 of 2)                    0/0/0  -> 0.00
  [8] 4 Strategy  (part 1 of 2)                    1/2/1  -> 1.33
  [9] 4 Strategy  (part 2 of 2)                    0/2/0  -> 0.67
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
candidate 1 (found by 2 of 84 passes): Implicitly generated runtime checks are widely deployed in the field today.
candidate 2 (found by 1 of 84 passes): Checks that require additional instrumentation to perform are provided by various flavours of sanitisers such as ASan, UBSan, etc.
candidate 3 (found by 1 of 84 passes): The GCC compiler option `-fwrapv`, which implements wraparound for signed integer addition using twos-complement representation, is a conforming implementation of the *ignore* semantic, silently executing well-defined replacement behaviour.

-->
