Verdict: Adequate to Strong (7/14)

The paper offers solid support on the core technical obstruction—the `operator new` timing gap—and on why library-only workarounds cannot close it, but it leaves several practical and procedural questions underdeveloped. The thinnest areas are the absence of any demonstrated implementation experience beyond a citation and the lack of coordination or interoperability discussion.

- The strongest part of the paper is its demonstration that the frame allocator must be available before the coroutine body runs, making post-invocation delivery mechanisms irrelevant.
- The paper also convincingly shows that avoiding the problem without language or library standardization would require hand-writing compiler-generated state machines.
- The case for who is affected rests on an assertion about platform combinations rather than evidence of real-world impact.
- The most glaring omission is any account of how the proposed facility would coordinate with existing coroutine machinery or interoperate across implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.00   accumulate 7.83   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.67  implementation 0.67
sample agreement: 92 of 105 section-criterion pairs unanimous (88%)
single-sample totals would have been: 8.00 / 9.00 / 5.50   (all 3 samples: 7.50)
headings: h2 14
on threshold: insufficiency
splits: motivation[13] 1/0/1  audience[12] 0/1/0  prior_art[4] 1/0/0  prior_art[6] 0/0/1
        prior_art[9] 1/1/2  prior_art[13] 1/2/2  prior_art[15] 0/1/0  vehicle[8] 2/2/0
        vehicle[12] 2/0/0  insufficiency[2] 0/0/1  insufficiency[5] 2/1/1
        insufficiency[7] 0/1/0  implementation[15] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 15 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            2/2/2  -> 2.00
  [6] 3. The Enumeration                           1/1/1  -> 1.00
  [7] 4. The Two Paths                             1/1/1  -> 1.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              2/2/2  -> 2.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   1/0/1  -> 0.67
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C++20 coroutines allocate their frame in `promise_type::operator new`, which the compiler calls before the coroutine body executes. Any mechanism that delivers the frame allocator after the coroutine is invoked arrives too late.
candidate 2 (found by 3 of 45 passes): The cost is that every coroutine in a call chain must carry the allocator in its parameter list.
candidate 3 (found by 3 of 45 passes): The `operator new` timing gap is unique to the frame allocator.
candidate 4 (found by 2 of 45 passes): To make `parse_header` a plain awaitable instead of a coroutine, one would have to hand-write the state machine the compiler generates.

## audience - grade 0.17 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [12] 9. Addressing TLS Concerns                   0/1/0  -> 0.33
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): A survey of platforms reveals that this concern, while intuitive, defends a platform combination that does not exist in practice.

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/1  -> 0.33
  [7] 4. The Two Paths                             2/2/2  -> 2.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          1/1/2  -> 1.33
  [10] 7. The Tradeoff                              1/1/1  -> 1.00
  [11] 8. The Hybrid                                1/1/1  -> 1.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   1/2/2  -> 1.67
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/1/0  -> 0.33
candidate 1 (found by 3 of 45 passes): [P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 5.2 documents the ergonomic consequences.
candidate 2 (found by 3 of 45 passes): Every row that delivers to `operator new` is either Path A (the allocator is in the parameter list) or Path B (the allocator is in ambient state).
candidate 3 (found by 3 of 45 passes): Path A makes the allocator visible in every signature. Path B makes it invisible.
candidate 4 (found by 3 of 45 passes): A conforming promise mixin ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 7) provides both paths.

## vehicle - grade 1.00 (fired in 2 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 2/2/0  -> 1.33
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   2/0/0  -> 0.67
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): A sender-environment bridge wrapper is Path A with automation at one boundary. The viral signature pollution remains for the entire chain below.
candidate 2 (found by 1 of 45 passes): A `coroutine_traits` specialization that detects an allocator parameter type and selects an allocator-aware promise is a compile-time optimization of Path A.
candidate 3 (found by 1 of 45 passes): The `operator new` timing gap is unique to the frame allocator.

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

## insufficiency - grade 1.67 (fired in 5 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            2/1/1  -> 1.33
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/1/0  -> 0.33
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/0/0  -> 0.00
  [13] 10. Anticipated Objections                   1/1/1  -> 1.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): To make `parse_header` a plain awaitable instead of a coroutine, one would have to hand-write the state machine the compiler generates.
candidate 2 (found by 3 of 45 passes): The only way to avoid the frame is to not use a coroutine, which means hand-writing the state machine the compiler generates.
candidate 3 (found by 2 of 45 passes): `await_transform` can inject context into the child's `await_suspend`. It cannot influence the child's `operator new`. Too late.
candidate 4 (found by 1 of 45 passes): The design space is closed. The two solutions are `allocator_arg_t` (parameter passing) and thread-local propagation (ambient state).

## implementation - grade 0.67  [binary: max] (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
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
  [15] References                                   0/2/0  -> 0.67
candidate 1 (found by 1 of 45 passes): [2] [cppalliance/corosio](https://github.com/cppalliance/corosio) - Coroutine-native networking library.

-->
