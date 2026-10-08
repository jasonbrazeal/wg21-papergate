Verdict: Strong (8/14)

The paper offers solid support in the areas of prior art, implementation experience, and the basic motivation for stackful context switching, but it leaves several essential parts of the standardization case largely unargued. The thinnest support concerns who is affected, how the facility would coordinate with existing standard features, and why a library solution is insufficient beyond the bare assertion that portable C++ cannot express it.

- The strongest support is the implementation experience, including concrete performance measurements, existing Boost usage, and reports from implementers working in both constexpr evaluation and libstdc++.
- The paper also establishes meaningful prior art by tracing its lineage through several earlier proposals and recording relevant committee feedback and rejections.
- The most glaring omission is the absence of any established account of who is affected by the proposal, leaving the audience and impact of the feature unclear.
- Equally unestablished is the coordination and interoperability story, since the paper does not show how the proposed facility would fit with the existing standard library, language rules, or tooling requirements.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 5 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 7.00   accumulate 8.33   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.33  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 62 of 70 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.50 / 7.50 / 8.00   (all 3 samples: 7.83)
headings: h2 7
on threshold: prior_art, vehicle, insufficiency
splits: motivation[9] 0/1/2  prior_art[5] 0/0/2  prior_art[6] 0/0/2  vehicle[6] 2/0/0
        implementation[2] 0/1/0  implementation[3] 0/1/0  implementation[5] 0/0/1
        implementation[9] 2/0/2
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
  [9] 1 Effects: Equivalent to:                    0/1/2  -> 1.00
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
  [4] Revision History  (part 1 of 3)              0/0/0  -> 0.00
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              0/0/2  -> 0.67
  [6] Revision History  (part 3 of 3)              0/0/2  -> 0.67
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed API supersedes the former proposals N3985, P0099R1, P0534R3 and P0876R2.
candidate 2 (found by 3 of 30 passes): P0876R8 diverged from the recommendations of the second SG1 round in Cologne 2019.
candidate 3 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 4 (found by 1 of 30 passes): P3346R0<ins>40 proposed to modify thread_local to mean fiber-specific. This was rejected by SG1 in Wrocław in 2024.67</ins>

## vehicle - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Recent WG21 History                          0/0/0  -> 0.00
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              0/0/0  -> 0.00
  [6] Revision History  (part 3 of 3)              2/0/0  -> 0.67
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): A low-level API enables a rich set of higher-level frameworks that provide specific syntaxes/semantics suitable for specific domains.

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

## implementation - grade 2.00  [binary: max] (fired in 6 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/1/0  -> 0.33
  [3] Recent WG21 History                          0/1/0  -> 0.33
  [4] Revision History  (part 1 of 3)              2/2/2  -> 2.00
  [5] Revision History  (part 2 of 3)              0/0/1  -> 0.33
  [6] Revision History  (part 3 of 3)              2/2/2  -> 2.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/0/2  -> 1.33
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in (implemented in Boost.Context,47 branch fiber).
candidate 2 (found by 2 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 3 (found by 1 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 4 (found by 1 of 30 passes): In Wrocław in November 2024, Nat Goodspeed presented implementation experience with libstdc++.

-->
