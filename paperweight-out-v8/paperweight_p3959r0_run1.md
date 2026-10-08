Verdict: Strong (8/14)

The paper gives a reasonably concrete account of the problem and of existing practice, but it leaves the standardization rationale incomplete in two important places: it does not explain why the change belongs in the standard rather than in implementations, and it does not show why a library-level solution would be insufficient. The strongest material concerns compatibility with existing `mdspan` implementations and the inherited design intent from `Kokkos::View`, while the weakest concerns the affected user population and the necessity of normative action.

- The paper establishes meaningful implementation experience by showing that both the reference `mdspan` implementation and libc++ already accept the proposed behavior without enforcing the contested preconditions.
- The paper establishes relevant prior art and coordination concerns by tracing the restriction to `Kokkos::View` and noting the common Python convention of permitting zero strides for zero extents.
- The paper claims a broad affected audience in Python-driven scientific computing but does not establish that this audience actually encounters the precondition violation in practice.
- The paper does not establish why the standard should change, nor why a library-level remedy would not address the issue.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 7.67   accumulate 8.00   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 1.50  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.50 / 7.50 / 8.00   (all 3 samples: 8.00)
headings: h2 8
on threshold: coordination, implementation
splits: motivation[5] 1/2/2  audience[6] 1/0/1  audience[8] 1/0/0  prior_art[8] 1/1/2
        implementation[8] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Design intent of layoutstride              1/2/2  -> 1.67
  [6] 5 Motivation                                 2/2/2  -> 2.00
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This change has two benefits. First, it would let users convert any empty `layout_left::mapping` or `layout_right::mapping` to `layout_stride::mapping`. Second, it would prevent unnecessary precondition violations when creating `mdspan` objects that view multidimensional arrays created in Python or other languages.
candidate 2 (found by 2 of 27 passes): Conversion from these `layout_right` or `layout_left` `mdspan` to `layout_stride` `mdspan` violates the preconditions of `layout_stride::mapping`’s converting constructor, specifically [mdspan.layout.stride.cons] 7.2, that requires all strides to be positive.
candidate 3 (found by 1 of 27 passes): These restrictions were always part of `layout_stride`’s design.
candidate 4 (found by 1 of 27 passes): The design intent of `layout_stride` is to support the following use cases.

## audience - grade 0.50 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Design intent of layoutstride              0/0/0  -> 0.00
  [6] 5 Motivation                                 1/0/1  -> 0.67
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             1/0/0  -> 0.33
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The past two decades have seen ever-increasing use of Python for data science, scientific computations, machine learning, and other domains that involve computations on multidimensional arrays.
candidate 2 (found by 1 of 27 passes): both the reference `mdspan` implementation and libc++’s implementation actually implement this proposal

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Design intent of layoutstride              2/2/2  -> 2.00
  [6] 5 Motivation                                 2/2/2  -> 2.00
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             1/1/2  -> 1.33
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This may affect use of some libraries like the [BLAS](https://www.netlib.org/blas/) and [LAPACK](https://www.netlib.org/lapack/) that forbid a zero stride, even if the corresponding matrix dimension is zero.
candidate 2 (found by 3 of 27 passes): It’s something `mdspan`’s layouts inherited from `Kokkos::View`.
candidate 3 (found by 2 of 27 passes): All these multidimensional array formats claim to provide what they call “strided” indexing. However, all of them support much more general layouts than what `layout_stride` supports, for three reasons.
candidate 4 (found by 2 of 27 passes): both the reference `mdspan` implementation and libc++’s implementation actually implement this proposal by not checking the preconditions and by producing a valid `layout_stride::mapping`.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Design intent of layoutstride              0/0/0  -> 0.00
  [6] 5 Motivation                                 0/0/0  -> 0.00
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               1/1/1  -> 1.00
  [5] 4 Design intent of layoutstride              0/0/0  -> 0.00
  [6] 5 Motivation                                 2/2/2  -> 2.00
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This change would relax preconditions of three existing `layout_stride::mapping` constructors.
candidate 2 (found by 1 of 27 passes): These reasons have motivated Python developers to define common binary interfaces for multidimensional array data.
candidate 3 (found by 1 of 27 passes): Many Python libraries for these domains have an implementation strategy of calling existing Fortran, C, or C++ libraries (such as the BLAS) with multidimensional arrays that are created and managed by Python code.
candidate 4 (found by 1 of 27 passes): Python multidimensional array formats have a common convention to permit zero strides for zero extents.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Design intent of layoutstride              0/0/0  -> 0.00
  [6] 5 Motivation                                 0/0/0  -> 0.00
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Design intent of layoutstride              0/0/0  -> 0.00
  [6] 5 Motivation                                 2/2/2  -> 2.00
  [7] 6 Relaxing the precondition does not viol... 0/0/0  -> 0.00
  [8] 7 Implementation                             2/1/1  -> 1.33
  [9] 8 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): [This Compiler Explorer link](https://godbolt.org/z/3Thfrb1W9) demonstrates that with both implementations.
candidate 2 (found by 3 of 27 passes): both the reference `mdspan` implementation and libc++’s implementation actually implement this proposal by not checking the preconditions and by producing a valid `layout_stride::mapping`.

-->
