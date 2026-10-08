Verdict: Strong to Excellent (12/14)

The paper makes a reasonably strong case for standardizing a way to obtain a `coroutine_handle<>` without a coroutine frame allocation, with the core motivation, prior art, and interoperability story well supported. The thinnest parts are the evidence that the affected audience is real and that the approach has been meaningfully validated in practice, since those rest on author assertion and a non-consensus committee poll rather than demonstrated need or broader implementation experience.

- The paper most convincingly establishes why the standard must act, since the current prohibition on specializing `coroutine_handle` and the allocation requirement for obtaining one are standard-level constraints that a library cannot remove.
- It also clearly shows coordination with existing practice, because the handle is already the type-erased boundary between awaitables and their consumers, and the proposed change would give senders zero-allocation access to that ecosystem.
- The weakest support is for who is affected, as the claim about high-throughput networking needing millions of operations per second is asserted rather than demonstrated, and the committee poll fell short of consensus.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 26. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 11.33   accumulate 12.33   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.50  coordination 2.00  insufficiency 2.00  implementation 1.33
sample agreement: 92 of 112 section-criterion pairs unanimous (82%)
single-sample totals would have been: 11.00 / 11.50 / 13.00   (all 3 samples: 11.83)
headings: h2 15
on threshold: vehicle
splits: motivation[5] 1/0/1  motivation[10] 2/1/2  motivation[11] 0/2/0  motivation[12] 2/1/1
        motivation[14] 1/1/2  audience[11] 0/1/2  prior_art[4] 0/0/1  prior_art[6] 1/0/0
        prior_art[10] 2/2/1  prior_art[13] 2/2/0  vehicle[7] 0/1/0  vehicle[14] 0/0/1
        coordination[2] 1/1/0  coordination[5] 0/0/1  coordination[9] 1/1/0
        coordination[13] 0/2/0  insufficiency[11] 0/0/1  implementation[4] 1/1/0
        implementation[10] 1/1/2  implementation[11] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  1/0/1  -> 0.67
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Shape of an I/O Operation             2/2/2  -> 2.00
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/1/2  -> 1.67
  [11] 8. Prior Art: P3203R0                        0/2/0  -> 0.67
  [12] 9. The Design                                2/1/1  -> 1.33
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/1/2  -> 1.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): One allocation per I/O operation. For high-throughput networking - millions of operations per second - that matters.
candidate 3 (found by 3 of 48 passes): Today they cannot - they need a coroutine frame to get a handle.
candidate 4 (found by 3 of 48 passes): Senders need frame visibility. The sender pipeline owns its operation state, knows its size at compile time, and inlines it.

## audience - grade 1.00 (fired in 2 of 16 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
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
  [11] 8. Prior Art: P3203R0                        0/1/2  -> 1.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): For high-throughput networking - millions of operations per second - that matters.
candidate 2 (found by 1 of 48 passes): The interest - nine in favour - suggests the use case resonates; the concerns point to the design space this paper explores.
candidate 3 (found by 1 of 48 passes): The EWG poll to forward the paper was not consensus (SF 0 / F 9 / N 8 / A 2 / SA 1).

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               1/0/0  -> 0.33
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/1  -> 1.67
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        2/2/0  -> 1.33
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The coroutine executor ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [1]) has two operations:
candidate 2 (found by 3 of 48 passes): The committee explored both frame-erased and frame-visible designs. It chose frame-erased. That was the right choice for I/O - type erasure through `coroutine_handle<>` gives type-erased streams, split compilation, and ABI stability.
candidate 3 (found by 3 of 48 passes): It is complementary, not competing.
candidate 4 (found by 3 of 48 passes): The paper proposes changing the standard's prohibition on specializing `coroutine_handle` from undefined behavior to implementation defined behavior.

## vehicle - grade 1.50 (fired in 6 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/1/0  -> 0.33
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/1  -> 1.00
  [10] 7. The Pragmatic Solution: Callback Handles  0/0/0  -> 0.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        1/1/1  -> 1.00
  [14] 11. Anticipated Objections                   0/0/1  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): Multiple coroutine models serving different domains is consistent with the committee's practice.
candidate 3 (found by 3 of 48 passes): The standard would need to mandate the two-pointer prefix layout - `resume` and `destroy` function pointers at offsets 0 and 1 - so that `from_address` on a user-provided struct produces a valid handle.
candidate 4 (found by 3 of 48 passes): The I/O library does not need two APIs - one for coroutines and one for senders. It needs one API and two ways to produce a handle.

## coordination - grade 2.00 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/1  -> 0.33
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/0  -> 0.67
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        0/2/0  -> 0.67
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): It gives senders something they do not have today: zero-allocation access to every IoAwaitable ever written - timers, channels, semaphores, I/O operations, and anything else the ecosystem produces.
candidate 2 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 3 (found by 2 of 48 passes): Awaitables accept `coroutine_handle<>`. Executors traffic in `coroutine_handle<>`. The handle is the type-erased boundary between the awaitable and its consumer.
candidate 4 (found by 1 of 48 passes): One I/O implementation. Both coroutines and senders consume it.

## insufficiency - grade 2.00 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               1/1/1  -> 1.00
  [7] 4. The Shape of an I/O Operation             1/1/1  -> 1.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/1  -> 0.33
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): A coroutine consuming a sender requires a bridge - and every bridge has a cost.
candidate 2 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 3 (found by 3 of 48 passes): A factory function cannot conjure storage without allocating - and allocation is the cost this paper eliminates.
candidate 4 (found by 2 of 48 passes): The sender already has its own operation state. The frame is overhead.

## implementation - grade 1.33  [binary: max] (fired in 3 of 16 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/0  -> 0.67
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/2  -> 1.33
  [11] 8. Prior Art: P3203R0                        0/0/1  -> 0.33
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy) [3] and [Corosio](https://github.com/cppalliance/corosio) [4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20] - it is not guaranteed by the current standard.
candidate 3 (found by 1 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20]
candidate 4 (found by 1 of 48 passes): Morgenstern demonstrates this in Boost.Cobalt for Python bindings and stackful coroutine integration.

-->
