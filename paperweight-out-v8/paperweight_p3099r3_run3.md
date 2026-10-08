Verdict: Strong (10/14)

The paper offers substantial support for standardizing user-defined diagnostic messages, particularly through concrete implementation experience and evidence of real-world use. Its case is thinnest where it needs to explain why the feature belongs in the standard rather than remaining a vendor extension, and why a library-based approach would be insufficient.

- The strongest support comes from established implementation experience, including deployment in libc++ and the LLVM codebase, plus working branches in both Clang and GCC.
- The paper clearly establishes coordination and interoperability, showing that both compiler forks agree on a layout that allows cross-compiler handler compatibility.
- Prior art and alternatives are well covered, with the Clang vendor attribute serving as a proven model and the paper explaining why the attribute-like syntax does not meet the ignorability litmus test.
- The most glaring omission is the lack of an established argument for why this cannot be delivered through a library facility rather than a core language change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 8.33   accumulate 10.17   max 12.00

## SUMMARY
grades: motivation 1.67  audience 1.50  prior_art 2.00  vehicle 0.83  coordination 1.67  insufficiency 0.17  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 9.50 / 10.00 / 10.00   (all 3 samples: 9.83)
headings: h2 6 + bold numbered 6
on threshold: motivation, audience, vehicle, coordination
splits: motivation[5] 1/1/2  prior_art[13] 0/0/1  vehicle[4] 1/2/2  coordination[4] 2/1/1
        insufficiency[4] 0/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/2/2  -> 2.00
  [5] 2 Discussion                                 1/1/2  -> 1.33
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
candidate 2 (found by 2 of 39 passes): including deployment experience in libc++ and the LLVM codebase ([P3460R0])
candidate 3 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:

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
  [13] 17 Language support library [support]        0/0/1  -> 0.33
candidate 1 (found by 3 of 39 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 3 of 39 passes): This composes with [P3400R4], whose `compute_message` facet can transform or replace the message before it reaches the handler.
candidate 4 (found by 2 of 39 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as *ignorable* constructs.

## vehicle - grade 0.83 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 1/2/2  -> 1.67
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] 3 Implementation experience                  0/0/0  -> 0.00
  [7] 4 Wording changes                            0/0/0  -> 0.00
  [8] 6 Basics [basic]                             0/0/0  -> 0.00
  [9] 7 Expressions [expr]                         0/0/0  -> 0.00
  [10] 8 Statements [stmt]                          0/0/0  -> 0.00
  [11] 9 Declarations [dcl]                         0/0/0  -> 0.00
  [12] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [13] 17 Language support library [support]        0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([P3460R0]), the time has come to propose standardising this feature for C++29.
candidate 2 (found by 1 of 39 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today

## coordination - grade 1.67 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 2/1/1  -> 1.33
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

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Motivation                                 0/1/0  -> 0.33
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
