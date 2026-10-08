Verdict: Adequate to Strong (7/14)

The paper offers some grounding for its standardization case, chiefly through prior discussion, a rejected alternative, and a working prototype, but it leaves several essential justifications asserted rather than demonstrated. The thinnest areas are the absence of any identified affected audience and the largely unsupported claims about why the standard, rather than a library or other mechanism, is the right vehicle.

- The strongest support comes from the implementation experience, with a concrete clang prototype and a compiler explorer link showing the proposed behavior for `std::uncaught_exceptions()`.
- The paper also establishes prior art and alternatives by citing LEWG’s rejection of the conservative removal approach and connecting the proposal to P3068 and P3842R2.
- The case for why the standard must act is only claimed, relying on assertions about avoiding breaking changes rather than showing what standardization uniquely enables.
- The most glaring omission is that the paper never establishes who is affected by the problem, leaving the motivating population and impact unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 6.67   accumulate 7.67   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.33  coordination 0.17  insufficiency 0.17  implementation 2.00
sample agreement: 69 of 77 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.50 / 7.00 / 7.00   (all 3 samples: 7.17)
headings: h2 10
on threshold: prior_art, vehicle, implementation
splits: motivation[6] 1/0/1  prior_art[1] 1/1/0  prior_art[5] 1/0/1  prior_art[6] 0/1/0
        prior_art[9] 1/1/0  vehicle[8] 0/1/1  coordination[5] 1/0/0  insufficiency[7] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           2/2/2  -> 2.00
  [6] Proposed solution                            1/0/1  -> 0.67
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): To make `constexpr` exception support complete, and allow all functionality withing constant evaluation.
candidate 2 (found by 3 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.
candidate 3 (found by 3 of 33 passes): This would make C++ much less surprising, but it will be probably a significant breaking change, altrough not really hard to fix
candidate 4 (found by 3 of 33 passes): Making this testing not mirror the runtime behaviour would break this model

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

## prior_art - grade 1.50 (fired in 8 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           1/0/1  -> 0.67
  [6] Proposed solution                            0/1/0  -> 0.33
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    1/1/0  -> 0.67
  [10] Wording                                      1/1/1  -> 1.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper was seen in previous revision by LEWG. It didn't get consensus and most of the group prefered the conservative approach of removing `constexpr` from `std::uncaught_exception()` and `std::current_exception()`.
candidate 2 (found by 3 of 33 passes): This is what P3820R0 proposes and [LEWG rejected it](https://wiki.isocpp.org/2025_Telecons:P3818).
candidate 3 (found by 3 of 33 passes): Also it returns back `constexpr` of `nested_exception` which was removed by [P3842R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3842r2.pdf) *"A conservative fix for constexpr uncaught_exceptions() and current_exception()"*.
candidate 4 (found by 2 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by [P3068 *"constexpr exceptions"*](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3068r6.html) interacting with [potentially-constant initialization [expr.const]](https://eel.is/c++draft/expr.const#8).

## vehicle - grade 1.33 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        0/1/1  -> 0.67
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Therefore I argue against creating new variable, instead I propose taking proposal of this paper, which will make sure there is no breaking change.
candidate 2 (found by 2 of 33 passes): Making this testing not mirror the runtime behaviour would break this model
candidate 3 (found by 1 of 33 passes): Because of the large impact, this is not proposed.

## coordination - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
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
candidate 1 (found by 1 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.

## insufficiency - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        1/0/0  -> 0.33
  [8] Constant evaluation shouldn't diverge        0/0/0  -> 0.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): This shows it's same functionality and it would burden users.

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
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
