Verdict: Strong (9/14)

The paper gives a workable account of why an index-based loop algorithm would be useful and shows that comparable ideas already exist in practice, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who would actually be served, why this belongs in the standard rather than a library, and how it would coordinate with existing compiler-driven loop annotations.

- The strongest support is the concrete prior art in CUB, Kokkos, and `views::indices`, along with implementation experience from a real pull request and substantial existing library code.
- The paper clearly establishes the motivating problem: expressing index-based iteration over multidimensional data is awkward with current element-wise or range-based tools.
- The least developed part is the claim that a library solution would not suffice, since the paper repeats the concern about losing multidimensional information but does not establish that this cannot be addressed outside the standard.
- The paper also does not establish who is affected beyond a general reference to “many non-Standard C++ approaches,” leaving the breadth and urgency of the need unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.33   accumulate 9.17   max 11.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.17  coordination 0.67  insufficiency 1.17  implementation 2.00
sample agreement: 55 of 63 section-criterion pairs unanimous (87%)
single-sample totals would have been: 9.00 / 9.50 / 9.00   (all 3 samples: 9.17)
headings: h2 8
on threshold: vehicle, insufficiency, implementation
splits: motivation[5] 0/1/0  audience[4] 0/1/0  vehicle[4] 0/1/1  vehicle[6] 2/2/1
        coordination[4] 2/0/2  insufficiency[4] 0/1/0  implementation[5] 0/0/1
        implementation[6] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         0/1/0  -> 0.33
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Trying to express this as an operation over elements would require computing pointer offsets by hand.
candidate 2 (found by 3 of 27 passes): Current practice limits how users can specify or hint at iteration order.
candidate 3 (found by 1 of 27 passes): We would like to propose `for_each_index`, an algorithm that enables single and multi-dimensional index-based loops.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  0/1/0  -> 0.33
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Many non-Standard C++ approaches loop over multidimensional indices.

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         2/2/2  -> 2.00
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): While the NVIDIA CUB library [[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) only permits `layout_left` and `layout_right`, we plan on allowing any arbitrary layouts including custom layouts.
candidate 2 (found by 3 of 27 passes): CUB[[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) provides two overload sets: one taking a layout mapping and iterating over its extents, and one taking just an `extents` object.
candidate 3 (found by 2 of 27 passes): [[P3060R3]](https://wg21.link/p3060r3) introduced the `views::indices` feature in C++26.
candidate 4 (found by 1 of 27 passes): C++ also has library-based solutions. The Kokkos performance-portability framework provides multidimensional loop iteration via `MDRangePolicy` overloads of its `parallel_for` algorithm [[Kokkos]](https://kokkos.org/kokkos-core-wiki/API/core/policies/MDRangePolicy.html).

## vehicle - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  0/1/1  -> 0.67
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      2/2/1  -> 1.67
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Using Ranges to iterate over an `mdspan` is verbose and hard to write.
candidate 2 (found by 1 of 27 passes): C++23’s introduction of `mdspan` ([[P0009R18]](https://wg21.link/p0009r18)) opens the question of how to invoke a callable on each element of a given `mdspan`.
candidate 3 (found by 1 of 27 passes): Ranges makes views opaque. This loses multidimensional information that could be used to optimize.
candidate 4 (found by 1 of 27 passes): Ranges flatten out multidimensional information. This hinders checking for error cases like attempting to do `std::ranges::copy` from a 2 x 3 x 5 `mdspan` to a 6 x 5 `mdspan`.

## coordination - grade 0.67 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/0/2  -> 1.33
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Many non-Standard C++ approaches loop over multidimensional indices. Compiler extensions like [[OpenACC]](https://www.openacc.org/) and [[OpenMP]](https://www.openmp.org/) let the user annotate their nested `for` loops.
candidate 2 (found by 1 of 27 passes): Many non-Standard C++ approaches loop over multidimensional indices. Compiler extensions like OpenACC and OpenMP let the user annotate their nested `for` loops.

## insufficiency - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  0/1/0  -> 0.33
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Ranges makes views opaque. This loses multidimensional information that could be used to optimize.
candidate 2 (found by 1 of 27 passes): Trying to express this as an operation over elements would require computing pointer offsets by hand.

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         0/0/1  -> 0.33
  [6] 5 Design Considerations                      0/1/1  -> 0.67
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It comes from a [pull request here](https://github.com/kokkos/mdspan/pull/247).
candidate 2 (found by 2 of 27 passes): They amount to several thousand lines of code in the Kokkos library, for example.
candidate 3 (found by 1 of 27 passes): While the NVIDIA CUB library [[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) only permits `layout_left` and `layout_right`, we plan on allowing any arbitrary layouts including custom layouts.

-->
