Verdict: Strong (9/14)

The paper offers substantial support in the areas that matter most for a proposal of this kind: it explains the motivating problem clearly, points to a companion rationale document and prior art, and demonstrates real implementation experience across multiple platforms. The support is thinnest where the standardization argument needs to be self-contained, since the claims about why the standard library or language is necessary, how the design interoperates with existing models, and why a library alone cannot suffice are asserted rather than demonstrated in this document.

- The strongest support is the concrete implementation experience, with the protocol and its components available in working code on three platforms.
- The paper clearly establishes why the problem matters, framing the coroutine execution model as a small protocol with broad consequences for structured concurrency.
- The prior art and alternatives are adequately covered through explicit references to a companion paper, existing proposals, and Boost.Asio.
- The most glaring omission is the absence of any discussion of who is affected by the proposal, leaving the audience and impact unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 6 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 8.67   accumulate 9.00   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 0.67  insufficiency 1.33  implementation 2.00
sample agreement: 83 of 91 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.00 / 8.50 / 9.50   (all 3 samples: 8.83)
headings: h2 12
on threshold: insufficiency
splits: motivation[8] 2/1/1  motivation[10] 0/1/1  vehicle[9] 1/0/1  coordination[5] 0/1/1
        coordination[7] 1/0/1  coordination[9] 1/0/0  insufficiency[8] 0/1/1
        implementation[4] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               1/1/1  -> 1.00
  [6] 3. What Coroutines Need                      2/2/2  -> 2.00
  [7] 4. The IoAwaitable Protocol                  1/1/1  -> 1.00
  [8] 5. IoAwaitable Is Structured Concurrency     2/1/1  -> 1.33
  [9] 6. Why Not exec::asawaitable?                2/2/2  -> 2.00
  [10] 7. Conclusion                                0/1/1  -> 0.67
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): For this to work, something must decide where the coroutine resumes, whether it should stop, and where its frame is allocated.
candidate 2 (found by 3 of 39 passes): The left column is small. The right column is not. Small protocol, big rewards. It earns its keep.
candidate 3 (found by 3 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 4 (found by 3 of 39 passes): The argument that senders provide structured concurrency and coroutines do not has it backwards: the *IoAwaitable* protocol is the layer from which structured concurrency constructs are assembled.

## audience - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

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
candidate 2 (found by 3 of 39 passes): See [P4172R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4172r0.pdf)[1] for design rationale and analysis of alternative approaches.
candidate 3 (found by 3 of 39 passes): A regular function cannot `co_await` (see [P4035R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4035r0.pdf)[7] for a discussion of coroutine escape hatches).
candidate 4 (found by 3 of 39 passes): This design borrows from [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html)[9].

## vehicle - grade 0.83 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     1/1/1  -> 1.00
  [9] 6. Why Not exec::asawaitable?                1/0/1  -> 0.67
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The language provides what a library would reimplement.
candidate 2 (found by 2 of 39 passes): The *IoAwaitable* protocol provides the coroutine execution model beneath it.

## coordination - grade 0.67 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What We Get                               0/1/1  -> 0.67
  [6] 3. What Coroutines Need                      0/0/0  -> 0.00
  [7] 4. The IoAwaitable Protocol                  1/0/1  -> 0.67
  [8] 5. IoAwaitable Is Structured Concurrency     0/0/0  -> 0.00
  [9] 6. Why Not exec::asawaitable?                1/0/0  -> 0.33
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Interoperable tasks, awaitables
candidate 2 (found by 2 of 39 passes): In a world with multiple coexisting async models, a coroutine that accidentally `co_await`s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 3 (found by 1 of 39 passes): A TAPS implementation needs coroutines that suspend, resume correctly, cancel, and allocate frames - exactly what this protocol provides.

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
  [8] 5. IoAwaitable Is Structured Concurrency     0/1/1  -> 0.67
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
  [4] 1. Disclosure                                0/2/0  -> 0.67
  [5] 2. What We Get                               0/0/0  -> 0.00
  [6] 3. What Coroutines Need                      1/1/1  -> 1.00
  [7] 4. The IoAwaitable Protocol                  0/0/0  -> 0.00
  [8] 5. IoAwaitable Is Structured Concurrency     2/2/2  -> 2.00
  [9] 6. Why Not exec::asawaitable?                0/0/0  -> 0.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Poll                      0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Everything in this paper comes from a complete implementation on three platforms: [Capy](https://github.com/cppalliance/capy)[2] (protocol) and [Corosio](https://github.com/cppalliance/corosio)[3].
candidate 2 (found by 3 of 39 passes): The protocol must: * Provide a reasonable, customizable default * Propagate the frame allocator to every coroutine frame in the chain automatically
candidate 3 (found by 3 of 39 passes): A full implementation is available in [Capy](https://github.com/cppalliance/capy)[2] (`include/boost/capy/ex/when_all.hpp`).
candidate 4 (found by 3 of 39 passes): A companion to `std::execution`, implemented on three platforms.

-->
