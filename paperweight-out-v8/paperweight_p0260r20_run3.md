Verdict: Strong (8/14)

The paper offers solid grounding in the problem’s importance, the design space, and the existence of working implementations, but it leaves the case for standardization itself largely asserted rather than demonstrated. The thinnest area is the absence of any concrete account of who is affected and how, which weakens the argument that this belongs in the standard rather than in a library or specification.

- The strongest support comes from implementation experience, with both a Boost queue and a partial reference implementation showing the design has been exercised in practice.
- The paper also establishes why concurrent queues matter and why the existing sequential `deque` cannot serve that role.
- Prior art and alternatives are well covered, including the range of queue flavors and pointers to earlier concurrency work.
- The most glaring omission is the lack of any established audience or affected-user analysis, leaving the proposal’s relevance to the broader C++ community unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.67   accumulate 8.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.17  coordination 0.50  insufficiency 0.67  implementation 2.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.50 / 8.50 / 8.00   (all 3 samples: 8.33)
headings: h2 12
on threshold: vehicle
splits: motivation[6] 1/2/1  vehicle[9] 0/0/1  insufficiency[5] 1/1/0  insufficiency[6] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              2/2/2  -> 2.00
  [6] 4. Existing Practice                         1/2/1  -> 1.33
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Concurrent queues are a fundamental structuring tool for concurrent programs.
candidate 2 (found by 3 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.
candidate 3 (found by 3 of 39 passes): This will not provide the most efficient implementation but serves all synchronization use cases.
candidate 4 (found by 3 of 39 passes): In short, we do not think that in a concurrent environment `push_front` provides sufficient semantic value to justify its cost.

## audience - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              1/1/1  -> 1.00
  [6] 4. Existing Practice                         2/2/2  -> 2.00
  [7] 5. Examples and Implementation               1/1/1  -> 1.00
  [8] 6. Conceptual Interface                      2/2/2  -> 2.00
  [9] 7. Concrete Queues                           2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Concurrent queues come in a several different flavours, e.g. - bounded vs. unbounded - blocking vs. overwriting - single-ended vs. multi-ended - strict FIFO ordering vs. priority based ordering
candidate 2 (found by 3 of 39 passes): [Boost Synchronized Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html) is an implementation of an early version of this proposal.
candidate 3 (found by 3 of 39 passes): A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).
candidate 4 (found by 3 of 39 passes): Background on this is found in [Memory Model Issues for Concurrent Data Structures (P0387R1)](https://wg21.link/P0387R1) and [Concurrency Safety in C++ Data Structures (P0495)](https://wg21.link/P0495).

## vehicle - grade 1.17 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      2/2/2  -> 2.00
  [9] 7. Concrete Queues                           0/0/1  -> 0.33
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.
candidate 2 (found by 1 of 39 passes): In addition to the concepts, the standard needs at least one concrete queue.

## coordination - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      1/1/1  -> 1.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## insufficiency - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              1/1/0  -> 0.67
  [6] 4. Existing Practice                         1/1/0  -> 0.67
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.
candidate 2 (found by 1 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure.
candidate 3 (found by 1 of 39 passes): Anthony Williams provided a queue in C++ Concurrency in Action. It’s unbounded.
candidate 4 (found by 1 of 39 passes): It was full of bugs and as such shows what will go wrong if C++ doesn’t provide a standard queue.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         2/2/2  -> 2.00
  [7] 5. Examples and Implementation               2/2/2  -> 2.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): [Boost Synchronized Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html) is an implementation of an early version of this proposal.
candidate 2 (found by 3 of 39 passes): A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).

-->
