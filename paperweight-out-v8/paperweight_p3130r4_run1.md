Verdict: Adequate (4/14)

The paper offers only a thin, largely asserted case for standardization: most of its central claims are gestured at rather than demonstrated, and several essential questions are left entirely unaddressed. The strongest material concerns the existence of a reference implementation, but even that is undercut by repeated admissions that parts of the proposed interface are not yet implemented.

- The paper’s most concrete support is its acknowledgment of a working prototype, though several specified functions and overloads are explicitly missing from it.
- The rationale for a standard library facility leans on an analogy to STL algorithms, but the paper does not show that the same benefits would follow here.
- The discussion of affected users and the insufficiency of a non-standard library is absent, leaving the audience and the necessity of standardization unclear.
- The paper does not establish who would be affected by the proposal, which is the most glaring omission in its case for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 5 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 4.33   accumulate 5.17   max 4.67

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.00  vehicle 0.33  coordination 0.33  insufficiency 0.00  implementation 1.00
sample agreement: 54 of 63 section-criterion pairs unanimous (86%)
single-sample totals would have been: 3.50 / 4.50 / 3.50   (all 3 samples: 3.83)
headings: h2 7
on threshold: none
splits: motivation[5] 1/2/1  motivation[7] 1/1/0  prior_art[3] 0/1/0  prior_art[7] 1/1/0
        vehicle[4] 1/1/0  coordination[4] 0/1/1  implementation[3] 1/0/0
        implementation[5] 1/1/0  implementation[6] 0/1/0
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 4 Graph Container Interface                  1/1/1  -> 1.00
  [5] 5 Adjacency List Interface  (part 1 of 2)    1/2/1  -> 1.33
  [6] 5 Adjacency List Interface  (part 2 of 2)    0/0/0  -> 0.00
  [7] 6 Edgelist Interface                         1/1/0  -> 0.67
  [8] 7 Using Existing Data Structures             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This achieves the same goals as the STL, where algorithms can be used on any container that meets the requirements of the algorithm.
candidate 2 (found by 2 of 27 passes): Exposing raw iterators directly would require concepts, algorithms, and user code to handle each storage strategy separately.
candidate 3 (found by 2 of 27 passes): an edge list is a flat range of `(``source``,` `target` `[,` `value``])` tuples suited to edge-centric algorithms such as Kruskal’s MST or bulk construction.
candidate 4 (found by 1 of 27 passes): Graph containers may store vertices and edges in very different data structures: a `vector`-based adjacency list uses integer indices as vertex identifiers while a `map`-based graph uses the map key.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 4 Graph Container Interface                  0/0/0  -> 0.00
  [5] 5 Adjacency List Interface  (part 1 of 2)    0/0/0  -> 0.00
  [6] 5 Adjacency List Interface  (part 2 of 2)    0/0/0  -> 0.00
  [7] 6 Edgelist Interface                         0/0/0  -> 0.00
  [8] 7 Using Existing Data Structures             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 7 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            1/1/1  -> 1.00
  [3] 2 Revision History                           0/1/0  -> 0.33
  [4] 4 Graph Container Interface                  1/1/1  -> 1.00
  [5] 5 Adjacency List Interface  (part 1 of 2)    1/1/1  -> 1.00
  [6] 5 Adjacency List Interface  (part 2 of 2)    1/1/1  -> 1.00
  [7] 6 Edgelist Interface                         1/1/0  -> 0.67
  [8] 7 Using Existing Data Structures             1/1/1  -> 1.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It also discusses how to use containers in the standard library to define a graph, and how to adapt existing graph data structures.
candidate 2 (found by 3 of 27 passes): This achieves the same goals as the STL, where algorithms can be used on any container that meets the requirements of the algorithm.
candidate 3 (found by 3 of 27 passes): There is precedent for this choice in the `sized_range` concept.
candidate 4 (found by 3 of 27 passes): Supporting multiple types can be addressed in different ways using C++ features.

## vehicle - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 4 Graph Container Interface                  1/1/0  -> 0.67
  [5] 5 Adjacency List Interface  (part 1 of 2)    0/0/0  -> 0.00
  [6] 5 Adjacency List Interface  (part 2 of 2)    0/0/0  -> 0.00
  [7] 6 Edgelist Interface                         0/0/0  -> 0.00
  [8] 7 Using Existing Data Structures             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This achieves the same goals as the STL, where algorithms can be used on any container that meets the requirements of the algorithm.

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 4 Graph Container Interface                  0/1/1  -> 0.67
  [5] 5 Adjacency List Interface  (part 1 of 2)    0/0/0  -> 0.00
  [6] 5 Adjacency List Interface  (part 2 of 2)    0/0/0  -> 0.00
  [7] 6 Edgelist Interface                         0/0/0  -> 0.00
  [8] 7 Using Existing Data Structures             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): They may be overridden for external adjacency list data structures to enable the use of algorithms on those data structures.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 4 Graph Container Interface                  0/0/0  -> 0.00
  [5] 5 Adjacency List Interface  (part 1 of 2)    0/0/0  -> 0.00
  [6] 5 Adjacency List Interface  (part 2 of 2)    0/0/0  -> 0.00
  [7] 6 Edgelist Interface                         0/0/0  -> 0.00
  [8] 7 Using Existing Data Structures             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 4 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Getting Started                            0/0/0  -> 0.00
  [3] 2 Revision History                           1/0/0  -> 0.33
  [4] 4 Graph Container Interface                  0/0/0  -> 0.00
  [5] 5 Adjacency List Interface  (part 1 of 2)    1/1/0  -> 0.67
  [6] 5 Adjacency List Interface  (part 2 of 2)    0/1/0  -> 0.33
  [7] 6 Edgelist Interface                         1/1/1  -> 1.00
  [8] 7 Using Existing Data Structures             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The `contains_edge``(``el``,``uid``,``vid``)`, `num_edges``(``el``)` and `has_edges``(``el``)` functions are not yet in the reference implementation; the `source_id`, `target_id` and `edge_value` CPOs are available now.
candidate 2 (found by 2 of 27 passes): The id form `partition_id``(``g``,``uid``)` — the convenience overload that would resolve to `partition_id``(``g``,*``find_vertex``(``g` `,``uid``))` — is not yet in the reference implementation.
candidate 3 (found by 1 of 27 passes): Ground the descriptor types introduced in r3 with concrete specifications backed by a working prototype
candidate 4 (found by 1 of 27 passes): These partition-filtered `out_edges` overloads are not yet in the reference implementation.

-->
