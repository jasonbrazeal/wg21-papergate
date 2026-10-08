Verdict: Adequate (7/14)

The paper offers some meaningful support for standardization, chiefly through its motivation and implementation experience, but much of the case remains asserted rather than demonstrated. The thinnest areas are the absence of any identified affected user population and the largely unsupported claims about why existing libraries or a non-standard library cannot suffice.

- The paper clearly establishes that graphs are a broadly important abstraction and that the authors have substantial implementation experience, including a public reference implementation and ported algorithms.
- The discussion of prior art names several influential graph libraries but does not substantiate the claim that they fail to meet modern C++ needs.
- The paper asserts that standardization is necessary and that a standalone library would not suffice, but it does not show why interoperability or C++23 concepts require a standard rather than a widely adopted library.
- The paper never identifies who would be affected by standardizing this library, leaving the intended user community and its needs unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 23. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.33   accumulate 7.83   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.00  vehicle 0.67  coordination 0.17  insufficiency 1.00  implementation 2.00
sample agreement: 153 of 161 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.00 / 6.50   (all 3 samples: 6.83)
headings: h2 22
on threshold: implementation
splits: motivation[18] 1/0/0  prior_art[2] 1/1/0  prior_art[10] 0/1/1  prior_art[13] 1/0/1
        prior_art[17] 0/0/1  vehicle[4] 0/1/0  coordination[19] 1/0/0  implementation[11] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 23 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   2/2/2  -> 2.00
  [5] 4 Goals and Priorities                       1/1/1  -> 1.00
  [6] 5 Example: Six Degrees of Kevin Bacon        1/1/1  -> 1.00
  [7] 6 What this proposal is not                  1/1/1  -> 1.00
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
  [18] 17 Language Requirements                     1/0/0  -> 0.33
  [19] 18 Namespaces                                1/1/1  -> 1.00
  [20] 19 Notes and Considerations                  1/1/1  -> 1.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): Graphs are an important abstraction in Computer Science and that arise in numerous problem domains.
candidate 2 (found by 3 of 69 passes): The main goal of this library is to provide a self-consistent and systematic library of software components for graph computations, based on well-defined graph representations.
candidate 3 (found by 3 of 69 passes): Note, however, that actor-actor relationships are not how data about actors is available in the wild (from IMDB, for example).
candidate 4 (found by 3 of 69 passes): Particular pain-points described in ad-hoc discussions with users include: property maps, parameter-passing, and adapting to existing graph data structures.

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

## prior_art - grade 1.00 (fired in 12 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            1/1/0  -> 0.67
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   1/1/1  -> 1.00
  [5] 4 Goals and Priorities                       1/1/1  -> 1.00
  [6] 5 Example: Six Degrees of Kevin Bacon        1/1/1  -> 1.00
  [7] 6 What this proposal is not                  1/1/1  -> 1.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              1/1/1  -> 1.00
  [10] 9 Implementation Experience                  0/1/1  -> 0.67
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                1/0/1  -> 0.67
  [14] 13 Prior Art                                 0/0/0  -> 0.00
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/1  -> 0.33
  [18] 17 Language Requirements                     1/1/1  -> 1.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  1/1/1  -> 1.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): It is informed by the authors’ past experience with the Boost Graph Library (BGL), the NWGraph library, the C++ GraphBLAS, proprietary graphs embedded in products, and the library originally proposed in P1709.
candidate 2 (found by 3 of 69 passes): Parallelism is not beneficial for some algorithms, such as for depth-first search.
candidate 3 (found by 3 of 69 passes): [P3337](https://www.wg21.link/P3337) (Comparison to other graph libraries)
candidate 4 (found by 3 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.

## vehicle - grade 0.67 (fired in 2 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
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
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 69 passes): We are currently unaware of any existing graph library that meets the same requirements and uses concepts and ranges from C++23.
candidate 2 (found by 1 of 69 passes): Since the introduction of the STL and the generic programming paradigm that is its intellectual foundation, there has been recognition of the need to extend the standard library to support hierarchical containers (containers of containers).
candidate 3 (found by 1 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.

## coordination - grade 0.17 (fired in 1 of 23 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [19] 18 Namespaces                                1/0/0  -> 0.33
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 69 passes): Graph containers and their views and algorithms are not interchangeable with existing containers and algorithms.

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
candidate 2 (found by 3 of 69 passes): We are currently unaware of any existing graph library that meets the same requirements and uses concepts and ranges from C++23.

## implementation - grade 2.00  [binary: max] (fired in 6 of 23 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [11] 10 Usage Experience                          0/1/0  -> 0.33
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
