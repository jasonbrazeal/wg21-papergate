Verdict: Adequate to Strong (7/14)

The paper offers solid support in the areas that matter most for a library-level design discussion: it clearly motivates the problem, engages seriously with prior art, and demonstrates real implementation experience. The case is much thinner, however, when it comes to explaining why this needs to be in the standard rather than shipped as a library, and it does not establish coordination with existing facilities or a standardization rationale.

- The strongest support is the concrete motivation and prior-art analysis, including a credible account of why `when_all` is the one combinator that cannot be replaced inside a coroutine body.
- Implementation experience is also well established, with an existing `io_result` type and a reported production use case.
- The weakest part is the absence of any established argument for why the standard should contain this, rather than a library.
- Coordination and interoperability with the broader sender/receiver and coroutine ecosystem are not established at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 7.33   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.00 / 7.50 / 7.50   (all 3 samples: 7.33)
headings: h2 12
on threshold: implementation
splits: motivation[4] 0/0/1  audience[8] 0/2/1  audience[9] 1/0/0  prior_art[2] 1/1/2
        prior_art[4] 1/1/2  insufficiency[11] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   2/2/2  -> 2.00
  [9] 6. Domain-Aware Combinators                  1/1/1  -> 1.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                2/2/2  -> 2.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): I/O errors arrive on the value channel. The combinator does not see them.
candidate 2 (found by 3 of 39 passes): The "write it once" benefit has inverted: one generic `when_all` plus N adapters is more total code than two `when_all` implementations (one generic, one I/O-aware) plus zero adapters.
candidate 3 (found by 3 of 39 passes): Dietmar Kühl identified the irreplaceable sender algorithms inside a coroutine body as `when_all`, the scheduling algorithms, `bulk`, and the scoping algorithms [7].
candidate 4 (found by 3 of 39 passes): The one sender algorithm that is genuinely irreplaceable inside a coroutine body is `when_all` - a coroutine body is sequential, and expressing concurrency requires a combinator.

## audience - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   0/2/1  -> 1.00
  [9] 6. Domain-Aware Combinators                  1/0/0  -> 0.33
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Chuanqi Xu (Alibaba) reported on the LEWG reflector (March 2026) that replacing `future.then().then()` chains with coroutines reduced binary size because every `then` clause creates a new symbol [6].
candidate 2 (found by 1 of 39 passes): Chuanqi Xu (Alibaba) independently confirmed that the concurrency combinators genuinely useful in production are all variants of `when_all` [6].

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/2  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/2  -> 1.33
  [5] 2. What whenall Should Do for I/O            2/2/2  -> 2.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   2/2/2  -> 2.00
  [9] 6. Domain-Aware Combinators                  2/2/2  -> 2.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                2/2/2  -> 2.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Peter Dimov's design [5]: the return type lifts the `error_code` out of each child's result into a single outer `io_result`.
candidate 2 (found by 3 of 39 passes): Chuanqi Xu (Alibaba) reported on the LEWG reflector (March 2026) that replacing `future.then().then()` chains with coroutines reduced binary size because every `then` clause creates a new symbol [6].
candidate 3 (found by 3 of 39 passes): A single `when_all` dispatches at compile time: the IoAwaitable overload inspects the result directly with zero adapter overhead, and the sender overload delegates to `std::execution::when_all` with no change to the existing behavior.
candidate 4 (found by 2 of 39 passes): examines three strategies for routing I/O compound results through the three-channel model, shows that all three fail to achieve correct error-driven cancellation, and proposes domain-aware combinators

## vehicle - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   0/0/0  -> 0.00
  [9] 6. Domain-Aware Combinators                  0/0/0  -> 0.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   0/0/0  -> 0.00
  [9] 6. Domain-Aware Combinators                  0/0/0  -> 0.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   1/1/1  -> 1.00
  [9] 6. Domain-Aware Combinators                  0/0/0  -> 0.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                0/0/1  -> 0.33
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Heap Allocation eLision Optimization (HALO) cannot elide the frame because `when_all` manages child lifetimes across concurrent operations.
candidate 2 (found by 1 of 39 passes): The compiler cannot prove the child coroutine's lifetime is bounded by the caller's scope.
candidate 3 (found by 1 of 39 passes): The one sender algorithm that is genuinely irreplaceable inside a coroutine body is `when_all` - a coroutine body is sequential, and expressing concurrency requires a combinator.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            2/2/2  -> 2.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   1/1/1  -> 1.00
  [9] 6. Domain-Aware Combinators                  0/0/0  -> 0.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): `io_result` is defined in [P4166R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4166r0.pdf) [9] and implemented in [Capy](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/io_result.hpp) [3].
candidate 2 (found by 3 of 39 passes): Chuanqi Xu (Alibaba) reported on the LEWG reflector (March 2026) that replacing `future.then().then()` chains with coroutines reduced binary size because every `then` clause creates a new symbol [6].

-->
