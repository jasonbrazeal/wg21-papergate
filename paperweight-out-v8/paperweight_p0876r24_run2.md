Verdict: Strong (9/14)

The paper offers meaningful support in a few areas, particularly prior art, implementation experience, and the performance motivation for a low-level context-switching facility, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who would be affected and why a library solution or existing coordination mechanisms would be insufficient.

- The strongest support comes from concrete implementation experience, including measured fiber-switch costs and existing libraries built on the proposed API.
- The paper also establishes relevant prior art by tracing earlier proposals and Boost.Fiber usage.
- The most glaring omission is any identification of the affected users or constituencies, which leaves the audience for standardization unclear.
- The arguments for why the standard is necessary and why a library will not do rest on repeated assertions about non-portability without being developed into a full case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 8.67   accumulate 8.50   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.17  coordination 0.33  insufficiency 1.00  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.00 / 9.00 / 8.50   (all 3 samples: 8.50)
headings: h2 6
on threshold: vehicle, insufficiency
splits: vehicle[5] 0/0/1  coordination[3] 0/2/0  implementation[2] 0/1/1
        implementation[5] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 2 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 3 (found by 3 of 30 passes): A kernel-level context switch is several orders of magnitude slower than a context switch at user-level.
candidate 4 (found by 1 of 30 passes): A static member function returning the active fiber requires a reference counted global variable and does not prevent accidentally attempting to resume the active fiber.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 4 of 4)              1/1/1  -> 1.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 2 (found by 3 of 30 passes): P0876R8 diverged from the recommendations of the second SG1 round in Cologne 2019.
candidate 3 (found by 3 of 30 passes): Boost.Fiber<ins>50</ins> uses this pattern for resuming user-land threads.
candidate 4 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified

## vehicle - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/1  -> 0.33
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): A low-level API enables a rich set of higher-level frameworks that provide specific syntaxes/semantics suitable for specific domains.

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/2/0  -> 0.67
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.

## insufficiency - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.

## implementation - grade 2.00  [binary: max] (fired in 5 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/1/1  -> 0.67
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/2/0  -> 0.67
  [6] Revision History  (part 4 of 4)              2/2/2  -> 2.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,<ins>48</ins> branch fiber).
candidate 2 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 3 (found by 2 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 4 (found by 1 of 30 passes): enumerates a number of higher-level abstraction libraries built upon the *[Boost.Context](http://www.boost.org/doc/libs/release/libs/context/doc/html/index.html)* implementation of the API proposed in this paper.

-->
