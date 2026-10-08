Verdict: Strong (11/14)

The paper gives a reasonably solid account of why requiring `[u]intptr_t` would remove a real portability friction and align C++ with existing practice, but it is thinner when it comes to showing that the change has actually been exercised in implementations rather than merely observed as ubiquitous. The strongest material concerns the widespread availability of the types and the concrete costs of their optionality, while the least developed parts are the arguments that a library solution cannot suffice and that there is meaningful implementation experience behind the proposal.

- The paper clearly establishes that the optionality of `[u]intptr_t` creates portability burdens and has already forced awkward design choices in standard library work.
- It also shows that surveyed conforming implementations already provide the types, so the standardization ask is well aligned with current practice.
- The case for why a library-only approach would be inadequate is asserted through examples of cost and suboptimal workarounds, but not developed into a full argument.
- The paper claims implementation experience, but the cited survey and examples do not yet demonstrate experience with requiring the types as a normative change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.50/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.50   corroborated 9.00   accumulate 11.50   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 1.00  implementation 1.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 11.00 / 10.50 / 10.50   (all 3 samples: 10.50)
headings: h3 7   <- NOT h2, check the unit list
on threshold: audience, vehicle, coordination
splits: motivation[4] 1/1/0  motivation[5] 1/2/1  prior_art[5] 0/2/0  vehicle[5] 2/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Status quo                                   1/1/0  -> 0.67
  [5] Impact analysis                              1/2/1  -> 1.33
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): However, `[u]intptr_t` being *optional* forces sub-optimal design choices such as making APIs optional or introducing workarounds.
candidate 2 (found by 3 of 24 passes): This disconnect in platforms in which the C implementation does not provide `[u]intptr_t` may impact developer productivity in those platforms.
candidate 3 (found by 3 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.
candidate 4 (found by 2 of 24 passes): There is consensus that this the right approach, but there is not enough implementation experience.

## audience - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              2/2/2  -> 2.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 2 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms.
candidate 3 (found by 2 of 24 passes): A survey found ubiquitous support for `[u]intptr_t` in *conforming* C++ implementations (*):
candidate 4 (found by 1 of 24 passes): We found that the following non-conforming platforms may be impacted by C++ requiring `[u]intptr_t`: - **[IBM i](https://www.ibm.com/products/ibm-i?utm_content=SRCWW&p1=Search&p4=43700074687253318&p5=e&p9=58700008221000440&gclid=EAIaIQobChMI9p6L2tXBhgMVKhOtBh0RBApyEAAYASAAEgKFSvD_BwE&gclsrc=aw.ds)**

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
candidate 3 (found by 2 of 24 passes): C and C++ do not currently provide an integer type suited for this use case, but some implementations do provide it as an extension, in platforms were this distinction is crucial, e.g., CHERI C/C++ implementations provide `ptraddr_t` in `<stddef.h>`
candidate 4 (found by 1 of 24 passes): We did not find any *conforming* implementation that is inconsistent in C and C++ with respect to the availability of `[u]intptr_t`: all implementations found provide these types in the headers of both programming languages.

## vehicle - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              2/1/0  -> 1.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This proposal advocates for requiring `[u]intptr_t` in C++ to ensure that all C++ code can rely on integer types capable of holding a pointer value.
candidate 2 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms. This has led to a large corpus of pre-existing code using `[u]intptr_t`. Requiring `[u]intptr_t` makes this code portable to all platforms C++ supports.
candidate 3 (found by 2 of 24 passes): Therefore, we conclude that C++ requiring `[u]intptr_t`: - does not regress current implementation support, and - does not require any implementation effort, for any currently conforming implementation.

## coordination - grade 1.50 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 2 (found by 3 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.

## insufficiency - grade 1.00 (fired in 2 of 8 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs
candidate 2 (found by 3 of 24 passes): There is a cost to doing nothing. Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.

## implementation - grade 1.00  [binary: max] (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms.
candidate 2 (found by 2 of 24 passes): This proposal advocates for requiring `[u]intptr_t` in C++ to ensure that all C++ code can rely on integer types capable of holding a pointer value.
candidate 3 (found by 1 of 24 passes): as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).

-->
