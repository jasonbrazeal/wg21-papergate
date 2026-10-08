Verdict: Adequate (6/14)

The paper offers some concrete grounding in an implemented prototype and a clear motivation tied to `constexpr` exceptions, but it does not build a complete case for standardization. The thinnest areas are the absence of any identified affected audience, the lack of a demonstrated need for a standard rather than a library solution, and the reliance on assertions rather than evidence for alternatives, coordination, and the standardization rationale.

- The strongest support is the implementation experience: the proposal is explicitly described as minimal and implemented, with a linked Clang prototype and a Compiler Explorer example.
- The paper establishes why the issue matters by connecting it to completing `constexpr` exception support and avoiding surprising silent breakage.
- The discussion of prior art and alternatives is only claimed, since it reports LEWG’s preference for a conservative fix but does not establish why this alternative should be set aside.
- The most glaring omission is the complete absence of any account of who is affected, leaving the proposal without a demonstrated constituency or impact analysis.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.67   accumulate 7.17   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.17  vehicle 0.83  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 6.50 / 7.00   (all 3 samples: 6.33)
headings: h2 10
on threshold: implementation
splits: prior_art[4] 0/1/0  prior_art[5] 1/0/1  prior_art[7] 2/2/0  prior_art[9] 0/0/1
        vehicle[7] 0/0/2  coordination[1] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           2/2/2  -> 2.00
  [6] Proposed solution                            1/1/1  -> 1.00
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): To make `constexpr` exception support complete, and allow all functionality withing constant evaluation.
candidate 2 (found by 3 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.
candidate 3 (found by 3 of 33 passes): This is a minimal and implemented solution which doesn't limit functionality, but removes the break.
candidate 4 (found by 3 of 33 passes): This would make C++ much less surprising, but it will be probably a significant breaking change, altrough not really hard to fix

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

## prior_art - grade 1.17 (fired in 8 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/1/0  -> 0.33
  [5] Potentially-constant initilization           1/0/1  -> 0.67
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        2/2/0  -> 1.33
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/1  -> 0.33
  [10] Wording                                      1/1/1  -> 1.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by [P3068 *"constexpr exceptions"*](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3068r6.html) interacting with [potentially-constant initialization [expr.const]](https://eel.is/c++draft/expr.const#8).
candidate 2 (found by 3 of 33 passes): This paper was seen in previous revision by LEWG. It didn't get consensus and most of the group prefered the conservative approach of removing `constexpr` from `std::uncaught_exception()` and `std::current_exception()`.
candidate 3 (found by 3 of 33 passes): Also it returns back `constexpr` of `nested_exception` which was removed by [P3842R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3842r2.pdf) *"A conservative fix for constexpr uncaught_exceptions() and current_exception()"*.
candidate 4 (found by 2 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.

## vehicle - grade 0.83 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/0/2  -> 0.67
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Making this testing not mirror the runtime behaviour would break this model
candidate 2 (found by 1 of 33 passes): Therefore I argue against creating new variable, instead I propose taking proposal of this paper, which will make sure there is no breaking change.

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
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
candidate 1 (found by 1 of 33 passes): This is also prerequirement for proper work of `constexpr` coroutines, like exception being thrown out of `std::generator`.
candidate 2 (found by 1 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by P3068 "constexpr exceptions" interacting with potentially-constant initialization [expr.const].

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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
