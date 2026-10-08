Verdict: Strong to Excellent (11/14)

The paper gives a reasonably solid account of why a const accessor transformation is needed and why it belongs in the standard rather than in user code, but it leans heavily on a single author’s experience and does not convincingly show that the feature cannot be delivered as a library.

- The strongest support is the concrete, repeated failure of the two-layer scheme in an `mdspan`-based generic algorithms library, which directly motivates standardization.
- The paper also establishes clear precedent in `ranges::as_const_view` and explains why a customization point is necessary for arbitrary user-defined accessors.
- The thinnest part is the claim about who is affected, since the evidence is limited to one author’s work in Kokkos and a consultation, with no broader user or library ecosystem shown.
- The most glaring omission is the case for why a library solution will not do, which is asserted mainly through uncertainty about arbitrary accessors rather than demonstrated with examples that resist library implementation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 11.00   accumulate 11.50   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.83  coordination 1.50  insufficiency 1.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 11.50 / 11.00 / 11.50   (all 3 samples: 11.33)
headings: h2 9
on threshold: audience, coordination, insufficiency
splits: vehicle[5] 2/1/2  vehicle[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 3)
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
candidate 1 (found by 3 of 30 passes): The Standard doesn’t currently have a way to take an arbitrary accessor and get a const element type version of it. This hinders development of generic `mdspan` algorithm libraries.
candidate 2 (found by 3 of 30 passes): The problem is that if users call this algorithm with `input` that has nonconst element type, and later call the algorithm with `input` that has const element type, `my_algorithm` will be instantiated twice.
candidate 3 (found by 3 of 30 passes): We want to solve this problem: “Given an arbitrary accessor, get the ‘same’ accessor but with const `element_type`.”
candidate 4 (found by 2 of 30 passes): Users might want to apply multiple transformations to accessors before creating an mdspan from them.

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

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)
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
candidate 2 (found by 3 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project. The scheme works there because Kokkos’ analog of `mdspan`, `Kokkos::View`, has a way to get a const element type version of a `Kokkos::View`.
candidate 3 (found by 3 of 30 passes): Ranges does this with an enumeration of various possibilities in [range.as.const.overview] 2. There is no customization point to change the behavior of `views::as_const` for user-defined types.
candidate 4 (found by 2 of 30 passes): Precedent from Ranges takes Option (2); it distinguishes the CPO from the function by namespace.

## vehicle - grade 1.83 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Authors                                    0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Summary                                    0/0/0  -> 0.00
  [5] 4 Motivation                                 2/1/2  -> 1.67
  [6] 5 Design                                     0/0/1  -> 0.33
  [7] 6 Should we generalize to “Accessor ele... 2/2/2  -> 2.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This suggests that we want a customization point so that users can define what “const version of an accessor” means for their own accessor types.
candidate 2 (found by 2 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 3 (found by 1 of 30 passes): This situation has come up in practice for the authors.
candidate 4 (found by 1 of 30 passes): We don’t want to force users to define the function for their custom accessors.

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
candidate 2 (found by 2 of 30 passes): This situation has come up in practice for the authors. One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.
candidate 3 (found by 1 of 30 passes): The same author consulted on how to implement the analogous two-layer scheme for an `mdspan`-based generic algorithms library, [RAPIDS RAFT](https://github.com/NVIDIA/raft). It didn’t work because there is no way currently to get a const element type version of an `mdspan`.

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
candidate 1 (found by 2 of 30 passes): We know how to do it for the Standard accessors like `default_accessor` and `aligned_accessor`, but we don’t know how to do it for an arbitrary user-defined accessor.
candidate 2 (found by 1 of 30 passes): Accessors don’t need to have template parameters at all. Even if they do have template parameters, the first template parameter doesn’t have to be the element type.

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
candidate 1 (found by 3 of 30 passes): [This Compiler Explorer link](https://godbolt.org/z/n6PoaGhMr) has a brief implementation.
candidate 2 (found by 2 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the [Kokkos](https://github.com/kokkos/kokkos) project.
candidate 3 (found by 1 of 30 passes): One author developed this two-layer scheme for generic algorithms in the kokkos-kernels subproject of the Kokkos project.

-->
