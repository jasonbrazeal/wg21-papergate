Verdict: Strong (10/14)

The paper offers solid grounding in prior art, design rationale, and implementation experience, but its affirmative case for standardization rests heavily on assertion rather than demonstrated need. The thinnest support appears where the paper must show that existing library approaches cannot suffice and that the affected community and interoperability requirements are real enough to justify a standard.

- The strongest support comes from the companion rationale paper and the availability of a complete three-platform implementation, which together establish that the design has been thought through and exercised in practice.
- The paper clearly establishes why the protocol matters and that alternatives have been considered, particularly through its references to P4172R0 and Boost.Asio.
- The weakest part of the case is the claim that a library will not do, which is asserted but not backed by evidence that the type-erasure and heap-allocation problems cannot be solved outside the standard.
- Most glaringly, the paper does not establish who is actually affected by the absence of this protocol, leaving the audience and the urgency of standardization largely unproven.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.33   accumulate 10.17   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.33  coordination 0.67  insufficiency 1.17  implementation 2.00
sample agreement: 82 of 91 section-criterion pairs unanimous (90%)
single-sample totals would have been: 10.00 / 10.00 / 9.00   (all 3 samples: 9.50)
headings: h2 12
on threshold: vehicle, insufficiency
splits: motivation[4] 0/0/1  audience[6] 0/2/0  vehicle[9] 2/2/1  coordination[7] 1/0/1
        coordination[8] 0/0/1  coordination[9] 1/1/0  insufficiency[8] 1/0/0
        implementation[4] 1/0/0  implementation[6] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      2/2/2  -> 2.00
  [7] 4. The IoAwaitable Protocol                  1/1/1  -> 1.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): For this to work, something must decide where the coroutine resumes, whether it should stop, and where its frame is allocated.
candidate 2 (found by 3 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.
candidate 3 (found by 3 of 39 passes): This is the question that drives the entire protocol. The awaitable cannot just call `h.resume()` - that resumes on the current thread, possibly while holding a lock, possibly re-entering code that is not re-entrant.
candidate 4 (found by 3 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.

## audience - grade 0.33 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/2/0  -> 0.67
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): | MSVC | Recycling | 1265.2 | 3.10x |

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      1/1/1  -> 1.00
  [7] 4. The IoAwaitable Protocol                  2/2/2  -> 2.00
  [8] 5. IoAwaitable Is Structured Concurrency     2/2/2  -> 2.00
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A companion paper, [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf) [1], provides the design rationale, evidence framework, preemptive objections, and analysis of alternative approaches.
candidate 2 (found by 3 of 39 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 39 passes): See [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf) [1] for design rationale and analysis of alternative approaches.
candidate 4 (found by 3 of 39 passes): This design borrows from [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html) [9].

## vehicle - grade 1.33 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                2/2/1  -> 1.67
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Small protocol, big rewards. It earns its keep.
candidate 2 (found by 3 of 39 passes): The language provides what a library would reimplement.
candidate 3 (found by 2 of 39 passes): The sender composition algebra does not apply to compound results - such as `[ec, n]` - without data loss or shared state; the sender three-channel model is in tension with `error_code` as a value-channel result.
candidate 4 (found by 1 of 39 passes): The *IoAwaitable* protocol provides the coroutine execution model beneath it.

## coordination - grade 0.67 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  1/0/1  -> 0.67
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/1  -> 0.33
  [9] 6. Why Not exec::asawaitable?                1/1/0  -> 0.67
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 2 (found by 2 of 39 passes): A TAPS implementation needs coroutines that suspend, resume correctly, cancel, and allocate frames - exactly what this protocol provides.
candidate 3 (found by 1 of 39 passes): The synchronous entry point requires an escape hatch in every async framework.

## insufficiency - grade 1.17 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/0/0  -> 0.33
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Under type erasure, `connect(sndr, rcvr)` produces a type-dependent `op_state` that must be heap-allocated when either side is erased.
candidate 2 (found by 1 of 39 passes): The language provides what a library would reimplement.

## implementation - grade 2.00  [binary: max] (fired in 5 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      1/0/1  -> 0.67
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     2/2/2  -> 2.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Everything in this paper comes from a complete implementation on three platforms: [Capy](https://github.com/cppalliance/capy) [2] (protocol) and [Corosio](https://github.com/cppalliance/corosio) [3].
candidate 2 (found by 3 of 39 passes): A full implementation is available in [Capy](https://github.com/cppalliance/capy) [2] (`include/boost/capy/ex/when_all.hpp`).
candidate 3 (found by 2 of 39 passes): The protocol must: * Provide a reasonable, customizable default * Propagate the frame allocator to every coroutine frame in the chain automatically
candidate 4 (found by 2 of 39 passes): A companion to `std::execution`, implemented on three platforms.

-->
