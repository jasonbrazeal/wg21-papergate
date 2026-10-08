Verdict: Adequate to Strong (7/14)

The paper offers a mixed case for its own standardization, with its strongest material concentrated in the technical critique of existing practice and the author’s implementation experience. The argument is thinnest where it needs to show that the problem is broadly shared and that standardization, rather than a library, is the necessary remedy.

- The paper’s most concrete support comes from its account of Boost.Beast’s three-layer composition burden and the author’s maintenance of Capy and Corosio as practical coroutine-native I/O foundations.
- The prior-art discussion is grounded in the committee’s own decision to set aside the Networking TS, which lends the framing historical weight.
- The claim that affected deployments include Facebook, NVIDIA, and Bloomberg is asserted without evidence tying those deployments to the proposed direction.
- The most glaring omission is any treatment of coordination and interoperability with existing or in-flight standardization efforts, leaving the proposal’s relationship to the broader ecosystem unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 23. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.33   accumulate 7.83   max 8.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 1.67  vehicle 0.17  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 74 of 84 section-criterion pairs unanimous (88%)
single-sample totals would have been: 7.00 / 8.00 / 7.50   (all 3 samples: 7.33)
headings: h2 11
on threshold: prior_art, implementation
splits: motivation[2] 0/2/2  motivation[5] 1/0/0  motivation[9] 0/2/1  audience[7] 1/0/0
        audience[9] 0/2/2  audience[10] 0/1/1  prior_art[2] 2/0/0  prior_art[7] 2/2/0
        vehicle[4] 0/0/1  implementation[4] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/2  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
  [5] 2. What P2464R0 Did                          1/0/0  -> 0.33
  [6] 3. The Two Framings                          2/2/2  -> 2.00
  [7] 4. The Three Criteria Under Both Framings    2/2/2  -> 2.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/2/1  -> 1.00
  [10] Ecosystem-scale validation:                  2/2/2  -> 2.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The work framing imposes requirements on the executor that the continuation framing does not.
candidate 2 (found by 3 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 3 (found by 3 of 36 passes): In 2026, no replacement has shipped.
candidate 4 (found by 2 of 36 passes): When the completion mechanism is fixed to `coroutine_handle<>`, the operation state becomes concrete, the stream becomes type-erasable without per-operation allocation, the I/O library compiles once, and the ABI stabilizes across transport changes.

## audience - grade 1.00 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    1/0/0  -> 0.33
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/2/2  -> 1.33
  [10] Ecosystem-scale validation:                  0/1/1  -> 0.67
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): deployments at Facebook, NVIDIA, Bloomberg - GPU dispatch, thread pools, infrastructure.
candidate 2 (found by 2 of 36 passes): Deployments | [Capy](https://github.com/cppalliance/capy)[6], [Corosio](https://github.com/cppalliance/corosio)[7].
candidate 3 (found by 1 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.

## prior_art - grade 1.67 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/0/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. What P2464R0 Did                          2/2/2  -> 2.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    2/2/0  -> 1.33
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Ecosystem-scale validation:                  0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The paper concluded that the Networking TS should be set aside. The committee acted on the analysis.
candidate 2 (found by 2 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 3 (found by 1 of 36 passes): Under the work framing, the three deficiencies hold. Under the continuation framing, they do not arise.

## vehicle - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] Ecosystem-scale validation:                  0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): None of these properties are achievable when the operation state must be parameterized on an arbitrary completion handler type.

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
candidate 1 (found by 2 of 36 passes): None of these properties are achievable when the operation state must be parameterized on an arbitrary completion handler type.
candidate 2 (found by 1 of 36 passes): When the completion mechanism is fixed to `coroutine_handle<>`, the operation state becomes concrete, the stream becomes type-erasable without per-operation allocation, the I/O library compiles once, and the ABI stabilizes across transport changes.

## implementation - grade 2.00  [binary: max] (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/0  -> 0.33
  [5] 2. What P2464R0 Did                          0/0/0  -> 0.00
  [6] 3. The Two Framings                          0/0/0  -> 0.00
  [7] 4. The Three Criteria Under Both Framings    2/2/2  -> 2.00
  [8] 5. Outcomes                                  0/0/0  -> 0.00
  [9] 2026 evidence                                0/0/0  -> 0.00
  [10] Ecosystem-scale validation:                  1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Boost.Beast (Boost 1.66, 2017) deployed three layers of composed asynchronous operations - socket reads into HTTP parsing into WebSocket framing - and every layer required its own state machine, its own intermediate completion handler, and its own lifetime management.
candidate 2 (found by 3 of 36 passes): Deployments | [Capy](https://github.com/cppalliance/capy)[6], [Corosio](https://github.com/cppalliance/corosio)[7].
candidate 3 (found by 1 of 36 passes): The author developed and maintains [Capy](https://github.com/cppalliance/capy)[6] and [Corosio](https://github.com/cppalliance/corosio)[7] and believes coroutine-native I/O is a practical foundation for networking in C++.

-->
