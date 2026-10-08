Verdict: Strong (9/14)

The paper offers solid support for the relevance of `[u]intptr_t` and for the existence of prior art and coordination needs, but its case is much thinner when it comes to demonstrating who is concretely affected, why a library solution is insufficient, and what implementation experience actually exists.

- The strongest part of the paper is its demonstration that `[u]intptr_t` already appears in related proposals and C provenance work, and that inventing C++-only alternatives would harm C compatibility.
- The paper also credibly establishes that the absence of `[u]intptr_t` creates portability and API-design friction, with the `atomic_ref::address` discussion and libvlc example providing concrete motivation.
- The weakest established area is implementation experience: the paper asserts ubiquitous support but does not turn that survey into evidence that standardizing the requirement has been exercised in practice.
- The most glaring omission is the failure to establish why a library-level solution would not suffice, since the paper gestures at portability overheads without showing that non-standard library approaches are inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 8.33   accumulate 9.33   max 10.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.33  coordination 1.50  insufficiency 0.17  implementation 1.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.00 / 8.50 / 9.50   (all 3 samples: 9.00)
headings: h3 7   <- NOT h2, check the unit list
on threshold: vehicle, coordination
splits: motivation[4] 0/0/1  audience[5] 1/0/1  vehicle[5] 0/0/2  insufficiency[3] 1/0/0
        implementation[3] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Status quo                                   0/0/1  -> 0.33
  [5] Impact analysis                              1/1/1  -> 1.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 2 (found by 3 of 24 passes): This disconnect in platforms in which the C implementation does not provide `[u]intptr_t` may impact developer productivity in those platforms.
candidate 3 (found by 3 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.
candidate 4 (found by 1 of 24 passes): There is consensus that this the right approach, but there is not enough implementation experience.

## audience - grade 1.00 (fired in 3 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              1/0/1  -> 0.67
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 2 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms.
candidate 3 (found by 2 of 24 passes): A survey found ubiquitous support for `[u]intptr_t` in *conforming* C++ implementations (*):

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   2/2/2  -> 2.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Proposals like [P2835](https://wg21.link/p2835) and [P3125](https://wg21.link/P3125) use `[u]intptr_t` as an integer type capable of holding a pointer value in their APIs.
candidate 2 (found by 3 of 24 passes): The C programming language proposal [N2889](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2889.htm) explored requiring `[u]intptr_t`. It was rejected for C23 but adopted into [ISO/IEC CD TS 6010 - A provenance-aware memory object model for C](https://www.iso.org/standard/81899.html) ([N3005](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3005.pdf)) to enable C to gain experience with the proposal.
candidate 3 (found by 3 of 24 passes): Adding new C++ types that are not available in C would reduce C++'s compatibility with C.

## vehicle - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/2  -> 0.67
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Requiring `[u]intptr_t` makes this code portable to all platforms C++ supports. Inventing new C++ types would make this code non-idiomatic and cause significant churn on all ecosystems for little added value.
candidate 2 (found by 1 of 24 passes): Therefore, we conclude that C++ requiring `[u]intptr_t`: - does not regress current implementation support, and - does not require any implementation effort, for any currently conforming implementation.
candidate 3 (found by 1 of 24 passes): Requiring `[u]intptr_t` makes this code portable to all platforms C++ supports.

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
candidate 1 (found by 3 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.
candidate 2 (found by 2 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 3 (found by 1 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/0/0  -> 0.33
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs

## implementation - grade 1.00  [binary: max] (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/0/0  -> 0.33
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms.
candidate 2 (found by 1 of 24 passes): as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).

-->
