Verdict: Strong to Excellent (11/14)

The paper offers solid support for the core motivation, the existence of viable prior art, and the need for a standard mechanism rather than a library-only solution. The thinnest parts are the claims about who is affected and how the proposal coordinates with existing practice, which rest on the authors’ own projects and assertions rather than broader evidence.

- The strongest support is the concrete implementation experience, including a Compiler Explorer link with tests and a working two-layer scheme in Kokkos.
- The paper clearly establishes why the standard is the right venue, given that custom accessors can represent memory spaces inaccessible to ordinary C++ code.
- The prior art and alternatives section is well grounded, with explicit references to `ranges::as_const_view`, CCCL, Kokkos, and the exec proposal P2855R1.
- The most glaring omission is the lack of established evidence for who is affected beyond the authors’ own kokkos-kernels work and a consultation on RAPIDS RAFT.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 11.00   accumulate 11.17   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.83  coordination 1.17  insufficiency 1.00  implementation 2.00
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 11.50 / 11.50 / 10.50   (all 3 samples: 11.00)
headings: h2 9
on threshold: audience, insufficiency
splits: prior_art[7] 0/0/2  vehicle[5] 1/2/2  vehicle[7] 2/1/2  coordination[5] 2/2/0
        implementation[5] 2/2/1
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
candidate 2 (found by 3 of 30 passes): Multidimensional algorithms make this problem worse because they have combinatorially more possibilities of equivalent input resulting in different instantiations.
candidate 3 (found by 3 of 30 passes): Users have good reasons to want a const element type version of an accessor directly.
candidate 4 (found by 3 of 30 passes): We want to solve this problem: “Given an arbitrary accessor, get the ‘same’ accessor but with const `element_type`.”

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
candidate 2 (found by 1 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/2  -> 2.00
  [6] 5 Design                                     2/2/2  -> 2.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/2  -> 0.67
  [8] 7 Implementation                             1/1/1  -> 1.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): It behaves like the `mdspan` analog of `ranges::as_const_view`.
candidate 2 (found by 3 of 30 passes): One coauthor has an implementation of an earlier draft of this proposal in a branch of the [CCCL](https://github.com/NVIDIA/cccl/) repository.
candidate 3 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project. The scheme works there because Kokkos’ analog of `mdspan`, `Kokkos::View`, has a way to get a const element type version of a `Kokkos::View`.
candidate 4 (found by 2 of 30 passes): Precedent from [exec] takes Option (1). We specifically refer to P2855R1 (Member customization points for Senders and Receivers), which was merged into P2300R10 and voted into C++26.

## vehicle - grade 1.83 (fired in 3 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 1/2/2  -> 1.67
  [6] 5 Design                                     2/2/2  -> 2.00
  [7] 6 Should we generalize to “Accessor ele... 2/1/2  -> 1.67
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 2 (found by 2 of 30 passes): Accessors introduce to the C++ Standard the possibility of separate “memory” spaces (where “memory” is in quotes because actual memory need not be involved) that are inaccessible to ordinary C++ code, except through the accessor’s `access` function.
candidate 3 (found by 1 of 30 passes): This situation has come up in practice for the authors.
candidate 4 (found by 1 of 30 passes): The `mdspan` design aims to make defining custom accessors simple. (That’s why it doesn’t ask users to define custom iterators, for example.)

## coordination - grade 1.17 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    1/1/1  -> 1.00
  [5] 4 Motivation                                 2/2/0  -> 1.33
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Should we generalize to “Accessor ele... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 2 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 3 (found by 1 of 30 passes): This hinders development of generic `mdspan` algorithm libraries.

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
candidate 1 (found by 1 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft). It didn’t work because there is no way currently to get a const element type version of an `mdspan`.
candidate 2 (found by 1 of 30 passes): We do NOT know how to (2). We know how to do it for the Standard accessors like `default_accessor` and `aligned_accessor`, but we don’t know how to do it for an arbitrary user-defined accessor.
candidate 3 (found by 1 of 30 passes): It didn’t work because there is no way currently to get a const element type version of an `mdspan`.

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
candidate 1 (found by 3 of 30 passes): [This Compiler Explorer link](https://godbolt.org/z/o3vfhnonP) has a brief implementation with tests.
candidate 2 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project.
candidate 3 (found by 1 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

-->
