Verdict: Excellent (13/14)

The paper offers substantial support for its own standardization, with the strongest evidence concentrated in the problem statement, prior art, implementation experience, and interoperability story. The thinnest part of the case is the claim that a library solution cannot suffice, which is asserted more than demonstrated.

- The paper convincingly establishes that coroutine-based I/O addresses a real, measured cost and that major production users already depend on the underlying model.
- The interoperability and prior-art sections show a long, consistent history of the contract the proposal builds on, including the committee’s own repeated attempts.
- The implementation experience is concrete, with compiler support, production deployments, and benchmarks showing zero-allocation performance.
- The argument that a library cannot solve the problem is the most glaring omission, since the paper asserts constraints on type erasure and operation-state pooling without fully establishing why they resist a non-standard solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.67/14)

Provisionally addressed: 7 of 7. Provisional points: 12.67 of 14. Unsupported quotes rejected: 22. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.67   corroborated 12.00   accumulate 13.17   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.00  implementation 2.00
sample agreement: 95 of 112 section-criterion pairs unanimous (85%)
single-sample totals would have been: 13.00 / 13.00 / 13.00   (all 3 samples: 12.67)
headings: h2 15
on threshold: audience, insufficiency
splits: audience[5] 0/1/0  audience[10] 2/0/2  audience[11] 1/1/2  prior_art[7] 2/0/2
        prior_art[14] 0/1/0  vehicle[2] 1/0/1  vehicle[6] 2/0/1  vehicle[9] 1/2/0
        vehicle[10] 2/1/2  vehicle[12] 0/0/1  coordination[2] 0/1/0  coordination[9] 1/0/0
        coordination[11] 0/0/1  insufficiency[9] 0/1/0  insufficiency[11] 2/2/1
        insufficiency[12] 0/0/1  implementation[12] 1/1/0
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
candidate 1 (found by 3 of 48 passes): C++20 gave the committee `co_await`, `coroutine_handle<>`, and `promise_type`. It did not give the committee standard I/O operations that use them.
candidate 2 (found by 3 of 48 passes): Coroutines are not free. Three costs are irreducible.
candidate 3 (found by 3 of 48 passes): The serial I/O domain - networking, files, pipes, TLS - has no standard facility.
candidate 4 (found by 3 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.

## audience - grade 1.67 (fired in 4 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/1/0  -> 0.33
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       2/0/2  -> 1.33
  [11] 8. One Allocation Per Operation              1/1/2  -> 1.33
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 2 (found by 3 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.
candidate 3 (found by 2 of 48 passes): The [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman)[16] measures the cost. 100,000,000 `read_some` calls on a single thread, no-op stream, five runs per configuration:
candidate 4 (found by 1 of 48 passes): Production codebases have used them for six years.

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/0/2  -> 1.33
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              1/1/1  -> 1.00
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               0/1/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): C++ already got an asynchronous model: regular C++20 coroutines.
candidate 2 (found by 3 of 48 passes): The four-layer composition example in [P4014R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4014r0.pdf)[4] Section 12 collapses from interleaved sender pipelines into a single coroutine.
candidate 3 (found by 3 of 48 passes): The Networking TS formalized it. The committee could not ship it. But the contract survived because it is correct.
candidate 4 (found by 3 of 48 passes): Small buffer optimization (SBO) is another mitigation.

## vehicle - grade 2.00 (fired in 8 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          2/0/1  -> 1.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             1/2/0  -> 1.00
  [10] 7. What The Frame Buys                       2/1/2  -> 1.67
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    0/0/1  -> 0.33
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): C++20 gave the committee `co_await`, `coroutine_handle<>`, and `promise_type`. It did not give the committee standard I/O operations that use them.
candidate 2 (found by 3 of 48 passes): The committee designed five language mechanisms for generality: the coroutine frame, type-erased `coroutine_handle<>`, the awaitable protocol, `promise_type`, and symmetric transfer.
candidate 3 (found by 2 of 48 passes): Underneath, five language mechanisms combine to produce type-erased streams, separate compilation, and ABI stability - properties the committee could not ship in twenty-one years of networking attempts.
candidate 4 (found by 2 of 48 passes): One standard async abstraction solves the interoperability problem.

## coordination - grade 2.00 (fired in 5 of 16 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             1/0/0  -> 0.33
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/1  -> 0.33
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The vtable layout of `any_read_stream` does not change. Libraries compiled today work with new transports tomorrow.
candidate 2 (found by 2 of 48 passes): The committee has been trying to standardize networking since N1925 (2005). The contract that every attempt has been built on comes from Asio.
candidate 3 (found by 1 of 48 passes): properties the committee could not ship in twenty-one years of networking attempts.
candidate 4 (found by 1 of 48 passes): The contract that every attempt has been built on comes from Asio.

## insufficiency - grade 1.00 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             0/1/0  -> 0.33
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              2/2/1  -> 1.67
  [12] 9. Anticipated Objections                    0/0/1  -> 0.33
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The pool must know each operation state's size at construction time - the size depends on both the sender and the receiver, so the pool is parameterized on the pipeline shape.
candidate 2 (found by 1 of 48 passes): Asio supports every async model - callbacks, futures, coroutines, and completion tokens.
candidate 3 (found by 1 of 48 passes): The coroutine model provides zero-allocation type erasure as a language consequence.
candidate 4 (found by 1 of 48 passes): The I/O types cannot be type-erased without per-operation allocation.

## implementation - grade 2.00  [binary: max] (fired in 8 of 16 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    1/1/0  -> 0.67
  [13] 10. The Design Fork                          1/1/1  -> 1.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Every major compiler implements them. Production codebases have used them for six years.
candidate 2 (found by 3 of 48 passes): [P2470R0](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2470r0.pdf)[13] "Slides for presentation of P2300R2" documented the deployments: Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 3 (found by 3 of 48 passes): A [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman)[16] of 100,000,000 `read_some` calls on concrete streams measures both models at ~30-31 ns/op with zero allocations.
candidate 4 (found by 3 of 48 passes): [ReadStream](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/concept/read_stream.hpp)[2] formalizes the same contract as a C++20 concept:

-->
