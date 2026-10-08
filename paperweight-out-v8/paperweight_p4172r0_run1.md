Verdict: Excellent (12/14)

The paper offers substantial support for the need to standardize its core vocabulary, particularly through concrete implementation experience and a clear account of why existing alternatives fail to compose. The case is thinnest where it relies on broad claims about affected populations and the impossibility of a library-only solution, since those points are asserted rather than demonstrated with the same specificity as the technical arguments.

- The strongest support comes from the documented production history of the service model and the availability of working implementations in Corosio and Capy.
- The paper convincingly establishes why standardization is necessary by showing that the two-argument `await_suspend` protocol creates a visible, portable boundary that non-compliant awaitables cannot cross.
- The discussion of prior art and alternatives is well grounded, especially in explaining why single-call invocation is impossible without language changes and why `allocator_arg_t` would impose unacceptable signature pollution.
- The most glaring omission is the lack of established evidence for who is affected and why a library cannot suffice, since the paper leans on general ecosystem observations rather than demonstrating that a non-standard shared vocabulary has actually failed in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 36. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 12.00   accumulate 12.67   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.00  implementation 2.00
sample agreement: 118 of 133 section-criterion pairs unanimous (89%)
single-sample totals would have been: 12.50 / 12.00 / 12.00   (all 3 samples: 12.17)
headings: h2 18
on threshold: audience
splits: motivation[6] 2/1/1  motivation[8] 0/2/2  motivation[11] 0/2/2  audience[12] 1/0/0
        prior_art[5] 0/2/0  prior_art[17] 1/0/0  vehicle[9] 2/2/0  vehicle[10] 0/1/0
        vehicle[13] 1/1/2  coordination[11] 0/0/1  coordination[12] 2/1/1
        coordination[13] 1/0/0  coordination[14] 2/1/0  implementation[8] 1/2/2
        implementation[14] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 2/1/1  -> 1.33
  [7] 4. Protocol Basics                           2/2/2  -> 2.00
  [8] 5. I/O Operations                            0/2/2  -> 1.33
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       1/1/1  -> 1.00
  [11] 8. Frame Allocator Propagation               0/2/2  -> 1.33
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
candidate 3 (found by 3 of 57 passes): The `allocator_arg_t` alternative (Section 8.1) would require every handler to carry the allocator and forward it at every `co_await`.
candidate 4 (found by 3 of 57 passes): Byte-oriented I/O - sockets, DNS, TLS, HTTP - is sequential by nature for many handlers.

## audience - grade 1.17 (fired in 2 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/0/0  -> 0.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                1/0/0  -> 0.33
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.
candidate 2 (found by 1 of 57 passes): Application developers - the largest population - do not have to be concurrency experts.

