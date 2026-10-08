Verdict: Strong (9/14)

The paper offers solid grounding in implementation experience and a clear account of the motivating problem, but its broader case for standardization rests on repeated references to a single vendor extension rather than independent evidence. The thinnest support appears where the paper needs to show why a library solution is insufficient and how the feature would coordinate with existing or future contract machinery.

- The strongest support is the demonstrated Clang implementation and deployment experience in libc++ and the LLVM codebase.
- The paper also clearly establishes why user-defined diagnostic messages matter for assertion readability and handler access.
- Prior art and alternatives are adequately covered through the vendor attribute, the `assert(expr && "Reason")` idiom, and comparison with existing practice.
- The most glaring omission is the lack of a developed argument for why a library facility cannot provide the same capability without core language changes.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 7 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 9.33   accumulate 8.67   max 10.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.67  coordination 0.83  insufficiency 0.17  implementation 2.00
sample agreement: 43 of 49 section-criterion pairs unanimous (88%)
single-sample totals would have been: 9.00 / 8.50 / 8.50   (all 3 samples: 8.67)
headings: h2 6
on threshold: coordination, implementation
splits: prior_art[1] 1/0/0  prior_art[5] 1/1/0  vehicle[3] 2/1/1  coordination[3] 2/1/2
        insufficiency[3] 0/1/0  implementation[4] 0/1/1
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
candidate 3 (found by 2 of 21 passes): The diagnostic message must also be accessible to the user-defined contract-violation handler as this is a primary motivation to add the feature.
candidate 4 (found by 1 of 21 passes): The security implications of this are currently not fully understood.

## audience - grade 1.00 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.
candidate 2 (found by 2 of 21 passes): Anecdotally, when a C++ compiler implementer first encountered the specification for C++26 Contracts, their immediate reaction was:
candidate 3 (found by 1 of 21 passes): The idiom `assert(expr && "Reason")` has become a common workaround, and many non-standard assertion facilities provide explicit support for diagnostic messages.

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 2/2/2  -> 2.00
  [5] 3 Proposed wording                           1/1/0  -> 0.67
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 3 of 21 passes): Option B follows the existing practice in Clang. However, it is the most noisy syntax, places the message before the predicate, and represents functionality that does not meet our current litmus test for attributes as ignorable constructs.
candidate 3 (found by 2 of 21 passes): The proposed changes are relative to the C++26 DIS. Note that the wording proposed here overlaps with the wording proposed in [[P3423R1](https://wg21.link/p3423r1)].
candidate 4 (found by 1 of 21 passes): This functionality is frequently requested and already available in Clang via a vendor attribute.

## vehicle - grade 0.67 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/1/1  -> 1.33
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase, the time has come to propose standardising this feature for C++29.
candidate 2 (found by 1 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:

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
candidate 1 (found by 1 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 1 of 21 passes): The handler can then display, log, or otherwise process the message, separately from the predicate expression, in whichever way best suits the program and its environment.
candidate 3 (found by 1 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/1/0  -> 0.33
  [4] 2 Discussion                                 0/0/0  -> 0.00
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Discussion                                 0/1/1  -> 0.67
  [5] 3 Proposed wording                           0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This enabled Clang to implement user-defined diagnostic messages on top of C++26 Contracts, and they are available as a vendor attribute today:
candidate 2 (found by 2 of 21 passes): Option A matches the current implementation in Clang and has the advantage that no changes to header <contracts> are required.
candidate 3 (found by 1 of 21 passes): Now that we have some implementation experience with this vendor extension, including deployment experience in libc++ and the LLVM codebase ([[P3460R0](https://wg21.link/p3460r0)]), the time has come to propose standardising this feature for C++29.

-->
