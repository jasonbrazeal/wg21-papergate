Verdict: Adequate (7/14)

The paper offers a mixed case for its own standardization: it grounds itself in recognizable prior art and points to real implementation experience, but it leaves several central justifications asserted rather than demonstrated. The thinnest support concerns the affected audience, the insufficiency of a library-only solution, and the concrete need for a standard facility.

- The strongest support is the implementation experience, with named projects and reference implementations showing the ideas have been exercised outside the paper.
- The prior art and alternatives section is also solid, connecting the design to existing coroutine task work and monadic sender concepts.
- The most glaring omission is the absence of any established audience or user community that would be affected by standardization.
- The paper likewise does not establish why a library solution would be inadequate, leaving the core rationale for a standard unwritten.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.67   accumulate 7.17   max 7.33

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 131 of 140 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.00 / 6.00   (all 3 samples: 6.50)
headings: h2 19
on threshold: motivation, implementation
splits: motivation[9] 1/0/0  motivation[14] 2/1/2  motivation[16] 0/1/1  motivation[17] 0/2/0
        motivation[18] 1/0/0  prior_art[17] 1/1/0  vehicle[11] 1/1/0  vehicle[18] 1/1/0
        implementation[4] 1/1/0
## END SUMMARY

## motivation - grade 1.33 (fired in 14 of 20 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             1/1/1  -> 1.00
  [7] 4. Transformation                            1/1/1  -> 1.00
  [8] 5. Monadic Composition                       1/1/1  -> 1.00
  [9] 6. Execution Contexts                        1/0/0  -> 0.33
  [10] 7. Environment                               1/1/1  -> 1.00
  [11] 8. Structured Concurrency                    1/1/1  -> 1.00
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         1/1/1  -> 1.00
  [14] 11. Async Scopes                             2/1/2  -> 1.67
  [15] 12. The task Coroutine Type                  1/1/1  -> 1.00
  [16] 13. Composition                              0/1/1  -> 0.67
  [17] 14. Real World Examples                      0/2/0  -> 0.67
  [18] 15. Conclusion                               1/0/0  -> 0.33
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 60 passes): Regular C++ has no dedicated cancellation channel; the three-channel model is one of the properties the Sub-Language adds.
candidate 3 (found by 3 of 60 passes): The most natural operation in the Sub-Language: take what came before, apply a function, and carry the result forward.
candidate 4 (found by 3 of 60 passes): Sometimes the next step in a computation is itself a whole new computation.

## audience - grade 0.00 (fired in 0 of 20 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             0/0/0  -> 0.00
  [7] 4. Transformation                            0/0/0  -> 0.00
  [8] 5. Monadic Composition                       0/0/0  -> 0.00
  [9] 6. Execution Contexts                        0/0/0  -> 0.00
  [10] 7. Environment                               0/0/0  -> 0.00
  [11] 8. Structured Concurrency                    0/0/0  -> 0.00
  [12] 9. Signal Adaptation                         0/0/0  -> 0.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             0/0/0  -> 0.00
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      0/0/0  -> 0.00
  [18] 15. Conclusion                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 13 of 20 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Theoretical Foundations                   2/2/2  -> 2.00
  [6] 3. Value Lifting                             2/2/2  -> 2.00
  [7] 4. Transformation                            1/1/1  -> 1.00
  [8] 5. Monadic Composition                       1/1/1  -> 1.00
  [9] 6. Execution Contexts                        2/2/2  -> 2.00
  [10] 7. Environment                               2/2/2  -> 2.00
  [11] 8. Structured Concurrency                    1/1/1  -> 1.00
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             2/2/2  -> 2.00
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      1/1/0  -> 0.67
  [18] 15. Conclusion                               1/1/1  -> 1.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): The final sections cover the `task` coroutine type ([P3552R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3552r3.html), "Add a Coroutine Task Type") [2]
