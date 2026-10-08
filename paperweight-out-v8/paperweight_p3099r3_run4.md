Verdict: Strong (10/14)

The paper gives a reasonably solid account of existing practice, prior art, and implementation experience, but it does not fully close the loop on why this feature belongs in the standard rather than remaining a vendor extension or library facility. The thinnest part of the case is the absence of any real argument that a library solution is insufficient, and the claim that standardization is timely rests more on assertion than on demonstrated need.

- The strongest support comes from concrete implementation experience in Clang, including deployment in libc++ and the LLVM codebase, as well as compatible branches in GCC and Clang.
- The paper clearly establishes who is affected by pointing to frequent requests, a common `assert(expr && "Reason")` workaround, and immediate implementer interest upon seeing the C++26 Contracts specification.
- Coordination and interoperability are well supported by the shared message layout between compiler forks and the composability with the `compute_message` facet from P3400R4.
- The most glaring omission is the failure to establish why a library cannot provide this functionality, leaving the necessity of standardization for this feature unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.33/14, close to Excellent)

Provisionally addressed: 6 of 7. Provisional points: 10.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.33   corroborated 10.00   accumulate 11.00   max 12.00

## SUMMARY
grades: motivation 1.83  audience 1.50  prior_art 2.00  vehicle 1.00  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 90 of 91 section-criterion pairs unanimous (99%)
single-sample totals would have been: 10.50 / 10.50 / 10.00   (all 3 samples: 10.33)
headings: h2 6 + bold numbered 6
on threshold: audience, vehicle
splits: motivation[5] 2/2/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 2/2/1  -> 1.67
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

## audience - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 1/1/1  -> 1.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  2/2/2  -> 2.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): User-defined diagnostic messages have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/7P1EWzEdq`.
candidate 3 (found by 2 of 39 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:
candidate 4 (found by 1 of 39 passes): The idiom `assert(expr` `&&` `"Reason")` has become a common workaround, and many non-standard assertion facilities provide explicit support for diagnostic messages.

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
candidate 2 (found by 3 of 39 passes): Option B follows the existing practice in Clang.
candidate 3 (found by 3 of 39 passes): This composes with [P3400R4], whose `compute_message` facet can transform or replace the message before it reaches the handler.
candidate 4 (found by 2 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:

## vehicle - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
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
candidate 1 (found by 3 of 39 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([P3460R0]), the time has come to propose standardising this feature for C++29.

## coordination - grade 2.00 (fired in 2 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
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
candidate 2 (found by 2 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today
candidate 3 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:

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
candidate 4 (found by 2 of 39 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header `<contracts>` are required.

-->
