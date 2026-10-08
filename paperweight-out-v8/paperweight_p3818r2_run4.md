Verdict: Strong (8/14)

The paper gives a reasonably clear account of why the interaction it addresses matters and why a standard change is the appropriate remedy, but its support is uneven: the strongest material concerns motivation, alternatives, and implementation experience, while the case for who is affected and how the change coordinates with the broader ecosystem is largely asserted rather than shown.

- The paper most convincingly establishes that the proposed change addresses a real, surprising breakage introduced by constexpr exceptions and that a minimal implemented solution exists.
- It also adequately explains why a library-only approach would not suffice and why the standard is the right place for the fix.
- The discussion of coordination and interoperability gestures at important consequences, such as constexpr coroutines, but does not develop them into a demonstrated need.
- The paper never establishes who is affected by the problem, leaving the practical scope and urgency of the proposal largely unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 7.33   accumulate 8.33   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 1.50  coordination 0.33  insufficiency 0.50  implementation 2.00
sample agreement: 70 of 77 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.50 / 8.50 / 8.00   (all 3 samples: 8.00)
headings: h2 10
on threshold: prior_art, vehicle, implementation
splits: motivation[3] 2/1/1  prior_art[5] 1/1/2  prior_art[8] 1/0/1  prior_art[9] 0/1/0
        coordination[1] 0/1/0  coordination[5] 1/0/0  insufficiency[7] 0/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   2/1/1  -> 1.33
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           2/2/2  -> 2.00
  [6] Proposed solution                            1/1/1  -> 1.00
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by P3068 "constexpr exceptions" interacting with potentially-constant initialization [expr.const].
candidate 2 (found by 3 of 33 passes): To make `constexpr` exception support complete, and allow all functionality withing constant evaluation.
candidate 3 (found by 3 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.
candidate 4 (found by 3 of 33 passes): This is a minimal and implemented solution which doesn't limit functionality, but removes the break.

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/0/0  -> 0.00
  [8] Constant evaluation shouldn't diverge        0/0/0  -> 0.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 7 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           1/1/2  -> 1.33
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/0/1  -> 0.67
  [9] Implementation experience                    0/1/0  -> 0.33
  [10] Wording                                      1/1/1  -> 1.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by [P3068 *"constexpr exceptions"*](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3068r6.html) interacting with [potentially-constant initialization [expr.const]](https://eel.is/c++draft/expr.const#8).
candidate 2 (found by 3 of 33 passes): This paper was seen in previous revision by LEWG. It didn't get consensus and most of the group prefered the conservative approach of removing `constexpr` from `std::uncaught_exception()` and `std::current_exception()`.
candidate 3 (found by 3 of 33 passes): These two functions were stripped of `constexpr` modifier before releasing C++26 out of concerns of late changing behaviour with this paper.
candidate 4 (found by 3 of 33 passes): This is what P3820R0 proposes and [LEWG rejected it](https://wiki.isocpp.org/2025_Telecons:P3818).

## vehicle - grade 1.50 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Making this testing not mirror the runtime behaviour would break this model
candidate 2 (found by 2 of 33 passes): Therefore I argue against creating new variable, instead I propose taking proposal of this paper, which will make sure there is no breaking change.
candidate 3 (found by 1 of 33 passes): Because of the large impact, this is not proposed.

## coordination - grade 0.33 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           1/0/0  -> 0.33
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/0/0  -> 0.00
  [8] Constant evaluation shouldn't diverge        0/0/0  -> 0.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): This is also prerequirement for proper work of `constexpr` coroutines, like exception being thrown out of `std::generator`.
candidate 2 (found by 1 of 33 passes): These two functions were stripped of `constexpr` modifier before releasing C++26 out of concerns of late changing behaviour with this paper.

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/2/1  -> 1.00
  [8] Constant evaluation shouldn't diverge        0/0/0  -> 0.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Previous example shows multiple problems, even if we do introduce new function, we can still can't use it in `const int` variable initialization, because it would create new constant evaluation and fold into constant.

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            1/1/1  -> 1.00
  [7] Possible alternatives                        0/0/0  -> 0.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    2/2/2  -> 2.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This is a minimal and implemented solution which doesn't limit functionality, but removes the break.
candidate 2 (found by 3 of 33 passes): I also prototyped constexpr code coverage measurement
candidate 3 (found by 3 of 33 passes): The proposed solution was implemented in [my clang prototype of `constexpr` exception](https://github.com/hanickadot/llvm-project/commit/03fec7d6fc43d88e2d406201392c748d28f34357) for `std::uncaught_exceptions()`, and you can experiment with [it at the compiler explorer](https://compiler-explorer.com/z/Gsa3r74hr).

-->
