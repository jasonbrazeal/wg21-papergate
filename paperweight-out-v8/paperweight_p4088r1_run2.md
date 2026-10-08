Verdict: Excellent (13/14)

The paper makes a generally strong case for standardizing coroutine-native I/O, with most of the necessary groundwork—importance, affected users, prior art, implementation experience, and interoperability—backed by concrete evidence and shipped libraries. The support is thinnest where the paper argues that a library-only solution cannot suffice, since that argument is asserted rather than demonstrated.

- The strongest support comes from implementation experience, with two shipping libraries, a Boost review scheduled, and benchmarks showing zero-allocation performance comparable to existing models.
- The paper also establishes clearly why the standard matters, pointing to two decades of failed networking standardization and the absence of standard I/O operations for C++20 coroutines.
- Coordination and interoperability are well supported by the claim that the vtable layout remains stable, allowing libraries compiled today to work with future transports.
- The most glaring omission is the unproven assertion that the I/O types cannot be type-erased without per-operation allocation, which underpins the case against a library-only approach but is never established.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.83/14)

Provisionally addressed: 7 of 7. Provisional points: 12.83 of 14. Unsupported quotes rejected: 27. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.83   corroborated 12.00   accumulate 13.33   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.17  implementation 2.00
sample agreement: 94 of 112 section-criterion pairs unanimous (84%)
single-sample totals would have been: 13.50 / 12.50 / 13.00   (all 3 samples: 12.83)
headings: h2 15
on threshold: audience, insufficiency
splits: motivation[10] 2/0/0  motivation[14] 1/1/2  audience[5] 0/1/0  audience[9] 1/0/1
        audience[10] 2/0/0  audience[11] 1/1/2  prior_art[6] 0/2/0  vehicle[5] 2/1/1
        vehicle[6] 1/0/1  vehicle[9] 1/2/1  vehicle[12] 0/2/2  coordination[2] 0/1/0
        insufficiency[9] 1/0/0  insufficiency[12] 1/0/0  implementation[5] 1/0/1
        implementation[6] 1/1/2  implementation[12] 0/0/1  implementation[13] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 7)  (SHARED PASSAGE)
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
  [10] 7. What The Frame Buys                       2/0/0  -> 0.67
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/2  -> 1.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): properties the committee could not ship in twenty-one years of networking attempts.
candidate 2 (found by 3 of 48 passes): C++20 gave the committee `co_await`, `coroutine_handle<>`, and `promise_type`. It did not give the committee standard I/O operations that use them.
candidate 3 (found by 3 of 48 passes): Coroutines are not free. Three costs are irreducible.
candidate 4 (found by 3 of 48 passes): The serial I/O domain - networking, files, pipes, TLS - has no standard facility.

## audience - grade 1.67 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [9] 6. Why Did It Take Twenty Years?             1/0/1  -> 0.67
  [10] 7. What The Frame Buys                       2/0/0  -> 0.67
  [11] 8. One Allocation Per Operation              1/1/2  -> 1.33
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 2 (found by 3 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.
candidate 3 (found by 2 of 48 passes): Two libraries ship today ([Capy](https://github.com/cppalliance/capy) [2] and [Corosio](https://github.com/cppalliance/corosio) [3]) with a Boost review scheduled.
candidate 4 (found by 1 of 48 passes): Production codebases have used them for six years.

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          0/2/0  -> 0.67
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              1/1/1  -> 1.00
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): C++ already got an asynchronous model: regular C++20 coroutines.
candidate 2 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 48 passes): The `retry` algorithm requires approximately 120 lines of template machinery as a sender; the coroutine equivalent is seven lines.
candidate 4 (found by 3 of 48 passes): The Networking TS formalized it. The committee could not ship it. But the contract survived because it is correct.

## vehicle - grade 2.00 (fired in 7 of 16 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   2/1/1  -> 1.33
  [6] 3. What Senders Buy                          1/0/1  -> 0.67
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             1/2/1  -> 1.33
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    0/2/2  -> 1.33
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Coroutine-native I/O does not introduce a fourth model. It completes the third.
candidate 2 (found by 3 of 48 passes): The coroutine-native approach succeeds by committing to one completion mechanism and giving up the rest.
candidate 3 (found by 3 of 48 passes): The frame the compiler already built is a type-erased storage location that the awaitable reuses at zero per-operation cost.
candidate 4 (found by 3 of 48 passes): The committee designed five language mechanisms for generality: the coroutine frame, type-erased `coroutine_handle<>`, the awaitable protocol, `promise_type`, and symmetric transfer.

## coordination - grade 2.00 (fired in 3 of 16 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The vtable layout of `any_read_stream` does not change. Libraries compiled today work with new transports tomorrow.
candidate 2 (found by 1 of 48 passes): properties the committee could not ship in twenty-one years of networking attempts.
candidate 3 (found by 1 of 48 passes): The committee has been trying to standardize networking since [N1925] (2005). The contract that every attempt has been built on comes from Asio.
candidate 4 (found by 1 of 48 passes): The committee has been trying to standardize networking since [N1925](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2005/n1925.pdf) [8] (2005). The contract that every attempt has been built on comes from Asio.

## insufficiency - grade 1.17 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             1/0/0  -> 0.33
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    1/0/0  -> 0.33
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The pool must know each operation state's size at construction time - the size depends on both the sender and the receiver, so the pool is parameterized on the pipeline shape.
candidate 2 (found by 1 of 48 passes): The I/O operations must be templates, the operation states must be parameterized on the completion handler type, and the stream model cannot be type-erased without per-operation allocation.
candidate 3 (found by 1 of 48 passes): Under type erasure, the size depends on both the sender and receiver types, neither of which is known at compile time.
candidate 4 (found by 1 of 48 passes): The I/O types cannot be type-erased without per-operation allocation.

## implementation - grade 2.00  [binary: max] (fired in 8 of 16 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   1/0/1  -> 0.67
  [6] 3. What Senders Buy                          1/1/2  -> 1.33
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    0/0/1  -> 0.33
  [13] 10. The Design Fork                          0/0/1  -> 0.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): A [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman) [16] of 100,000,000 `read_some` calls on concrete streams measures both models at ~30-31 ns/op with zero allocations.
candidate 2 (found by 3 of 48 passes): [ReadStream](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/concept/read_stream.hpp) [2] formalizes the same contract as a C++20 concept:
candidate 3 (found by 3 of 48 passes): Two libraries ship today ([Capy](https://github.com/cppalliance/capy) [2] and [Corosio](https://github.com/cppalliance/corosio) [3]) with a Boost review scheduled.
candidate 4 (found by 3 of 48 passes): The [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman) [16] measures the cost. 100,000,000 `read_some` calls on a single thread, no-op stream, five runs per configuration:

-->
