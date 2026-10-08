Verdict: Strong to Excellent (11/14)

The paper offers solid support for the existence of a real gap in the standard and for the general shape of a customization-point solution, but it leans heavily on a single author’s experience and does not fully establish that the problem cannot be solved adequately by a library outside the standard.

- The strongest support is the demonstrated absence of any current standard mechanism for deriving a const-element accessor, which directly blocks generic `mdspan` algorithm development.
- The proposal also benefits from clear precedent in `ranges::as_const_view`, sender/receiver customization points, and allocator policy separation.
- The thinnest part is the claim that a library solution will not do, since the paper asserts this mainly through one consulting experience rather than a broader demonstration of why non-standard machinery is insufficient.
- The affected-user case is also underdeveloped, resting on a single author’s work in Kokkos kernels without evidence of wider demand or independent validation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 10.00   accumulate 11.17   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.67  coordination 1.50  insufficiency 1.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 11.50 / 10.50 / 11.50   (all 3 samples: 11.17)
headings: h2 9
on threshold: audience, vehicle, coordination, insufficiency
splits: motivation[6] 1/1/2  prior_art[8] 1/0/0  vehicle[5] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     1/1/2  -> 1.33
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 3 of 30 passes): Users should have a public interface for getting a const element type version of an accessor, not just a public interface for getting a const element type version of an mdspan.
candidate 3 (found by 3 of 30 passes): We want to solve this problem: “Given an arbitrary accessor, get the ‘same’ accessor but with const `element_type`.”
candidate 4 (found by 2 of 30 passes): Our experience is that if the algorithm is sufficiently complicated, then this reduces code size and compilation cost.

## audience - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
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

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     2/2/2  -> 2.00
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             1/0/0  -> 0.33
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This behaves like the `mdspan` analog of `ranges::as_const_view`.
candidate 2 (found by 3 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project.
candidate 3 (found by 3 of 30 passes): Precedent from [exec] takes Option (1). We specifically refer to P2855R1 (Member customization points for Senders and Receivers), which was merged into P2300R10 and voted into C++26.
candidate 4 (found by 3 of 30 passes): One can say that the C++ Standard’s allocators separate “policy” (`allocator_traits`) from the allocator itself.

## vehicle - grade 1.67 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 2/0/2  -> 1.33
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This suggests that we want a customization point so that users can define what “const version of an accessor” means for their own accessor types.
candidate 2 (found by 2 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

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
candidate 1 (found by 3 of 30 passes): This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 1 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft). It didn’t work because there is no way currently to get a const element type version of an `mdspan`.
candidate 3 (found by 1 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft).
candidate 4 (found by 1 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

## insufficiency - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 30 passes): It didn’t work because there is no way currently to get a const element type version of an `mdspan`.
candidate 2 (found by 1 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft). It didn’t work because there is no way currently to get a const element type version of an `mdspan`.

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             2/2/2  -> 2.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project.
candidate 2 (found by 3 of 30 passes): [This Compiler Explorer link](https://godbolt.org/z/n6PoaGhMr) has a brief implementation.

-->
