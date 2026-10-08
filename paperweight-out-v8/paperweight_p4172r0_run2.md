Verdict: Excellent (13/14)

The paper offers substantial support for its standardization case, with the strongest material concentrated in its account of prior art, the limits of library-only solutions, implementation experience, and the interoperability argument. The support is thinnest around the claim that the affected population is essentially universal, which is asserted in broad terms but not backed with evidence about who actually encounters the problem or how widely the proposed facilities would be adopted.

- The paper most convincingly establishes why a library will not do by pointing to a decade of template explosion, binary bloat, and ABI instability in Boost.Asio and Boost.Beast.
- The implementation experience section is well supported, citing unchanged production APIs, a concrete library implementation, and benchmark results favoring the recycling frame allocator.
- The coordination and interoperability case is clear in showing that without a shared protocol each networking library remains an island and that the two-argument `await_suspend` forms a real protocol boundary.
- The most glaring omission is the unsupported assertion that these facilities affect every audience and the largest population, which the paper claims rather than demonstrates.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.83/14)

Provisionally addressed: 7 of 7. Provisional points: 12.83 of 14. Unsupported quotes rejected: 29. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.83   corroborated 12.00   accumulate 13.67   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.50  implementation 2.00
sample agreement: 119 of 133 section-criterion pairs unanimous (89%)
single-sample totals would have been: 13.00 / 13.00 / 13.00   (all 3 samples: 12.83)
headings: h2 18
on threshold: audience, insufficiency
splits: motivation[11] 2/2/0  audience[6] 0/0/1  audience[9] 2/1/2  audience[14] 0/1/0
        prior_art[5] 2/0/2  prior_art[8] 0/2/0  prior_art[17] 1/0/1  vehicle[10] 2/1/1
        coordination[6] 1/0/0  coordination[13] 0/1/0  coordination[14] 2/1/1
        insufficiency[8] 1/2/0  implementation[8] 2/1/1  implementation[14] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 1/1/1  -> 1.00
  [7] 4. Protocol Basics                           2/2/2  -> 2.00
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       1/1/1  -> 1.00
  [11] 8. Frame Allocator Propagation               2/2/0  -> 1.33
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (P4133R0[... 2/2/2  -> 2.00
  [15] Appendix A: Understanding Asynchronous I/O   2/2/2  -> 2.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Without that waist, every stack reinvents incompatible task types and environments; an HTTP layer on one model does not compose with storage or RPC on another.
candidate 2 (found by 3 of 57 passes): The *IoAwaitable* approach - one template parameter, environment propagated through `io_env` - avoids this structural barrier.
candidate 3 (found by 3 of 57 passes): The motivating use case is a single line of code: `auto [ec, n] = co_await socket.read_some(buf);`
candidate 4 (found by 3 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.

## audience - grade 1.33 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/0/0  -> 0.00
  [6] 3. Audiences                                 0/0/1  -> 0.33
  [7] 4. Protocol Basics                           1/1/1  -> 1.00
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                2/1/2  -> 1.67
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/1/0  -> 0.33
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): These facilities are encountered by every audience.
candidate 2 (found by 3 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.
candidate 3 (found by 1 of 57 passes): The largest population.
candidate 4 (found by 1 of 57 passes): The patterns it captures are not. Type-erased executors, stop-token cancellation, and per-chain frame allocation have been refined across years of networking library development.

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Why Standardize                           2/0/2  -> 1.33
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           1/1/1  -> 1.00
  [8] 5. I/O Operations                            0/2/0  -> 0.67
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       2/2/2  -> 2.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   1/1/1  -> 1.00
  [16] Appendix B: anyreadstream                    1/1/1  -> 1.00
  [17] Appendix C: ioawaitablepromisebase           1/0/1  -> 0.67
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 2 (found by 3 of 57 passes): Additional context (buffer pools, logging handles, tenant IDs) can travel through the execution context's service model (Section 5.5) or through application-specific channels.
candidate 3 (found by 3 of 57 passes): Two-phase invocation was considered against single-call alternatives. The `operator new` timing constraint makes single-call impossible without language changes.
candidate 4 (found by 3 of 57 passes): The `allocator_arg_t` alternative (Section 8.1) would require every handler to carry the allocator and forward it at every `co_await`.

## vehicle - grade 2.00 (fired in 7 of 19 sections, strong in 4)  (SHARED PASSAGE)
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
  [11] 8. Frame Allocator Propagation               2/2/2  -> 2.00
  [12] 9. Ergonomics                                1/1/1  -> 1.00
  [13] 10. Complement: std::execution               1/1/1  -> 1.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.
candidate 2 (found by 3 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.
candidate 3 (found by 3 of 57 passes): The protocol chooses the other side of the fork: type-erase the executor through `executor_ref`, keep `task<T>` at one template parameter, and accept one vtable indirection per `dispatch`/`post` call.
candidate 4 (found by 3 of 57 passes): The `operator new` timing constraint makes single-call impossible without language changes.

## coordination - grade 2.00 (fired in 6 of 19 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 1/0/0  -> 0.33
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                1/1/1  -> 1.00
  [13] 10. Complement: std::execution               0/1/0  -> 0.33
  [14] 11. Evidence and Accountability (P4133R0[... 2/1/1  -> 1.33
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Each networking library builds on a different async model, so they cannot compose.
candidate 2 (found by 3 of 57 passes): Type erasure through `executor_ref` (Section 6.2) keeps `task<T>` at one template parameter. This enables separate compilation and ABI stability.
candidate 3 (found by 2 of 57 passes): The two-argument `await_suspend` is the protocol boundary. The caller's `await_transform` injects the environment as a pointer parameter.
candidate 4 (found by 2 of 57 passes): Without a shared protocol, each library is an island.

## insufficiency - grade 1.50 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 1/1/1  -> 1.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.
candidate 2 (found by 3 of 57 passes): The absence of a standard frame allocator propagation mechanism forces either `allocator_arg_t` signature pollution or reliance on `shared_ptr` for lifetime management.
candidate 3 (found by 2 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.
candidate 4 (found by 2 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.

## implementation - grade 2.00  [binary: max] (fired in 5 of 19 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/0/0  -> 0.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/1/1  -> 1.33
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 1/2/2  -> 1.67
  [15] Appendix A: Understanding Asynchronous I/O   2/2/2  -> 2.00
  [16] Appendix B: anyreadstream                    2/2/2  -> 2.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The service model, the shutdown ordering, and the `use_service`/`make_service` API have remained unchanged through over a decade of production use in Boost.Asio.
candidate 2 (found by 3 of 57 passes): The implementation is from the [Capy](https://github.com/cppalliance/capy)[3] library.
candidate 3 (found by 2 of 57 passes): The mimalloc result is the critical comparison: a state-of-the-art general-purpose allocator with per-thread caches, yet the recycling frame allocator is 1.28x faster.
candidate 4 (found by 2 of 57 passes): Corosio[4] | Linux (epoll, io_uring), Windows (IOCP), macOS (kqueue)

-->
