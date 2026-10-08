Verdict: Strong (9/14)

The paper gives a reasonably solid account of existing practice and deployment, but it leans heavily on the fact that Clang already ships the feature as a vendor extension rather than building an independent case for why the standard must absorb it. The thinnest part is the absence of any argument that a library-based approach could not meet the need, which leaves a noticeable gap in the standardization rationale.

- The strongest support comes from implementation experience, including deployment in libc++ and the LLVM codebase, which shows the feature is more than a speculative design.
- The paper also establishes coordination and interoperability by describing agreement between Clang and GCC forks on the message layout used by violation handlers.
- Prior art and alternatives are adequately covered, with the discussion of syntax options and the limits of the existing Clang attribute practice.
- The most glaring omission is the failure to explain why a library solution would not suffice, leaving the “why the standard” case dependent on momentum rather than necessity.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.33/14)

Provisionally addressed: 6 of 7. Provisional points: 9.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.33   corroborated 8.00   accumulate 9.83   max 11.33

## SUMMARY
grades: motivation 1.50  audience 1.50  prior_art 2.00  vehicle 0.67  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 89 of 91 section-criterion pairs unanimous (98%)
single-sample totals would have been: 10.00 / 8.50 / 9.50   (all 3 samples: 9.33)
headings: h2 6 + bold numbered 6
on threshold: motivation, audience, coordination
splits: vehicle[4] 2/1/1  coordination[4] 2/0/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 1/1/1  -> 1.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): A user-defined diagnostic message can provide additional information that can help developers more quickly understand why a particular assertion failed and how to resolve the issue.
candidate 3 (found by 3 of 39 passes): The diagnostic message must also be accessible to the user-defined contract-violation handler as this is a primary motivation to add the feature.

## audience - grade 1.50 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 2 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 1 of 39 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([P3460R0]), the time has come to propose standardising this feature for C++29.

## prior_art - grade 2.00 (fired in 4 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 2/2/2  -> 2.00
  [6] 3 Implementation experience                  2/2/2  -> 2.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today
candidate 3 (found by 1 of 39 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as ignorable constructs.
candidate 4 (found by 1 of 39 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as *ignorable* constructs.

## vehicle - grade 0.67 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/1/1  -> 1.33
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([P3460R0]), the time has come to propose standardising this feature for C++29.

## coordination - grade 1.67 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/0/2  -> 1.33
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  2/2/2  -> 2.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Because both forks agree on this layout, a violation handler built with either compiler can read messages produced by assertions compiled with the other.
candidate 2 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today.

## insufficiency - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 0/0/0  -> 0.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 1/1/1  -> 1.00
  [6] 3 Implementation experience                  2/2/2  -> 2.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 3 of 39 passes): User-defined diagnostic messages have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/7P1EWzEdq`.
candidate 4 (found by 2 of 39 passes): Option B follows the existing practice in Clang.

-->
