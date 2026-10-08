Verdict: Strong (10/14)

The paper’s support for its own standardization is uneven: it grounds the design in a real implementation and a companion rationale, but it leaves several audience and standardization arguments more asserted than demonstrated. The thinnest areas are the evidence about who is affected, the case for why this belongs in the standard rather than a library, and how it coordinates with adjacent async models.

- The strongest support comes from implementation experience, with the protocol described as fully implemented across three platforms and available in named projects.
- The paper also establishes prior art and alternatives by pointing to a companion paper that analyzes design rationale, evidence, objections, and alternative approaches.
- The argument for why a library will not do is established through the claim that the language provides what a library would otherwise reimplement and that type erasure forces heap allocation of operation state.
- The most glaring omission is the lack of established evidence for who is affected, since the cited performance table and broad claims about rewards do not substantiate the affected audience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 8.67   accumulate 11.17   max 11.67

## SUMMARY
grades: motivation 1.67  audience 1.17  prior_art 2.00  vehicle 1.00  coordination 0.50  insufficiency 1.50  implementation 2.00
sample agreement: 81 of 91 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.50 / 9.00 / 10.50   (all 3 samples: 9.83)
headings: h2 12
on threshold: motivation, audience, insufficiency
splits: motivation[6] 2/1/1  motivation[7] 1/0/1  audience[5] 0/0/1  prior_art[8] 2/1/2
        vehicle[7] 0/0/1  vehicle[10] 0/1/0  coordination[5] 1/0/0  coordination[7] 0/0/1
        coordination[9] 1/0/1  implementation[6] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 6 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      2/1/1  -> 1.33
  [7] 4. The IoAwaitable Protocol                  1/0/1  -> 0.67
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): For this to work, something must decide where the coroutine resumes, whether it should stop, and where its frame is allocated.
candidate 2 (found by 3 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.
candidate 3 (found by 3 of 39 passes): Under type erasure, `connect(sndr, rcvr)` produces a type-dependent `op_state` that must be heap-allocated when either side is erased.
candidate 4 (found by 2 of 39 passes): This is the question that drives the entire protocol.

## audience - grade 1.17 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/1  -> 0.33
  [6] 3. What Coroutines Need                      2/2/2  -> 2.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): | MSVC | Recycling | 1265.2 | 3.10x |
candidate 2 (found by 1 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.

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
  [8] 5. IoAwaitable Is Structured Concurrency     2/1/2  -> 1.67
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A companion paper, [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1], provides the design rationale, evidence framework, preemptive objections, and analysis of alternative approaches.
candidate 2 (found by 3 of 39 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 39 passes): See [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1] for design rationale and analysis of alternative approaches.
candidate 4 (found by 3 of 39 passes): Built on `std::stop_token`.

## vehicle - grade 1.00 (fired in 5 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/1  -> 0.33
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                1/1/1  -> 1.00
  [10] 7. Conclusion                                0/1/0  -> 0.33
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The language provides what a library would reimplement.
candidate 2 (found by 3 of 39 passes): The *IoAwaitable* protocol provides the coroutine execution model beneath it.
candidate 3 (found by 2 of 39 passes): Small protocol, big rewards. It earns its keep.
candidate 4 (found by 1 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.

## coordination - grade 0.50 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/0/0  -> 0.33
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/1  -> 0.33
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                1/0/1  -> 0.67
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): A TAPS implementation needs coroutines that suspend, resume correctly, cancel, and allocate frames - exactly what this protocol provides.
candidate 2 (found by 1 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.
candidate 3 (found by 1 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.

## insufficiency - grade 1.50 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The language provides what a library would reimplement.
candidate 2 (found by 3 of 39 passes): Under type erasure, `connect(sndr, rcvr)` produces a type-dependent `op_state` that must be heap-allocated when either side is erased.

## implementation - grade 2.00  [binary: max] (fired in 4 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
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
candidate 4 (found by 1 of 39 passes): The protocol must: * Provide a reasonable, customizable default * Propagate the frame allocator to every coroutine frame in the chain automatically

-->
