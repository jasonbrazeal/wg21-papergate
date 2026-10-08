Verdict: Excellent (13/14)

The paper offers substantial support for standardizing its coroutine-native I/O model, with the strongest evidence concentrated in prior art, implementation experience, and the case for why the standard is the right venue. The thinnest part of the argument is the claim that a library alone cannot solve the problem; the paper asserts this but does not fully establish it.

- The paper convincingly grounds its proposal in two decades of committee history and the production-tested Asio contract that prior networking efforts have relied on.
- It demonstrates real implementation experience through shipping libraries, compiler support, and benchmarks showing zero-allocation performance comparable to existing models.
- The argument that the standard is necessary rests on completing the C++20 coroutine model rather than introducing a competing abstraction, and this is well supported.
- The most glaring omission is the underdeveloped case for why a library solution would be insufficient, since the paper claims but does not establish that type erasure and operation-state sizing cannot be handled outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.50/14)

Provisionally addressed: 7 of 7. Provisional points: 12.50 of 14. Unsupported quotes rejected: 29. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.50   corroborated 13.00   accumulate 13.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 2.00  vehicle 1.83  coordination 1.83  insufficiency 1.00  implementation 2.00
sample agreement: 99 of 112 section-criterion pairs unanimous (88%)
single-sample totals would have been: 13.00 / 13.00 / 12.00   (all 3 samples: 12.50)
headings: h2 15
on threshold: insufficiency
splits: audience[11] 2/2/1  audience[13] 1/0/0  prior_art[4] 0/1/0  prior_art[6] 0/0/2
        prior_art[11] 1/2/2  vehicle[2] 0/1/0  vehicle[9] 1/2/1  vehicle[11] 2/1/2
        vehicle[12] 1/0/1  coordination[8] 2/2/1  coordination[13] 1/0/0
        implementation[6] 0/2/1  implementation[11] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): properties the committee could not ship in twenty-one years of networking attempts.
candidate 2 (found by 3 of 48 passes): C++20 gave the committee `co_await`, `coroutine_handle<>`, and `promise_type`. It did not give the committee standard I/O operations that use them.
candidate 3 (found by 3 of 48 passes): Coroutines are not free. Three costs are irreducible.
candidate 4 (found by 3 of 48 passes): The committee has been trying to standardize networking since N1925 (2005). The contract that every attempt has been built on comes from Asio.

## audience - grade 1.83 (fired in 4 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              2/2/1  -> 1.67
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          1/0/0  -> 0.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Production codebases have used them for six years.
candidate 2 (found by 3 of 48 passes): Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 3 (found by 3 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.
candidate 4 (found by 1 of 48 passes): Both companions provide structured concurrency (`when_all`, `when_any`), stop token propagation, non-exception error channels, and production deployment at scale.

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/0  -> 0.33
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          0/0/2  -> 0.67
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              1/2/2  -> 1.67
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): C++ already got an asynchronous model: regular C++20 coroutines.
candidate 2 (found by 3 of 48 passes): `any_sender` type-erases the sender, not the receiver. `connect(any_sender, receiver)` still stamps the receiver type into the operation state.
candidate 3 (found by 3 of 48 passes): The bridge crossing cost is ~10-14 ns with zero allocations ([P4092R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4092r0.pdf)[25], [P4093R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4093r0.pdf)[26]).
candidate 4 (found by 3 of 48 passes): The committee designed five language mechanisms for generality: the coroutine frame, type-erased `coroutine_handle<>`, the awaitable protocol, `promise_type`, and symmetric transfer.

## vehicle - grade 1.83 (fired in 8 of 16 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          1/1/1  -> 1.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             1/2/1  -> 1.33
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              2/1/2  -> 1.67
  [12] 9. Anticipated Objections                    1/0/1  -> 0.67
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O does not introduce a fourth model. It completes the third.
candidate 2 (found by 3 of 48 passes): One standard async abstraction solves the interoperability problem.
candidate 3 (found by 3 of 48 passes): The frame the compiler already built is a type-erased storage location that the awaitable reuses at zero per-operation cost.
candidate 4 (found by 3 of 48 passes): The coroutine model provides zero-allocation type erasure as a language consequence.

## coordination - grade 1.83 (fired in 3 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  2/2/1  -> 1.67
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          1/0/0  -> 0.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The vtable layout of `any_read_stream` does not change. Libraries compiled today work with new transports tomorrow.
candidate 2 (found by 2 of 48 passes): The committee has been trying to standardize networking since N1925 (2005). The contract that every attempt has been built on comes from Asio.
candidate 3 (found by 1 of 48 passes): The contract that every attempt has been built on comes from Asio.
candidate 4 (found by 1 of 48 passes): Both companions provide structured concurrency (`when_all`, `when_any`), stop token propagation, non-exception error channels, and production deployment at scale.

## insufficiency - grade 1.00 (fired in 1 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): Under type erasure, the size depends on both the sender and receiver types, neither of which is known at compile time.
candidate 2 (found by 1 of 48 passes): The frame the compiler already built is the storage the awaitable already uses. No pool. No size calculation. No API threading. No per-connection management.
candidate 3 (found by 1 of 48 passes): The pool must know each operation state's size at construction time - the size depends on both the sender and the receiver, so the pool is parameterized on the pipeline shape.

## implementation - grade 2.00  [binary: max] (fired in 8 of 16 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          0/2/1  -> 1.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              1/0/0  -> 0.33
  [12] 9. Anticipated Objections                    1/1/1  -> 1.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Every major compiler implements them. Production codebases have used them for six years.
candidate 2 (found by 3 of 48 passes): A [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman)[16] of 100,000,000 `read_some` calls on concrete streams measures both models at ~30-31 ns/op with zero allocations.
candidate 3 (found by 3 of 48 passes): [ReadStream](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/concept/read_stream.hpp)[2] formalizes the same contract as a C++20 concept:
candidate 4 (found by 3 of 48 passes): Two libraries ship today ([Capy](https://github.com/cppalliance/capy)[2] and [Corosio](https://github.com/cppalliance/corosio)[3]) with a Boost review scheduled.

-->
