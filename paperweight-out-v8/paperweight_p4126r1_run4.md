Verdict: Excellent (12/14)

The paper makes a broadly coherent case for standardizing a zero-allocation bridge between coroutine awaitables and senders, with most of the necessary justification resting on concrete examples, acknowledged ABI reliance, and a clear account of why library-only approaches fall short. The support is thinnest around implementation experience, where the paper leans on de facto compiler behavior and the author’s own projects rather than demonstrating independent, standards-track validation.

- The strongest support is the repeated, concrete demonstration that current code works across all three major compilers only by relying on an undocumented ABI, which directly motivates standardization.
- The paper clearly establishes why a library cannot solve the problem, since factory functions cannot avoid allocation and bridges impose per-operation costs.
- The coordination story is well grounded in the type-erased `coroutine_handle` boundary and the claim that the entire awaitable ecosystem becomes available to senders.
- The most glaring omission is implementation experience, where the paper asserts compiler convergence and cites the author’s own libraries but does not establish broader or independent implementation validation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 20. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 11.00   accumulate 12.67   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.83  insufficiency 1.83  implementation 1.00
sample agreement: 89 of 112 section-criterion pairs unanimous (79%)
single-sample totals would have been: 11.50 / 12.00 / 11.50   (all 3 samples: 11.67)
headings: h2 15
on threshold: audience, vehicle
splits: motivation[7] 2/0/2  motivation[10] 2/1/1  motivation[11] 1/0/2  motivation[14] 2/1/2
        audience[14] 0/1/0  prior_art[6] 1/0/0  prior_art[9] 2/2/0  prior_art[12] 0/2/2
        prior_art[13] 2/2/1  prior_art[14] 1/2/1  vehicle[2] 1/0/1  vehicle[10] 0/1/0
        vehicle[13] 0/1/1  vehicle[14] 1/0/0  coordination[9] 0/0/1  coordination[12] 1/2/2
        insufficiency[2] 0/1/0  insufficiency[6] 0/0/1  insufficiency[7] 1/0/1
        insufficiency[12] 2/2/1  insufficiency[14] 1/1/0  implementation[4] 0/0/1
        implementation[12] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Shape of an I/O Operation             2/0/2  -> 1.33
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/1/1  -> 1.33
  [11] 8. Prior Art: P3203R0                        1/0/2  -> 1.00
  [12] 9. The Design                                1/1/1  -> 1.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   2/1/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): One I/O implementation. Both coroutines and senders consume it. Zero allocation for either path.
candidate 3 (found by 3 of 48 passes): Each addresses a use case the others structurally cannot.
candidate 4 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.

## audience - grade 1.50 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               1/1/1  -> 1.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  0/0/0  -> 0.00
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/1/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 4 of 48 passes): For high-throughput networking - millions of operations per second - that matters.
candidate 2 (found by 3 of 48 passes): The EWG poll to forward the paper was not consensus (SF 0 / F 9 / N 8 / A 2 / SA 1).

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               1/0/0  -> 0.33
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/0  -> 1.33
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/1  -> 1.00
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                0/2/2  -> 1.33
  [13] 10. What This Enables                        2/2/1  -> 1.67
  [14] 11. Anticipated Objections                   1/2/1  -> 1.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 48 passes): The coroutine executor ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [1]) has two operations:
candidate 3 (found by 3 of 48 passes): The committee explored both frame-erased and frame-visible designs. It chose frame-erased. That was the right choice for I/O - type erasure through `coroutine_handle<>` gives type-erased streams, split compilation, and ABI stability.
candidate 4 (found by 3 of 48 passes): relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20]

## vehicle - grade 1.50 (fired in 7 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             1/1/1  -> 1.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/1  -> 1.00
  [10] 7. The Pragmatic Solution: Callback Handles  0/1/0  -> 0.33
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        0/1/1  -> 0.67
  [14] 11. Anticipated Objections                   1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The awaitable is the right shape for an I/O operation because it is the shape that makes the language feature free, and this paper makes it free for senders as well.
candidate 2 (found by 3 of 48 passes): Multiple coroutine models serving different domains is consistent with the committee's practice.
candidate 3 (found by 3 of 48 passes): This means the standard would need to mandate the two-pointer prefix layout - `resume` and `destroy` function pointers at offsets 0 and 1 - so that `from_address` on a user-provided struct produces a valid handle.
candidate 4 (found by 2 of 48 passes): The I/O library does not need two APIs - one for coroutines and one for senders. It needs one API and two ways to produce a handle.

## coordination - grade 1.83 (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/1  -> 0.33
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                1/2/2  -> 1.67
  [13] 10. What This Enables                        1/1/1  -> 1.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The handle is the type-erased boundary between the awaitable and its consumer.
candidate 2 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 3 (found by 2 of 48 passes): The entire awaitable ecosystem opens to senders.
candidate 4 (found by 1 of 48 passes): It gives senders something they do not have today: zero-allocation access to every IoAwaitable ever written - timers, channels, semaphores, I/O operations, and anything else the ecosystem produces.

## insufficiency - grade 1.83 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/1  -> 0.33
  [7] 4. The Shape of an I/O Operation             1/0/1  -> 0.67
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/1  -> 1.67
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/1/0  -> 0.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 2 (found by 3 of 48 passes): A factory function cannot conjure storage without allocating - and allocation is the cost this paper eliminates.
candidate 3 (found by 2 of 48 passes): A coroutine consuming a sender requires a bridge - and every bridge has a cost.
candidate 4 (found by 2 of 48 passes): That is one allocation per I/O operation. For high-throughput networking - millions of operations per second - that matters.

## implementation - grade 1.00  [binary: max] (fired in 3 of 16 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/1  -> 1.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                1/1/0  -> 0.67
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20] - it is not guaranteed by the current standard.
candidate 2 (found by 2 of 48 passes): The coroutine frame layout with two function pointers at the front is not an implementation accident - it is the layout every compiler chose independently
candidate 3 (found by 1 of 48 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy) [3] and [Corosio](https://github.com/cppalliance/corosio) [4] and believes coroutine-native I/O is a practical foundation for networking in C++.

-->
