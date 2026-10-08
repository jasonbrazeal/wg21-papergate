Verdict: Adequate to Strong (8/14)

The paper offers a solid foundation in places, particularly in its analysis of prior art and its concrete implementation experience, but it leaves several essential parts of its standardization case asserted rather than demonstrated. The thinnest support concerns the claims that only a standard can deliver the proposed design and that the affected deployments and ABI benefits are real rather than assumed.

- The strongest support comes from the documented analysis that led the committee to set aside the Networking TS and from the Boost.Beast experience showing the costs of layered completion handlers.
- The paper also establishes that the deficiencies identified in earlier work depend on the framing used, which gives the proposal a clear analytical basis.
- The case weakens where it asserts, without evidence, that the affected users include major deployments at Facebook, NVIDIA, and Bloomberg.
- The most glaring omission is the absence of substantiation for the claim that the desired properties cannot be achieved by a library or without standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 20. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.33   accumulate 7.67   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 1.67  vehicle 0.17  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.00 / 8.50   (all 3 samples: 7.67)
headings: h2 10
on threshold: audience, prior_art, implementation
splits: audience[9] 1/2/2  prior_art[2] 2/0/2  vehicle[4] 0/0/1  implementation[4] 2/0/1
        implementation[7] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          2/2/2  -> 2.00
  [7] 4. The Three Criteria Under Both Framings    2/2/2  -> 2.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                2/2/2  -> 2.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The process had no mechanism to verify that the analysis examined every applicable framing, and no mechanism to revisit the outcome against evidence.
candidate 2 (found by 3 of 33 passes): The generality that the completion token provides is genuine, but the cost is that it forecloses the optimizations that networking in C++ has needed for twenty years.
candidate 3 (found by 3 of 33 passes): The work framing imposes requirements on the executor that the continuation framing does not.
candidate 4 (found by 3 of 33 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.

## audience - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                1/2/2  -> 1.67
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Deployments at Facebook, NVIDIA, Bloomberg - GPU dispatch, thread pools, infrastructure.
candidate 2 (found by 1 of 33 passes): Deployments | [Capy](https://github.com/cppalliance/capy) [6], [Corosio](https://github.com/cppalliance/corosio) [7]. | [P2470R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2470r0.pdf) [15]: Facebook, NVIDIA, Bloomberg - GPU dispatch, thread pools, infrastructure.

## prior_art - grade 1.67 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/0/2  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          2/2/2  -> 2.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The paper concluded that the Networking TS should be set aside. The committee acted on the analysis.
candidate 2 (found by 2 of 33 passes): Under the work framing, the three deficiencies hold. Under the continuation framing, they do not arise. [P2464R0] analyzed under the work framing only.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/1  -> 0.33
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): None of these properties are achievable when the operation state must be parameterized on an arbitrary completion handler type.

## coordination - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): the ABI stabilizes across transport changes
candidate 2 (found by 1 of 33 passes): the ABI stabilizes across transport changes.
candidate 3 (found by 1 of 33 passes): the operation state becomes concrete, the stream becomes type-erasable without per-operation allocation, the I/O library compiles once, and the ABI stabilizes across transport changes.

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): None of these properties are achievable when the operation state must be parameterized on an arbitrary completion handler type.

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/0/1  -> 1.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    2/1/1  -> 1.33
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                2/2/2  -> 2.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 2 (found by 3 of 33 passes): Deployments | [Capy](https://github.com/cppalliance/capy) [6], [Corosio](https://github.com/cppalliance/corosio) [7].
candidate 3 (found by 2 of 33 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy) [6] and [Corosio](https://github.com/cppalliance/corosio) [7] and believes coroutine-native I/O is a practical foundation for networking in C++.

-->
