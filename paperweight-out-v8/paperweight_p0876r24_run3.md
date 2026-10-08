Verdict: Strong (10/14)

The paper offers solid grounding in prior art and implementation experience, but its case for standardization is uneven: the strongest arguments concern what cannot be done portably and what has already been demonstrated in practice, while the weakest concern who is concretely affected and how the facility would coordinate with existing standard features. The absence of any established discussion of coordination and interoperability is the most conspicuous gap.

- The paper clearly establishes that stackful context switching cannot be written in portable C++ and that prior proposals and Boost.Context provide meaningful implementation and design experience.
- The claimed benefit for debuggers, performance analyzers, and higher-level frameworks is plausible but not tied to demonstrated demand or a concrete affected population.
- The paper does not establish how `fiber_context` would coordinate with existing standard facilities such as threads, thread_local, exceptions, or tooling interfaces.
- The claim about Baidu’s deployed bthread instances is asserted without supporting evidence, leaving the affected-user case thin.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 9.50   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.33  coordination 0.00  insufficiency 1.17  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.00 / 9.00 / 9.50   (all 3 samples: 9.50)
headings: h2 6
on threshold: audience, vehicle, insufficiency, implementation
splits: motivation[9] 0/2/2  vehicle[5] 2/0/0  insufficiency[4] 0/0/1  implementation[6] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 3)  (SHARED PASSAGE)
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
  [9] 1 Effects: Equivalent to:                    0/2/2  -> 1.33
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching without the need for a scheduler.
candidate 2 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 3 (found by 2 of 30 passes): One particularly valuable consequence of adding `fiber_context` to the Standard will be to add fiber awareness to debuggers, performance analyzers and other tools that inspect a running C++ program.
candidate 4 (found by 2 of 30 passes): A low-level API enables a rich set of higher-level frameworks that provide specific syntaxes/semantics suitable for specific domains.

## audience - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Baidu’s bthread <ins>55</ins> has 1 million+ deployed instances (not counting clients) and thousands of kinds of services.

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              2/2/2  -> 2.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              1/1/1  -> 1.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): P3346R0<ins>41 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.68</ins>
candidate 2 (found by 3 of 30 passes): implemented in Boost.Context,<ins>48</ins> branch fiber
candidate 3 (found by 2 of 30 passes): This revision addresses concerns, questions and suggestions from the past meetings. The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 4 (found by 2 of 30 passes): P3620R0 notes that thread_local storage is shared between all the fibers on a thread. P3346R0 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław.

## vehicle - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              2/0/0  -> 0.67
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.
candidate 3 (found by 1 of 30 passes): A low-level API enables a rich set of higher-level frameworks that provide specific syntaxes/semantics suitable for specific domains.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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

## insufficiency - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              0/0/1  -> 0.33
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): A higher-level fiber-based library that emulates the std::thread API, such as Boost.Fiber, necessarily implements a fiber scheduler, permitting implicit fiber suspension.

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              1/0/0  -> 0.33
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 2 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 3 (found by 1 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,48 branch fiber).

-->
