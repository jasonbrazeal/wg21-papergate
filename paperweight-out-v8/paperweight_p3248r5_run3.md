Verdict: Strong (10/14)

The paper offers solid support for the core rationale, the existence of prior art, and the need for a standard solution, but its case is thinner when it comes to demonstrating who is concretely affected, why a library-level workaround cannot suffice, and whether there is meaningful implementation experience beyond a survey of existing practice.

- The strongest support is the documented prior art and the evidence that all surveyed conforming implementations already provide the types, which grounds the proposal in existing practice and related standardization efforts.
- The paper also clearly establishes why the standard is the right venue, since the absence of a guarantee creates portability burdens and the ABI implications are already fixed by platform conventions.
- The weakest part is the claim about who is affected, which relies on a single external example and a general assertion about portability rather than a broader demonstration of real-world impact.
- The most glaring omission is implementation experience, since the paper points to existing availability but does not show experience with the proposed normative requirement itself.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 10.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.67  coordination 1.50  insufficiency 0.50  implementation 1.00
sample agreement: 48 of 56 section-criterion pairs unanimous (86%)
single-sample totals would have been: 10.00 / 9.50 / 10.00   (all 3 samples: 9.50)
headings: h3 7   <- NOT h2, check the unit list
on threshold: vehicle, coordination
splits: motivation[5] 0/1/1  audience[3] 1/1/0  audience[5] 1/0/1  prior_art[5] 0/2/0
        vehicle[3] 0/0/1  vehicle[5] 2/0/2  coordination[5] 1/2/0  implementation[6] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/1/1  -> 0.67
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.
candidate 2 (found by 2 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 3 (found by 2 of 24 passes): This disconnect in platforms in which the C implementation does not provide `[u]intptr_t` may impact developer productivity in those platforms.
candidate 4 (found by 1 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs

## audience - grade 0.83 (fired in 3 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/0  -> 0.67
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              1/0/1  -> 0.67
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms.
candidate 2 (found by 2 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 3 (found by 2 of 24 passes): A survey found ubiquitous support for `[u]intptr_t` in *conforming* C++ implementations (*):

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   2/2/2  -> 2.00
  [5] Impact analysis                              0/2/0  -> 0.67
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Proposals like [P2835](https://wg21.link/p2835) and [P3125](https://wg21.link/P3125) use `[u]intptr_t` as an integer type capable of holding a pointer value in their APIs.
candidate 2 (found by 3 of 24 passes): The C programming language proposal [N2889](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2889.htm) explored requiring `[u]intptr_t`. It was rejected for C23 but adopted into [ISO/IEC CD TS 6010 - A provenance-aware memory object model for C](https://www.iso.org/standard/81899.html) ([N3005](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3005.pdf)) to enable C to gain experience with the proposal.
candidate 3 (found by 1 of 24 passes): We found that the following non-conforming platforms may be impacted by C++ requiring `[u]intptr_t`:
candidate 4 (found by 1 of 24 passes): This proposal advocates for Option 1, i.e., for C++ to require `[u]intptr_t`, because: - **Pre-existing code**: All implementations surveyed provide these on all platforms.

## vehicle - grade 1.67 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/1  -> 0.33
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              2/0/2  -> 1.33
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms. This has led to a large corpus of pre-existing code using `[u]intptr_t`. Requiring `[u]intptr_t` makes this code portable to all platforms C++ supports.
candidate 2 (found by 2 of 24 passes): We did not find any *conforming* implementation that is inconsistent in C and C++ with respect to the availability of `[u]intptr_t`: all implementations found provide these types in the headers of both programming languages.
candidate 3 (found by 1 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs

## coordination - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              1/2/0  -> 1.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 2 (found by 2 of 24 passes): Platforms whose ABI specifies `intmax_t` to be smaller than the platform's pointer size are allowed to provide wider `[u]intptr_t` integer types since C23 and C++23 due to extended integer type support.
candidate 3 (found by 1 of 24 passes): This disconnect in platforms in which the C implementation does not provide `[u]intptr_t` may impact developer productivity in those platforms.
candidate 4 (found by 1 of 24 passes): C++ Platform ABIs specify the size and alignment of pointers and the calling convention of Integer types, fixing the ABI of `[u]intptr_t`.

## insufficiency - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): There is a cost to doing nothing. Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.
candidate 2 (found by 1 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.

## implementation - grade 1.00  [binary: max] (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       0/1/1  -> 0.67
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This proposal advocates for requiring `[u]intptr_t` in C++ to ensure that all C++ code can rely on integer types capable of holding a pointer value.
candidate 2 (found by 2 of 24 passes): All implementations surveyed provide these on all platforms.

-->
