Verdict: Excellent (14/14)

The paper offers substantial support for its own standardization, with particularly strong evidence across ecosystem impact, prior art, implementation experience, and the limits of library-only solutions. The support is thinnest where the argument relies on extrapolating from a small number of independent reports and bridging examples to a claim about failure at much greater scale.

- The strongest support comes from concrete implementation evidence, including NVIDIA’s reference implementation, Boost.Asio’s production precedent, and four working cross-library composition examples.
- The paper also establishes clearly why a library-only solution cannot address the open query protocol’s adaptation burden and why a standard type would serve as a common interoperability point.
- The most notable weakness is that the predicted ecosystem fragmentation rests on five reports and a handful of examples, leaving the scale of the claimed structural risk more asserted than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (13.50/14)

Provisionally addressed: 7 of 7. Provisional points: 13.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 13.50   corroborated 13.00   accumulate 14.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.83  coordination 2.00  insufficiency 1.67  implementation 2.00
sample agreement: 100 of 112 section-criterion pairs unanimous (89%)
single-sample totals would have been: 13.50 / 14.00 / 13.00   (all 3 samples: 13.50)
headings: h2 15
on threshold: insufficiency
splits: audience[2] 0/0/1  audience[10] 0/2/2  prior_art[4] 1/0/0  prior_art[14] 0/2/2
        vehicle[2] 2/2/1  vehicle[6] 1/0/1  vehicle[13] 0/1/1  coordination[13] 0/0/2
        insufficiency[2] 1/2/1  insufficiency[9] 1/2/1  implementation[13] 0/0/1
        implementation[14] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 16 sections, strong in 7)  (SHARED PASSAGE)
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
  [12] 9. Concepts Mitigate the Risk                2/2/2  -> 2.00
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The findings documented in this paper and in [P3801R0], "Concerns about the design of `std::execution::task`," are structural consequences of making `task` do more than one thing.
candidate 2 (found by 3 of 48 passes): A standard task type provides a lingua franca. It eliminates pairwise bridges.
candidate 3 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 4 (found by 3 of 48 passes): When the Environment changes, the return type changes, and every caller breaks.

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
  [10] 7. Design Intent                             0/2/2  -> 1.33
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               1/1/1  -> 1.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 2 (found by 3 of 48 passes): Nine coroutine libraries are surveyed below.
candidate 3 (found by 3 of 48 passes): seven independent libraries converging on one-parameter designs
candidate 4 (found by 2 of 48 passes): Everybody (millions) | Uses coroutines and awaitables defined by the standard library, Boost, and other high-quality libraries

## prior_art - grade 2.00 (fired in 11 of 16 sections, strong in 8)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. P3552R3                                   2/2/2  -> 2.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              1/1/1  -> 1.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        2/2/2  -> 2.00
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                2/2/2  -> 2.00
  [13] 10. Frequently Raised Concerns               2/2/2  -> 2.00
  [14] 11. Conclusion                               0/2/2  -> 1.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The risk to the ecosystem is structural, documented by the specification itself, by NVIDIA's reference implementation, by the only production precedent (Boost.Asio), and by `task`'s own author.
candidate 2 (found by 3 of 48 passes): Dietmar Kühl responded to every concern with professionalism and technical precision, and wrote [P3796R1], "Coroutine Task Issues," to collect the issues himself.
candidate 3 (found by 3 of 48 passes): P2300R10 defines `queryable` as the base concept for all objects that respond to property queries - schedulers, senders, receivers, and environments all refine it.
candidate 4 (found by 3 of 48 passes): Asio's case is mild. The executor concept has a closed interface. `any_io_executor` provides an escape hatch at the cost of one virtual dispatch per operation.

## vehicle - grade 1.83 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/1  -> 1.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 1/0/1  -> 0.67
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           1/1/1  -> 1.00
  [9] 6. The Asio Precedent                        0/0/0  -> 0.00
  [10] 7. Design Intent                             2/2/2  -> 2.00
  [11] 8. The Ecosystem                             1/1/1  -> 1.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/1/1  -> 0.67
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): Good stewardship of the standard means shipping features narrow and widening with evidence.
candidate 2 (found by 3 of 48 passes): Asio is the most widely deployed C++ async library; the standard proposal carries normative weight.
candidate 3 (found by 2 of 48 passes): The query set is open by design, and the only adaptation mechanism - `write_env` - requires the caller to know every missing query by name.
candidate 4 (found by 2 of 48 passes): The `Environment` parameter moves that diversity into the return type, producing the fragmentation that Section 5 documents.

## coordination - grade 2.00 (fired in 7 of 16 sections, strong in 4)  (SHARED PASSAGE)
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
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/2  -> 0.67
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): when two libraries define different environments, how does one task `co_await` the other?
candidate 2 (found by 3 of 48 passes): A standard task type provides a lingua franca. It eliminates pairwise bridges. It gives the ecosystem a common type that every library can accept and return.
candidate 3 (found by 3 of 48 passes): Five independent reports illustrate the kind of failure the `Environment` parameter will produce at greater scale:
candidate 4 (found by 2 of 48 passes): the structural interoperability risk documented here

## insufficiency - grade 1.67 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        1/2/1  -> 1.33
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             0/0/0  -> 0.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/0  -> 0.00
  [14] 11. Conclusion                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The query set is open by design, and the only adaptation mechanism - `write_env` - requires the caller to know every missing query by name.
candidate 2 (found by 3 of 48 passes): The caller must construct the domain-specific objects correctly, manage their lifetimes, and know the semantic requirements of each query. `write_env` does not help with any of this.
candidate 3 (found by 3 of 48 passes): The type-erasure mechanism that Asio provides for executors has no analogue for an open query protocol.

## implementation - grade 2.00  [binary: max] (fired in 4 of 16 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. P3552R3                                   0/0/0  -> 0.00
  [6] 3. The Claim                                 0/0/0  -> 0.00
  [7] 4. destructible                              0/0/0  -> 0.00
  [8] 5. Two Libraries, Two Environments           2/2/2  -> 2.00
  [9] 6. The Asio Precedent                        0/0/0  -> 0.00
  [10] 7. Design Intent                             0/0/0  -> 0.00
  [11] 8. The Ecosystem                             2/2/2  -> 2.00
  [12] 9. Concepts Mitigate the Risk                0/0/0  -> 0.00
  [13] 10. Frequently Raised Concerns               0/0/1  -> 0.33
  [14] 11. Conclusion                               1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): NVIDIA's reference implementation defines custom forwarding queries in [nvexec/stream/common.cuh](https://github.com/NVIDIA/stdexec/blob/main/include/nvexec/stream/common.cuh)[28]:
candidate 2 (found by 3 of 48 passes): The [cross_await](https://github.com/klemens-morgenstern/cross_await)[30] repository (Klemens Morgenstern) contains four cross-library composition examples, 51-105 lines each.
candidate 3 (found by 1 of 48 passes): The cross_await bridges in Section 8 refute this. Four working examples, 51-105 lines each.
candidate 4 (found by 1 of 48 passes): by the reference implementation (NVIDIA's custom queries, Section 5.3), by the only production precedent (Asio, Section 6)

-->
