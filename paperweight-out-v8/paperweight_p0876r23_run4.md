Verdict: Strong (8/14)

The paper offers meaningful support in a few areas, particularly implementation experience and prior art, but it leaves several core parts of the standardization case largely unargued. The thinnest support concerns who would be affected, how the facility would coordinate with existing language and library features, and why a library solution cannot suffice.

- The strongest support is the implementation experience, including Boost.Context, reported cycle counts, and use in a constexpr evaluator.
- The paper also establishes prior art by situating itself against earlier proposals and a rejected thread_local modification.
- The most glaring omission is the absence of any established account of who is affected by the proposed facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 5 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.33  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.00 / 8.50 / 9.00   (all 3 samples: 8.33)
headings: h2 7
on threshold: vehicle, insufficiency
splits: motivation[9] 2/0/0  vehicle[5] 0/0/2  vehicle[6] 0/1/0  implementation[3] 1/0/0
        implementation[5] 1/0/0  implementation[9] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              2/2/2  -> 2.00
  [6] Revision History  (part 3 of 3)              2/2/2  -> 2.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/0/0  -> 0.67
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 2 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 3 (found by 3 of 30 passes): A kernel-level context switch is several orders of magnitude slower than a context switch at user-level.
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
candidate 1 (found by 3 of 30 passes): P3346R0<ins>40 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.
candidate 2 (found by 2 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R312 and P0876R22.36
candidate 3 (found by 2 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 4 (found by 1 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.

## vehicle - grade 1.33 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              0/0/2  -> 0.67
  [6] Revision History  (part 3 of 3)              0/1/0  -> 0.33
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.
candidate 3 (found by 1 of 30 passes): A low-level API enables a rich set of higher-level frameworks that provide specific syntaxes/semantics suitable for specific domains.

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

## implementation - grade 2.00  [binary: max] (fired in 6 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          1/0/0  -> 0.33
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              1/0/0  -> 0.33
  [6] Revision History  (part 3 of 3)              2/2/2  -> 2.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/2/0  -> 0.67
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 2 (found by 3 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in (implemented in Boost.Context,47 branch fiber).
candidate 3 (found by 2 of 30 passes): enumerates a number of higher-level abstraction libraries built upon the *[Boost.Context](http://www.boost.org/doc/libs/release/libs/context/doc/html/index.html)* implementation of the API proposed in this paper.
candidate 4 (found by 1 of 30 passes): In Wrocław in November 2024, Nat Goodspeed presented implementation experience with libstdc++.

-->
