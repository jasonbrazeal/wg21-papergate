Verdict: Strong (10/14)

The paper offers solid grounding in its motivating problem, its relationship to prior work, and its implementation experience, but it leans heavily on a companion paper and on repeated slogans where it needs direct evidence about affected users, standardization necessity, and interoperability. The thinnest support is around the claim that the language, rather than a library, is required, and around who concretely benefits.

- The strongest support is the existence of complete, maintained implementations on three platforms, which gives the design a concrete basis.
- The paper clearly situates itself against prior art and alternatives, especially through the companion rationale document and the acknowledged debt to Boost.Asio.
- The case for why the standard must act, rather than a library, rests on brief assertions and a single type-erasure example rather than a sustained argument.
- The most glaring omission is evidence about who is affected: the benchmark table and the repeated “small protocol, big rewards” line do not establish the claimed audience or impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 8.67   accumulate 10.83   max 12.00

## SUMMARY
grades: motivation 1.67  audience 1.33  prior_art 2.00  vehicle 1.17  coordination 0.33  insufficiency 1.33  implementation 2.00
sample agreement: 79 of 91 section-criterion pairs unanimous (87%)
single-sample totals would have been: 9.50 / 10.50 / 9.50   (all 3 samples: 9.83)
headings: h2 12
on threshold: motivation, audience, insufficiency
splits: motivation[4] 0/1/1  motivation[6] 1/2/1  motivation[7] 0/1/1  motivation[10] 1/0/0
        audience[5] 0/1/1  prior_art[8] 1/2/2  vehicle[7] 1/0/0  vehicle[9] 2/1/1
        coordination[9] 0/1/1  insufficiency[8] 1/1/0  implementation[4] 0/2/1
        implementation[6] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 8 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/1  -> 0.67
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      1/2/1  -> 1.33
  [7] 4. The IoAwaitable Protocol                  0/1/1  -> 0.67
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                1/0/0  -> 0.33
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): For this to work, something must decide where the coroutine resumes, whether it should stop, and where its frame is allocated.
candidate 2 (found by 2 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.
candidate 3 (found by 2 of 39 passes): This is the question that drives the entire protocol.
candidate 4 (found by 2 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.

## audience - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/1/1  -> 0.67
  [6] 3. What Coroutines Need                      2/2/2  -> 2.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): | MSVC | Recycling | 1265.2 | 3.10x |
candidate 2 (found by 2 of 39 passes): Small protocol, big rewards. It earns its keep.

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
  [8] 5. IoAwaitable Is Structured Concurrency     1/2/2  -> 1.67
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A companion paper, [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1], provides the design rationale, evidence framework, preemptive objections, and analysis of alternative approaches.
candidate 2 (found by 3 of 39 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 39 passes): See [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1] for design rationale and analysis of alternative approaches.
candidate 4 (found by 3 of 39 passes): This design borrows from [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html)[9].

## vehicle - grade 1.17 (fired in 4 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  1/0/0  -> 0.33
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                2/1/1  -> 1.33
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Small protocol, big rewards. It earns its keep.
candidate 2 (found by 3 of 39 passes): The language provides what a library would reimplement.
candidate 3 (found by 1 of 39 passes): The two-argument signature is also a compile-time boundary check.
candidate 4 (found by 1 of 39 passes): Under type erasure, `connect(sndr, rcvr)` produces a type-dependent `op_state` that must be heap-allocated when either side is erased.

## coordination - grade 0.33 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/1/1  -> 0.67
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): A TAPS implementation needs coroutines that suspend, resume correctly, cancel, and allocate frames - exactly what this protocol provides.

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

## implementation - grade 2.00  [binary: max] (fired in 5 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/2/1  -> 1.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/1  -> 0.33
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     2/2/2  -> 2.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Everything in this paper comes from a complete implementation on three platforms: [Capy](https://github.com/cppalliance/capy)[2] (protocol) and [Corosio](https://github.com/cppalliance/corosio)[3].
candidate 2 (found by 3 of 39 passes): A full implementation is available in [Capy](https://github.com/cppalliance/capy)[2] (`include/boost/capy/ex/when_all.hpp`).
candidate 3 (found by 3 of 39 passes): A companion to `std::execution`, implemented on three platforms.
candidate 4 (found by 1 of 39 passes): Falco and Gerbino developed and maintain [Capy](https://github.com/cppalliance/capy)[2] and [Corosio](https://github.com/cppalliance/corosio)[3]

-->
