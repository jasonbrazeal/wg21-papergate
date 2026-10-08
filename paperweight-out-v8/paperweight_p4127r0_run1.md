Verdict: Adequate to Strong (7/14)

The paper makes a focused case for the core technical problem and for the claim that existing library-level mechanisms cannot solve it, but it leaves several essential parts of the standardization argument largely unaddressed. The strongest material concerns the timing of coroutine frame allocation and the closure of the design space into two known paths, while the thinnest areas are the absence of any demonstrated user population, implementation experience, or coordination story.

- The paper clearly establishes why the allocator-delivery timing problem matters and why a library-only solution is insufficient.
- It credibly shows that prior art and plausible alternatives reduce to either parameter passing or ambient state, with no third path available.
- It asserts, but does not establish, that the problem requires standardization rather than being addressable through existing or conventional mechanisms.
- It offers no evidence about who is affected, no implementation experience, and no discussion of coordination or interoperability with related standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 7.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.83  implementation 0.00
sample agreement: 93 of 105 section-criterion pairs unanimous (89%)
single-sample totals would have been: 5.50 / 8.00 / 7.00   (all 3 samples: 6.83)
headings: h2 14
on threshold: none
splits: motivation[4] 0/1/0  motivation[7] 2/1/1  motivation[13] 0/1/1  prior_art[4] 0/0/2
        prior_art[9] 2/1/1  prior_art[11] 1/2/1  prior_art[13] 2/2/1  prior_art[15] 0/0/1
        vehicle[8] 0/2/2  vehicle[12] 0/2/0  insufficiency[2] 0/1/0  insufficiency[13] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 15 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/0  -> 0.33
  [5] 2. The Constraint                            2/2/2  -> 2.00
  [6] 3. The Enumeration                           1/1/1  -> 1.00
  [7] 4. The Two Paths                             2/1/1  -> 1.33
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              2/2/2  -> 2.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   0/1/1  -> 0.67
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

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/2  -> 0.67
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           1/1/1  -> 1.00
  [7] 4. The Two Paths                             2/2/2  -> 2.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          2/1/1  -> 1.33
  [10] 7. The Tradeoff                              1/1/1  -> 1.00
  [11] 8. The Hybrid                                1/2/1  -> 1.33
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   2/2/1  -> 1.67
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/1  -> 0.33
candidate 1 (found by 3 of 45 passes): C++20 provides a finite set of customization points for coroutines.
candidate 2 (found by 3 of 45 passes): [P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 5.2 documents the ergonomic consequences.
candidate 3 (found by 3 of 45 passes): Every row that delivers to `operator new` is either Path A (the allocator is in the parameter list) or Path B (the allocator is in ambient state).
candidate 4 (found by 3 of 45 passes): A conforming promise mixin ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 7) provides both paths.

## vehicle - grade 1.00 (fired in 2 of 15 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 0/2/2  -> 1.33
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/2/0  -> 0.67
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): Each alternative that appears to offer a third path reduces to Path A, Path B, or arrives too late.
candidate 2 (found by 1 of 45 passes): A sender-environment bridge wrapper is Path A with automation at one boundary. The viral signature pollution remains for the entire chain below.
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

## insufficiency - grade 1.83 (fired in 3 of 15 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/0/0  -> 0.00
  [13] 10. Anticipated Objections                   1/2/2  -> 1.67
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): `await_transform` can inject context into the child's `await_suspend`. It cannot influence the child's `operator new`. Too late.
candidate 2 (found by 2 of 45 passes): A function that contains `co_await` is a coroutine - it has a frame, allocated by the call expression, before `await_transform` runs.
candidate 3 (found by 1 of 45 passes): The design space is closed. The two solutions are `allocator_arg_t` (parameter passing) and thread-local propagation (ambient state).
candidate 4 (found by 1 of 45 passes): The wrapper is not present at internal call sites. It solves the sender-to-coroutine boundary but not the coroutine-to-coroutine chain.

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
