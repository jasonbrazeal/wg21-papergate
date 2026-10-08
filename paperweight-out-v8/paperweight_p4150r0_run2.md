Verdict: Strong (9/14)

The paper offers substantial support for its standardization case in the areas of motivation, prior art, implementation experience, and the need for a standard facility, but it leaves the affected audience unestablished and only gestures at coordination and interoperability.

- The strongest support comes from the paper’s demonstration that existing practice and library-based solutions already provide multidimensional iteration control, yet C++ ranges lose the layout information needed to optimize such operations.
- The paper also convincingly shows why a library-only solution would defeat `mdspan`’s core design goals and why users cannot reasonably be expected to compute pointer offsets by hand.
- The thinnest part of the case is the absence of any established description of who is affected by the lack of standardization.
- The claim about coordination and interoperability with non-Standard C++ approaches is asserted but not backed by concrete examples or discussion of how standardization would align with those efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 7.33   accumulate 9.33   max 10.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 1.67  coordination 0.17  insufficiency 1.50  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.50 / 9.50 / 9.50   (all 3 samples: 9.00)
headings: h2 8
on threshold: motivation, vehicle, insufficiency, implementation
splits: motivation[3] 0/1/0  motivation[4] 0/2/2  motivation[5] 1/1/0  vehicle[4] 0/2/2
        coordination[4] 1/0/0  implementation[5] 1/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/1/0  -> 0.33
  [4] 3 Motivation and Background                  0/2/2  -> 1.33
  [5] 4 Proposed Interface                         1/1/0  -> 0.67
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Current practice limits how users can specify or hint at iteration order.
candidate 2 (found by 2 of 27 passes): Trying to express this as an operation over elements would require computing pointer offsets by hand.
candidate 3 (found by 2 of 27 passes): This ensures that the implementation always gets an iteration order hint.
candidate 4 (found by 1 of 27 passes): std::ranges::for_each( std::execution::par_unseq, std::views::cartesian_product( std::views::indices(A.extent(0)), std::views::indices(A.extent(1))), [=] (auto idx) { auto [i, j] = idx; B[j, i] = A[i, j]; });

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
candidate 2 (found by 2 of 27 passes): The Kokkos performance-portability framework provides multidimensional loop iteration via `MDRangePolicy` overloads of its `parallel_for` algorithm [[Kokkos]](https://kokkos.org/kokkos-core-wiki/API/core/policies/MDRangePolicy.html).
candidate 3 (found by 2 of 27 passes): CUB [[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) only permits `layout_left` and `layout_right`. OpenACC and OpenMP permit permutation of loop index orders and have tiling options, but do not take arbitrary layouts.
candidate 4 (found by 1 of 27 passes): C++ also has library-based solutions. The Kokkos performance-portability framework provides multidimensional loop iteration via `MDRangePolicy` overloads of its `parallel_for` algorithm [[Kokkos]](https://kokkos.org/kokkos-core-wiki/API/core/policies/MDRangePolicy.html).

## vehicle - grade 1.67 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  0/2/2  -> 1.33
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Ranges makes views opaque. This loses multidimensional information that could be used to optimize.
candidate 2 (found by 2 of 27 passes): Both compiler extensions and library solutions give users ways to control iteration order.

## coordination - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  1/0/0  -> 0.33
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Many non-Standard C++ approaches loop over multidimensional indices.

## insufficiency - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  1/1/1  -> 1.00
  [5] 4 Proposed Interface                         0/0/0  -> 0.00
  [6] 5 Design Considerations                      2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Ranges makes views opaque. This loses multidimensional information that could be used to optimize.
candidate 2 (found by 1 of 27 passes): Asking users to do this would defeat two key design features of `mdspan`: genericity over the layout and accessor, and the familiar multidimensional array syntax.
candidate 3 (found by 1 of 27 passes): Asking users to do this would defeat two key design features of `mdspan`: 1. genericity over the layout and accessor, and 2. the familiar multidimensional array syntax.
candidate 4 (found by 1 of 27 passes): Trying to express this as an operation over elements would require computing pointer offsets by hand.

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation and Background                  2/2/2  -> 2.00
  [5] 4 Proposed Interface                         1/0/1  -> 0.67
  [6] 5 Design Considerations                      1/1/1  -> 1.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It comes from a [pull request here](https://github.com/kokkos/mdspan/pull/247).
candidate 2 (found by 3 of 27 passes): They amount to several thousand lines of code in the Kokkos library, for example.
candidate 3 (found by 2 of 27 passes): While the NVIDIA CUB library [[CUB]](https://nvidia.github.io/cccl/unstable/cub/api/structcub_1_1DeviceFor.html) only permits `layout_left` and `layout_right`, we plan on allowing any arbitrary layouts including custom layouts.

-->
