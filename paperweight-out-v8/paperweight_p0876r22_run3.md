Verdict: Strong (8/14)

The paper offers solid grounding in prior work and practical implementation experience, but it leaves the case for standardization incomplete where it matters most: it does not show who is affected, how the facility would coordinate with existing language and library features, or why a library solution is insufficient beyond the bare observation that portable C++ cannot express stack switching. The strongest support is retrospective and technical, while the thinnest support concerns the actual need for a standard rather than a widely used implementation.

- The paper clearly situates itself against earlier proposals and rejected alternatives, and it demonstrates meaningful implementation experience through Boost and measured context-switch costs.
- The claim that the facility cannot be written in portable C++ is credited as a reason the problem matters, but it is not enough on its own to establish why standardization is necessary.
- The paper does not establish who is affected by the absence of a standard facility, leaving the audience and impact unclear.
- The most glaring omission is the lack of any established discussion of coordination and interoperability with the rest of the standard, which is essential for a facility touching execution stacks and exceptions.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.00 / 8.00 / 8.00   (all 3 samples: 8.00)
headings: h2 6
on threshold: vehicle, insufficiency
splits: prior_art[2] 1/1/2  implementation[2] 1/0/0  implementation[4] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 3 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.
candidate 3 (found by 3 of 30 passes): A kernel-level context switch is several orders of magnitude slower than a context switch at user-level.
candidate 4 (found by 2 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/2  -> 1.33
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 2 (found by 3 of 30 passes): P0876R8 diverged from the recommendations of the second SG1 round in Cologne 2019.
candidate 3 (found by 3 of 30 passes): P3346R0<ins>39 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.66</ins>
candidate 4 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified

## vehicle - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
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
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/0/0  -> 0.33
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/0/2  -> 1.33
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 2 (found by 2 of 30 passes): Boost.Context patch that produces correct fiber-specific exception behavior on Windows and Linux using libstdc++.
candidate 3 (found by 2 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,46 branch fiber).
candidate 4 (found by 1 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.

-->
