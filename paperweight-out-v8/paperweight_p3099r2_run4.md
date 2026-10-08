Verdict: Strong (9/14)

The paper offers concrete implementation evidence and a clear account of existing practice, but its broader case for standardization rests on assertions that are not fully developed. The strongest support concerns what has already been built and deployed, while the thinnest areas involve why a library solution is insufficient and how the feature coordinates with the wider ecosystem.

- The paper establishes implementation experience through the Clang vendor attribute and its deployment in libc++ and the LLVM codebase.
- The paper establishes prior art and alternatives by comparing syntax options against the existing Clang practice and the facilities in P3400R1.
- The paper claims but does not establish who is affected, relying on anecdotal reaction and a general statement of frequent requests rather than demonstrated breadth of need.
- The paper does not establish why a library will not do, leaving that essential part of the standardization case unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.00   max 11.33

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.00  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 6
on threshold: audience, vehicle, coordination, implementation
splits: audience[1] 0/1/1  audience[3] 2/2/1  prior_art[5] 0/0/1  coordination[3] 2/1/2
        implementation[4] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 2/2/2  -> 2.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 21 passes): A user-defined diagnostic message can provide additional information that can help developers more quickly understand why a particular assertion failed and how to resolve the issue.
candidate 3 (found by 2 of 21 passes): The security implications of this are currently not fully understood.
candidate 4 (found by 1 of 21 passes): The diagnostic message must also be accessible to the user-defined contract-violation handler as this is a primary motivation to add the feature.

## audience - grade 1.17 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/1  -> 1.67
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 2 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 3 (found by 1 of 21 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:

## prior_art - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 2/2/2  -> 2.00
  [5] 3 Proposed wording                           0/0/1  -> 0.33
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 1 of 21 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as ignorable constructs.
candidate 3 (found by 1 of 21 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as ignorable constructs
candidate 4 (found by 1 of 21 passes): Option A requires no additional syntax apart from what [[P3400R1]] already provides, and is the most extensible.

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase
candidate 2 (found by 1 of 21 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([[P3460R0](https://wg21.link/p3460r0)]), the time has come to propose standardising this feature for C++29.

## coordination - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/1/2  -> 1.67
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today
candidate 2 (found by 1 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 1/0/1  -> 0.67
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 1 of 21 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header <contracts> are required.
candidate 3 (found by 1 of 21 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header `<contracts>` are required.

-->
