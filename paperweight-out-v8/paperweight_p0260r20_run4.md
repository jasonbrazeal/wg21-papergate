Verdict: Strong (8/14)

The paper offers solid support for the need to standardize concurrent queue concepts and at least one concrete implementation, with credible prior art, implementation experience, and a clear statement of why existing facilities fall short. The case is thinnest around who specifically is affected and around the claims that a library solution would be insufficient or that the proposed concepts would actually coordinate disparate implementations.

- The strongest support is the combination of established prior art, implementation experience, and the clear argument that existing sequential containers cannot serve concurrent programs.
- The paper also establishes why the standard should contain both concepts and a concrete queue, rather than leaving users to rely on ad hoc implementations.
- The weakest part is the absence of any established discussion of who is affected by the lack of a standard concurrent queue.
- The claims about interoperability and the inadequacy of a library-only solution remain asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.33   accumulate 8.17   max 9.33

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.50  coordination 0.50  insufficiency 0.17  implementation 2.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.00 / 8.00 / 8.50   (all 3 samples: 8.00)
headings: h2 12
on threshold: vehicle
splits: motivation[9] 1/2/1  motivation[12] 2/1/2  prior_art[6] 2/0/0  insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              2/2/2  -> 2.00
  [6] 4. Existing Practice                         1/1/1  -> 1.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           1/2/1  -> 1.33
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/1/2  -> 1.67
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Concurrent queues are a fundamental structuring tool for concurrent programs.
candidate 2 (found by 3 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.
candidate 3 (found by 3 of 39 passes): It was full of bugs and as such shows what will go wrong if C++ doesn’t provide a standard queue.
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

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              1/1/1  -> 1.00
  [6] 4. Existing Practice                         2/0/0  -> 0.67
  [7] 5. Examples and Implementation               1/1/1  -> 1.00
  [8] 6. Conceptual Interface                      2/2/2  -> 2.00
  [9] 7. Concrete Queues                           2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure.
candidate 2 (found by 3 of 39 passes): [P3570R0: optional variants in sender/receiver](https://wg21.link/P3570) provides a mechanism to return different values for coroutines than for direct receivers. This revision proposes to use this mechanism.
candidate 3 (found by 3 of 39 passes): Background on this is found in [Memory Model Issues for Concurrent Data Structures (P0387R1)](https://wg21.link/P0387R1) and [Concurrency Safety in C++ Data Structures (P0495)](https://wg21.link/P0495).
candidate 4 (found by 3 of 39 passes): However, at least Thread Building Blocks uses the existing terminology.

## vehicle - grade 1.50 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      2/2/2  -> 2.00
  [9] 7. Concrete Queues                           1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.
candidate 2 (found by 3 of 39 passes): In addition to the concepts, the standard needs at least one concrete queue.

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

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/1  -> 0.33
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 2)
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
