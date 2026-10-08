Verdict: Adequate (7/14)

The paper offers a narrow but genuine basis for its standardization case, centered on a concrete interaction with P3068 and a working prototype, but it leaves several essential parts of the argument largely unaddressed. The strongest material concerns the problem’s origin and the existence of an implemented fix, while the thinnest areas are the absence of any identified user population and the lack of discussion about coordination or interoperability.

- The paper clearly ties its motivation to a specific silent breakage introduced by P3068 and explains why that interaction matters for constexpr exceptions.
- It provides implementation experience through a clang prototype and a compiler explorer link, and it documents prior discussion in LEWG, including the rejected alternative.
- The case for why the standard must change, rather than a library-level or other solution, is asserted but not substantiated.
- The paper never establishes who is affected by the problem or how the change would coordinate with existing practice and adjacent features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.33   accumulate 7.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.67  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 6.50 / 6.50   (all 3 samples: 6.50)
headings: h2 10
on threshold: prior_art, implementation
splits: motivation[6] 0/1/1  prior_art[9] 1/0/0  vehicle[7] 0/2/0  vehicle[8] 1/0/1
        insufficiency[7] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           2/2/2  -> 2.00
  [6] Proposed solution                            0/1/1  -> 0.67
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by P3068 "constexpr exceptions" interacting with potentially-constant initialization [expr.const].
candidate 2 (found by 3 of 33 passes): To make `constexpr` exception support complete, and allow all functionality withing constant evaluation.
candidate 3 (found by 3 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.
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

## prior_art - grade 1.50 (fired in 7 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           1/1/1  -> 1.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        2/2/2  -> 2.00
  [8] Constant evaluation shouldn't diverge        1/1/1  -> 1.00
  [9] Implementation experience                    1/0/0  -> 0.33
  [10] Wording                                      1/1/1  -> 1.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes solution to surprising silent code breakage introduced by [P3068 *"constexpr exceptions"*](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3068r6.html) interacting with [potentially-constant initialization [expr.const]](https://eel.is/c++draft/expr.const#8).
candidate 2 (found by 3 of 33 passes): This paper was seen in previous revision by LEWG. It didn't get consensus and most of the group prefered the conservative approach of removing `constexpr` from `std::uncaught_exception()` and `std::current_exception()`.
candidate 3 (found by 3 of 33 passes): This is a problem for `constexpr` exceptions, which needs `constexpr` marked functions in order for them work inside constant evaluation.
candidate 4 (found by 3 of 33 passes): This is what P3820R0 proposes and [LEWG rejected it](https://wiki.isocpp.org/2025_Telecons:P3818).

## vehicle - grade 0.67 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        0/2/0  -> 0.67
  [8] Constant evaluation shouldn't diverge        1/0/1  -> 0.67
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Making this testing not mirror the runtime behaviour would break this model
candidate 2 (found by 1 of 33 passes): Therefore I argue against creating new variable, instead I propose taking proposal of this paper, which will make sure there is no breaking change.

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

## insufficiency - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Past discussions                             0/0/0  -> 0.00
  [5] Potentially-constant initilization           0/0/0  -> 0.00
  [6] Proposed solution                            0/0/0  -> 0.00
  [7] Possible alternatives                        1/0/1  -> 0.67
  [8] Constant evaluation shouldn't diverge        0/0/0  -> 0.00
  [9] Implementation experience                    0/0/0  -> 0.00
  [10] Wording                                      0/0/0  -> 0.00
  [11] 17.9 Exception handling [support.exception]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This shows it's same functionality and it would burden users.

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
