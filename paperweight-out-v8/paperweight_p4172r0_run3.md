Verdict: Excellent (13/14)

The paper offers substantial support for most of the standardization case, with particularly strong evidence on prior art, the limits of library-only solutions, and implementation experience. The support is thinnest around who is affected: the paper asserts breadth of impact but does not demonstrate it with concrete populations, adoption data, or representative use cases.

- The strongest support is the implementation and historical record, including a decade of unchanged Boost.Asio service APIs and a production-ready reference implementation.
- The paper also convincingly establishes why a library will not do, citing template explosion, ABI instability, and the failure of twenty years of ecosystem effort to produce a shared async vocabulary.
- The most glaring omission is the audience claim, which rests on broad assertions like “the largest population” and “every audience” without evidence of who actually encounters these facilities or at what scale.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.83/14)

Provisionally addressed: 7 of 7. Provisional points: 12.83 of 14. Unsupported quotes rejected: 27. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.83   corroborated 12.00   accumulate 13.83   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.50  implementation 2.00
sample agreement: 117 of 133 section-criterion pairs unanimous (88%)
single-sample totals would have been: 12.50 / 13.50 / 13.00   (all 3 samples: 12.83)
headings: h2 18
on threshold: audience, insufficiency
splits: motivation[6] 1/1/2  motivation[7] 1/2/2  audience[5] 0/1/0  audience[6] 0/1/1
        audience[7] 0/1/1  prior_art[17] 0/1/0  vehicle[8] 2/1/1  vehicle[10] 1/1/0
        coordination[11] 2/0/0  coordination[12] 1/0/2  coordination[14] 1/2/1
        insufficiency[8] 1/2/0  insufficiency[12] 0/0/1  insufficiency[14] 1/1/0
        implementation[8] 1/2/1  implementation[14] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 19 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 1/1/2  -> 1.33
  [7] 4. Protocol Basics                           1/2/2  -> 1.67
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       1/1/1  -> 1.00
  [11] 8. Frame Allocator Propagation               2/2/2  -> 2.00
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (P4133R0[... 2/2/2  -> 2.00
  [15] Appendix A: Understanding Asynchronous I/O   2/2/2  -> 2.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Without that waist, every stack reinvents incompatible task types and environments; an HTTP layer on one model does not compose with storage or RPC on another.
candidate 2 (found by 3 of 57 passes): This compiles silently when promise and awaitable are mismatched - a coroutine from one async model can `co_await` an awaitable from another, producing runtime errors instead of compile-time failures.
candidate 3 (found by 3 of 57 passes): The mimalloc result is the critical comparison: a state-of-the-art general-purpose allocator with per-thread caches, yet the recycling frame allocator is 1.28x faster.
candidate 4 (found by 3 of 57 passes): Every `co_await` in the chain must forward the allocator.

## audience - grade 1.33 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/1/0  -> 0.33
  [6] 3. Audiences                                 0/1/1  -> 0.67
  [7] 4. Protocol Basics                           0/1/1  -> 0.67
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The largest population.
candidate 2 (found by 2 of 57 passes): These facilities are encountered by every audience.
candidate 3 (found by 2 of 57 passes): The mimalloc result is the critical comparison: a state-of-the-art general-purpose allocator with per-thread caches, yet the recycling frame allocator is 1.28x faster.
candidate 4 (found by 1 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           1/1/1  -> 1.00
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       2/2/2  -> 2.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   1/1/1  -> 1.00
  [16] Appendix B: anyreadstream                    1/1/1  -> 1.00
  [17] Appendix C: ioawaitablepromisebase           0/1/0  -> 0.33
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This paper is the companion record: why each facility exists, what alternatives were considered, how each choice was forced by the constraints of the domain, and where the historical evidence lives.
candidate 2 (found by 3 of 57 passes): The alternative of leaving coroutine I/O vocabulary to the ecosystem was considered. [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html)[5] has been available for over twenty years. In that time, the C++ ecosystem has not produced a shared task type or environment protocol for async I/O.
candidate 3 (found by 3 of 57 passes): The *IoAwaitable* model uses `std::stop_token` directly with bounded, forward-only propagation, avoiding this cost.
candidate 4 (found by 3 of 57 passes): The `allocator_arg_t` alternative (Section 8.1) would require every handler to carry the allocator and forward it at every `co_await`.

## vehicle - grade 2.00 (fired in 7 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/1/1  -> 1.33
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       1/1/0  -> 0.67
  [11] 8. Frame Allocator Propagation               2/2/2  -> 2.00
  [12] 9. Ergonomics                                1/1/1  -> 1.00
  [13] 10. Complement: std::execution               1/1/1  -> 1.00
  [14] 11. Evidence and Accountability (P4133R0[... 1/1/1  -> 1.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.
candidate 2 (found by 3 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.
candidate 3 (found by 3 of 57 passes): Type erasure through `executor_ref` (Section 6.2) keeps `task<T>` at one template parameter. This enables separate compilation and ABI stability.
candidate 4 (found by 2 of 57 passes): The `operator new` timing constraint makes single-call impossible without language changes.

## coordination - grade 2.00 (fired in 5 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               2/0/0  -> 0.67
  [12] 9. Ergonomics                                1/0/2  -> 1.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 1/2/1  -> 1.33
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Each networking library builds on a different async model, so they cannot compose.
candidate 2 (found by 2 of 57 passes): The two-argument `await_suspend` is the protocol boundary. The caller's `await_transform` injects the environment as a pointer parameter.
candidate 3 (found by 2 of 57 passes): Type erasure through `executor_ref` (Section 6.2) keeps `task<T>` at one template parameter. This enables separate compilation and ABI stability.
candidate 4 (found by 2 of 57 passes): At least one demonstrated case of two independent libraries composing through the protocol without glue code.

## insufficiency - grade 1.50 (fired in 5 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           1/1/1  -> 1.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            1/2/0  -> 1.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/1  -> 0.33
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 1/1/0  -> 0.67
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Each networking library builds on a different async model, so they cannot compose.
candidate 2 (found by 3 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.
candidate 3 (found by 2 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.
candidate 4 (found by 2 of 57 passes): The absence of a standard frame allocator propagation mechanism forces either `allocator_arg_t` signature pollution or reliance on `shared_ptr` for lifetime management.

## implementation - grade 2.00  [binary: max] (fired in 5 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/0/0  -> 0.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            1/2/1  -> 1.33
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/1  -> 0.33
  [15] Appendix A: Understanding Asynchronous I/O   2/2/2  -> 2.00
  [16] Appendix B: anyreadstream                    2/2/2  -> 2.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The service model, the shutdown ordering, and the `use_service`/`make_service` API have remained unchanged through over a decade of production use in Boost.Asio.
candidate 2 (found by 3 of 57 passes): If you are eager to experiment, [Corosio](https://github.com/cppalliance/corosio)[4] implements these concepts in production-ready code.
candidate 3 (found by 3 of 57 passes): The implementation is from the [Capy](https://github.com/cppalliance/capy)[3] library.
candidate 4 (found by 2 of 57 passes): The mimalloc result is the critical comparison: a state-of-the-art general-purpose allocator with per-thread caches, yet the recycling frame allocator is 1.28x faster.

-->
