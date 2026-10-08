Verdict: Excellent (13/14)

The paper offers substantial support for standardizing its coroutine-native async model, with the strongest evidence concentrated in its account of existing practice, prior art, and the language-level properties that make the approach viable. The case is thinnest where it argues that a library solution cannot suffice, since those claims are asserted rather than demonstrated.

- The paper’s strongest support comes from documented production use, shipped libraries, and benchmark data showing zero-allocation performance on concrete streams.
- It clearly establishes why the standard is the right venue by tying the design to language mechanisms that enable type erasure, separate compilation, and ABI stability.
- The most glaring omission is the lack of established evidence for the claim that the pool must know operation state sizes at construction time, which underpins the argument against a library-only solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.67/14)

Provisionally addressed: 7 of 7. Provisional points: 12.67 of 14. Unsupported quotes rejected: 27. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.67   corroborated 12.00   accumulate 12.83   max 13.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 1.50  insufficiency 1.17  implementation 2.00
sample agreement: 97 of 112 section-criterion pairs unanimous (87%)
single-sample totals would have been: 12.00 / 12.00 / 14.00   (all 3 samples: 12.67)
headings: h2 15
on threshold: coordination, insufficiency
splits: audience[9] 0/1/0  audience[12] 0/0/1  prior_art[4] 0/1/1  prior_art[11] 1/2/2
        vehicle[5] 0/2/1  vehicle[6] 1/0/1  vehicle[9] 2/1/1  vehicle[12] 1/1/0
        vehicle[14] 0/1/1  coordination[2] 1/0/0  coordination[10] 1/0/2
        insufficiency[11] 1/2/2  insufficiency[12] 0/0/2  implementation[4] 0/1/0
        implementation[8] 0/2/2
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
candidate 1 (found by 3 of 48 passes): C++20 gave the committee `co_await`, `coroutine_handle<>`, and `promise_type`. It did not give the committee standard I/O operations that use them.
candidate 2 (found by 3 of 48 passes): Coroutines are not free. Three costs are irreducible.
candidate 3 (found by 3 of 48 passes): The frame allocation is the cost every design avoids. This design accepts it. The frame the compiler already built is a type-erased storage location that the awaitable reuses at zero per-operation cost.
candidate 4 (found by 3 of 48 passes): Six objections to the coroutine-native model are well-known. We concede every one.

## audience - grade 2.00 (fired in 4 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             0/1/0  -> 0.33
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    0/0/1  -> 0.33
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 2 (found by 3 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.
candidate 3 (found by 1 of 48 passes): Two libraries ship today ([Capy](https://github.com/cppalliance/capy) [2] and [Corosio](https://github.com/cppalliance/corosio) [3]) with a Boost review scheduled.
candidate 4 (found by 1 of 48 passes): The `retry` algorithm: approximately 120 lines as a sender, seven as a coroutine.

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/1  -> 0.67
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
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
candidate 2 (found by 3 of 48 passes): The four-layer composition example in [P4014R2](https://isocpp.org/files/papers/P4014R2.pdf) [4] Section 12 collapses from interleaved sender pipelines into a single coroutine.
candidate 3 (found by 3 of 48 passes): Senders and coroutines are not either/or. Niebler framed this directly [12]:
candidate 4 (found by 3 of 48 passes): HALO ([P0981R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p0981r0.html) [14] "Halo: coroutine Heap Allocation eLision Optimization") can elide the allocation when the compiler proves the frame's lifetime is bounded by the caller's scope, but no compiler guarantees HALO.

## vehicle - grade 2.00 (fired in 8 of 16 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/2/1  -> 1.00
  [6] 3. What Senders Buy                          1/0/1  -> 0.67
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             2/1/1  -> 1.33
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    1/1/0  -> 0.67
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/1/1  -> 0.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Underneath, five language mechanisms combine to produce type-erased streams, separate compilation, and ABI stability - properties the committee could not ship in twenty-one years of networking attempts.
candidate 2 (found by 3 of 48 passes): The coroutine-native approach succeeds by committing to one completion mechanism and giving up the rest.
candidate 3 (found by 2 of 48 passes): One standard async abstraction solves the interoperability problem.
candidate 4 (found by 2 of 48 passes): The frame the compiler already built is a type-erased storage location that the awaitable reuses at zero per-operation cost.

## coordination - grade 1.50 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          0/0/0  -> 0.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       1/0/2  -> 1.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The committee has been trying to standardize networking since N1925 (2005). The contract that every attempt has been built on comes from Asio.
candidate 2 (found by 2 of 48 passes): The vtable layout of `any_read_stream` does not change. Libraries compiled today work with new transports tomorrow.
candidate 3 (found by 1 of 48 passes): ABI stability - properties the committee could not ship in twenty-one years of networking attempts.

## insufficiency - grade 1.17 (fired in 2 of 16 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
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
  [11] 8. One Allocation Per Operation              1/2/2  -> 1.67
  [12] 9. Anticipated Objections                    0/0/2  -> 0.67
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The pool must know each operation state's size at construction time - the size depends on both the sender and the receiver, so the pool is parameterized on the pipeline shape.
candidate 2 (found by 1 of 48 passes): The coroutine model provides zero-allocation type erasure as a language consequence.
candidate 3 (found by 1 of 48 passes): The I/O types cannot be type-erased without per-operation allocation. The stream cannot be separately compiled.

## implementation - grade 2.00  [binary: max] (fired in 9 of 16 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/0  -> 0.33
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  0/2/2  -> 1.33
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    1/1/1  -> 1.00
  [13] 10. The Design Fork                          1/1/1  -> 1.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Every major compiler implements them. Production codebases have used them for six years.
candidate 2 (found by 3 of 48 passes): [P2470R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2470r0.pdf) [13] "Slides for presentation of P2300R2" documented the deployments: Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 3 (found by 3 of 48 passes): A [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman) [16] of 100,000,000 `read_some` calls on concrete streams measures both models at ~30-31 ns/op with zero allocations.
candidate 4 (found by 3 of 48 passes): Two libraries ship today ([Capy](https://github.com/cppalliance/capy) [2] and [Corosio](https://github.com/cppalliance/corosio) [3]) with a Boost review scheduled.

-->
