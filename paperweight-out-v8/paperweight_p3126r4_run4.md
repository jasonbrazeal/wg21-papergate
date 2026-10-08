Verdict: Adequate to Strong (7/14)

The paper offers some grounding for standardization through its implementation experience and its explanation of why graph abstractions matter, but it leaves several essential parts of the case asserted rather than demonstrated. The thinnest support concerns who is affected, coordination with existing practice, and why a library outside the standard cannot suffice.

- The strongest support is the concrete reference implementation and the authors’ direct experience porting algorithms from Boost Graph and NWGraph.
- The paper clearly explains the general importance of graph abstractions and the pain points in current graph programming.
- The discussion of prior art names several influential libraries but does not show specifically how they fall short of the proposal’s goals.
- The paper never identifies the affected users or establishes how the proposed library would coordinate with existing graph libraries and data structures.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 23. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 7.83   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.17  vehicle 0.67  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 152 of 161 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 7.50 / 7.00   (all 3 samples: 6.83)
headings: h2 22
on threshold: implementation
splits: motivation[6] 2/1/1  motivation[7] 0/1/1  motivation[18] 1/1/0  prior_art[4] 0/2/2
        prior_art[10] 1/0/0  prior_art[13] 1/0/1  prior_art[21] 1/0/0  vehicle[4] 0/1/0
        vehicle[19] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 23 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   2/2/2  -> 2.00
  [5] 4 Goals and Priorities                       1/1/1  -> 1.00
  [6] 5 Example: Six Degrees of Kevin Bacon        2/1/1  -> 1.33
  [7] 6 What this proposal is not                  0/1/1  -> 0.67
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/0  -> 0.00
  [10] 9 Implementation Experience                  0/0/0  -> 0.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                0/0/0  -> 0.00
  [14] 13 Prior Art                                 2/2/2  -> 2.00
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              1/1/1  -> 1.00
  [18] 17 Language Requirements                     1/1/0  -> 0.67
  [19] 18 Namespaces                                1/1/1  -> 1.00
  [20] 19 Notes and Considerations                  1/1/1  -> 1.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): Graphs are an important abstraction in Computer Science and that arise in numerous problem domains.
