Verdict: Strong (9/14)

The paper offers solid support in the areas of prior art, implementation experience, and coordination with existing contracts machinery, but its case is noticeably thinner when it comes to showing who is affected and why a library solution cannot suffice. The strongest material is concrete and verifiable, while the weakest relies on anecdote and assertion rather than demonstrated need.

- The paper clearly establishes that the feature has working implementations, including a Clang vendor attribute and branches available on Compiler Explorer, which grounds the proposal in real experience.
- It also establishes coordination and interoperability by showing that the proposed message layout works across Clang and GCC and composes with P3400R4’s message facet.
- The claim that the feature is frequently requested and widely needed is asserted through anecdote and a common workaround idiom, but the paper does not establish the breadth or depth of that need.
- The most glaring omission is the failure to establish why a library facility would not be adequate, since the only support offered is the existence of the Clang vendor attribute rather than an argument against library-based alternatives.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.33   accumulate 9.50   max 10.33

## SUMMARY
grades: motivation 1.67  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 1.83  insufficiency 0.17  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 10.00 / 9.00 / 8.50   (all 3 samples: 9.17)
headings: h2 6 + bold numbered 6
on threshold: motivation
splits: motivation[5] 2/1/1  prior_art[13] 1/0/0  coordination[4] 2/2/1  insufficiency[4] 1/0/0
        implementation[13] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 2/1/1  -> 1.33
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

## audience - grade 1.00 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 1/1/1  -> 1.00
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
candidate 2 (found by 2 of 39 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:
candidate 3 (found by 1 of 39 passes): The idiom `assert(expr` `&&` `"Reason")` has become a common workaround, and many non-standard assertion facilities provide explicit support for diagnostic messages.

## prior_art - grade 2.00 (fired in 5 of 13 sections, strong in 3)  (SHARED PASSAGE)
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
  [13] 17 Language support library [support]        1/0/0  -> 0.33
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 3 of 39 passes): This composes with [P3400R4], whose `compute_message` facet can transform or replace the message before it reaches the handler.
candidate 4 (found by 1 of 39 passes): Option A requires no additional syntax apart from what [P3400R4] already provides, and is the most extensible.

## vehicle - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 1/1/1  -> 1.00
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

## coordination - grade 1.83 (fired in 2 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/1  -> 1.67
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
candidate 3 (found by 1 of 39 passes): The handler can then display, log, or otherwise process the message, separately from the predicate expression, in whichever way best suits the program and its environment.

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 1/0/0  -> 0.33
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today

## implementation - grade 2.00  [binary: max] (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
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
  [13] 17 Language support library [support]        0/0/1  -> 0.33
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 3 of 39 passes): User-defined diagnostic messages have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/7P1EWzEdq`.
candidate 4 (found by 1 of 39 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header <contracts> are required.

-->
