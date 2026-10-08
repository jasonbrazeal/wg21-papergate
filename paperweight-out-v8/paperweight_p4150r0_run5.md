Verdict: Strong (10/14)

The paper gives a reasonably solid account of why multidimensional iteration is awkward through existing Ranges facilities and points to real implementation experience, but it leaves important parts of the standardization case asserted rather than demonstrated. The thinnest areas concern who specifically benefits and whether the functionality truly cannot be delivered as a library, since those claims are made without supporting evidence.

- The strongest support is the concrete implementation experience, including a pull request and substantial existing code in Kokkos.
- The paper also establishes the motivating problem and the existence of prior art in Kokkos and NVIDIA CUB.
- The case for standardization over a library solution is only claimed, with little demonstration that the optimization and syntax goals cannot be met otherwise.
- The most glaring omission is any identification of the affected users or communities, leaving the proposal’s audience and impact unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 6 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 10.00   accumulate 10.17   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 2.00  coordination 1.00  insufficiency 1.17  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.50 / 10.00 / 10.00   (all 3 samples: 10.17)
headings: h2 8
on threshold: coordination, insufficiency, implementation
splits: prior_art[6] 0/2/0  insufficiency[4] 1/0/0  implementation[5] 0/1/1
        implementation[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Using Ranges to iterate over an `mdspan` is verbose and hard to write.
candidate 2 (found by 3 of 27 passes): Current practice limits how users can specify or hint at iteration order.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  0/0/0  -> 0.00
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         2/2/2  -> 2.00
  [6] 5 Design Considerations                      0/2/0  -> 0.67
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): C++ also has library-based solutions. The Kokkos performance-portability framework provides multidimensional loop iteration via `MDRangePolicy` overloads of its `parallel_for` algorithm [[Kokkos]](https://kokkos.org/kokkos-core-wiki/API/core/policies/MDRangePolicy.html).
candidate 2 (found by 3 of 27 passes): While the NVIDIA CUB library [[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) only permits `layout_left` and `layout_right`, we plan on allowing any arbitrary layouts including custom layouts.
candidate 3 (found by 1 of 27 passes): CUB[[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) provides two overload sets: one taking a layout mapping and iterating over its extents, and one taking just an `extents` object.

## vehicle - grade 2.00 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Ranges makes views opaque. This loses multidimensional information that could be used to optimize.
candidate 2 (found by 1 of 27 passes): Using Ranges to iterate over an `mdspan` is verbose and hard to write.
candidate 3 (found by 1 of 27 passes): Asking users to do this would defeat two key design features of `mdspan`: genericity over the layout and accessor, and the familiar multidimensional array syntax.
candidate 4 (found by 1 of 27 passes): Both compiler extensions and library solutions give users ways to control iteration order.

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Many non-Standard C++ approaches loop over multidimensional indices. Compiler extensions like OpenACC and OpenMP let the user annotate their nested for loops.

## insufficiency - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  1/0/0  -> 0.33
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
  [5] 4 Proposed Interface                         0/1/1  -> 0.67
  [6] 5 Design Considerations                      0/0/1  -> 0.33
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It comes from a [pull request here](https://github.com/kokkos/mdspan/pull/247).
candidate 2 (found by 2 of 27 passes): While the NVIDIA CUB library [[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) only permits `layout_left` and `layout_right`, we plan on allowing any arbitrary layouts including custom layouts.
candidate 3 (found by 1 of 27 passes): They amount to several thousand lines of code in the Kokkos library, for example.

-->
