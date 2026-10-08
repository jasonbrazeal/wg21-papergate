Verdict: Excellent (12/14)

The paper makes a generally strong case for its own standardization, with most of the necessary burdens met through concrete examples, clear motivation, and demonstrated implementation experience. The support is thinnest around committee reception and the absence of a consensus path forward, which leaves the political viability of the proposal less settled than its technical argument.

- The paper most convincingly establishes why a library solution cannot suffice, since the sender pipeline already owns operation state and allocating a coroutine frame solely to obtain a handle is pure overhead.
- It also grounds its case well in implementation experience, showing that the underlying technique works on all three major compilers today even though it relies on a de facto ABI rather than a standard guarantee.
- The discussion of prior art and alternatives is thorough, crediting the committee's earlier frame-erased choice for I/O while explaining why frame-visible access serves a different need.
- The most glaring omission is a clear account of how the proposal addresses the lack of EWG consensus, since the poll results suggest meaningful opposition that the paper does not appear to confront directly.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 9.67   accumulate 13.17   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 1.67  implementation 1.67
sample agreement: 92 of 112 section-criterion pairs unanimous (82%)
single-sample totals would have been: 12.50 / 12.00 / 12.50   (all 3 samples: 11.83)
headings: h2 15
on threshold: audience, vehicle, coordination, insufficiency, implementation
splits: motivation[4] 1/0/0  motivation[5] 1/0/1  motivation[7] 2/0/0  motivation[10] 1/2/1
        motivation[11] 1/2/1  motivation[12] 1/2/1  prior_art[10] 2/2/1  prior_art[14] 2/1/2
        vehicle[8] 0/0/1  vehicle[10] 0/1/0  vehicle[13] 0/1/1  vehicle[14] 1/0/0
        coordination[9] 0/0/1  insufficiency[2] 1/0/1  insufficiency[6] 0/0/1
        insufficiency[9] 1/0/1  insufficiency[10] 2/0/2  insufficiency[13] 0/0/1
        implementation[10] 2/2/1  implementation[11] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 12 of 16 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. The Goal                                  1/0/1  -> 0.67
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Shape of an I/O Operation             2/0/0  -> 0.67
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/2/1  -> 1.33
  [11] 8. Prior Art: P3203R0                        1/2/1  -> 1.33
  [12] 9. The Design                                1/2/1  -> 1.33
  [13] 10. What This Enables                        2/2/2  -> 2.00
  [14] 11. Anticipated Objections                   2/2/2  -> 2.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): Senders need frame visibility. The sender pipeline owns its operation state, knows its size at compile time, and inlines it.
candidate 3 (found by 3 of 48 passes): Each addresses a use case the others structurally cannot.
candidate 4 (found by 3 of 48 passes): Every IoAwaitable anyone has written - timers, mutexes, channels, semaphores, file I/O, database queries, HTTP clients - becomes consumable by sender pipelines at zero allocation cost.

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

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               1/1/1  -> 1.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/1  -> 1.67
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        2/2/2  -> 2.00
  [14] 11. Anticipated Objections                   2/1/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 48 passes): The coroutine executor ([P4003R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4003r1.pdf)[1]) has two operations:
candidate 3 (found by 3 of 48 passes): The awaitable-to-sender bridge in [P4093R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4093r0.pdf)[5] demonstrates this: the bridge creates a coroutine whose sole purpose is to hold a handle that the reactor can resume.
candidate 4 (found by 3 of 48 passes): The committee explored both frame-erased and frame-visible designs. It chose frame-erased. That was the right choice for I/O - type erasure through `coroutine_handle<>` gives type-erased streams, split compilation, and ABI stability.

## vehicle - grade 1.50 (fired in 8 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             1/1/1  -> 1.00
  [8] 5. The Timeline                              0/0/1  -> 0.33
  [9] 6. Three Kinds of Coroutines                 1/1/1  -> 1.00
  [10] 7. The Pragmatic Solution: Callback Handles  0/1/0  -> 0.33
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        0/1/1  -> 0.67
  [14] 11. Anticipated Objections                   1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): It gives senders something they do not have today: zero-allocation access to every IoAwaitable ever written - timers, channels, semaphores, I/O operations, and anything else the ecosystem produces.
candidate 2 (found by 3 of 48 passes): The awaitable is the right shape for an I/O operation because it is the shape that makes the language feature free, and this paper makes it free for senders as well.
candidate 3 (found by 2 of 48 passes): Multiple coroutine models serving different domains is consistent with the committee's practice.
candidate 4 (found by 2 of 48 passes): The standard would need to mandate the two-pointer prefix layout - `resume` and `destroy` function pointers at offsets 0 and 1 - so that `from_address` on a user-provided struct produces a valid handle.

## coordination - grade 1.50 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
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
  [12] 9. The Design                                1/1/1  -> 1.00
  [13] 10. What This Enables                        1/1/1  -> 1.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Executors traffic in `coroutine_handle<>`. The handle is the type-erased boundary between the awaitable and its consumer.
candidate 2 (found by 3 of 48 passes): The sender ecosystem and the awaitable ecosystem merge.
candidate 3 (found by 2 of 48 passes): A general bridge to standard awaitables would also need to handle the `void`-returning and `bool`-returning variants of `await_suspend`.
candidate 4 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.

## insufficiency - grade 1.67 (fired in 8 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/1  -> 0.33
  [7] 4. The Shape of an I/O Operation             1/1/1  -> 1.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/0/1  -> 0.67
  [10] 7. The Pragmatic Solution: Callback Handles  2/0/2  -> 1.33
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        0/0/1  -> 0.33
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The sender pipeline already has operation state. Allocating a frame to hold nothing the sender needs is overhead.
candidate 2 (found by 2 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 3 (found by 2 of 48 passes): Each addresses a use case the others structurally cannot.
candidate 4 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.

## implementation - grade 1.67  [binary: max] (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/1  -> 1.67
  [11] 8. Prior Art: P3203R0                        0/0/2  -> 0.67
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html)[20] - it is not guaranteed by the current standard.
candidate 2 (found by 1 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html)[20]
candidate 3 (found by 1 of 48 passes): Morgenstern demonstrates this in Boost.Cobalt for Python bindings and stackful coroutine integration.

-->
