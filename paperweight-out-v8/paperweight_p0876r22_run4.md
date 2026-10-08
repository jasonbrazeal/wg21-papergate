Verdict: Strong (8/14)

The paper offers solid support in a few important areas, particularly its implementation experience and its account of prior art, but it leaves several core parts of the standardization case largely unargued. The thinnest support concerns who would be affected, how the facility would coordinate with existing standard components, and why a library solution is insufficient.

- The strongest support is the concrete implementation experience, including reported performance and work in libstdc++ and Boost.Context.
- The paper also clearly establishes prior art and alternatives by situating itself against earlier proposals and rejected directions.
- A notable weakness is that the affected audience is never identified, so the scope of the problem remains abstract.
- The most glaring omission is the lack of any established discussion of coordination and interoperability with the rest of the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 5 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 6.00   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.67  vehicle 1.33  coordination 0.00  insufficiency 1.17  implementation 2.00
sample agreement: 59 of 70 section-criterion pairs unanimous (84%)
single-sample totals would have been: 8.00 / 8.50 / 8.50   (all 3 samples: 7.83)
headings: h2 6
on threshold: motivation, prior_art, vehicle, insufficiency, implementation
splits: motivation[5] 2/0/2  motivation[6] 1/1/2  prior_art[5] 2/2/0  prior_art[6] 0/0/2
        vehicle[5] 0/2/0  insufficiency[5] 0/0/1  implementation[2] 1/0/0
        implementation[3] 2/0/1  implementation[4] 2/2/0  implementation[5] 0/1/0
        implementation[9] 2/0/0
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/0/2  -> 1.33
  [6] Revision History  (part 3 of 4)              1/1/2  -> 1.33
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 2 (found by 3 of 30 passes): Sometimes it is useful to inject a new function (for instance, to throw an exception or assign the synthesized fiber to the caller as described in returning synthesized `fiber_context` object from `resume()`) into a suspended fiber.
candidate 3 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 4 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.

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

## prior_art - grade 1.67 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              2/2/0  -> 1.33
  [6] Revision History  (part 3 of 4)              0/0/2  -> 0.67
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 2 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 3 (found by 2 of 30 passes): P0876R8 diverged from the recommendations of the second SG1 round in Cologne 2019.
candidate 4 (found by 2 of 30 passes): P3346R0<ins>39 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.66</ins>

## vehicle - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 4)              0/2/0  -> 0.67
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.

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
  [5] Revision History  (part 2 of 4)              0/0/1  -> 0.33
  [6] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): A higher-level fiber-based library that emulates the std::thread API, such as Boost.Fiber, necessarily implements a fiber scheduler, permitting implicit fiber suspension.

## implementation - grade 2.00  [binary: max] (fired in 6 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/0/0  -> 0.33
  [3] Recent WG21 History                          2/0/1  -> 1.00
  [4] Revision History  (part 1 of 4)              2/2/0  -> 1.33
  [5] Revision History  (part 2 of 4)              0/1/0  -> 0.33
  [6] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [7] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/0/0  -> 0.67
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): In Wrocław in November 2024, Nat Goodspeed presented implementation experience with libstdc++.
candidate 2 (found by 2 of 30 passes): Boost.Context patch that produces correct fiber-specific exception behavior on Windows and Linux using libstdc++.
candidate 3 (found by 2 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,46 branch fiber).
candidate 4 (found by 1 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.

-->
