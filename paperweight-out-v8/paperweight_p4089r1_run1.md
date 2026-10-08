Verdict: Excellent (14/14)

The paper offers substantial support for its own standardization, with every major category of need marked as established and backed by concrete evidence from production libraries, reference implementations, and ecosystem surveys. The support is thinnest only in that the argument leans heavily on structural and empirical claims rather than demonstrating a formal impossibility, but the convergence of independent reports and prior art makes the case coherent and well-grounded.

- The strongest support comes from the documented convergence of seven independent libraries on a one-parameter design, which directly evidences the ecosystem-wide risk the paper identifies.
- The paper also establishes why a library-level solution cannot suffice, since the open query protocol lacks any discovery or type-erasure mechanism comparable to what Asio provides for executors.
- The most notable limitation is that the paper does not demonstrate a formal or exhaustive proof that the two-parameter design must fail, relying instead on structural inference and reported symptoms.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (13.67/14)

Provisionally addressed: 7 of 7. Provisional points: 13.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 13.67   corroborated 14.00   accumulate 14.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.83  coordination 2.00  insufficiency 1.83  implementation 2.00
sample agreement: 97 of 112 section-criterion pairs unanimous (87%)
single-sample totals would have been: 13.00 / 14.00 / 14.00   (all 3 samples: 13.67)
headings: h2 15
on threshold: none
splits: motivation[14] 2/1/2  audience[2] 0/0/1  audience[10] 2/2/0  audience[13] 2/1/1
        prior_art[4] 0/0/1  prior_art[5] 1/1/2  prior_art[8] 0/2/0  prior_art[12] 2/0/0
        prior_art[14] 0/1/1  vehicle[9] 1/1/0  vehicle[11] 1/2/2  coordination[13] 2/0/2
        insufficiency[8] 1/2/2  implementation[2] 1/0/0  implementation[9] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   1/1/1  -> 1.00
  [6] 3. The Claim                                 1/1/1  -> 1.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                1/1/1  -> 1.00
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               2/1/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 2 (found by 3 of 48 passes): When the Environment changes, the return type changes, and every caller breaks.
candidate 3 (found by 3 of 48 passes): The ecosystem independently arrived at the design that avoids the problem documented in Section 5.
candidate 4 (found by 3 of 48 passes): The `Environment` parameter in [P3552R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3552r3.html) [1] creates a structural risk to the task type diversity that C++20 coroutines were designed to enable.

## audience - grade 2.00 (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           0/0/0  -> 0.00
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             2/2/0  -> 1.33
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               2/1/1  -> 1.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 2 (found by 2 of 48 passes): Everybody (millions) | Uses coroutines and awaitables defined by the standard library, Boost, and other high-quality libraries
candidate 3 (found by 2 of 48 passes): Nine coroutine libraries are surveyed below.
candidate 4 (found by 2 of 48 passes): the empirical evidence in Section 8 - seven independent libraries converging on one-parameter designs - shows that the ecosystem treats the principle as operative.

## prior_art - grade 2.00 (fired in 11 of 16 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. P3552R3                                   1/1/2  -> 1.33
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              1/1/1  -> 1.00
  [8] 5. Two Libraries, Two Environments           0/2/0  -> 0.67
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                2/0/0  -> 0.67
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               0/1/1  -> 0.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The risk to the ecosystem is structural, documented by the specification itself, by NVIDIA's reference implementation, by the only production precedent (Boost.Asio), and by `task`'s own author.
candidate 2 (found by 3 of 48 passes): P2300R10 defines `queryable` as the base concept for all objects that respond to property queries - schedulers, senders, receivers, and environments all refine it.
candidate 3 (found by 3 of 48 passes): The `Environment` parameter inverts this layering: it puts environment customization in the coroutine type itself, forcing a new type for each domain.
candidate 4 (found by 2 of 48 passes): The findings documented in this paper and in [P3801R0] [2], "Concerns about the design of `std::execution::task`," are structural consequences of making `task` do more than one thing.

## vehicle - grade 1.83 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 1/1/1  -> 1.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           1/1/1  -> 1.00
  [9] 6. The Asio Precedent                        1/1/0  -> 0.67
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             1/2/2  -> 1.67
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The risk to the ecosystem is structural, documented by the specification itself, by NVIDIA's reference implementation, by the only production precedent (Boost.Asio), and by `task`'s own author.
candidate 2 (found by 3 of 48 passes): Good stewardship of the standard means shipping features narrow and widening with evidence.
candidate 3 (found by 2 of 48 passes): A standard task type provides a lingua franca. It eliminates pairwise bridges. It gives the ecosystem a common type that every library can accept and return.
candidate 4 (found by 2 of 48 passes): The mild case already exhibits the predicted symptoms at smaller scale.

## coordination - grade 2.00 (fired in 6 of 16 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 1/1/1  -> 1.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               2/0/2  -> 1.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): when two libraries define different environments, how does one task `co_await` the other?
candidate 2 (found by 3 of 48 passes): A standard task type provides a lingua franca. It eliminates pairwise bridges. It gives the ecosystem a common type that every library can accept and return.
candidate 3 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 4 (found by 2 of 48 passes): Nine coroutine libraries are surveyed below. Asio is the most widely deployed C++ async library; the standard proposal carries normative weight.

## insufficiency - grade 1.83 (fired in 3 of 16 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           1/2/2  -> 1.67
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             0/0/0  -> 0.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The query set is open by design, and the only adaptation mechanism - `write_env` - requires the caller to know every missing query by name.
candidate 2 (found by 3 of 48 passes): The type-erasure mechanism that Asio provides for executors has no analogue for an open query protocol.
candidate 3 (found by 2 of 48 passes): The caller must construct the domain-specific objects correctly, manage their lifetimes, and know the semantic requirements of each query. `write_env` does not help with any of this.
candidate 4 (found by 1 of 48 passes): The caller must know every custom query from every library, by name, and inject them all manually. There is no discovery mechanism - no way to ask an environment "what queries do you need?"

## implementation - grade 2.00  [binary: max] (fired in 5 of 16 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        1/2/2  -> 1.67
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/0  -> 0.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The only production two-parameter coroutine type is Asio's `awaitable<T, Executor>`.
candidate 2 (found by 3 of 48 passes): The [cross_await](https://github.com/klemens-morgenstern/cross_await) [30] repository (Klemens Morgenstern) contains four cross-library composition examples, 51-105 lines each.
candidate 3 (found by 3 of 48 passes): by the reference implementation (NVIDIA's custom queries, Section 5.3), by the only production precedent (Asio, Section 6)
candidate 4 (found by 2 of 48 passes): NVIDIA's reference implementation defines custom forwarding queries in [nvexec/stream/common.cuh](https://github.com/NVIDIA/stdexec/blob/main/include/nvexec/stream/common.cuh) [28]:

-->
