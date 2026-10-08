Verdict: Strong to Excellent (11/14)

The paper offers solid support for the core technical motivation and the existence of a real gap in the standard, but its case thins considerably when it comes to showing who beyond the authors has encountered the problem and why a non-standard library solution is insufficient. The strongest material concerns prior art, customization-point design, and implementation experience, while the weakest concerns the breadth of affected users and the practical failure of library-only workarounds.

- The paper clearly establishes why a const-element accessor transformation matters for generic `mdspan` algorithm libraries and why a customization point is needed.
- The discussion of prior art and alternatives is well grounded, especially the comparison to `ranges::as_const_view` and the allocator-traits separation.
- The implementation experience is credible, with a compiler explorer example and a concrete Kokkos-kernels use case.
- The most glaring omission is the lack of established evidence that a library-only solution would not suffice, since the claim about RAPIDS RAFT is asserted without supporting detail.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 10.67   accumulate 11.50   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.67  coordination 1.50  insufficiency 1.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 11.00 / 11.00 / 11.50   (all 3 samples: 11.17)
headings: h2 9
on threshold: audience, coordination, insufficiency
splits: vehicle[6] 2/1/2  vehicle[7] 1/2/2  implementation[5] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     1/1/1  -> 1.00
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 3 of 30 passes): We want to solve this problem: “Given an arbitrary accessor, get the ‘same’ accessor but with const `element_type`.”
candidate 3 (found by 2 of 30 passes): The problem is that if users call this algorithm with `input` that has nonconst element type, and later call the algorithm with `input` that has const element type, `my_algorithm` will be instantiated twice.
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
candidate 1 (found by 3 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     2/2/2  -> 2.00
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This behaves like the `mdspan` analog of `ranges::as_const_view`.
candidate 2 (found by 2 of 30 passes): Precedent from Ranges takes Option (2); it distinguishes the CPO from the function by namespace.
candidate 3 (found by 2 of 30 passes): One can say that the C++ Standard’s allocators separate “policy” (`allocator_traits`) from the allocator itself.
candidate 4 (found by 1 of 30 passes): The scheme works there because Kokkos’ analog of `mdspan`, `Kokkos::View`, has a way to get a const element type version of a `Kokkos::View`.

## vehicle - grade 1.67 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 1/1/1  -> 1.00
  [6] 5 Design                                     2/1/2  -> 1.67
  [7] 6 Should we generalize to “Accessor ele... 1/2/2  -> 1.67
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This situation has come up in practice for the authors.
candidate 2 (found by 3 of 30 passes): This suggests that we want a customization point so that users can define what “const version of an accessor” means for their own accessor types.
candidate 3 (found by 1 of 30 passes): Precedent from Ranges takes Option (2); it distinguishes the CPO from the function by namespace.
candidate 4 (found by 1 of 30 passes): We know of no precedent for Option (3).

## coordination - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 3 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project. The scheme works there because Kokkos’ analog of mdspan, Kokkos::View, has a way to get a const element type version of a Kokkos::View.

## insufficiency - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft). It didn’t work because there is no way currently to get a const element type version of an `mdspan`.

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 2/2/1  -> 1.67
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             2/2/2  -> 2.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [This Compiler Explorer link](https://godbolt.org/z/n6PoaGhMr) has a brief implementation.
candidate 2 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 3 (found by 1 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project.

-->
