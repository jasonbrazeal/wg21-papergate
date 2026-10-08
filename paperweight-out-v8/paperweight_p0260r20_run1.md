Verdict: Strong (8/14)

The paper offers solid support for the importance of concurrent queues, the inadequacy of the existing sequential `deque`, and the existence of prior art and implementation experience, but it leaves significant gaps around who is affected and why a library-only solution would be insufficient. The thinnest areas are the absence of any demonstrated user constituency and the lack of an argument that standardization, rather than a third-party library, is necessary.

- The strongest support is the paper’s clear explanation that concurrent queues are fundamental and that the standard `deque` cannot serve concurrent use cases.
- The paper also credibly establishes prior art and implementation experience through references to existing designs, a partial implementation, and Boost’s synchronized queue.
- The case for coordination and interoperability is asserted through the value of common concepts, but it is not backed by evidence of actual cross-implementation use or need.
- The most glaring omission is the lack of any established audience or affected users, alongside the failure to explain why a library outside the standard would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.50  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 8.00 / 8.00 / 8.00   (all 3 samples: 8.00)
headings: h2 12
on threshold: vehicle, implementation
splits: motivation[6] 1/2/1  motivation[9] 1/1/2  implementation[6] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 2)
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
  [9] 7. Concrete Queues                           1/1/2  -> 1.33
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Concurrent queues are a fundamental structuring tool for concurrent programs.
candidate 2 (found by 3 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.
candidate 3 (found by 3 of 39 passes): In short, we do not think that in a concurrent environment `push_front` provides sufficient semantic value to justify its cost.
candidate 4 (found by 2 of 39 passes): It was full of bugs and as such shows what will go wrong if C++ doesn’t provide a standard queue.

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

## prior_art - grade 2.00 (fired in 5 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              1/1/1  -> 1.00
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               1/1/1  -> 1.00
  [8] 6. Conceptual Interface                      2/2/2  -> 2.00
  [9] 7. Concrete Queues                           2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure.
candidate 2 (found by 3 of 39 passes): A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).
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

## insufficiency - grade 0.00 (fired in 0 of 13 sections, strong in 0)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         0/2/2  -> 1.33
  [7] 5. Examples and Implementation               2/2/2  -> 2.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).
candidate 2 (found by 2 of 39 passes): [Boost Synchronized Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html) is an implementation of an early version of this proposal.

-->
