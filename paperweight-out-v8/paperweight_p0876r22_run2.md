Verdict: Strong (9/14)

The paper offers solid grounding in implementation experience and a clear articulation of why stackful context switching cannot be expressed in portable C++, but its case thins considerably when it comes to showing who is affected and why standardization—rather than a library or tooling convention—is the necessary remedy.

- The strongest support comes from concrete implementation evidence, including measured fiber-switch costs and prior Boost experience with exception behavior.
- The paper clearly establishes that the facility cannot be written in portable C++ and that standardization would enable fiber awareness in debuggers and performance analyzers.
- The most glaring omission is the lack of established evidence about the affected user base, with only a single uncorroborated deployment claim from Baidu’s bthread.
- The paper also does not adequately establish why a library or existing practice cannot suffice, since the portability and tooling arguments are asserted rather than demonstrated against realistic alternatives.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.33/14)

Provisionally addressed: 7 of 7. Provisional points: 9.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.33   corroborated 8.67   accumulate 9.67   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 1.67  vehicle 1.17  coordination 0.50  insufficiency 1.00  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.50 / 8.50 / 10.50   (all 3 samples: 9.33)
headings: h2 6
on threshold: audience, prior_art, vehicle, insufficiency
splits: motivation[6] 0/2/1  prior_art[2] 2/1/1  prior_art[5] 2/0/2  vehicle[5] 0/0/1
        coordination[4] 0/0/2  coordination[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 3 of 4)              0/2/1  -> 1.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 2 (found by 3 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.
candidate 3 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 4 (found by 2 of 30 passes): Sometimes it is useful to inject a new function (for instance, to throw an exception or assign the synthesized fiber to the caller as described in returning synthesized `fiber_context` object from `resume()`) into a suspended fiber.

## audience - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Baidu’s bthread <ins>53</ins> has 1 million+ deployed instances (not counting clients) and thousands of kinds of services.

## prior_art - grade 1.67 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     2/1/1  -> 1.33
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/0/2  -> 1.33
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 2 (found by 2 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 3 (found by 2 of 30 passes): P4003R0 suggests a special recycling frame allocator which must be propagated through the call chain.
candidate 4 (found by 2 of 30 passes): P3346R0<ins>39 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.66</ins>

## vehicle - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              0/0/1  -> 0.33
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.

## coordination - grade 0.50 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              0/0/2  -> 0.67
  [5] Revision History  (part 2 of 4)              1/0/0  -> 0.33
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 2 (found by 3 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,46 branch fiber).
candidate 3 (found by 2 of 30 passes): Boost.Context patch that produces correct fiber-specific exception behavior on Windows and Linux using libstdc++.
candidate 4 (found by 2 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified

-->
