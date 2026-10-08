Verdict: Strong (9/14)

The paper gives a reasonably concrete account of the portability problem and the existing ecosystem pressure around `[u]intptr_t`, but its affirmative case for standardization leans heavily on assertion rather than demonstrated necessity. The strongest material concerns the real-world friction caused by optionality, while the thinnest concerns the absence of direct evidence that a standard mandate, rather than continued implementation practice or a library-level accommodation, is the necessary remedy.

- The paper establishes that optional `[u]intptr_t` creates measurable portability and design costs, with a concrete example in the libvlc change.
- It also establishes that prior art in both C and C++ has repeatedly converged on `[u]intptr_t` for pointer-capable integer APIs.
- The claim that existing widespread implementation support justifies a requirement is asserted, but the paper does not connect that prevalence to a demonstrated failure mode that only standardization can fix.
- The paper does not establish implementation experience with the proposed requirement itself, since the cited experience is with optional provision and workarounds rather than with mandatory `[u]intptr_t` under the proposed rules.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 7.67   accumulate 10.17   max 11.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 1.67  vehicle 1.00  coordination 1.33  insufficiency 0.50  implementation 1.00
sample agreement: 49 of 56 section-criterion pairs unanimous (88%)
single-sample totals would have been: 9.50 / 9.50 / 9.00   (all 3 samples: 9.00)
headings: h3 7   <- NOT h2, check the unit list
on threshold: audience, prior_art, vehicle, coordination
splits: motivation[5] 0/2/1  prior_art[4] 2/2/0  coordination[5] 2/0/0  coordination[6] 1/2/2
        insufficiency[3] 0/1/1  insufficiency[6] 1/0/0  implementation[3] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/2/1  -> 1.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.
candidate 2 (found by 2 of 24 passes): However, `[u]intptr_t` being *optional* forces sub-optimal design choices such as making APIs optional or introducing workarounds.
candidate 3 (found by 2 of 24 passes): This disconnect in platforms in which the C implementation does not provide `[u]intptr_t` may impact developer productivity in those platforms.
candidate 4 (found by 1 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).

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
candidate 3 (found by 1 of 24 passes): We found that the following non-conforming platforms may be impacted by C++ requiring `[u]intptr_t`: - **[IBM i](https://www.ibm.com/products/ibm-i?utm_content=SRCWW&p1=Search&p4=43700074687253318&p5=e&p9=58700008221000440&gclid=EAIaIQobChMI9p6L2tXBhgMVKhOtBh0RBApyEAAYASAAEgKFSvD_BwE&gclsrc=aw.ds)** ... - **[Elbrus](https://en.wikipedia.org/wiki/MCST)** ...
candidate 4 (found by 1 of 24 passes): We found that the following non-conforming platforms may be impacted by C++ requiring `[u]intptr_t`: - **IBM i** ... - **Elbrus** ...

## prior_art - grade 1.67 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   2/2/0  -> 1.33
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Proposals like [P2835](https://wg21.link/p2835) and [P3125](https://wg21.link/P3125) use `[u]intptr_t` as an integer type capable of holding a pointer value in their APIs.
candidate 2 (found by 2 of 24 passes): The C programming language proposal [N2889](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2889.htm) explored requiring `[u]intptr_t`. It was rejected for C23 but adopted into [ISO/IEC CD TS 6010 - A provenance-aware memory object model for C](https://www.iso.org/standard/81899.html) ([N3005](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3005.pdf)) to enable C to gain experience with the proposal.
candidate 3 (found by 2 of 24 passes): Adding new C++ types that are not available in C would reduce C++'s compatibility with C.
candidate 4 (found by 1 of 24 passes): C and C++ do not currently provide an integer type suited for this use case, but some implementations do provide it as an extension, in platforms were this distinction is crucial, e.g., CHERI C/C++ implementations provide `ptraddr_t` in `<stddef.h>`

## vehicle - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms. This has led to a large corpus of pre-existing code using `[u]intptr_t`. Requiring `[u]intptr_t` makes this code portable to all platforms C++ supports.

## coordination - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              2/0/0  -> 0.67
  [6] Design                                       1/2/2  -> 1.67
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs, as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).
candidate 2 (found by 3 of 24 passes): Platforms whose ABI specifies `intmax_t` to be smaller than the platform's pointer size are allowed to provide wider `[u]intptr_t` integer types since C23 and C++23 due to extended integer type support.
candidate 3 (found by 1 of 24 passes): C++ Platform ABIs specify the size and alignment of pointers and the calling convention of Integer types, fixing the ABI of `[u]intptr_t`.

## insufficiency - grade 0.50 (fired in 2 of 8 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   0/1/1  -> 0.67
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       1/0/0  -> 0.33
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): The potential absence of `[u]intptr_t` compromises the portability of high-level software and attempts to address this introduce software engineering overheads and potential portability bugs
candidate 2 (found by 1 of 24 passes): There is a cost to doing nothing. Significant time was spent on `atomic_ref::address` to find a sub-optimal solution when the right solution everyone agrees on is `uintptr_t`.

## implementation - grade 1.00  [binary: max] (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changelog                                    0/0/0  -> 0.00
  [3] Motivation                                   0/1/1  -> 0.67
  [4] Status quo                                   0/0/0  -> 0.00
  [5] Impact analysis                              0/0/0  -> 0.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording changes                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): All implementations surveyed provide these on all platforms.
candidate 2 (found by 1 of 24 passes): This proposal advocates for requiring `[u]intptr_t` in C++ to ensure that all C++ code can rely on integer types capable of holding a pointer value.
candidate 3 (found by 1 of 24 passes): as seen in [libvlc PR#1519](https://code.videolan.org/videolan/vlc/-/merge_requests/1519).

-->
