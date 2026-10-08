Verdict: Excellent (14/14)

The paper offers substantial support for its own standardization, with nearly every required element backed by concrete evidence, working examples, and independent corroboration. The support is thinnest where the argument leans on structural inference rather than direct demonstration, but even there the paper grounds its claims in reference implementations and production precedent.

- The strongest support comes from the implementation experience section, where the paper cites NVIDIA’s reference implementation, Asio’s production coroutine type, and a public repository of cross-library examples.
- The case for why a library will not do is well established through the open-ended query protocol and the absence of any discovery mechanism for required environment queries.
- The paper’s coordination and interoperability argument is reinforced by the C++20 awaitable protocol serving as the demonstrated interop surface across four working examples.
- The most notable omission is any direct evidence that the proposed alternative has been exercised at the scale or diversity of environments where the current design is claimed to fail.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (13.83/14)

Provisionally addressed: 7 of 7. Provisional points: 13.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 13.83   corroborated 14.00   accumulate 14.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.83  coordination 2.00  insufficiency 2.00  implementation 2.00
sample agreement: 100 of 112 section-criterion pairs unanimous (89%)
single-sample totals would have been: 14.00 / 14.00 / 14.00   (all 3 samples: 13.83)
headings: h2 15
on threshold: none
splits: motivation[13] 2/2/1  motivation[14] 1/2/2  audience[2] 1/0/0  audience[8] 1/0/0
        prior_art[2] 2/2/1  vehicle[9] 0/2/2  vehicle[10] 2/2/1  vehicle[11] 1/1/2
        vehicle[13] 1/0/2  insufficiency[11] 1/0/0  implementation[4] 0/2/0
        implementation[13] 0/0/1
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
  [13] 10. Frequently Raised Concerns               2/2/1  -> 1.67
  [14] 11. Conclusion                               1/2/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The Environment parameter in `std::execution::task` makes cross-library coroutine interoperability structurally impossible without knowing every query by name.
candidate 2 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 3 (found by 3 of 48 passes): When the Environment changes, the return type changes, and every caller breaks.
candidate 4 (found by 3 of 48 passes): The ecosystem independently arrived at the design that avoids the problem documented in Section 5.

## audience - grade 2.00 (fired in 6 of 16 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           1/0/0  -> 0.33
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 2 (found by 3 of 48 passes): Nine coroutine libraries are surveyed below. Asio is the most widely deployed C++ async library; the standard proposal carries normative weight.
candidate 3 (found by 3 of 48 passes): Four working examples, 51-105 lines each.
candidate 4 (found by 2 of 48 passes): Everybody (millions) | Uses coroutines and awaitables defined by the standard library, Boost, and other high-quality libraries

## prior_art - grade 2.00 (fired in 9 of 16 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/1  -> 1.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   1/1/1  -> 1.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              1/1/1  -> 1.00
  [8] 5. Two Libraries, Two Environments           0/0/0  -> 0.00
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                2/2/2  -> 2.00
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               1/1/1  -> 1.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The findings documented in this paper and in [P3801R0] [2], "Concerns about the design of `std::execution::task`," are structural consequences of making `task` do more than one thing.
candidate 2 (found by 3 of 48 passes): P2300R10 defines `queryable` as the base concept for all objects that respond to property queries - schedulers, senders, receivers, and environments all refine it.
candidate 3 (found by 3 of 48 passes): The `Environment` parameter inverts this layering: it puts environment customization in the coroutine type itself, forcing a new type for each domain.
candidate 4 (found by 3 of 48 passes): The `Environment` parameter in [P3552R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3552r3.html) [1] creates a structural risk to the task type diversity that C++20 coroutines were designed to enable.

## vehicle - grade 1.83 (fired in 8 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 1/1/1  -> 1.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        0/2/2  -> 1.33
  [10] 7. Design Intent                             2/2/1  -> 1.67
  [11] 8. The Ecosystem                             1/1/2  -> 1.33
  [12] 9. Concepts Mitigate the Risk                1/1/1  -> 1.00
  [13] 10. Frequently Raised Concerns               1/0/2  -> 1.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The risk to the ecosystem is structural, documented by the specification itself, by NVIDIA's reference implementation, by the only production precedent (Boost.Asio), and by `task`'s own author.
candidate 2 (found by 3 of 48 passes): A standard task type provides a lingua franca. It eliminates pairwise bridges. It gives the ecosystem a common type that every library can accept and return.
candidate 3 (found by 3 of 48 passes): Good stewardship of the standard means shipping features narrow and widening with evidence.
candidate 4 (found by 3 of 48 passes): Asio is the most widely deployed C++ async library; the standard proposal carries normative weight.

## coordination - grade 2.00 (fired in 6 of 16 sections, strong in 5)  (SHARED PASSAGE)
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
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): A standard task type provides a lingua franca. It eliminates pairwise bridges. It gives the ecosystem a common type that every library can accept and return.
candidate 2 (found by 3 of 48 passes): NVIDIA's reference implementation defines custom forwarding queries in [nvexec/stream/common.cuh](https://github.com/NVIDIA/stdexec/blob/main/include/nvexec/stream/common.cuh) [28]:
candidate 3 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 4 (found by 3 of 48 passes): The cross_await bridges in Section 8 refute this. Four working examples, 51-105 lines each. The C++20 awaitable protocol is the interop surface.

## insufficiency - grade 2.00 (fired in 4 of 16 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             1/0/0  -> 0.33
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The query set is open by design, and the only adaptation mechanism - `write_env` - requires the caller to know every missing query by name.
candidate 2 (found by 3 of 48 passes): The type-erasure mechanism that Asio provides for executors has no analogue for an open query protocol.
candidate 3 (found by 2 of 48 passes): The caller must know every custom query from every library, by name, and inject them all manually. There is no discovery mechanism - no way to ask an environment "what queries do you need?"
candidate 4 (found by 1 of 48 passes): `write_env` does not help with any of this. It is a syntactic mechanism for injecting key-value pairs. The semantic burden is entirely on the caller.

## implementation - grade 2.00  [binary: max] (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/2/0  -> 0.67
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        1/1/1  -> 1.00
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/1  -> 0.33
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): NVIDIA's reference implementation defines custom forwarding queries in [nvexec/stream/common.cuh](https://github.com/NVIDIA/stdexec/blob/main/include/nvexec/stream/common.cuh) [28]:
candidate 2 (found by 3 of 48 passes): The only production two-parameter coroutine type is Asio's `awaitable<T, Executor>`.
candidate 3 (found by 3 of 48 passes): The [cross_await](https://github.com/klemens-morgenstern/cross_await) [30] repository (Klemens Morgenstern) contains four cross-library composition examples, 51-105 lines each.
candidate 4 (found by 1 of 48 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy) [22] and [Corosio](https://github.com/cppalliance/corosio) [23]

-->
