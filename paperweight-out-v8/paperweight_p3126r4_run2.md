Verdict: Adequate to Strong (7/14)

The paper offers meaningful support in two areas—why graphs matter and the existence of a reference implementation—but leaves most of the burden of justification unproven, particularly around who is affected and why standardization, rather than a library, is necessary. The thinnest support is in the absence of any identified user community or concrete interoperability story.

- The strongest support is the reference implementation and the authors’ direct experience porting algorithms from Boost Graph and NWGraph.
- The paper clearly establishes that graphs are a broadly important abstraction across problem domains.
- The claims about prior art and alternatives gesture at relevant libraries but do not demonstrate how they fall short for modern C++ users.
- The most glaring omission is any account of who would be affected by standardizing this work, leaving the audience and impact unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 23. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 8.33   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.00  vehicle 0.83  coordination 0.50  insufficiency 1.00  implementation 2.00
sample agreement: 156 of 161 section-criterion pairs unanimous (97%)
single-sample totals would have been: 8.00 / 7.00 / 7.50   (all 3 samples: 7.33)
headings: h2 22
on threshold: implementation
splits: motivation[20] 1/1/0  prior_art[4] 1/0/2  prior_art[9] 0/0/1  prior_art[17] 0/1/1
        vehicle[14] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 23 sections, strong in 2)
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
  [18] 17 Language Requirements                     0/0/0  -> 0.00
  [19] 18 Namespaces                                1/1/1  -> 1.00
  [20] 19 Notes and Considerations                  1/1/0  -> 0.67
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): Graphs are an important abstraction in Computer Science and that arise in numerous problem domains.
candidate 2 (found by 3 of 69 passes): The main goal of this library is to provide a self-consistent and systematic library of software components for graph computations, based on well-defined graph representations.
candidate 3 (found by 3 of 69 passes): Note, however, that actor-actor relationships are not how data about actors is available in the wild (from IMDB, for example).
candidate 4 (found by 3 of 69 passes): We feel that providing a broader set of algorithms to address different interests is the better choice.

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

## prior_art - grade 1.00 (fired in 11 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            1/1/1  -> 1.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Overview                                   1/0/2  -> 1.00
  [5] 4 Goals and Priorities                       1/1/1  -> 1.00
  [6] 5 Example: Six Degrees of Kevin Bacon        1/1/1  -> 1.00
  [7] 6 What this proposal is not                  1/1/1  -> 1.00
  [8] 7 Impact on the Standard                     0/0/0  -> 0.00
  [9] 8 Interaction with Other Papers              0/0/1  -> 0.33
  [10] 9 Implementation Experience                  0/0/0  -> 0.00
  [11] 10 Usage Experience                          0/0/0  -> 0.00
  [12] 11 Deployment Experience                     0/0/0  -> 0.00
  [13] 12 Performance Considerations                1/1/1  -> 1.00
  [14] 13 Prior Art                                 0/0/0  -> 0.00
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/1/1  -> 0.67
  [18] 17 Language Requirements                     1/1/1  -> 1.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  1/1/1  -> 1.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): It is informed by the authors’ past experience with the Boost Graph Library (BGL), the NWGraph library, the C++ GraphBLAS, proprietary graphs embedded in products, and the library originally proposed in P1709.
candidate 2 (found by 3 of 69 passes): The algorithms are being ported from Boost Graph and NWGraph to the [github.com/stdgraph/graph-v3](https://github.com/stdgraph/graph-v3) implementation used for this proposal.
candidate 3 (found by 3 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.
candidate 4 (found by 3 of 69 passes): The reference implementation provides backward compatibility to C++20 via an external `expected` library (e.g., `tl``::``expected`).

## vehicle - grade 0.83 (fired in 2 of 23 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
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
  [14] 13 Prior Art                                 2/0/0  -> 0.67
  [15] 14 Alternatives                              1/1/1  -> 1.00
  [16] 15 Feature Test Macro                        0/0/0  -> 0.00
  [17] 16 Freestanding                              0/0/0  -> 0.00
  [18] 17 Language Requirements                     0/0/0  -> 0.00
  [19] 18 Namespaces                                0/0/0  -> 0.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.
candidate 2 (found by 1 of 69 passes): However, the resulting library relies on its own (opaque) data structures for representing graphs and would not be inter-operable with modern C++ approaches to library and application design.

## coordination - grade 0.50 (fired in 1 of 23 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
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
  [19] 18 Namespaces                                1/1/1  -> 1.00
  [20] 19 Notes and Considerations                  0/0/0  -> 0.00
  [21] 20 Issues Status                             0/0/0  -> 0.00
  [22] Acknowledgements                             0/0/0  -> 0.00
  [23] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 69 passes): For these reasons, we recommend separate namespace(s) for the graph functionality.
candidate 2 (found by 1 of 69 passes): there are some domain-specific terms that may clash with existing or future names, such as `degree` and `partition_id`.

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
candidate 2 (found by 2 of 69 passes): Although the prior efforts have served, and do serve, important roles, they do not meet the needs or expectations of modern C++ development.
candidate 3 (found by 1 of 69 passes): We are currently unaware of any existing graph library that meets the same requirements and uses concepts and ranges from C++23.

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
