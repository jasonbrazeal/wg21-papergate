Verdict: Strong (8/14)

The paper offers solid grounding in implementation experience and prior art, but its case for standardization is uneven: the central argument that the facility cannot be written portably is asserted rather than demonstrated, and the sections on affected users and interoperability are effectively absent.

- The strongest support comes from concrete implementation experience, including a measured 11-cycle fiber switch and use of fibers to model constexpr coroutines.
- The discussion of prior art is substantive, showing continuity with earlier proposals and a rejected alternative for fiber-specific `thread_local`.
- The thinnest part of the paper is its failure to establish who is affected or how the proposed facility would coordinate with existing standard library and tooling features.
- The most glaring omission is the lack of any established argument for why a standard library facility, rather than a non-portable implementation-specific extension, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 5 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.00   accumulate 8.17   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.17  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.50 / 8.00 / 8.00   (all 3 samples: 8.17)
headings: h2 7
on threshold: vehicle, insufficiency
splits: motivation[5] 2/2/0  vehicle[2] 1/0/0  implementation[4] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              2/2/0  -> 1.33
  [6] Revision History  (part 3 of 3)              2/2/2  -> 2.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 3 of 30 passes): A kernel-level context switch is several orders of magnitude slower than a context switch at user-level.
candidate 3 (found by 2 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 4 (found by 2 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              0/0/0  -> 0.00
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              2/2/2  -> 2.00
  [6] Revision History  (part 3 of 3)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R312 and P0876R22.36
candidate 2 (found by 3 of 30 passes): P3346R0<ins>40 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.
candidate 3 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 4 (found by 2 of 30 passes): P0876R8 diverged from the recommendations of the second SG1 round in Cologne 2019.

## vehicle - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/0/0  -> 0.33
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): The API is suitable to act as building-block for high-level constructs such as stackful coroutines as well as cooperative multitasking
candidate 3 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              0/0/0  -> 0.00
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/0  -> 1.33
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              2/2/2  -> 2.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 2 (found by 3 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in (implemented in Boost.Context,47 branch fiber).
candidate 3 (found by 2 of 30 passes): enumerates a number of higher-level abstraction libraries built upon the *[Boost.Context](http://www.boost.org/doc/libs/release/libs/context/doc/html/index.html)* implementation of the API proposed in this paper.
candidate 4 (found by 2 of 30 passes): Consider [the following program](https://github.com/secondlife/3p-boost/blob/nat/exstate/tests/early_exc_destroy.cpp).

-->
