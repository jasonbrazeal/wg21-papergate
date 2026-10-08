Verdict: Adequate to Strong (7/14)

The paper offers some grounding for its proposal through an implemented prototype and a clear statement of the problem it addresses, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas are the absence of any identified affected users, the lack of coordination or interoperability analysis, and only cursory treatment of alternatives and why a library-only solution would not suffice.

- The strongest support is the implementation experience, with a linked clang prototype and compiler explorer example demonstrating the proposed change.
- The paper clearly states why the issue matters, connecting it to surprising breakage from the interaction of constexpr exceptions with potentially-constant initialization.
- Prior art and alternatives are mentioned but not established, since the discussion of LEWG’s preference and the rejected library workaround is brief and does not show a full comparison.
- The most glaring omission is the complete absence of any account of who is affected by the problem or the proposed change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 7.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.17  vehicle 0.83  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 70 of 77 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.50 / 7.50 / 6.50   (all 3 samples: 6.67)
headings: h2 10
on threshold: implementation
splits: motivation[3] 1/2/1  motivation[6] 0/1/0  prior_art[1] 1/0/1  prior_art[5] 2/0/2
        vehicle[5] 1/0/1  vehicle[7] 0/2/0  insufficiency[7] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/2/1  -> 1.33
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           2/2/2  -> 2.00
  [6] Proposed solution                            0/1/0  -> 0.33
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): To make `constexpr` exception support complete, and allow all functionality withing constant evaluation.
candidate 2 (found by 3 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.
candidate 3 (found by 3 of 33 passes): This would make C++ much less surprising, but it will be probably a significant breaking change, altrough not really hard to fix
candidate 4 (found by 2 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by P3068 "constexpr exceptions" interacting with potentially-constant initialization [expr.const].

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

## prior_art - grade 1.17 (fired in 5 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/1  -> 0.67
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           2/0/2  -> 1.33
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/0/0  -> 0.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      1/1/1  -> 1.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper was seen in previous revision by LEWG. It didn't get consensus and most of the group prefered the conservative approach of removing `constexpr` from `std::uncaught_exception()` and `std::current_exception()`.
candidate 2 (found by 3 of 33 passes): I also prototyped constexpr code coverage measurement
candidate 3 (found by 3 of 33 passes): Also it returns back `constexpr` of `nested_exception` which was removed by [P3842R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3842r2.pdf) *"A conservative fix for constexpr uncaught_exceptions() and current_exception()"*.
candidate 4 (found by 2 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by [P3068 *"constexpr exceptions"*](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3068r6.html) interacting with [potentially-constant initialization [expr.const]](https://eel.is/c++draft/expr.const#8).

## vehicle - grade 0.83 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           1/0/1  -> 0.67
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/2/0  -> 0.67
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Making this testing not mirror the runtime behaviour would break this model
candidate 2 (found by 2 of 33 passes): In order to do we must make the potentially-constant initialization evaluation fail when it reaches these two function in question.
candidate 3 (found by 1 of 33 passes): Therefore I argue against creating new variable, instead I propose taking proposal of this paper, which will make sure there is no breaking change.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## insufficiency - grade 0.67 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        2/2/0  -> 1.33
  [8] Constant evaluation shouldn't diverge        0/0/0  -> 0.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Removing `constexpr` from `uncaught_exceptions` (not from `currrent_exception` as that one is not touched by the paper) and introduce a same function under similar name.
candidate 2 (found by 1 of 33 passes): Previous example shows multiple problems, even if we do introduce new function, we can still can't use it in `const int` variable initialization, because it would create new constant evaluation and fold into constant.

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
