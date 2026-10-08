Verdict: Strong (8/14)

The paper offers meaningful support in the areas of implementation experience and prior art, largely because the feature already exists as a Clang vendor attribute and has been exercised in real codebases. Its case is much thinner when it comes to explaining why standardization, rather than continued vendor extension, is necessary, and it does not address why a library-based solution would be inadequate.

- The strongest support is the concrete implementation experience in Clang, including deployment in libc++ and the LLVM codebase, which grounds the proposal in existing practice.
- The paper also establishes prior art and alternatives by comparing syntax options against the current Clang extension and existing contract facilities.
- The discussion of who is affected relies on anecdote and frequency-of-request claims without demonstrating the breadth or severity of the need.
- The most glaring omission is the absence of any argument for why a library solution cannot provide the requested diagnostic capability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.83   max 10.67

## SUMMARY
grades: motivation 1.50  audience 1.33  prior_art 2.00  vehicle 0.50  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.50 / 8.50 / 8.00   (all 3 samples: 8.33)
headings: h2 6
on threshold: motivation, audience, coordination, implementation
splits: audience[3] 2/2/1  implementation[1] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 1/1/1  -> 1.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 3 of 21 passes): A user-defined diagnostic message can provide additional information that can help developers more quickly understand why a particular assertion failed and how to resolve the issue.
candidate 3 (found by 3 of 21 passes): The diagnostic message must also be accessible to the user-defined contract-violation handler as this is a primary motivation to add the feature.

## audience - grade 1.33 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/1  -> 1.67
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 1 of 21 passes): including deployment experience in libc++ and the LLVM codebase ([[P3460R0](https://wg21.link/p3460r0)])
candidate 3 (found by 1 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 4 (found by 1 of 21 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:

## prior_art - grade 2.00 (fired in 2 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 2/2/2  -> 2.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 2 of 21 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as ignorable constructs.
candidate 3 (found by 1 of 21 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([[P3460R0](https://wg21.link/p3460r0)]), the time has come to propose standardising this feature for C++29.
candidate 4 (found by 1 of 21 passes): Option A requires no additional syntax apart from what [[P3400R1](https://wg21.link/p3400r1)] already provides, and is the most extensible.

## vehicle - grade 0.50 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase, the time has come to propose standardising this feature for C++29.

## coordination - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
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

## implementation - grade 2.00  [binary: max] (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 1/1/1  -> 1.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 2 of 21 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header <contracts> are required.
candidate 3 (found by 1 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 4 (found by 1 of 21 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header `<contracts>` are required.

-->
