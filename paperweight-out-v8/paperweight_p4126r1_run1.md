Verdict: Excellent (12/14)

The paper makes a reasonably strong case for standardizing its proposed mechanism, with the most convincing support concentrated in the technical necessity, prior art, and interoperability arguments. The thinnest parts are the human and practical dimensions: who exactly is affected and whether the approach has enough implementation experience behind it to justify standardization.

- The paper is most persuasive when it shows that the only current way to obtain a `coroutine_handle<>` is through a coroutine, which forces an allocation and makes the proposed standard wording necessary rather than merely convenient.
- It also establishes clearly that existing alternatives such as coroutine-native I/O and `std::execution` are complementary, and that a library-only solution cannot guarantee the frame ABI the technique depends on.
- The discussion of affected users leans on a single high-throughput networking scenario and a divided EWG poll, so the breadth and urgency of the constituency remain asserted rather than demonstrated.
- Implementation experience is the most glaring omission: the cited projects and the claim that the code works on three compilers are offered as belief and anecdote, without enough evidence of deployment, scale, or long-term use to establish that the design has been validated in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 25. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 10.33   accumulate 12.67   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.67  coordination 1.83  insufficiency 1.50  implementation 1.33
sample agreement: 93 of 112 section-criterion pairs unanimous (83%)
single-sample totals would have been: 12.00 / 12.50 / 11.50   (all 3 samples: 11.67)
headings: h2 15
on threshold: audience, vehicle, insufficiency
splits: motivation[5] 1/1/0  motivation[7] 2/0/2  motivation[10] 2/1/1  motivation[12] 1/2/2
        audience[11] 1/2/2  prior_art[6] 1/0/0  prior_art[10] 2/2/0  vehicle[7] 1/0/1
        vehicle[9] 2/1/1  coordination[9] 0/1/1  coordination[12] 2/1/2  coordination[13] 2/2/0
        insufficiency[6] 1/0/1  insufficiency[7] 1/0/1  insufficiency[9] 1/1/0
        insufficiency[12] 2/1/0  insufficiency[14] 1/0/0  implementation[4] 1/0/1
        implementation[10] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 16 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  1/1/0  -> 0.67
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Shape of an I/O Operation             2/0/2  -> 1.33
  [8] 5. The Timeline                              2/2/2  -> 2.00
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/1/1  -> 1.33
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                1/2/2  -> 1.67
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): One allocation per I/O operation. For high-throughput networking - millions of operations per second - that matters.
candidate 2 (found by 3 of 48 passes): Senders need frame visibility. The sender pipeline owns its operation state, knows its size at compile time, and inlines it.
candidate 3 (found by 3 of 48 passes): Each addresses a use case the others structurally cannot.
candidate 4 (found by 3 of 48 passes): That is one allocation per I/O operation. For high-throughput networking - millions of operations per second - that matters.

## audience - grade 1.33 (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
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
  [11] 8. Prior Art: P3203R0                        1/2/2  -> 1.67
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): For high-throughput networking - millions of operations per second - that matters.
candidate 2 (found by 2 of 48 passes): The EWG poll to forward the paper was not consensus (SF 0 / F 9 / N 8 / A 2 / SA 1).
candidate 3 (found by 1 of 48 passes): The interest - nine in favour - suggests the use case resonates; the concerns point to the design space this paper explores.

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 5)
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
  [9] 6. Three Kinds of Coroutines                 2/2/2  -> 2.00
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/0  -> 1.33
  [11] 8. Prior Art: P3203R0                        2/2/2  -> 2.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        2/2/2  -> 2.00
  [14] 11. Anticipated Objections                   2/2/2  -> 2.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 48 passes): The coroutine executor ([P4003R3](https://isocpp.org/files/papers/P4003R3.pdf) [1]) has two operations:
candidate 3 (found by 3 of 48 passes): The committee explored both frame-erased and frame-visible designs. It chose frame-erased. That was the right choice for I/O - type erasure through `coroutine_handle<>` gives type-erased streams, split compilation, and ABI stability.
candidate 4 (found by 3 of 48 passes): It is complementary, not competing.

## vehicle - grade 1.67 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             1/0/1  -> 0.67
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 2/1/1  -> 1.33
  [10] 7. The Pragmatic Solution: Callback Handles  0/0/0  -> 0.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/2/2  -> 2.00
  [13] 10. What This Enables                        1/1/1  -> 1.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 2 (found by 3 of 48 passes): This means the standard would need to mandate the two-pointer prefix layout - `resume` and `destroy` function pointers at offsets 0 and 1 - so that `from_address` on a user-provided struct produces a valid handle.
candidate 3 (found by 3 of 48 passes): The I/O library does not need two APIs - one for coroutines and one for senders. It needs one API and two ways to produce a handle.
candidate 4 (found by 2 of 48 passes): The awaitable is the right shape for an I/O operation because it is the shape that makes the language feature free, and this paper makes it free for senders as well.

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
  [9] 6. Three Kinds of Coroutines                 0/1/1  -> 0.67
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/1/2  -> 1.67
  [13] 10. What This Enables                        2/2/0  -> 1.33
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 2 (found by 2 of 48 passes): The handle is the type-erased boundary between the awaitable and its consumer.
candidate 3 (found by 1 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine, and a coroutine requires a frame allocation.
candidate 4 (found by 1 of 48 passes): It gives awaitable authors a new consumer base without modifying a single line of their code.

## insufficiency - grade 1.50 (fired in 6 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               1/0/1  -> 0.67
  [7] 4. The Shape of an I/O Operation             1/0/1  -> 0.67
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 1/1/0  -> 0.67
  [10] 7. The Pragmatic Solution: Callback Handles  2/2/2  -> 2.00
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                2/1/0  -> 1.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0] - it is not guaranteed by the current standard.
candidate 2 (found by 2 of 48 passes): The only way to obtain a `coroutine_handle<>` today is from a coroutine.
candidate 3 (found by 2 of 48 passes): A coroutine consuming a sender requires a bridge - and every bridge has a cost.
candidate 4 (found by 2 of 48 passes): Each addresses a use case the others structurally cannot.

## implementation - grade 1.33  [binary: max] (fired in 2 of 16 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/1  -> 0.67
  [5] 2. The Goal                                  0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Shape of an I/O Operation             0/0/0  -> 0.00
  [8] 5. The Timeline                              0/0/0  -> 0.00
  [9] 6. Three Kinds of Coroutines                 0/0/0  -> 0.00
  [10] 7. The Pragmatic Solution: Callback Handles  1/2/1  -> 1.33
  [11] 8. Prior Art: P3203R0                        0/0/0  -> 0.00
  [12] 9. The Design                                0/0/0  -> 0.00
  [13] 10. What This Enables                        0/0/0  -> 0.00
  [14] 11. Anticipated Objections                   0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy) [3] and [Corosio](https://github.com/cppalliance/corosio) [4] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 2 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20] - it is not guaranteed by the current standard.
candidate 3 (found by 1 of 48 passes): The following code works on all three major compilers today but relies on the de facto coroutine frame ABI documented by [P3203R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3203r0.html) [20]

-->