candidate 2 (found by 3 of 69 passes): The main goal of this library is to provide a self-consistent and systematic library of software components for graph computations, based on well-defined graph representations.
candidate 3 (found by 3 of 69 passes): Particular pain-points described in ad-hoc discussions with users include: property maps, parameter-passing, and adapting to existing graph data structures.
candidate 4 (found by 3 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.

## audience - grade 0.00 (fired in 0 of 23 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   0/0/0  -> 0.00
  [5] 4 Goals and Priorities                       0/0/0  -> 0.00
  [6] 5 Example: Six Degrees of Kevin Bacon        0/0/0  -> 0.00
  [7] 6 What this proposal is not                  0/0/0  -> 0.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/0  -> 0.00
  [10] 9 Implementation Experience                  0/0/0  -> 0.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                0/0/0  -> 0.00
  [14] 13 Prior Art                                 0/0/0  -> 0.00
  [15] 14 Alternatives                              0/0/0  -> 0.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/0  -> 0.00
  [18] 17 Language Requirements                     0/0/0  -> 0.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 13 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            1/1/1  -> 1.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   0/2/2  -> 1.33
  [5] 4 Goals and Priorities                       1/1/1  -> 1.00
  [6] 5 Example: Six Degrees of Kevin Bacon        1/1/1  -> 1.00
  [7] 6 What this proposal is not                  1/1/1  -> 1.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              1/1/1  -> 1.00
  [10] 9 Implementation Experience                  1/0/0  -> 0.33
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                1/0/1  -> 0.67
  [14] 13 Prior Art                                 0/0/0  -> 0.00
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              1/1/1  -> 1.00
  [18] 17 Language Requirements                     1/1/1  -> 1.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  1/1/1  -> 1.00
  [21] 20 Issues Status                             1/0/0  -> 0.33
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): This paper is one of several interrelated papers for a proposed Graph Library for the Standard C++ Library.
candidate 2 (found by 3 of 69 passes): It is informed by the authors’ past experience with the Boost Graph Library (BGL), the NWGraph library, the C++ GraphBLAS, proprietary graphs embedded in products, and the library originally proposed in P1709.
candidate 3 (found by 3 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.
candidate 4 (found by 3 of 69 passes): We are unable to support freestanding implementations in this proposal because many of the algorithms and views require a `stack` or `queue`, which are not available in a freestanding environment.

## vehicle - grade 0.67 (fired in 3 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   0/1/0  -> 0.33
  [5] 4 Goals and Priorities                       0/0/0  -> 0.00
  [6] 5 Example: Six Degrees of Kevin Bacon        0/0/0  -> 0.00
  [7] 6 What this proposal is not                  0/0/0  -> 0.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/0  -> 0.00
  [10] 9 Implementation Experience                  0/0/0  -> 0.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                0/0/0  -> 0.00
  [14] 13 Prior Art                                 0/0/0  -> 0.00
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/0  -> 0.00
  [18] 17 Language Requirements                     0/0/0  -> 0.00
  [19] 18 Namespaces                                0/1/0  -> 0.33
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 69 passes): We are currently unaware of any existing graph library that meets the same requirements and uses concepts and ranges from C++23.
candidate 2 (found by 1 of 69 passes): Since the introduction of the STL and the generic programming paradigm that is its intellectual foundation, there has been recognition of the need to extend the standard library to support hierarchical containers (containers of containers).
candidate 3 (found by 1 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.
candidate 4 (found by 1 of 69 passes): For these reasons, we recommend separate namespace(s) for the graph functionality.

## coordination - grade 0.00 (fired in 0 of 23 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   0/0/0  -> 0.00
  [5] 4 Goals and Priorities                       0/0/0  -> 0.00
  [6] 5 Example: Six Degrees of Kevin Bacon        0/0/0  -> 0.00
  [7] 6 What this proposal is not                  0/0/0  -> 0.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/0  -> 0.00
  [10] 9 Implementation Experience                  0/0/0  -> 0.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                0/0/0  -> 0.00
  [14] 13 Prior Art                                 0/0/0  -> 0.00
  [15] 14 Alternatives                              0/0/0  -> 0.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/0  -> 0.00
  [18] 17 Language Requirements                     0/0/0  -> 0.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 2 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   0/0/0  -> 0.00
  [5] 4 Goals and Priorities                       0/0/0  -> 0.00
  [6] 5 Example: Six Degrees of Kevin Bacon        0/0/0  -> 0.00
  [7] 6 What this proposal is not                  0/0/0  -> 0.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/0  -> 0.00
  [10] 9 Implementation Experience                  0/0/0  -> 0.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                0/0/0  -> 0.00
  [14] 13 Prior Art                                 1/1/1  -> 1.00
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/0  -> 0.00
  [18] 17 Language Requirements                     0/0/0  -> 0.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): However, the resulting library relies on its own (opaque) data structures for representing graphs and would not be inter-operable with modern C++ approaches to library and application design.
candidate 2 (found by 2 of 69 passes): We are currently unaware of any existing graph library that meets the same requirements and uses concepts and ranges from C++23.
candidate 3 (found by 1 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.

## implementation - grade 2.00  [binary: max] (fired in 5 of 23 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   0/0/0  -> 0.00
  [5] 4 Goals and Priorities                       1/1/1  -> 1.00
  [6] 5 Example: Six Degrees of Kevin Bacon        0/0/0  -> 0.00
  [7] 6 What this proposal is not                  0/0/0  -> 0.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/0  -> 0.00
  [10] 9 Implementation Experience                  2/2/2  -> 2.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                1/1/1  -> 1.00
  [14] 13 Prior Art                                 1/1/1  -> 1.00
  [15] 14 Alternatives                              0/0/0  -> 0.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/0  -> 0.00
  [18] 17 Language Requirements                     1/1/1  -> 1.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): It is informed by the authors’ past experience with the Boost Graph Library (BGL), the NWGraph library, the C++ GraphBLAS, proprietary graphs embedded in products, and the library originally proposed in P1709.
candidate 2 (found by 3 of 69 passes): The github [github.com/stdgraph/graph-v3](https://github.com/stdgraph/graph-v3) repository contains a reference implementation for this proposal.
candidate 3 (found by 3 of 69 passes): The algorithms are being ported from Boost Graph and NWGraph to the github.com/stdgraph/graph-v3 implementation used for this proposal.
candidate 4 (found by 3 of 69 passes): The reference library has been extended to support many of the features and capabilities of **boost::graph**.

-->
