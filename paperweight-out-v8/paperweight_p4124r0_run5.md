Verdict: Adequate (6/14)

The paper makes a credible case that the problem it addresses is real and that existing approaches to routing I/O results through sender combinators are inadequate, but it leaves several essential parts of the standardization argument asserted rather than demonstrated. The strongest material concerns the conceptual need for an I/O-aware `when_all` and the failure of generic alternatives; the thinnest concerns evidence that this belongs in the standard rather than a library, and there is no meaningful discussion of coordination or interoperability.

- The paper establishes why the problem matters by showing that I/O errors arrive on the value channel, that generic adapters invert the “write it once” benefit, and that `when_all` is the one sender algorithm genuinely irreplaceable inside a coroutine body.
- The prior-art section is well supported, examining three strategies for routing I/O compound results and showing that all fail to achieve correct error-driven cancellation, while also positioning coroutine-native I/O as complementary to `std::execution`.
- The argument for standardization over a library is only claimed, resting on assertions about type-system selection and HALO limitations without enough supporting evidence.
- The most glaring omission is coordination and interoperability, where the paper offers nothing to show how the proposal fits with existing or planned I/O and execution facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.33   accumulate 6.50   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.50  implementation 1.00
sample agreement: 82 of 91 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.50)
headings: h2 12
on threshold: none
splits: motivation[10] 0/2/0  audience[8] 1/1/2  prior_art[9] 2/0/2  vehicle[11] 1/0/1
        insufficiency[8] 1/0/1  insufficiency[11] 1/0/0  implementation[5] 0/2/0
        implementation[9] 0/1/0  implementation[11] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               2/2/2  -> 2.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   2/2/2  -> 2.00
  [9] 6. Domain-Aware Combinators                  1/1/1  -> 1.00
  [10] 7. Comparison                                0/2/0  -> 0.67
  [11] 8. Conclusion                                2/2/2  -> 2.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): I/O errors arrive on the value channel. The combinator does not see them.
candidate 2 (found by 3 of 39 passes): The "write it once" benefit has inverted: one generic `when_all` plus N adapters is more total code than two `when_all` implementations (one generic, one I/O-aware) plus zero adapters.
candidate 3 (found by 3 of 39 passes): Dietmar Kühl identified the irreplaceable sender algorithms inside a coroutine body as `when_all`, the scheduling algorithms, `bulk`, and the scoping algorithms [7].
candidate 4 (found by 3 of 39 passes): The one sender algorithm that is genuinely irreplaceable inside a coroutine body is `when_all` - a coroutine body is sequential, and expressing concurrency requires a combinator.

## audience - grade 0.67 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   1/1/2  -> 1.33
  [9] 6. Domain-Aware Combinators                  0/0/0  -> 0.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Chuanqi Xu (Alibaba) reported on the LEWG reflector (March 2026) that replacing `future.then().then()` chains with coroutines reduced binary size because every `then` clause creates a new symbol [6].

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. What whenall Should Do for I/O            2/2/2  -> 2.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   2/2/2  -> 2.00
  [9] 6. Domain-Aware Combinators                  2/0/2  -> 1.33
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                2/2/2  -> 2.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): examines three strategies for routing I/O compound results through the three-channel model, shows that all three fail to achieve correct error-driven cancellation, and proposes domain-aware combinators
candidate 2 (found by 3 of 39 passes): Coroutine-native I/O and `std::execution` are complementary.
candidate 3 (found by 3 of 39 passes): Peter Dimov's design [5]: the return type lifts the `error_code` out of each child's result into a single outer `io_result`.
candidate 4 (found by 3 of 39 passes): Chuanqi Xu (Alibaba) reported on the LEWG reflector (March 2026) that replacing `future.then().then()` chains with coroutines reduced binary size because every `then` clause creates a new symbol [6].

## vehicle - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
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
  [11] 8. Conclusion                                1/0/1  -> 0.67
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): Two implementations behind one name, selected by the type system, is a stronger design than one implementation that requires per-call-site adaptation to work correctly for I/O.
candidate 2 (found by 1 of 39 passes): The one sender algorithm that is genuinely irreplaceable inside a coroutine body is `when_all` - a coroutine body is sequential, and expressing concurrency requires a combinator.

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

## insufficiency - grade 0.50 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/0/0  -> 0.00
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   1/0/1  -> 0.67
  [9] 6. Domain-Aware Combinators                  0/0/0  -> 0.00
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                1/0/0  -> 0.33
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Heap Allocation eLision Optimization (HALO) cannot elide the frame because `when_all` manages child lifetimes across concurrent operations.
candidate 2 (found by 1 of 39 passes): The one sender algorithm that is genuinely irreplaceable inside a coroutine body is `when_all` - a coroutine body is sequential, and expressing concurrency requires a combinator.

## implementation - grade 1.00  [binary: max] (fired in 4 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What whenall Should Do for I/O            0/2/0  -> 0.67
  [6] 3. The Problem                               0/0/0  -> 0.00
  [7] 4. The Adapter                               0/0/0  -> 0.00
  [8] 5. The Cost of the Adapter                   1/1/1  -> 1.00
  [9] 6. Domain-Aware Combinators                  0/1/0  -> 0.33
  [10] 7. Comparison                                0/0/0  -> 0.00
  [11] 8. Conclusion                                1/1/0  -> 0.67
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Chuanqi Xu (Alibaba) reported on the LEWG reflector (March 2026) that replacing `future.then().then()` chains with coroutines reduced binary size because every `then` clause creates a new symbol [6].
candidate 2 (found by 2 of 39 passes): Two implementations behind one name, selected by the type system, is a stronger design than one implementation that requires per-call-site adaptation to work correctly for I/O.
candidate 3 (found by 1 of 39 passes): implemented in [Capy](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/io_result.hpp) [3].
candidate 4 (found by 1 of 39 passes): Dietmar Kühl identified the irreplaceable sender algorithms inside a coroutine body as `when_all`, the scheduling algorithms, `bulk`, and the scoping algorithms [7].

-->
