Verdict: Strong (8/14)

The paper offers solid grounding in existing practice, particularly through the Clang vendor attribute and its use in libc++ and LLVM, but it leaves several parts of the standardization case more asserted than demonstrated. The thinnest areas are the absence of any argument for why a library solution would be insufficient and the underdeveloped discussion of coordination and interoperability.

- The strongest support is the implementation experience, with the feature already available in Clang and deployed in real codebases.
- The paper also clearly establishes why the feature matters and that prior art exists, including a concrete vendor extension.
- The case for who is affected and why the standard should adopt this now rests mainly on anecdote and the fact of deployment rather than a broader demonstrated need.
- The most glaring omission is that the paper never addresses why a library-based approach would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.67   max 10.33

## SUMMARY
grades: motivation 1.67  audience 1.33  prior_art 2.00  vehicle 0.50  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.50 / 8.00 / 8.50   (all 3 samples: 8.33)
headings: h2 6
on threshold: motivation, audience, coordination, implementation
splits: motivation[4] 1/1/2  audience[3] 2/1/2  prior_art[5] 0/0/1  coordination[3] 2/2/1
        implementation[1] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 1/1/2  -> 1.33
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
  [3] 1 Motivation                                 2/1/2  -> 1.67
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 1 of 21 passes): including deployment experience in libc++ and the LLVM codebase ([[P3460R0](https://wg21.link/p3460r0)])
candidate 3 (found by 1 of 21 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:
candidate 4 (found by 1 of 21 passes): including deployment experience in libc++ and the LLVM codebase

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
candidate 2 (found by 3 of 21 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as ignorable constructs.
candidate 3 (found by 1 of 21 passes): The proposed changes are relative to the C++26 DIS. Note that the wording proposed here overlaps with the wording proposed in [[P3423R1](https://wg21.link/p3423r1)].

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

## coordination - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/1  -> 1.67
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today
candidate 2 (found by 1 of 21 passes): The handler can then display, log, or otherwise process the message, separately from the predicate expression, in whichever way best suits the program and its environment.

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
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
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
