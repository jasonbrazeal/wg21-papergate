Verdict: Excellent (13/14)

The paper offers substantial support for its own standardization, with particularly strong evidence in implementation experience, prior art, and the case for why a library alone cannot solve the problem. The thinnest area is the claim about who is affected: the paper asserts broad impact but does not demonstrate it with the same concreteness it brings elsewhere.

- The strongest support comes from implementation experience, where over a decade of Boost.Asio stability and independent adoption in stdexec give the design real-world weight.
- The paper also establishes clearly why a library will not do, showing that incompatible async models cannot compose without a shared waist.
- The most glaring omission is the affected-audience claim, which relies on assertions like “the largest population” without evidence tying those groups to the specific facilities proposed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.67/14)

Provisionally addressed: 7 of 7. Provisional points: 12.67 of 14. Unsupported quotes rejected: 24. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.67   corroborated 12.00   accumulate 13.50   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.50  implementation 2.00
sample agreement: 112 of 133 section-criterion pairs unanimous (84%)
single-sample totals would have been: 13.00 / 13.00 / 12.50   (all 3 samples: 12.67)
headings: h2 18
on threshold: audience, insufficiency
splits: motivation[7] 2/0/2  motivation[14] 2/2/1  motivation[15] 0/2/0  audience[6] 0/1/0
        audience[7] 0/1/0  audience[12] 0/1/0  prior_art[5] 0/2/2  prior_art[6] 0/0/2
        prior_art[7] 1/1/0  prior_art[17] 1/0/0  vehicle[10] 2/1/1  vehicle[11] 2/1/2
        vehicle[12] 1/0/1  vehicle[14] 0/0/1  coordination[9] 0/2/0  coordination[13] 1/0/0
        insufficiency[8] 2/0/2  insufficiency[9] 2/2/1  insufficiency[10] 0/1/0
        insufficiency[14] 1/1/0  implementation[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 1/1/1  -> 1.00
  [7] 4. Protocol Basics                           2/0/2  -> 1.33
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       1/1/1  -> 1.00
  [11] 8. Frame Allocator Propagation               2/2/2  -> 2.00
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (D4133R0 ... 2/2/1  -> 1.67
  [15] Appendix A: Understanding Asynchronous I/O   0/2/0  -> 0.67
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Without that waist, every stack reinvents incompatible task types and environments; an HTTP layer on one model does not compose with storage or RPC on another.
candidate 2 (found by 3 of 57 passes): This compiles silently when promise and awaitable are mismatched - a coroutine from one async model can `co_await` an awaitable from another, producing runtime errors instead of compile-time failures.
candidate 3 (found by 3 of 57 passes): The `allocator_arg_t` alternative (Section 8.1) would require every handler to carry the allocator and forward it at every `co_await`.
candidate 4 (found by 3 of 57 passes): The absence of a standard frame allocator propagation mechanism forces either `allocator_arg_t` signature pollution or reliance on `shared_ptr` for lifetime management.

## audience - grade 1.17 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/0/0  -> 0.00
  [6] 3. Audiences                                 0/1/0  -> 0.33
  [7] 4. Protocol Basics                           0/1/0  -> 0.33
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/1/0  -> 0.33
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (D4133R0 ... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The mimalloc result is the critical comparison: a state-of-the-art general-purpose allocator with per-thread caches, yet the recycling frame allocator is 1.28x faster.
candidate 2 (found by 1 of 57 passes): The largest population.
candidate 3 (found by 1 of 57 passes): These facilities are encountered by every audience.
candidate 4 (found by 1 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.

## prior_art - grade 2.00 (fired in 12 of 19 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Why Standardize                           0/2/2  -> 1.33
  [6] 3. Audiences                                 0/0/2  -> 0.67
  [7] 4. Protocol Basics                           1/1/0  -> 0.67
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       2/2/2  -> 2.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (D4133R0 ... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   1/1/1  -> 1.00
  [16] Appendix B: anyreadstream                    1/1/1  -> 1.00
  [17] Appendix C: ioawaitablepromisebase           1/0/0  -> 0.33
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This paper is the companion record: why each facility exists, what alternatives were considered, how each choice was forced by the constraints of the domain, and where the historical evidence lives.
candidate 2 (found by 3 of 57 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 57 passes): The *IoAwaitable* model uses `std::stop_token` directly with bounded, forward-only propagation, avoiding this cost.
candidate 4 (found by 3 of 57 passes): Two-phase invocation was considered against single-call alternatives. The `operator new` timing constraint makes single-call impossible without language changes.

## vehicle - grade 2.00 (fired in 8 of 19 sections, strong in 4)  (SHARED PASSAGE)
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
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       2/1/1  -> 1.33
  [11] 8. Frame Allocator Propagation               2/1/2  -> 1.67
  [12] 9. Ergonomics                                1/0/1  -> 0.67
  [13] 10. Complement: std::execution               1/1/1  -> 1.00
  [14] 11. Evidence and Accountability (D4133R0 ... 0/0/1  -> 0.33
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.
candidate 2 (found by 3 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.
candidate 3 (found by 3 of 57 passes): The `operator new` timing constraint makes single-call impossible without language changes.
candidate 4 (found by 3 of 57 passes): The parameter list is the explicit, visible, portable path.

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
  [9] 6. Task Types                                0/2/0  -> 0.67
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                1/1/1  -> 1.00
  [13] 10. Complement: std::execution               1/0/0  -> 0.33
  [14] 11. Evidence and Accountability (D4133R0 ... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Without that waist, every stack reinvents incompatible task types and environments; an HTTP layer on one model does not compose with storage or RPC on another.
candidate 2 (found by 3 of 57 passes): Type erasure through `executor_ref` (Section 6.2) keeps `task<T>` at one template parameter. This enables separate compilation and ABI stability.
candidate 3 (found by 2 of 57 passes): The two-argument `await_suspend` is the protocol boundary. The caller's `await_transform` injects the environment as a pointer parameter.
candidate 4 (found by 1 of 57 passes): The two-argument `await_suspend` is the protocol boundary. The caller's `await_transform` injects the environment as a pointer parameter. A non-compliant awaitable produces a compile-time failure when a compliant coroutine's `await_transform` calls the two-argument form.

## insufficiency - grade 1.50 (fired in 5 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           1/1/1  -> 1.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/0/2  -> 1.33
  [9] 6. Task Types                                2/2/1  -> 1.67
  [10] 7. Application Surface                       0/1/0  -> 0.33
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (D4133R0 ... 1/1/0  -> 0.67
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Each networking library builds on a different async model, so they cannot compose.
candidate 2 (found by 2 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.
candidate 3 (found by 2 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.
candidate 4 (found by 2 of 57 passes): The absence of a standard frame allocator propagation mechanism forces either `allocator_arg_t` signature pollution or reliance on `shared_ptr` for lifetime management.

## implementation - grade 2.00  [binary: max] (fired in 6 of 19 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           1/0/0  -> 0.33
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (D4133R0 ... 2/2/2  -> 2.00
  [15] Appendix A: Understanding Asynchronous I/O   2/2/2  -> 2.00
  [16] Appendix B: anyreadstream                    2/2/2  -> 2.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The service model, the shutdown ordering, and the `use_service`/`make_service` API have remained unchanged through over a decade of production use in Boost.Asio.
candidate 2 (found by 3 of 57 passes): Independently, Ian Petersen has adopted the frame allocator pattern within stdexec itself: `exec::function<...>` ([NVIDIA/stdexec#2040](https://github.com/NVIDIA/stdexec/pull/2040) [43], [exec/function.hpp](https://github.com/NVIDIA/stdexec/blob/main/include/exec/function.hpp) [44]) introduces a `get_frame_allocator` environment query to achieve the same amortized-zero-allocation behaviour for type-erased senders, explicitly crediting the Capy recycling allocator as the inspiration.
candidate 3 (found by 3 of 57 passes): The implementation is from the [Capy](https://github.com/cppalliance/capy) [3] library.
candidate 4 (found by 2 of 57 passes): The mimalloc result is the critical comparison: a state-of-the-art general-purpose allocator with per-thread caches, yet the recycling frame allocator is 1.28x faster.

-->
