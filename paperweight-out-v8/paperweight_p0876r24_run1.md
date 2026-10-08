Verdict: Strong (9/14)

The paper offers solid grounding in prior art and implementation experience, but its case for standardization rests heavily on a single technical claim—that stackful context switching cannot be done portably—and it does not adequately develop the broader rationale around affected users, coordination with other facilities, or why a library approach is insufficient.

- The strongest support comes from demonstrated implementation experience, including concrete performance data and use in constexpr coroutine modeling.
- The paper also clearly situates itself against prior proposals and existing Boost practice, establishing that the design has been explored and refined.
- The thinnest support is in showing who is affected and why standardization specifically is needed, since the paper asserts rather than demonstrates the limits of portable library implementations and the value of standardizing this particular low-level API.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.67   accumulate 9.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 1.00  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 6
on threshold: vehicle, insufficiency
splits: motivation[5] 2/2/0  motivation[9] 2/0/0  audience[5] 2/0/2  prior_art[2] 1/2/1
        coordination[5] 0/2/0  implementation[6] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 3 of 4)              2/2/0  -> 1.33
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/0/0  -> 0.67
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 3 of 30 passes): Symmetric fibers are more efficient, have fewer restrictions (no caller-callee relationship) and can be used to create a wider set of applications (generators, cooperative multitasking, backtracking ...).
candidate 3 (found by 2 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 4 (found by 1 of 30 passes): This paper proposes a minimal API that enables stackful context switching without the need for a scheduler.

## audience - grade 0.67 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              2/0/2  -> 1.33
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Baidu’s bthread <ins>55</ins> has 1 million+ deployed instances (not counting clients) and thousands of kinds of services.

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/2/1  -> 1.33
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              1/1/1  -> 1.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 2 (found by 3 of 30 passes): P3346R0<ins>41 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.68</ins>
candidate 3 (found by 3 of 30 passes): implemented in Boost.Context,<ins>48</ins> branch fiber
candidate 4 (found by 2 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified

## vehicle - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.
candidate 2 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/2/0  -> 0.67
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): A low-level API enables a rich set of higher-level frameworks that provide specific syntaxes/semantics suitable for specific domains.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              2/1/2  -> 1.67
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 2 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 3 (found by 2 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,48 branch fiber).
candidate 4 (found by 1 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,<ins>48</ins> branch fiber).

-->
