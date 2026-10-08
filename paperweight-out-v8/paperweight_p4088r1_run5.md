Verdict: Excellent (13/14)

The paper offers substantial support for standardizing its proposed facility, with particularly strong evidence of real-world use, implementation maturity, and interoperability with existing practice. The case is thinnest where it argues that a library solution cannot achieve the same goals, since that reasoning is asserted rather than demonstrated through comparison or counterexample.

- The strongest support comes from documented production deployments at Facebook, NVIDIA, and Bloomberg, alongside benchmarks showing zero-allocation performance comparable to existing models.
- The paper convincingly establishes that the coroutine-native approach builds on language mechanisms the committee already standardized and that its type-erasure and zero-allocation properties follow from those mechanisms.
- The interoperability argument is well grounded in the survival of the underlying I/O contract across two decades of standardization attempts and multiple transport implementations.
- The most glaring omission is the lack of established evidence that a library-only implementation would be insufficient, leaving the necessity of language-level standardization asserted but not proven.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.50/14)

Provisionally addressed: 7 of 7. Provisional points: 12.50 of 14. Unsupported quotes rejected: 24. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.50   corroborated 13.00   accumulate 12.83   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 2.00  vehicle 2.00  coordination 1.83  insufficiency 0.83  implementation 2.00
sample agreement: 102 of 112 section-criterion pairs unanimous (91%)
single-sample totals would have been: 12.50 / 13.00 / 12.00   (all 3 samples: 12.50)
headings: h2 15
on threshold: insufficiency
splits: audience[9] 1/0/1  audience[11] 1/2/2  audience[12] 1/0/1  prior_art[11] 1/2/1
        vehicle[8] 0/1/0  vehicle[9] 1/2/1  vehicle[12] 1/0/0  coordination[8] 2/2/1
        coordination[14] 1/0/0  insufficiency[11] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 8)
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
candidate 4 (found by 3 of 48 passes): The serial I/O domain - networking, files, pipes, TLS - has no standard facility.

## audience - grade 1.83 (fired in 5 of 16 sections, strong in 2)
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
  [9] 6. Why Did It Take Twenty Years?             1/0/1  -> 0.67
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              1/2/2  -> 1.67
  [12] 9. Anticipated Objections                    1/0/1  -> 0.67
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 2 (found by 3 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.
candidate 3 (found by 2 of 48 passes): Production codebases have used them for six years.
candidate 4 (found by 2 of 48 passes): On the `stdexec` issue tracker, a user [reported](https://github.com/NVIDIA/stdexec/issues/1564) [28] that `let_error([](int)` `{ ... })` does not compile when the upstream sender can also complete with `std::exception_ptr`.

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              1/2/1  -> 1.33
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): C++ already got an asynchronous model: regular C++20 coroutines.
candidate 2 (found by 3 of 48 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 48 passes): The four-layer composition example in [P4014R2](https://isocpp.org/files/papers/P4014R2.pdf) [4] Section 12 collapses from interleaved sender pipelines into a single coroutine.
candidate 4 (found by 3 of 48 passes): Senders and coroutines are not either/or. Niebler framed this directly [12]:

## vehicle - grade 2.00 (fired in 8 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          1/1/1  -> 1.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/1/0  -> 0.33
  [9] 6. Why Did It Take Twenty Years?             1/2/1  -> 1.33
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    1/0/0  -> 0.33
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The coroutine-native approach succeeds by committing to one completion mechanism and giving up the rest.
candidate 2 (found by 3 of 48 passes): The frame the compiler already built is a type-erased storage location that the awaitable reuses at zero per-operation cost.
candidate 3 (found by 3 of 48 passes): The coroutine model provides zero-allocation type erasure as a language consequence.
candidate 4 (found by 3 of 48 passes): The committee designed five language mechanisms for generality: the coroutine frame, type-erased `coroutine_handle<>`, the awaitable protocol, `promise_type`, and symmetric transfer.

## coordination - grade 1.83 (fired in 3 of 16 sections, strong in 2)
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
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The committee has been trying to standardize networking since N1925 (2005). The contract that every attempt has been built on comes from Asio.
candidate 2 (found by 2 of 48 passes): The vtable layout of `any_read_stream` does not change. Libraries compiled today work with new transports tomorrow.
candidate 3 (found by 1 of 48 passes): The Networking TS formalized it. The committee could not ship it. But the contract survived because it is correct.
candidate 4 (found by 1 of 48 passes): The contract has survived POSIX, BSD sockets, IOCP, Asio, the Networking TS, io_uring, and every transport from TCP to QUIC.

## insufficiency - grade 0.83 (fired in 1 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
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
  [11] 8. One Allocation Per Operation              2/2/1  -> 1.67
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): The pool must know each operation state's size at construction time - the size depends on both the sender and the receiver, so the pool is parameterized on the pipeline shape.
candidate 2 (found by 1 of 48 passes): A fixed SBO buffer must be sized for the worst case or fall back to heap allocation.
candidate 3 (found by 1 of 48 passes): The coroutine model provides zero-allocation type erasure as a language consequence.

## implementation - grade 2.00  [binary: max] (fired in 7 of 16 sections, strong in 5)
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
  [12] 9. Anticipated Objections                    1/1/1  -> 1.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Every major compiler implements them. Production codebases have used them for six years.
candidate 2 (found by 3 of 48 passes): [P2470R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2470r0.pdf) [13] "Slides for presentation of P2300R2" documented the deployments: Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 3 (found by 3 of 48 passes): A [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman) [16] of 100,000,000 `read_some` calls on concrete streams measures both models at ~30-31 ns/op with zero allocations.
candidate 4 (found by 3 of 48 passes): [ReadStream](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/concept/read_stream.hpp) [2] formalizes the same contract as a C++20 concept:

-->
