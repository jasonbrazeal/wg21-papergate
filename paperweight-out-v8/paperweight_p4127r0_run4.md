Verdict: Adequate to Strong (8/14)

The paper makes a solid case that the frame-allocation timing problem is real, that the design space collapses to two paths, and that no library-level mechanism can reach the allocator in time. The support is thinnest around the human and practical dimensions: who is actually affected, whether the feature interoperates with existing coroutine machinery, and whether anyone has tried building it.

- The strongest support is the closed analysis showing every alternative reduces to passing the allocator as a parameter, using ambient state, or arriving too late.
- The paper also clearly establishes why a library solution cannot work, since the frame is allocated before any awaitable machinery can run.
- The most glaring omission is the absence of any account of who is affected and at what scale, which leaves the urgency of standardization ungrounded.
- Equally missing is implementation experience or coordination evidence, so the proposal offers no signal that the design has been validated in practice or can fit existing implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 7.83   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.67  coordination 0.00  insufficiency 2.00  implementation 0.00
sample agreement: 96 of 105 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.00 / 8.00 / 7.00   (all 3 samples: 7.67)
headings: h2 14
on threshold: vehicle
splits: motivation[4] 0/0/1  prior_art[2] 1/0/0  prior_art[4] 0/0/1  prior_art[6] 0/1/1
        prior_art[9] 1/1/2  prior_art[13] 1/2/1  vehicle[2] 1/0/0  vehicle[12] 2/2/0
        insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 15 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. The Constraint                            2/2/2  -> 2.00
  [6] 3. The Enumeration                           1/1/1  -> 1.00
  [7] 4. The Two Paths                             2/2/2  -> 2.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              2/2/2  -> 2.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   1/1/1  -> 1.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C++20 coroutines allocate their frame in `promise_type::operator new`, which the compiler calls before the coroutine body executes. Any mechanism that delivers the frame allocator after the coroutine is invoked arrives too late.
candidate 2 (found by 3 of 45 passes): To make `parse_header` a plain awaitable instead of a coroutine, one would have to hand-write the state machine the compiler generates.
candidate 3 (found by 3 of 45 passes): The compiler passes exactly one set of runtime values to `operator new`: the frame size and the coroutine's parameter list. No other runtime information is available at that point.
candidate 4 (found by 3 of 45 passes): The cost is that every coroutine in a call chain must carry the allocator in its parameter list.

## audience - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 0/0/0  -> 0.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/0/0  -> 0.00
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/1/1  -> 0.67
  [7] 4. The Two Paths                             2/2/2  -> 2.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          1/1/2  -> 1.33
  [10] 7. The Tradeoff                              1/1/1  -> 1.00
  [11] 8. The Hybrid                                1/1/1  -> 1.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   1/2/1  -> 1.33
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): [P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 5.2 documents the ergonomic consequences.
candidate 2 (found by 3 of 45 passes): `coroutine_traits<R, Args...>` selects the `promise_type` based on the coroutine's return type and parameter types. It operates at compile time. It can change *which* `operator new` runs. It cannot inject a runtime value that is not already in the parameter list.
candidate 3 (found by 3 of 45 passes): Every row that delivers to `operator new` is either Path A (the allocator is in the parameter list) or Path B (the allocator is in ambient state).
candidate 4 (found by 3 of 45 passes): A conforming promise mixin ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 7) provides both paths.

## vehicle - grade 1.67 (fired in 3 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   2/2/0  -> 1.33
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): Each alternative that appears to offer a third path reduces to Path A, Path B, or arrives too late.
candidate 2 (found by 2 of 45 passes): The `operator new` timing gap is unique to the frame allocator.
candidate 3 (found by 1 of 45 passes): The design space is closed.
candidate 4 (found by 1 of 45 passes): It cannot inject a runtime value that is not already in the parameter list.

## coordination - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 0/0/0  -> 0.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/0/0  -> 0.00
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 2.00 (fired in 3 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/1  -> 0.33
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/0/0  -> 0.00
  [13] 10. Anticipated Objections                   2/2/2  -> 2.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): A function that contains `co_await` is a coroutine - it has a frame, allocated by the call expression, before `await_transform` runs.
candidate 2 (found by 2 of 45 passes): The wrapper is not present at internal call sites. It solves the sender-to-coroutine boundary but not the coroutine-to-coroutine chain.
candidate 3 (found by 1 of 45 passes): To make `parse_header` a plain awaitable instead of a coroutine, one would have to hand-write the state machine the compiler generates.
candidate 4 (found by 1 of 45 passes): `await_transform` can inject context into the child's `await_suspend`. It cannot influence the child's `operator new`. Too late.

## implementation - grade 0.00  [binary: max] (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 0/0/0  -> 0.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/0/0  -> 0.00
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
