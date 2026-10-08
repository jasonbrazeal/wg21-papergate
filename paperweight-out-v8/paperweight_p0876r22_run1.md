Verdict: Strong (8/14)

The paper offers meaningful support in a few areas—particularly prior art, implementation experience, and the value of tooling integration—but it leaves several core parts of its standardization case unproven, especially around affected users and coordination with the broader standard. The thinnest support concerns the argument that this facility belongs in the standard rather than in a library, since the paper asserts the point without developing it.

- The strongest support comes from implementation experience, including concrete performance data and evidence from constexpr coroutine work that fibers were the natural implementation choice.
- The paper also credibly establishes prior art and alternatives by tracing the evolution of earlier proposals and noting where the current design diverges from past committee feedback.
- The case for why the standard should contain this facility is asserted but not established, resting on the claim that portable C++ cannot express it without showing why standardization is the necessary remedy.
- The most glaring omission is the absence of any account of who is affected, leaving the proposal without a clear constituency or demonstrated need among C++ users.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 5 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 7.00   accumulate 8.17   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 1.00  coordination 0.00  insufficiency 1.17  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.50 / 7.50 / 8.00   (all 3 samples: 7.83)
headings: h2 6
on threshold: prior_art, vehicle, insufficiency, implementation
splits: prior_art[5] 2/0/2  insufficiency[5] 1/0/0  implementation[4] 2/0/2
        implementation[9] 0/2/2
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
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 2 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 3 (found by 3 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.
candidate 4 (found by 2 of 30 passes): Sometimes it is useful to inject a new function (for instance, to throw an exception or assign the synthesized fiber to the caller as described in returning synthesized `fiber_context` object from `resume()`) into a suspended fiber.

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

## prior_art - grade 1.67 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/0/2  -> 1.33
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 2 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 3 (found by 2 of 30 passes): P0876R8 diverged from the recommendations of the second SG1 round in Cologne 2019.
candidate 4 (found by 1 of 30 passes): P4003R0 suggests a special recycling frame allocator which must be propagated through the call chain.

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

## insufficiency - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              1/0/0  -> 0.33
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): Copying a `fiber_context` must not be permitted!

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/0/2  -> 1.33
  [5] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/2/2  -> 1.33
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 2 (found by 3 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,46 branch fiber).
candidate 3 (found by 2 of 30 passes): Boost.Context patch that produces correct fiber-specific exception behavior on Windows and Linux using libstdc++.
candidate 4 (found by 2 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified

-->
