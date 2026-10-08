Verdict: Adequate to Strong (8/14)

The paper offers real support in the areas that matter most for a standardization case: it shows why the problem is significant, documents prior art and the committee’s own history with the issue, and points to implementation experience. The support is thinnest where the paper needs to show that the work belongs in the standard rather than in a library, and it is essentially absent on coordination and interoperability with existing or adjacent standardization efforts.

- The strongest support is the established record of prior art and committee action, including the decision to set aside the Networking TS and the documented limitations of the continuation framing.
- The paper also establishes implementation experience through the author’s own projects and reported deployments, alongside the concrete historical example of Boost.Beast’s layered asynchronous complexity.
- The case for why the standard is the right venue is only claimed, resting on a single assertion about operation state parameterization rather than a fuller argument.
- The most glaring omission is coordination and interoperability, where the paper offers no established account of how the proposal fits with existing networking, coroutine, or execution work in the committee.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 19. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.00   accumulate 8.00   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 1.67  vehicle 0.50  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.00 / 8.50 / 7.00   (all 3 samples: 7.67)
headings: h2 11
on threshold: prior_art
splits: motivation[9] 2/1/2  audience[7] 0/0/1  audience[9] 2/2/0  audience[10] 0/1/1
        prior_art[9] 0/1/0  prior_art[10] 2/2/0  implementation[4] 2/2/1
        implementation[9] 0/0/1  implementation[10] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 6)  (SHARED PASSAGE)
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
  [9] 2026 evidence                                2/1/2  -> 1.67
  [10] Ecosystem-scale validation:                  2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The process had no mechanism to verify that the analysis examined every applicable framing, and no mechanism to revisit the outcome against evidence.
candidate 2 (found by 3 of 36 passes): The work framing imposes requirements on the executor that the continuation framing does not.
candidate 3 (found by 3 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 4 (found by 3 of 36 passes): In 2026, no replacement has shipped.

## audience - grade 1.00 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/1  -> 0.33
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                2/2/0  -> 1.33
  [10] Ecosystem-scale validation:                  0/1/1  -> 0.67
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Deployments | [Capy](https://github.com/cppalliance/capy)[6], [Corosio](https://github.com/cppalliance/corosio)[7].
candidate 2 (found by 1 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 3 (found by 1 of 36 passes): Seven published examples (2024): thread pools, embedded systems, cooperative multitasking, custom algorithms.
candidate 4 (found by 1 of 36 passes): deployments at Facebook, NVIDIA, Bloomberg - GPU dispatch, thread pools, infrastructure.

## prior_art - grade 1.67 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          2/2/2  -> 2.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/1/0  -> 0.33
  [10] Ecosystem-scale validation:                  2/2/0  -> 1.33
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The paper concluded that the Networking TS should be set aside. The committee acted on the analysis.
candidate 2 (found by 2 of 36 passes): The continuation framing, in 2021. Five years.
candidate 3 (found by 1 of 36 passes): The paper concluded that the Networking TS should be set aside.
candidate 4 (found by 1 of 36 passes): [P2762R2](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2762r2.pdf)[12] (Kühl, 2023): five routing options documented, single-argument error channel "somewhat limiting."

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] Ecosystem-scale validation:                  0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): None of these properties are achievable when the operation state must be parameterized on an arbitrary completion handler type.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    0/0/0  -> 0.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Ecosystem-scale validation:                  0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] Ecosystem-scale validation:                  0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): None of these properties are achievable when the operation state must be parameterized on an arbitrary completion handler type.

## implementation - grade 2.00  [binary: max] (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/1  -> 1.67
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    2/2/2  -> 2.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/1  -> 0.33
  [10] Ecosystem-scale validation:                  1/1/2  -> 1.33
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy)[6] and [Corosio](https://github.com/cppalliance/corosio)[7] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 2 (found by 3 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 3 (found by 3 of 36 passes): Deployments | [Capy](https://github.com/cppalliance/capy)[6], [Corosio](https://github.com/cppalliance/corosio)[7].
candidate 4 (found by 1 of 36 passes): deployments at Facebook, NVIDIA, Bloomberg - GPU dispatch, thread pools, infrastructure.

-->
