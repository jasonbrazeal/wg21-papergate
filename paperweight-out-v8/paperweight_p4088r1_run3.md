Verdict: Strong to Excellent (12/14)

The paper makes a strong case for standardizing its coroutine-native I/O model, with particularly solid grounding in prior art, the need for a standard solution, and implementation experience. The support is thinnest around who is affected and why a library alone cannot deliver the same result, where the paper asserts more than it demonstrates.

- The strongest support comes from the paper’s account of prior art and alternatives, showing clearly how existing models fail and how the proposed approach differs from Asio and sender/receiver pipelines.
- The case for why this belongs in the standard is also well established, especially the argument that language-level coroutine frames provide type erasure and ABI stability that library-only approaches cannot match.
- Implementation experience is credibly documented through compiler support, production use, and benchmarks, though the paper leans on a small number of named deployments.
- The most glaring omission is the thin evidence for who is affected: the paper cites a few companies and a benchmark but does not establish the breadth of the problem or the cost to the broader C++ community.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 28. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 11.00   accumulate 12.67   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.83  coordination 1.67  insufficiency 1.17  implementation 2.00
sample agreement: 96 of 112 section-criterion pairs unanimous (86%)
single-sample totals would have been: 11.00 / 13.50 / 12.00   (all 3 samples: 11.83)
headings: h2 15
on threshold: coordination, insufficiency
splits: audience[5] 0/1/1  audience[6] 2/2/0  audience[11] 0/1/2  prior_art[4] 1/0/1
        prior_art[7] 2/2/0  vehicle[8] 0/0/1  vehicle[11] 2/2/1  vehicle[13] 0/1/0
        coordination[2] 0/1/0  coordination[10] 0/2/2  coordination[12] 1/0/0
        coordination[13] 0/1/0  insufficiency[11] 1/2/2  insufficiency[12] 0/2/0
        implementation[4] 0/1/0  implementation[12] 1/0/1
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
candidate 4 (found by 3 of 48 passes): The committee has been trying to standardize networking since [N1925] (2005). The contract that every attempt has been built on comes from Asio.

## audience - grade 1.17 (fired in 3 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/1/1  -> 0.67
  [6] 3. What Senders Buy                          2/2/0  -> 1.33
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/0  -> 0.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              0/1/2  -> 1.00
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 2 (found by 2 of 48 passes): The benchmark in Section 7.4 documents the cost: one allocation per operation, +23 ns.
candidate 3 (found by 1 of 48 passes): Production codebases have used them for six years.
candidate 4 (found by 1 of 48 passes): Every major compiler implements them. Production codebases have used them for six years.

## prior_art - grade 2.00 (fired in 10 of 16 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/1  -> 0.67
  [5] 2. Two Models Already Ship                   2/2/2  -> 2.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/2/0  -> 1.33
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             0/0/0  -> 0.00
  [10] 7. What The Frame Buys                       0/0/0  -> 0.00
  [11] 8. One Allocation Per Operation              2/2/2  -> 2.00
  [12] 9. Anticipated Objections                    2/2/2  -> 2.00
  [13] 10. The Design Fork                          2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): C++ already got an asynchronous model: regular C++20 coroutines.
candidate 2 (found by 3 of 48 passes): The four-layer composition example in [P4014R2](https://isocpp.org/files/papers/P4014R2.pdf) [4] Section 12 collapses from interleaved sender pipelines into a single coroutine.
candidate 3 (found by 3 of 48 passes): The completion token disappeared. In Asio, `async_read_some(mb, t)` takes a completion token `t` that determines the async model - callback, future, coroutine, or use_awaitable.
candidate 4 (found by 3 of 48 passes): Small buffer optimization (SBO) is another mitigation. SBO works for `std::function` because callable objects are often small - a few pointers.

## vehicle - grade 1.83 (fired in 8 of 16 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Two Models Already Ship                   0/0/0  -> 0.00
  [6] 3. What Senders Buy                          1/1/1  -> 1.00
  [7] 4. What Coroutines Pay                       0/0/0  -> 0.00
  [8] 5. Twenty Years, Nine Lines                  0/0/1  -> 0.33
  [9] 6. Why Did It Take Twenty Years?             1/1/1  -> 1.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              2/2/1  -> 1.67
  [12] 9. Anticipated Objections                    0/0/0  -> 0.00
  [13] 10. The Design Fork                          0/1/0  -> 0.33
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Underneath, five language mechanisms combine to produce type-erased streams, separate compilation, and ABI stability - properties the committee could not ship in twenty-one years of networking attempts.
candidate 2 (found by 3 of 48 passes): One standard async abstraction solves the interoperability problem.
candidate 3 (found by 3 of 48 passes): The coroutine-native approach succeeds by committing to one completion mechanism and giving up the rest.
candidate 4 (found by 3 of 48 passes): The frame the compiler already built is a type-erased storage location that the awaitable reuses at zero per-operation cost.

## coordination - grade 1.67 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
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
  [10] 7. What The Frame Buys                       0/2/2  -> 1.33
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    1/0/0  -> 0.33
  [13] 10. The Design Fork                          0/1/0  -> 0.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The committee has been trying to standardize networking since N1925 (2005). The contract that every attempt has been built on comes from Asio.
candidate 2 (found by 2 of 48 passes): The vtable layout of `any_read_stream` does not change. Libraries compiled today work with new transports tomorrow.
candidate 3 (found by 1 of 48 passes): properties the committee could not ship in twenty-one years of networking attempts.
candidate 4 (found by 1 of 48 passes): C and C++ interact through `extern "C"`. CPU and GPU interact through memory copies.

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
  [12] 9. Anticipated Objections                    0/2/0  -> 0.67
  [13] 10. The Design Fork                          0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The pool must know each operation state's size at construction time - the size depends on both the sender and the receiver, so the pool is parameterized on the pipeline shape.
candidate 2 (found by 1 of 48 passes): The coroutine model provides zero-allocation type erasure as a language consequence.
candidate 3 (found by 1 of 48 passes): The I/O types cannot be type-erased without per-operation allocation. The stream cannot be separately compiled.

## implementation - grade 2.00  [binary: max] (fired in 9 of 16 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/0  -> 0.33
  [5] 2. Two Models Already Ship                   1/1/1  -> 1.00
  [6] 3. What Senders Buy                          2/2/2  -> 2.00
  [7] 4. What Coroutines Pay                       2/2/2  -> 2.00
  [8] 5. Twenty Years, Nine Lines                  2/2/2  -> 2.00
  [9] 6. Why Did It Take Twenty Years?             2/2/2  -> 2.00
  [10] 7. What The Frame Buys                       2/2/2  -> 2.00
  [11] 8. One Allocation Per Operation              0/0/0  -> 0.00
  [12] 9. Anticipated Objections                    1/0/1  -> 0.67
  [13] 10. The Design Fork                          1/1/1  -> 1.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Every major compiler implements them. Production codebases have used them for six years.
candidate 2 (found by 3 of 48 passes): [P2470R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2470r0.pdf) [13] "Slides for presentation of P2300R2" documented the deployments: Facebook ("monthly users number in the billions"), NVIDIA ("fully invested in P2300... we plan to ship in production"), and Bloomberg (experimentation).
candidate 3 (found by 3 of 48 passes): A [benchmark](https://github.com/sgerbino/capy/tree/pr/beman-bench/bench/beman) [16] of 100,000,000 `read_some` calls on concrete streams measures both models at ~30-31 ns/op with zero allocations.
candidate 4 (found by 3 of 48 passes): [ReadStream](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/concept/read_stream.hpp) [2] formalizes the same contract as a C++20 concept:

-->
