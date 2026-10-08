Verdict: Excellent (12/14)

The paper makes a solid case for standardizing its proposed mechanism, with particularly strong support on implementation experience, prior art, and the limits of a library-only solution. The thinnest part of the argument is the direct case for why the standard itself must act, where several key claims are asserted rather than demonstrated.

- The strongest support comes from the demonstrated cross-compiler implementation experience and the documented de facto ABI that already works in practice.
- The paper clearly establishes why a library cannot achieve the zero-allocation handle creation it targets, since obtaining a `coroutine_handle<>` today requires a coroutine frame.
- The discussion of prior art and alternatives credibly positions the proposal as complementary to sender-based and coroutine-native I/O rather than competing with them.
- The most glaring omission is the lack of an established argument for why the standard must mandate the specific two-pointer prefix layout, beyond asserting that it would be necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 11.00   accumulate 13.50   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.33  coordination 1.50  insufficiency 1.83  implementation 2.00
sample agreement: 98 of 112 section-criterion pairs unanimous (88%)
single-sample totals would have been: 13.00 / 11.50 / 12.00   (all 3 samples: 12.17)
headings: h2 15
on threshold: audience, vehicle, coordination, implementation
splits: motivation[7] 0/0/2  motivation[14] 2/1/2  vehicle[2] 0/1/1  vehicle[7] 1/1/0
        vehicle[12] 2/1/2  vehicle[13] 0/1/1  vehicle[14] 0/1/1  coordination[10] 2/2/1
        coordination[12] 2/1/1  coordination[13] 2/1/1  insufficiency[7] 1/0/1
        insufficiency[12] 2/1/2  insufficiency[13] 1/0/0  implementation[11] 0/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 16 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  1/1/1  -> 1.00
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Shape of an I/O Operation             0/0/2  -> 0.67
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/1  -> 1.00
  [11] 8. Prior Art: P3203R0                        1/1/1  -> 1.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        2/2/2  -> 2.00
  [14] 11. Anticipated Objections                   2/1/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): One I/O implementation. Both coroutines and senders consume it. Zero allocation for either path.
candidate 3 (found by 3 of 48 passes): Each addresses a use case the others structurally cannot.
candidate 4 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.

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

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 5)
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
  [10] 7. The Pragmatic Solution: Callback Handles  1/1/1  -> 1.00
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        2/2/2  -> 2.00
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 48 passes): The coroutine executor ([P4003R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4003r1.pdf)[1]) has two operations:
candidate 3 (found by 3 of 48 passes): The awaitable-to-sender bridge in [P4093R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4093r0.pdf)[5] demonstrates this: the bridge creates a coroutine whose sole purpose is to hold a handle that the reactor can resume.
candidate 4 (found by 3 of 48 passes): The committee explored both frame-erased and frame-visible designs. It chose frame-erased. That was the right choice for I/O - type erasure through `coroutine_handle<>` gives type-erased streams, split compilation, and ABI stability.

## vehicle - grade 1.33 (fired in 6 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             1/1/0  -> 0.67
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/1  -> 1.00
  [10] 7. The Pragmatic Solution: Callback Handles  0/0/0  -> 0.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/1/2  -> 1.67
  [13] 10. What This Enables                        0/1/1  -> 0.67
  [14] 11. Anticipated Objections                   0/1/1  -> 0.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The standard would need to mandate the two-pointer prefix layout - `resume` and `destroy` function pointers at offsets 0 and 1 - so that `from_address` on a user-provided struct produces a valid handle.
candidate 2 (found by 2 of 48 passes): The awaitable is the right shape for an I/O operation because it is the shape that makes the language feature free, and this paper makes it free for senders as well.
candidate 3 (found by 2 of 48 passes): Multiple coroutine models serving different domains is consistent with the committee's practice.
candidate 4 (found by 2 of 48 passes): The I/O library does not need two APIs - one for coroutines and one for senders. It needs one API and two ways to produce a handle.

## coordination - grade 1.50 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/1  -> 1.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/1  -> 1.67
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/1/1  -> 1.33
  [13] 10. What This Enables                        2/1/1  -> 1.33
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The `callback_frame` struct has `resume` and `destroy` function pointers at offsets 0 and 1 - matching the coroutine frame layout that all three major compilers use.
candidate 2 (found by 2 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 3 (found by 2 of 48 passes): The I/O library does not need two APIs - one for coroutines and one for senders. It needs one API and two ways to produce a handle.
candidate 4 (found by 1 of 48 passes): It gives awaitable authors a new consumer base without modifying a single line of their code.

## insufficiency - grade 1.83 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             1/0/1  -> 0.67
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/1/2  -> 1.67
  [13] 10. What This Enables                        1/0/0  -> 0.33
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 3 (found by 3 of 48 passes): A factory function cannot conjure storage without allocating - and allocation is the cost this paper eliminates.
candidate 4 (found by 2 of 48 passes): Today they cannot - they need a coroutine frame to get a handle.

## implementation - grade 2.00  [binary: max] (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
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
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/2/1  -> 1.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html)[20]
candidate 2 (found by 1 of 48 passes): [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html)[20] documents that all three major compilers (MSVC, GCC, Clang) use the same coroutine frame layout:
candidate 3 (found by 1 of 48 passes): Morgenstern demonstrates this in Boost.Cobalt for Python bindings and stackful coroutine integration.

-->
