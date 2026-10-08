Verdict: Strong (10/14)

The paper offers solid grounding in implementation experience and a clear articulation of the problem, but its case for standardization leans heavily on companion material and asserted benefits rather than evidence contained in the proposal itself. The thinnest support appears where the paper claims broad impact, interoperability, and the necessity of language-level action without demonstrating those points directly.

- The strongest support is the availability of complete, cross-platform implementations for the protocol and related facilities.
- The paper clearly establishes why coroutine resumption and allocation decisions matter and what can go wrong without a defined protocol.
- The discussion of prior art and alternatives is adequately anchored by references to a companion paper and existing libraries.
- The most glaring omission is the lack of direct evidence for who is affected, with only a single performance table offered and no broader demonstration of user or ecosystem impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 7 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 10.00   accumulate 10.67   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.00  coordination 0.67  insufficiency 1.33  implementation 2.00
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 10.50 / 10.00 / 9.50   (all 3 samples: 10.00)
headings: h2 12
on threshold: audience, insufficiency
splits: vehicle[5] 0/1/1  vehicle[9] 1/0/1  coordination[7] 1/0/0  insufficiency[8] 1/1/0
        implementation[4] 0/1/0  implementation[13] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
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
candidate 2 (found by 3 of 39 passes): The awaitable cannot just call `h.resume()` - that resumes on the current thread, possibly while holding a lock, possibly re-entering code that is not re-entrant.
candidate 3 (found by 3 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 4 (found by 3 of 39 passes): Under type erasure, `connect(sndr, rcvr)` produces a type-dependent `op_state` that must be heap-allocated when either side is erased.

## audience - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      2/2/2  -> 2.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): | MSVC | Recycling | 1265.2 | 3.10x |

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
candidate 1 (found by 3 of 39 passes): A companion paper, [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1], provides the design rationale, evidence framework, preemptive objections, and analysis of alternative approaches.
candidate 2 (found by 3 of 39 passes): Coroutine-native I/O and `std::execution` are complementary.
candidate 3 (found by 3 of 39 passes): See [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1] for design rationale and analysis of alternative approaches.
candidate 4 (found by 3 of 39 passes): This design borrows from [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html)[9].

## vehicle - grade 1.00 (fired in 4 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/1/1  -> 0.67
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  1/1/1  -> 1.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                1/0/1  -> 0.67
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The two-argument signature is also a compile-time boundary check.
candidate 2 (found by 3 of 39 passes): The language provides what a library would reimplement.
candidate 3 (found by 2 of 39 passes): This protocol is a companion to [P2300R10](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2300r10.html)[6] `std::execution`.
candidate 4 (found by 2 of 39 passes): The *IoAwaitable* protocol provides the coroutine execution model beneath it.

## coordination - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  1/0/0  -> 0.33
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Interoperable tasks, awaitables
candidate 2 (found by 1 of 39 passes): If only this proposal ships and nothing else, we get:
candidate 3 (found by 1 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.

## insufficiency - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/0  -> 0.67
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Under type erasure, `connect(sndr, rcvr)` produces a type-dependent `op_state` that must be heap-allocated when either side is erased.
candidate 2 (found by 2 of 39 passes): The language provides what a library would reimplement.

## implementation - grade 2.00  [binary: max] (fired in 6 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/0  -> 0.33
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      1/1/1  -> 1.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     2/2/2  -> 2.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/2/0  -> 0.67
candidate 1 (found by 3 of 39 passes): Everything in this paper comes from a complete implementation on three platforms: [Capy](https://github.com/cppalliance/capy)[2] (protocol) and [Corosio](https://github.com/cppalliance/corosio)[3].
candidate 2 (found by 3 of 39 passes): The protocol must: * Provide a reasonable, customizable default * Propagate the frame allocator to every coroutine frame in the chain automatically
candidate 3 (found by 3 of 39 passes): A full implementation is available in [Capy](https://github.com/cppalliance/capy)[2] (`include/boost/capy/ex/when_all.hpp`).
candidate 4 (found by 3 of 39 passes): A companion to `std::execution`, implemented on three platforms.

-->
