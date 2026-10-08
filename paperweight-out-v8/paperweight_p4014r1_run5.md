Verdict: Adequate (5/14)

The paper offers a solid conceptual foundation for its proposal, particularly in connecting the design to established asynchronous programming models and prior art, but it leaves several essential standardization questions largely unaddressed. The thinnest support concerns who is affected, why a library solution is insufficient, and whether the claimed implementation experience actually demonstrates readiness for standardization.

- The paper clearly establishes why the problem matters by identifying real gaps in regular C++ for cancellation, context queries, and structured concurrency.
- The treatment of prior art and alternatives is strong, grounding the design in Moggi's monadic framework and positioning it as complementary to `std::execution` rather than redundant.
- The claim that this is "C++26's asynchronous programming model" is asserted without evidence about committee direction, existing practice, or consensus.
- The paper never establishes who is affected by the proposal or why a library-only approach would fail to meet their needs.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 5 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.67   accumulate 6.00   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.50  insufficiency 0.00  implementation 1.33
sample agreement: 130 of 140 section-criterion pairs unanimous (93%)
single-sample totals would have been: 5.50 / 6.50 / 6.00   (all 3 samples: 5.50)
headings: h2 19
on threshold: motivation
splits: motivation[4] 1/0/0  motivation[9] 0/1/0  motivation[11] 2/2/1  motivation[14] 1/1/2
        motivation[17] 2/1/1  prior_art[10] 2/2/1  prior_art[14] 2/2/1  prior_art[17] 0/1/0
        vehicle[18] 0/1/0  implementation[17] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 14 of 20 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             1/1/1  -> 1.00
  [7] 4. Transformation                            1/1/1  -> 1.00
  [8] 5. Monadic Composition                       1/1/1  -> 1.00
  [9] 6. Execution Contexts                        0/1/0  -> 0.33
  [10] 7. Environment                               1/1/1  -> 1.00
  [11] 8. Structured Concurrency                    2/2/1  -> 1.67
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         1/1/1  -> 1.00
  [14] 11. Async Scopes                             1/1/2  -> 1.33
  [15] 12. The task Coroutine Type                  1/1/1  -> 1.00
  [16] 13. Composition                              1/1/1  -> 1.00
  [17] 14. Real World Examples                      2/1/1  -> 1.33
  [18] 15. Conclusion                               1/1/1  -> 1.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Regular C++ has no dedicated cancellation channel; the three-channel model is one of the properties the Sub-Language adds.
candidate 2 (found by 3 of 60 passes): A pipeline sometimes needs to ask its surroundings a question - what scheduler am I running on, what allocator should I use, has anyone asked me to stop?
candidate 3 (found by 3 of 60 passes): Run things at the same time, wait for all of them, and know that nothing outlives its scope.
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
  [10] 7. Environment                               2/2/1  -> 1.67
  [11] 8. Structured Concurrency                    1/1/1  -> 1.00
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             2/2/1  -> 1.67
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      0/1/0  -> 0.33
  [18] 15. Conclusion                               1/1/1  -> 1.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 60 passes): In the Sender Sub-Language, `just(x)` is monadic return and `let_value(f)` is monadic bind. `then(f)` is the functor lift - `fmap` - a specialization where the function returns a plain value rather than a new sender.
candidate 3 (found by 3 of 60 passes): In Moggi's framework[6], `sync_wait` is the counit - the elimination form that collapses the monadic layer back to a plain value.
candidate 4 (found by 3 of 60 passes): These are the functorial action on morphisms[6] - Moggi's `fmap`, the lifting T(f) : T(A) -> T(B) for a function f : A -> B.

## vehicle - grade 0.17 (fired in 1 of 20 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [18] 15. Conclusion                               0/1/0  -> 0.33
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 60 passes): Sub-Language is C++26's asynchronous programming model - the standard's answer to structured concurrency and heterogeneous execution.

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
candidate 1 (found by 2 of 60 passes): Every C++ developer learns the same abstractions. Every codebase uses the same patterns. Every team shares the same vocabulary for asynchronous programming.
candidate 2 (found by 1 of 60 passes): Every codebase uses the same patterns. Every team shares the same vocabulary for asynchronous programming.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 20 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
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
  [17] 14. Real World Examples                      0/2/2  -> 1.33
  [18] 15. Conclusion                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy)[3] and [Corosio](https://github.com/cppalliance/corosio)[4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 2 of 60 passes): The following examples are drawn from the [stdexec](https://github.com/NVIDIA/stdexec)[25] reference implementation (whose algorithm customization model is addressed by [P3826R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3826r5.pdf) ("Fix Sender Algorithm Customization")[26]) and the [sender-examples](https://github.com/steve-downey/sender-examples)[27] repository.

-->
