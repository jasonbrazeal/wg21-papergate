Verdict: Adequate to Strong (7/14)

The paper gives a partial but uneven account of why its abstractions belong in the standard, with the strongest material concentrated in conceptual background, prior art, and implementation experience. The case thins considerably when it turns to the standard’s unique role, the breadth of the affected community, and why a library solution would be insufficient.

- The paper clearly grounds its ideas in existing practice and recognizable functional-programming concepts, and it points to concrete implementations and reference code.
- It asserts that the Sub-Language gives C++ capabilities statements alone cannot express, but does not develop that into a demonstrated need for standardization rather than a library.
- The claim that every developer, codebase, and team would share the same vocabulary is presented as a benefit without evidence about who is actually affected or how coordination would work.
- The paper offers no substantive argument for why a library would not suffice, leaving one of the central questions about standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 7.17   max 7.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 132 of 140 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 6.00   (all 3 samples: 6.83)
headings: h2 19
on threshold: motivation
splits: motivation[6] 2/1/1  motivation[11] 1/2/1  motivation[17] 2/1/1  motivation[18] 0/1/0
        prior_art[17] 1/0/1  prior_art[18] 0/1/1  vehicle[11] 1/1/0  vehicle[18] 1/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 12 of 20 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             2/1/1  -> 1.33
  [7] 4. Transformation                            1/1/1  -> 1.00
  [8] 5. Monadic Composition                       1/1/1  -> 1.00
  [9] 6. Execution Contexts                        0/0/0  -> 0.00
  [10] 7. Environment                               1/1/1  -> 1.00
  [11] 8. Structured Concurrency                    1/2/1  -> 1.33
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         1/1/1  -> 1.00
  [14] 11. Async Scopes                             2/2/2  -> 2.00
  [15] 12. The task Coroutine Type                  1/1/1  -> 1.00
  [16] 13. Composition                              1/1/1  -> 1.00
  [17] 14. Real World Examples                      2/1/1  -> 1.33
  [18] 15. Conclusion                               0/1/0  -> 0.33
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Regular C++ has no dedicated cancellation channel; the three-channel model is one of the properties the Sub-Language adds.
candidate 2 (found by 3 of 60 passes): Regular C++ has no cancellation equivalent.
candidate 3 (found by 3 of 60 passes): A pipeline sometimes needs to ask its surroundings a question - what scheduler am I running on, what allocator should I use, has anyone asked me to stop?
candidate 4 (found by 3 of 60 passes): Sometimes the shape of a completion does not quite fit what the next stage expects.

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
  [17] 14. Real World Examples                      1/0/1  -> 0.67
  [18] 15. Conclusion                               0/1/1  -> 0.67
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): The final sections cover the `task` coroutine type ([P3552R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3552r3.html), "Add a Coroutine Task Type")[2]
candidate 2 (found by 3 of 60 passes): In the Sender Sub-Language, `just(x)` is monadic return and `let_value(f)` is monadic bind. `then(f)` is the functor lift - `fmap` - a specialization where the function returns a plain value rather than a new sender.
candidate 3 (found by 3 of 60 passes): These are the functorial action on morphisms[6] - Moggi's `fmap`, the lifting T(f) : T(A) -> T(B) for a function f : A -> B.
candidate 4 (found by 3 of 60 passes): A Kleisli arrow[6][15] is a morphism A -> T(B) - a function from a plain value to a computation.

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
candidate 1 (found by 3 of 60 passes): Every C++ developer learns the same abstractions. Every codebase uses the same patterns. Every team shares the same vocabulary for asynchronous programming.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 20 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
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
candidate 1 (found by 3 of 60 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy)[3] and [Corosio](https://github.com/cppalliance/corosio)[4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 3 of 60 passes): The following examples are drawn from the [stdexec](https://github.com/NVIDIA/stdexec)[25] reference implementation (whose algorithm customization model is addressed by [P3826R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3826r5.pdf) ("Fix Sender Algorithm Customization")[26]) and the [sender-examples](https://github.com/steve-downey/sender-examples)[27] repository.

-->
