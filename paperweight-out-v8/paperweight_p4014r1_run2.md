Verdict: Adequate (5/14)

The paper offers some grounding in prior art and related work, but it does not build a complete case for standardization. The thinnest areas are the absence of an affected audience, a rationale for why the standard rather than a library is needed, and any demonstration that the proposed facility cannot be delivered outside the standard.

- The strongest support is the discussion of prior art, including links to related proposals and established abstractions such as Kleisli arrows and scheduler affinity primitives.
- The paper claims implementation experience through references to Capy, Corosio, stdexec, and sender-examples, but it does not show that this experience validates the specific design being proposed.
- The paper does not establish who is affected by the proposal or what user or industry need would be met by standardization.
- Most notably, the paper never explains why a library would not suffice, leaving the central question of standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.33   accumulate 5.83   max 5.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 1.33
sample agreement: 134 of 140 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 4.83)
headings: h2 19
on threshold: none
splits: motivation[9] 0/1/0  motivation[16] 1/1/0  motivation[17] 2/0/0  prior_art[14] 1/2/1
        implementation[4] 1/2/0  implementation[17] 0/2/2
## END SUMMARY

## motivation - grade 1.00 (fired in 12 of 20 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Theoretical Foundations                   0/0/0  -> 0.00
  [6] 3. Value Lifting                             1/1/1  -> 1.00
  [7] 4. Transformation                            1/1/1  -> 1.00
  [8] 5. Monadic Composition                       1/1/1  -> 1.00
  [9] 6. Execution Contexts                        0/1/0  -> 0.33
  [10] 7. Environment                               1/1/1  -> 1.00
  [11] 8. Structured Concurrency                    1/1/1  -> 1.00
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         1/1/1  -> 1.00
  [14] 11. Async Scopes                             1/1/1  -> 1.00
  [15] 12. The task Coroutine Type                  1/1/1  -> 1.00
  [16] 13. Composition                              1/1/0  -> 0.67
  [17] 14. Real World Examples                      2/0/0  -> 0.67
  [18] 15. Conclusion                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Regular C++ has no dedicated cancellation channel; the three-channel model is one of the properties the Sub-Language adds.
candidate 2 (found by 3 of 60 passes): The most natural operation in the Sub-Language: take what came before, apply a function, and carry the result forward.
candidate 3 (found by 3 of 60 passes): A pipeline sometimes needs to ask its surroundings a question - what scheduler am I running on, what allocator should I use, has anyone asked me to stop?
candidate 4 (found by 3 of 60 passes): These algorithms give C++ something its statements alone cannot express - concurrent execution with structured lifetime guarantees.

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

## prior_art - grade 2.00 (fired in 12 of 20 sections, strong in 3)
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
  [10] 7. Environment                               1/1/1  -> 1.00
  [11] 8. Structured Concurrency                    1/1/1  -> 1.00
  [12] 9. Signal Adaptation                         1/1/1  -> 1.00
  [13] 10. Data Parallelism                         0/0/0  -> 0.00
  [14] 11. Async Scopes                             1/2/1  -> 1.33
  [15] 12. The task Coroutine Type                  0/0/0  -> 0.00
  [16] 13. Composition                              0/0/0  -> 0.00
  [17] 14. Real World Examples                      0/0/0  -> 0.00
  [18] 15. Conclusion                               1/1/1  -> 1.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): The final sections cover the `task` coroutine type ([P3552R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3552r3.html), "Add a Coroutine Task Type")[2] and the composition patterns that emerge when senders and coroutines interleave.
candidate 2 (found by 3 of 60 passes): These are the functorial action on morphisms[6] - Moggi's `fmap`, the lifting T(f) : T(A) -> T(B) for a function f : A -> B.
candidate 3 (found by 3 of 60 passes): A Kleisli arrow[6][15] is a morphism A -> T(B) - a function from a plain value to a computation.
candidate 4 (found by 3 of 60 passes): affine is the scheduler affinity primitive, redesigned by P3941R4[16] and renamed from affine_on by P4151R1[17].

## vehicle - grade 0.00 (fired in 0 of 20 sections, strong in 0)
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
  [4] 1. Disclosure                                1/2/0  -> 1.00
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
candidate 1 (found by 2 of 60 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy)[3] and [Corosio](https://github.com/cppalliance/corosio)[4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 2 of 60 passes): The following examples are drawn from the [stdexec](https://github.com/NVIDIA/stdexec)[25] reference implementation ... and the [sender-examples](https://github.com/steve-downey/sender-examples)[27] repository.

-->