candidate 2 (found by 3 of 60 passes): In the Sender Sub-Language, `just(x)` is monadic return and `let_value(f)` is monadic bind. `then(f)` is the functor lift - `fmap` - a specialization where the function returns a plain value rather than a new sender.
candidate 3 (found by 3 of 60 passes): In Moggi's framework [6], `sync_wait` is the counit - the elimination form that collapses the monadic layer back to a plain value.
candidate 4 (found by 3 of 60 passes): These are the functorial action on morphisms [6] - Moggi's `fmap`, the lifting T(f) : T(A) -> T(B) for a function f : A -> B.

## vehicle - grade 0.67 (fired in 2 of 20 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             0/0/0  -> 0.00
  [7] 4. Transformation                            0/0/0  -> 0.00
  [8] 5. Monadic Composition                       0/0/0  -> 0.00
  [9] 6. Execution Contexts                        0/0/0  -> 0.00
  [10] 7. Environment                               0/0/0  -> 0.00
  [11] 8. Structured Concurrency                    1/1/0  -> 0.67
  [12] 9. Signal Adaptation                         0/0/0  -> 0.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             0/0/0  -> 0.00
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      0/0/0  -> 0.00
  [18] 15. Conclusion                               1/1/0  -> 0.67
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 60 passes): These algorithms give C++ something its statements alone cannot express - concurrent execution with structured lifetime guarantees.
candidate 2 (found by 2 of 60 passes): Sub-Language is C++26's asynchronous programming model - the standard's answer to structured concurrency and heterogeneous execution.

## coordination - grade 0.50 (fired in 1 of 20 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             0/0/0  -> 0.00
  [7] 4. Transformation                            0/0/0  -> 0.00
  [8] 5. Monadic Composition                       0/0/0  -> 0.00
  [9] 6. Execution Contexts                        0/0/0  -> 0.00
  [10] 7. Environment                               0/0/0  -> 0.00
  [11] 8. Structured Concurrency                    0/0/0  -> 0.00
  [12] 9. Signal Adaptation                         0/0/0  -> 0.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             0/0/0  -> 0.00
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      0/0/0  -> 0.00
  [18] 15. Conclusion                               1/1/1  -> 1.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 60 passes): Every codebase uses the same patterns. Every team shares the same vocabulary for asynchronous programming.
candidate 2 (found by 1 of 60 passes): Every team shares the same vocabulary for asynchronous programming.

## insufficiency - grade 0.00 (fired in 0 of 20 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             0/0/0  -> 0.00
  [7] 4. Transformation                            0/0/0  -> 0.00
  [8] 5. Monadic Composition                       0/0/0  -> 0.00
  [9] 6. Execution Contexts                        0/0/0  -> 0.00
  [10] 7. Environment                               0/0/0  -> 0.00
  [11] 8. Structured Concurrency                    0/0/0  -> 0.00
  [12] 9. Signal Adaptation                         0/0/0  -> 0.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             0/0/0  -> 0.00
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      0/0/0  -> 0.00
  [18] 15. Conclusion                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 20 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/0  -> 0.67
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             0/0/0  -> 0.00
  [7] 4. Transformation                            0/0/0  -> 0.00
  [8] 5. Monadic Composition                       0/0/0  -> 0.00
  [9] 6. Execution Contexts                        0/0/0  -> 0.00
  [10] 7. Environment                               0/0/0  -> 0.00
  [11] 8. Structured Concurrency                    0/0/0  -> 0.00
  [12] 9. Signal Adaptation                         0/0/0  -> 0.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             0/0/0  -> 0.00
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      2/2/2  -> 2.00
  [18] 15. Conclusion                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 60 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy) [3] and [Corosio](https://github.com/cppalliance/corosio) [4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 2 of 60 passes): The following examples are drawn from the [stdexec](https://github.com/NVIDIA/stdexec) [25] reference implementation (whose algorithm customization model is addressed by [P3826R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3826r5.html) ("Fix Sender Algorithm Customization") [26]) and the [sender-examples](https://github.com/steve-downey/sender-examples) [27] repository.
candidate 3 (found by 1 of 60 passes): The following examples are drawn from the [stdexec](https://github.com/NVIDIA/stdexec) [25] reference implementation ... and the [sender-examples](https://github.com/steve-downey/sender-examples) [27] repository.

-->
