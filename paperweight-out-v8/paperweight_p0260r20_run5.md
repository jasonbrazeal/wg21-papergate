Verdict: Adequate to Strong (8/14)

The paper offers solid grounding for the need it addresses and for the existence of usable prior work, but its case for standardization specifically rests on assertions that are not developed into evidence. The thinnest support concerns who would be affected by the proposed facility and why a non-standard library solution would be insufficient.

- The paper clearly establishes that concurrent queues are a fundamental tool and that existing standard containers such as `deque` cannot safely fill that role.
- It also demonstrates implementation experience through the Boost Synchronized Queue and a partial reference implementation.
- The discussion of prior art and alternatives is credible, pointing to earlier WG21 papers and existing terminology in Thread Building Blocks.
- The most glaring omission is any account of who is affected, leaving the audience for the proposed standardization unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 7.67   accumulate 8.33   max 9.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 1.33  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.00 / 9.00 / 7.50   (all 3 samples: 7.83)
headings: h2 12
on threshold: motivation, vehicle
splits: motivation[5] 2/2/1  motivation[12] 1/2/1  prior_art[6] 0/2/2  vehicle[8] 1/2/2
        insufficiency[5] 0/1/1  insufficiency[6] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              2/2/1  -> 1.67
  [6] 4. Existing Practice                         1/1/1  -> 1.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        1/2/1  -> 1.33
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Concurrent queues are a fundamental structuring tool for concurrent programs.
candidate 2 (found by 3 of 39 passes): It was full of bugs and as such shows what will go wrong if C++ doesn’t provide a standard queue.
candidate 3 (found by 2 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.
candidate 4 (found by 2 of 39 passes): This will not provide the most efficient implementation but serves all synchronization use cases.

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
  [6] 4. Existing Practice                         0/2/2  -> 1.33
  [7] 5. Examples and Implementation               1/1/1  -> 1.00
  [8] 6. Conceptual Interface                      2/2/2  -> 2.00
  [9] 7. Concrete Queues                           2/2/2  -> 2.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure.
candidate 2 (found by 3 of 39 passes): Background on this is found in [Memory Model Issues for Concurrent Data Structures (P0387R1)](https://wg21.link/P0387R1) and [Concurrency Safety in C++ Data Structures (P0495)](https://wg21.link/P0495).
candidate 3 (found by 3 of 39 passes): However, at least Thread Building Blocks uses the existing terminology.
candidate 4 (found by 2 of 39 passes): [Boost Synchronized Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html) is an implementation of an early version of this proposal.

## vehicle - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/0/0  -> 0.00
  [6] 4. Existing Practice                         0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      1/2/2  -> 1.67
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

## insufficiency - grade 0.50 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Acknowledgments                           0/0/0  -> 0.00
  [4] 2. Revision History                          0/0/0  -> 0.00
  [5] 3. Introduction                              0/1/1  -> 0.67
  [6] 4. Existing Practice                         0/1/0  -> 0.33
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Conceptual Interface                      0/0/0  -> 0.00
  [9] 7. Concrete Queues                           0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Old Revision History                      0/0/0  -> 0.00
  [12] 10. Historic Contents                        0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.
candidate 2 (found by 1 of 39 passes): The first concurrent queue I’ve seen was in [Hughes97]. It was full of bugs and as such shows what will go wrong if C++ doesn’t provide a standard queue.

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
