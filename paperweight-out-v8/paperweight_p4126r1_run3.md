Verdict: Strong to Excellent (11/14)

The paper makes a generally strong case for why its proposed facility belongs in the standard, with most of the necessary argumentation backed by concrete reasoning about allocation costs, ABI constraints, and the limits of library-only solutions. The support is thinnest where it matters for committee confidence: the implementation experience is asserted rather than demonstrated through a shipped, standards-track implementation or broader deployment evidence.

- The paper most convincingly establishes why the standard must act, showing that the current coroutine frame ABI is de facto but not guaranteed, and that only standardization can make zero-allocation sender access to awaitables reliable.
- It also clearly establishes why a library cannot solve the problem, since factory functions cannot conjure storage without allocation and every coroutine-sender bridge imposes a cost.
- The coordination and interoperability case is well supported by the observation that the handle is the type-erased boundary between awaitable and consumer, and that the code already works across all three major compilers only by relying on undocumented ABI.
- The most glaring omission is implementation experience, where the paper offers author-maintained projects and a belief in practicality but does not establish that the proposed facility has been implemented and exercised at a level that would reassure the committee about standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 18. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 10.00   accumulate 12.50   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.83  insufficiency 1.50  implementation 1.00
sample agreement: 92 of 112 section-criterion pairs unanimous (82%)
single-sample totals would have been: 12.00 / 12.00 / 11.50   (all 3 samples: 11.33)
headings: h2 15
on threshold: audience, vehicle, insufficiency
splits: motivation[7] 0/2/2  motivation[10] 2/2/1  motivation[11] 0/1/1  motivation[14] 1/2/2
        prior_art[10] 1/2/2  prior_art[12] 2/0/2  prior_art[13] 1/0/0  prior_art[14] 2/1/1
        vehicle[2] 1/1/0  vehicle[10] 1/1/0  vehicle[13] 1/0/1  coordination[9] 1/0/0
        coordination[13] 1/2/2  insufficiency[2] 0/1/0  insufficiency[6] 1/0/0
        insufficiency[10] 0/2/2  insufficiency[12] 2/2/1  insufficiency[14] 1/0/0
        implementation[4] 1/0/0  implementation[11] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Shape of an I/O Operation             0/2/2  -> 1.33
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/1  -> 1.67
  [11] 8. Prior Art: P3203R0                        0/1/1  -> 0.67
  [12] 9. The Design                                1/1/1  -> 1.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/2/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): One I/O implementation. Both coroutines and senders consume it. Zero allocation for either path.
candidate 3 (found by 3 of 48 passes): Senders need frame visibility. The sender pipeline owns its operation state, knows its size at compile time, and inlines it.
candidate 4 (found by 3 of 48 passes): Each addresses a use case the others structurally cannot.

## audience - grade 1.50 (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
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
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): For high-throughput networking - millions of operations per second - that matters.
candidate 2 (found by 3 of 48 passes): The EWG poll to forward the paper was not consensus (SF 0 / F 9 / N 8 / A 2 / SA 1).

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/2/2  -> 1.67
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                2/0/2  -> 1.33
  [13] 10. What This Enables                        1/0/0  -> 0.33
  [14] 11. Anticipated Objections                   2/1/1  -> 1.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 48 passes): The coroutine executor ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [1]) has two operations:
candidate 3 (found by 3 of 48 passes): The committee explored both frame-erased and frame-visible designs. It chose frame-erased. That was the right choice for I/O - type erasure through `coroutine_handle<>` gives type-erased streams, split compilation, and ABI stability.
candidate 4 (found by 3 of 48 passes): It is complementary, not competing.

## vehicle - grade 1.50 (fired in 7 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             1/1/1  -> 1.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/1  -> 1.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/0  -> 0.67
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        1/0/1  -> 0.67
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The awaitable is the right shape for an I/O operation because it is the shape that makes the language feature free, and this paper makes it free for senders as well.
candidate 2 (found by 3 of 48 passes): This means the standard would need to mandate the two-pointer prefix layout - `resume` and `destroy` function pointers at offsets 0 and 1 - so that `from_address` on a user-provided struct produces a valid handle.
candidate 3 (found by 3 of 48 passes): Two protocols for the same socket operation means two implementations to maintain, two sets of bugs, and two surfaces to audit.
candidate 4 (found by 2 of 48 passes): It gives senders something they do not have today: zero-allocation access to every IoAwaitable ever written - timers, channels, semaphores, I/O operations, and anything else the ecosystem produces.

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
  [9] 6. Three Kinds of Coroutines                 1/0/0  -> 0.33
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                1/1/1  -> 1.00
  [13] 10. What This Enables                        1/2/2  -> 1.67
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 2 (found by 3 of 48 passes): The handle is the type-erased boundary between the awaitable and its consumer.
candidate 3 (found by 1 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 4 (found by 1 of 48 passes): The IoAwaitable protocol ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [1]) defines a contract between a coroutine and an I/O reactor: the coroutine suspends, the reactor performs the operation, and the executor resumes the coroutine when the result is ready.

## insufficiency - grade 1.50 (fired in 6 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               1/0/0  -> 0.33
  [7] 4. The Shape of an I/O Operation             1/1/1  -> 1.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  0/2/2  -> 1.33
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/1  -> 1.67
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): A coroutine consuming a sender requires a bridge - and every bridge has a cost.
candidate 2 (found by 3 of 48 passes): A factory function cannot conjure storage without allocating - and allocation is the cost this paper eliminates.
candidate 3 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 4 (found by 1 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.

## implementation - grade 1.00  [binary: max] (fired in 3 of 16 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/1  -> 1.00
  [11] 8. Prior Art: P3203R0                        2/0/0  -> 0.67
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20] - it is not guaranteed by the current standard.
candidate 2 (found by 1 of 48 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy) [3] and [Corosio](https://github.com/cppalliance/corosio) [4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 3 (found by 1 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20]
candidate 4 (found by 1 of 48 passes): [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20] documents that all three major compilers (MSVC, GCC, Clang) use the same coroutine frame layout

-->
