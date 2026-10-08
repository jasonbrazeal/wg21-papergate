Verdict: Adequate to Strong (7/14)

The paper offers solid support in the areas where the problem is most concrete: the timing constraint on coroutine frame allocation, the closed nature of the design space, and the inability of library-level mechanisms to intervene early enough. Its case is thinnest around the actual need for standardization, since the affected audience, the insufficiency of existing practice, and any implementation experience are asserted rather than demonstrated.

- The strongest support is the established argument that the allocator must be known before the coroutine body runs, which makes the standardization question both real and technically specific.
- The paper also convincingly shows that every viable mechanism reduces to parameter passing or ambient state, and that library facilities cannot close the timing gap.
- The weakest part is the absence of implementation experience, leaving the proposal without evidence that the design works outside the paper’s own framing.
- The most glaring omission is the lack of coordination and interoperability analysis, which is entirely unaddressed despite being essential for a language-level change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.67   accumulate 7.00   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 1.50  implementation 0.00
sample agreement: 98 of 105 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.50 / 6.50 / 8.00   (all 3 samples: 6.67)
headings: h2 14
on threshold: insufficiency
splits: prior_art[6] 1/0/1  prior_art[10] 1/2/2  vehicle[2] 1/0/0  vehicle[8] 0/0/2
        vehicle[12] 0/1/1  insufficiency[2] 0/1/0  insufficiency[13] 1/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            1/1/1  -> 1.00
  [6] 3. The Enumeration                           1/1/1  -> 1.00
  [7] 4. The Two Paths                             1/1/1  -> 1.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              2/2/2  -> 2.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   1/1/1  -> 1.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C++20 coroutines allocate their frame in `promise_type::operator new`, which the compiler calls before the coroutine body executes. Any mechanism that delivers the frame allocator after the coroutine is invoked arrives too late.
candidate 2 (found by 3 of 45 passes): The compiler passes exactly one set of runtime values to `operator new`: the frame size and the coroutine's parameter list. No other runtime information is available at that point.
candidate 3 (found by 3 of 45 passes): The cost is that every coroutine in a call chain must carry the allocator in its parameter list.
candidate 4 (found by 3 of 45 passes): A single allocator for every coroutine chain in the process is insufficient for deployments that need per-tenant budgets, bounded pools, or allocation tracking scoped to individual request chains.

## audience - grade 0.50 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
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
  [12] 9. Addressing TLS Concerns                   1/1/1  -> 1.00
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): A survey of platforms reveals that this concern, while intuitive, defends a platform combination that does not exist in practice.

## prior_art - grade 2.00 (fired in 8 of 15 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           1/0/1  -> 0.67
  [7] 4. The Two Paths                             2/2/2  -> 2.00
  [8] 5. The Rejected Alternatives                 2/2/2  -> 2.00
  [9] 6. The Design Space                          1/1/1  -> 1.00
  [10] 7. The Tradeoff                              1/2/2  -> 1.67
  [11] 8. The Hybrid                                1/1/1  -> 1.00
  [12] 9. Addressing TLS Concerns                   2/2/2  -> 2.00
  [13] 10. Anticipated Objections                   2/2/2  -> 2.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): [P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 5.2 documents the ergonomic consequences.
candidate 2 (found by 3 of 45 passes): A `coroutine_traits` specialization that detects an allocator parameter type and selects an allocator-aware promise is a compile-time optimization of Path A.
candidate 3 (found by 3 of 45 passes): Every row that delivers to `operator new` is either Path A (the allocator is in the parameter list) or Path B (the allocator is in ambient state).
candidate 4 (found by 3 of 45 passes): A conforming promise mixin ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [4] Section 7) provides both paths.

## vehicle - grade 0.67 (fired in 3 of 15 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Constraint                            0/0/0  -> 0.00
  [6] 3. The Enumeration                           0/0/0  -> 0.00
  [7] 4. The Two Paths                             0/0/0  -> 0.00
  [8] 5. The Rejected Alternatives                 0/0/2  -> 0.67
  [9] 6. The Design Space                          0/0/0  -> 0.00
  [10] 7. The Tradeoff                              0/0/0  -> 0.00
  [11] 8. The Hybrid                                0/0/0  -> 0.00
  [12] 9. Addressing TLS Concerns                   0/1/1  -> 0.67
  [13] 10. Anticipated Objections                   0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): The `operator new` timing gap is unique to the frame allocator.
candidate 2 (found by 1 of 45 passes): The design space is closed. The two solutions are `allocator_arg_t` (parameter passing) and thread-local propagation (ambient state).
candidate 3 (found by 1 of 45 passes): Each alternative that appears to offer a third path reduces to Path A, Path B, or arrives too late.

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

## insufficiency - grade 1.50 (fired in 3 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
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
  [13] 10. Anticipated Objections                   1/0/2  -> 1.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): `await_transform` can inject context into the child's `await_suspend`. It cannot influence the child's `operator new`. Too late.
candidate 2 (found by 2 of 45 passes): The only way to avoid the frame is to not use a coroutine, which means hand-writing the state machine the compiler generates.
candidate 3 (found by 1 of 45 passes): The design space is closed.
candidate 4 (found by 1 of 45 passes): It cannot inject a runtime value that is not already in the parameter list.

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
