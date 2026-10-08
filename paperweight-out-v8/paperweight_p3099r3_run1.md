Verdict: Strong (9/14)

The paper gives a reasonably solid account of existing practice and implementation experience, but it leaves some parts of its standardization case more asserted than demonstrated, particularly around who is affected and why the standard is the right venue. The strongest support is concrete and compiler-specific, while the thinnest area is the absence of any argument for why a library solution would not suffice.

- The paper clearly establishes that user-defined diagnostic messages are already implemented in Clang and in GCC branches, with enough detail to show real deployment and interoperability.
- It also establishes prior art and coordination by pointing to existing vendor attributes and compatibility between compiler forks.
- The claim that this feature matters broadly rests mainly on frequency of requests and anecdotal implementer reaction, without evidence of the affected user population.
- The paper does not establish why a library approach cannot provide the same capability, leaving a notable gap in the standardization rationale.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.17   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 1.50  insufficiency 0.00  implementation 2.00
sample agreement: 89 of 91 section-criterion pairs unanimous (98%)
single-sample totals would have been: 8.50 / 9.50 / 9.00   (all 3 samples: 9.00)
headings: h2 6 + bold numbered 6
on threshold: coordination
splits: audience[6] 1/0/0  coordination[4] 0/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 2/2/2  -> 2.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): The diagnostic message must also be accessible to the user-defined contract-violation handler as this is a primary motivation to add the feature.
candidate 3 (found by 2 of 39 passes): A user-defined diagnostic message can provide additional information that can help developers more quickly understand why a particular assertion failed and how to resolve the issue.
candidate 4 (found by 1 of 39 passes): The ability to optionally provide such a message is valuable for any assertion facility, including contract assertions.

## audience - grade 1.00 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 1/1/1  -> 1.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  1/0/0  -> 0.33
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:
candidate 3 (found by 1 of 39 passes): User-defined diagnostic messages have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/7P1EWzEdq`.

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
candidate 2 (found by 3 of 39 passes): This composes with [P3400R4], whose `compute_message` facet can transform or replace the message before it reaches the handler.
candidate 3 (found by 2 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today
candidate 4 (found by 2 of 39 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as *ignorable* constructs.

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

## coordination - grade 1.50 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 0/2/1  -> 1.00
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
candidate 2 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today
candidate 3 (found by 1 of 39 passes): The ability to optionally provide such a message is valuable for any assertion facility, including contract assertions.

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
candidate 3 (found by 3 of 39 passes): Option B follows the existing practice in Clang.
candidate 4 (found by 3 of 39 passes): User-defined diagnostic messages have been implemented in branches of GCC and Clang that are available on Compiler Explorer: `https://godbolt.org/z/7P1EWzEdq`.

-->