## prior_art - grade 2.00 (fired in 9 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. Why Standardize                           0/2/0  -> 0.67
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       2/2/2  -> 2.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                2/2/2  -> 2.00
  [13] 10. Complement: std::execution               2/2/2  -> 2.00
  [14] 11. Evidence and Accountability (P4133R0[... 0/0/0  -> 0.00
  [15] Appendix A: Understanding Asynchronous I/O   1/1/1  -> 1.00
  [16] Appendix B: anyreadstream                    1/1/1  -> 1.00
  [17] Appendix C: ioawaitablepromisebase           1/0/0  -> 0.33
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This paper is the companion record: why each facility exists, what alternatives were considered, how each choice was forced by the constraints of the domain, and where the historical evidence lives.
candidate 2 (found by 3 of 57 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 57 passes): Two-phase invocation was considered against single-call alternatives. The `operator new` timing constraint makes single-call impossible without language changes.
candidate 4 (found by 3 of 57 passes): The `allocator_arg_t` alternative (Section 8.1) would require every handler to carry the allocator and forward it at every `co_await`.

## vehicle - grade 2.00 (fired in 8 of 19 sections, strong in 3)  (SHARED PASSAGE)
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
  [9] 6. Task Types                                2/2/0  -> 1.33
  [10] 7. Application Surface                       0/1/0  -> 0.33
  [11] 8. Frame Allocator Propagation               2/2/2  -> 2.00
  [12] 9. Ergonomics                                1/1/1  -> 1.00
  [13] 10. Complement: std::execution               1/1/2  -> 1.33
  [14] 11. Evidence and Accountability (P4133R0[... 1/1/1  -> 1.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.
candidate 2 (found by 3 of 57 passes): The two-argument signature with `io_env const*` ensures that a coroutine from a different model (one whose `await_transform` does not inject `io_env`) fails to compile.
candidate 3 (found by 3 of 57 passes): The parameter list is the explicit, visible, portable path.
candidate 4 (found by 3 of 57 passes): The absence of a standard frame allocator propagation mechanism forces either `allocator_arg_t` signature pollution or reliance on `shared_ptr` for lifetime management.

## coordination - grade 2.00 (fired in 7 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           2/2/2  -> 2.00
  [6] 3. Audiences                                 1/1/1  -> 1.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            2/2/2  -> 2.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/1  -> 0.33
  [12] 9. Ergonomics                                2/1/1  -> 1.33
  [13] 10. Complement: std::execution               1/0/0  -> 0.33
  [14] 11. Evidence and Accountability (P4133R0[... 2/1/0  -> 1.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The *IoAwaitable* approach - one template parameter, environment propagated through `io_env` - avoids this structural barrier.
candidate 2 (found by 3 of 57 passes): Type erasure through `executor_ref` (Section 6.2) keeps `task<T>` at one template parameter. This enables separate compilation and ABI stability.
candidate 3 (found by 2 of 57 passes): Each networking library builds on a different async model, so they cannot compose.
candidate 4 (found by 2 of 57 passes): The two-argument `await_suspend` is the protocol boundary. The caller's `await_transform` injects the environment as a pointer parameter. A non-compliant awaitable produces a compile-time failure when a compliant coroutine's `await_transform` calls the two-argument form.

## insufficiency - grade 1.00 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           1/1/1  -> 1.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            0/0/0  -> 0.00
  [9] 6. Task Types                                0/0/0  -> 0.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                1/1/1  -> 1.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 1/1/1  -> 1.00
  [15] Appendix A: Understanding Asynchronous I/O   0/0/0  -> 0.00
  [16] Appendix B: anyreadstream                    0/0/0  -> 0.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Twenty years of observed ecosystem behavior is sufficient to record that a shared vocabulary requires standardization.
candidate 2 (found by 3 of 57 passes): Type erasure through `executor_ref` (Section 6.2) keeps `task<T>` at one template parameter.
candidate 3 (found by 3 of 57 passes): The absence of a standard frame allocator propagation mechanism forces either `allocator_arg_t` signature pollution or reliance on `shared_ptr` for lifetime management.

## implementation - grade 2.00  [binary: max] (fired in 5 of 19 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Why Standardize                           0/0/0  -> 0.00
  [6] 3. Audiences                                 0/0/0  -> 0.00
  [7] 4. Protocol Basics                           0/0/0  -> 0.00
  [8] 5. I/O Operations                            1/2/2  -> 1.67
  [9] 6. Task Types                                2/2/2  -> 2.00
  [10] 7. Application Surface                       0/0/0  -> 0.00
  [11] 8. Frame Allocator Propagation               0/0/0  -> 0.00
  [12] 9. Ergonomics                                0/0/0  -> 0.00
  [13] 10. Complement: std::execution               0/0/0  -> 0.00
  [14] 11. Evidence and Accountability (P4133R0[... 2/0/0  -> 0.67
  [15] Appendix A: Understanding Asynchronous I/O   2/2/2  -> 2.00
  [16] Appendix B: anyreadstream                    2/2/2  -> 2.00
  [17] Appendix C: ioawaitablepromisebase           0/0/0  -> 0.00
  [18] Acknowledgements                             0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The service model, the shutdown ordering, and the `use_service`/`make_service` API have remained unchanged through over a decade of production use in Boost.Asio.
candidate 2 (found by 3 of 57 passes): [Corosio](https://github.com/cppalliance/corosio)[4] implements these concepts in production-ready code.
candidate 3 (found by 3 of 57 passes): The implementation is from the [Capy](https://github.com/cppalliance/capy)[3] library.
candidate 4 (found by 2 of 57 passes): Boost.Asio and Boost.Beast made streams templates; the result was template explosion, binary bloat, and ABI instability across a decade of production use.

-->
