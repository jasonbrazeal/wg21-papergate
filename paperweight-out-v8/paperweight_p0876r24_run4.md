Verdict: Strong (9/14)

The paper offers solid grounding in prior art and implementation experience, but its case for standardization rests heavily on a single technical claim—that `fiber_context` cannot be written in portable C++—which is asserted rather than demonstrated, and the affected-user and interoperability arguments remain largely undeveloped.

- The strongest support comes from concrete implementation experience, including Boost.Context-derived libraries, measured context-switch costs, and use of fibers in constexpr coroutine implementations.
- The paper clearly establishes relevant prior art by superseding earlier proposals and pointing to Boost.Fiber and Boost.Context as working models.
- The thinnest part of the case is the repeated but unelaborated assertion that the facility cannot be written in portable C++, which carries much of the burden for both “why the standard” and “why a library will not do.”
- The most glaring omission is the lack of substantiation for who is affected beyond a single uncorroborated deployment figure from Baidu’s bthread.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.67   accumulate 9.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 1.00  implementation 2.00
sample agreement: 63 of 70 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 6
on threshold: vehicle, insufficiency
splits: motivation[4] 2/0/2  motivation[9] 1/1/2  audience[5] 2/2/0  coordination[5] 0/0/2
        implementation[2] 1/1/0  implementation[4] 0/1/0  implementation[6] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              2/0/2  -> 1.33
  [5] Revision History  (part 3 of 4)              2/2/2  -> 2.00
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    1/1/2  -> 1.33
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes a minimal API that enables stackful context switching **without** the need for a scheduler.
candidate 2 (found by 3 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 3 (found by 3 of 30 passes): Without fiber-specific exception state, `std::uncaught_exceptions` displays up to 2 (one exception in `main`, one in `fiber()`), and `std::current_exception` displays:
candidate 4 (found by 2 of 30 passes): A kernel-level context switch is several orders of magnitude slower than a context switch at user-level.

## audience - grade 0.67 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              2/2/0  -> 1.33
  [6] Revision History  (part 4 of 4)              0/0/0  -> 0.00
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Baidu’s bthread <ins>55</ins> has 1 million+ deployed instances (not counting clients) and thousands of kinds of services.

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
candidate 2 (found by 3 of 30 passes): Boost.Fiber<ins>50</ins> uses this pattern for resuming user-land threads.
candidate 3 (found by 3 of 30 passes): An implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,<ins>48</ins> branch fiber).
candidate 4 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified

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
candidate 1 (found by 2 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++.
candidate 2 (found by 1 of 30 passes): Because it creates and switches between different function call stacks, though, the `fiber_context` facility cannot be written in portable C++. There is real value to integrating this library into the Standard.

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 4)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 4)              0/0/0  -> 0.00
  [5] Revision History  (part 3 of 4)              0/0/2  -> 0.67
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

## implementation - grade 2.00  [binary: max] (fired in 5 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] abstract                                     1/1/0  -> 0.67
  [3] Revision History  (part 1 of 4)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 4)              0/1/0  -> 0.33
  [5] Revision History  (part 3 of 4)              0/0/0  -> 0.00
  [6] Revision History  (part 4 of 4)              1/2/1  -> 1.33
  [7] acknowledgments                              0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] 1 Effects: Equivalent to:                    2/2/2  -> 2.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): With a Boost implementation which predates the proposed changes to [[except]](https://eel.is/c++draft/except) (in an Itanium C++ ABI environment), it is possible to observe cases where an exception is destroyed at a different point than specified
candidate 2 (found by 2 of 30 passes): It’s telling that when Hana Dusikova was working on implementations of P3367R3 constexpr coroutines, the “easiest way to model a coroutine,” the “obvious first choice,” was to use fibers in the constexpr evaluator.
candidate 3 (found by 2 of 30 passes): enumerates a number of higher-level abstraction libraries built upon the *[Boost.Context](http://www.boost.org/doc/libs/release/libs/context/doc/html/index.html)* implementation of the API proposed in this paper.
candidate 4 (found by 2 of 30 passes): A fiber switch takes 11 CPU cycles on a x86_64-Linux system† using an implementation based on the strategy described in fiber switch using the calling convention (implemented in Boost.Context,<ins>48</ins> branch fiber).

-->
