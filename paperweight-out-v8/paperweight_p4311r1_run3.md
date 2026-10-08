Verdict: Strong (11/14)

The paper gives a reasonably solid account of why a const accessor transformation would be useful and how it connects to existing practice, but its support is uneven: the strongest material concerns motivation, prior art, and implementation experience, while the claims about affected users, interoperability, and the impossibility of a library solution are asserted more than demonstrated.

- The paper clearly establishes the core problem and the need for a public accessor-level interface, not merely an mdspan-level one.
- The prior art and implementation experience are concrete, including a compiler-explorer implementation and a working analogue in Kokkos.
- The discussion of coordination and interoperability leans on the same general statements about generic mdspan libraries without showing how the proposed facility would actually integrate with existing or forthcoming specifications.
- The claim that a library cannot solve the problem is the thinnest part of the paper, since it mainly asserts that user-defined accessors are unknowable without exploring what a non-intrusive or opt-in library mechanism could achieve.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.50/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.50   corroborated 11.00   accumulate 10.67   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.83  coordination 0.83  insufficiency 0.83  implementation 2.00
sample agreement: 62 of 70 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.00 / 11.00 / 10.50   (all 3 samples: 10.50)
headings: h2 9
on threshold: audience
splits: motivation[6] 2/1/2  prior_art[8] 0/1/1  vehicle[5] 1/2/2  vehicle[6] 0/2/1
        coordination[5] 0/0/2  insufficiency[4] 0/1/0  insufficiency[5] 2/2/0
        implementation[5] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     2/1/2  -> 1.67
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 3 of 30 passes): The problem is that if users call this algorithm with `input` that has nonconst element type, and later call the algorithm with `input` that has const element type, `my_algorithm` will be instantiated twice.
candidate 3 (found by 3 of 30 passes): We want to solve this problem: “Given an arbitrary accessor, get the ‘same’ accessor but with const `element_type`.”
candidate 4 (found by 2 of 30 passes): Users should have a public interface for getting a const element type version of an accessor, not just a public interface for getting a const element type version of an mdspan.

## audience - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 2 (found by 1 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project. The same author consulted on how to implement the analogous two-layer scheme for an mdspan-based generic algorithms library, RAPIDS RAFT.

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     2/2/2  -> 2.00
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/1/1  -> 0.67
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It behaves like the `mdspan` analog of `ranges::as_const_view`.
candidate 2 (found by 3 of 30 passes): C++ Standard allocators have “value type rebind.”
candidate 3 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project. The scheme works there because Kokkos’ analog of `mdspan`, `Kokkos::View`, has a way to get a const element type version of a `Kokkos::View`.
candidate 4 (found by 2 of 30 passes): Precedent from [exec] takes Option (1). We specifically refer to P2855R1 (Member customization points for Senders and Receivers), which was merged into P2300R10 and voted into C++26.

## vehicle - grade 1.83 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 1/2/2  -> 1.67
  [6] 5 Design                                     0/2/1  -> 1.00
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 2 (found by 1 of 30 passes): This situation has come up in practice for the authors.
candidate 3 (found by 1 of 30 passes): Users should have a public interface for getting a const element type version of an accessor, not just a public interface for getting a const element type version of an mdspan.
candidate 4 (found by 1 of 30 passes): Users have good reasons to want a const element type version of an accessor directly.

## coordination - grade 0.83 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 0/0/2  -> 0.67
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 1 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 3 (found by 1 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft). It didn’t work because there is no way currently to get a const element type version of an `mdspan`.

## insufficiency - grade 0.83 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/1/0  -> 0.33
  [5] 4 Motivation                                 2/2/0  -> 1.33
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 1 of 30 passes): It didn’t work because there is no way currently to get a const element type version of an `mdspan`.
candidate 3 (found by 1 of 30 passes): We know how to do it for the Standard accessors like `default_accessor` and `aligned_accessor`, but we don’t know how to do it for an arbitrary user-defined accessor.

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 2/1/2  -> 1.67
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             2/2/2  -> 2.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [This Compiler Explorer link](https://godbolt.org/z/o3vfhnonP) has a brief implementation with tests.
candidate 2 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project.
candidate 3 (found by 1 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

-->
