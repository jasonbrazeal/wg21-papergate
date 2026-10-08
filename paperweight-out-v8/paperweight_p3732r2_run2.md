Verdict: Strong (9/14)

The paper offers a solid foundation for why the proposed numeric algorithms matter and how they relate to existing practice, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who would actually be affected and whether the standard is the only viable venue for the work.

- The strongest support is the concrete implementation experience, including a prototype and partial deployment in oneDPL.
- The paper also clearly establishes the motivating gap in parallel numeric algorithms and the relevant prior art from P2214R2, P1673R13, and MPI.
- The case for why a library solution would not suffice rests mainly on an observation about transform views, without showing that this limitation cannot be addressed outside the standard.
- The most glaring omission is any identification of the affected users or communities, leaving the practical audience for the proposal unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 8.67   accumulate 8.50   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 94 of 98 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.00 / 9.50 / 8.00   (all 3 samples: 8.50)
headings: h2 10
on threshold: coordination, insufficiency
splits: motivation[8] 0/1/0  prior_art[4] 2/1/0  vehicle[6] 0/2/0  vehicle[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 2/2/2  -> 2.00
  [5] 3 Proposal summary                           0/0/0  -> 0.00
  [6] 4 Scope rationale and design  (part 1 of 3)  2/2/2  -> 2.00
  [7] 4 Scope rationale and design  (part 2 of 3)  2/2/2  -> 2.00
  [8] 4 Scope rationale and design  (part 3 of 3)  0/1/0  -> 0.33
  [9] 5 Specifying an identity for reductions a... 2/2/2  -> 2.00
  [10] 5 Specifying an identity for reductions a... 1/1/1  -> 1.00
  [11] 6 Implementation                             0/0/0  -> 0.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Still we are missing `<numeric>` algorithms that are extremely useful for parallelism and important for HPC use cases, like `reduce` and `scan`.
candidate 2 (found by 3 of 42 passes): The situation is different for parallel execution, because more than one accumulator must be initialized.
candidate 3 (found by 3 of 42 passes): It’s important for both performance and functionality that users be able to specify an identity value for parallel reductions.
candidate 4 (found by 2 of 42 passes): Use of `transform_view` and `zip_transform_view` can make it harder for implementations to parallelize `ranges` algorithms.

## audience - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 0/0/0  -> 0.00
  [5] 3 Proposal summary                           0/0/0  -> 0.00
  [6] 4 Scope rationale and design  (part 1 of 3)  0/0/0  -> 0.00
  [7] 4 Scope rationale and design  (part 2 of 3)  0/0/0  -> 0.00
  [8] 4 Scope rationale and design  (part 3 of 3)  0/0/0  -> 0.00
  [9] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [10] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [11] 6 Implementation                             0/0/0  -> 0.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 7 of 14 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 2/1/0  -> 1.00
  [5] 3 Proposal summary                           1/1/1  -> 1.00
  [6] 4 Scope rationale and design  (part 1 of 3)  2/2/2  -> 2.00
  [7] 4 Scope rationale and design  (part 2 of 3)  2/2/2  -> 2.00
  [8] 4 Scope rationale and design  (part 3 of 3)  2/2/2  -> 2.00
  [9] 5 Specifying an identity for reductions a... 2/2/2  -> 2.00
  [10] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [11] 6 Implementation                             2/2/2  -> 2.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [[P2214R2]](https://wg21.link/p2214r2) points out that `ranges::transform_inclusive_scan(r, o, f, g)` can be rewritten as `ranges::inclusive_scan(r | views::transform(g), o, f)`.
candidate 2 (found by 3 of 42 passes): Our approach combines the syntactic constraints used for the `fold_*` family of algorithms, with the semantic approach of [[P1673R13]] and the C++17 parallel numeric algorithms.
candidate 3 (found by 3 of 42 passes): MPI’s reductions compute the analog of `reduce_first`. Users have no way to specify either an initial value or an identity for their custom operations.
candidate 4 (found by 3 of 42 passes): The oneAPI DPC++ library ([oneDPL](https://github.com/uxlfoundation/oneDPL)) has a partial deployment experience. The implementation is done as experimental with the following deviations from this proposal:

## vehicle - grade 0.50 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 0/0/0  -> 0.00
  [5] 3 Proposal summary                           0/0/0  -> 0.00
  [6] 4 Scope rationale and design  (part 1 of 3)  0/2/0  -> 0.67
  [7] 4 Scope rationale and design  (part 2 of 3)  0/0/0  -> 0.00
  [8] 4 Scope rationale and design  (part 3 of 3)  0/0/0  -> 0.00
  [9] 5 Specifying an identity for reductions a... 0/1/0  -> 0.33
  [10] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [11] 6 Implementation                             0/0/0  -> 0.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The problem is *`movable-box`*. As [[range.move.wrap]](https://wg21.link/range.move.wrap) 1.3 explains, since `copyable<decltype(f2)>` is not modeled, *`movable-box`*`<decltype(f2)>` provides a nontrivial, not deleted copy assignment operator.
candidate 2 (found by 1 of 42 passes): Other parallel programming models provide all combinations of design options.

## coordination - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 0/0/0  -> 0.00
  [5] 3 Proposal summary                           0/0/0  -> 0.00
  [6] 4 Scope rationale and design  (part 1 of 3)  0/0/0  -> 0.00
  [7] 4 Scope rationale and design  (part 2 of 3)  0/0/0  -> 0.00
  [8] 4 Scope rationale and design  (part 3 of 3)  0/0/0  -> 0.00
  [9] 5 Specifying an identity for reductions a... 2/2/2  -> 2.00
  [10] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [11] 6 Implementation                             0/0/0  -> 0.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Other parallel programming models provide all combinations of design options. Some compute only `reduce_first`, some only `reduce`, and some compute both.

## insufficiency - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 0/0/0  -> 0.00
  [5] 3 Proposal summary                           0/0/0  -> 0.00
  [6] 4 Scope rationale and design  (part 1 of 3)  2/2/2  -> 2.00
  [7] 4 Scope rationale and design  (part 2 of 3)  0/0/0  -> 0.00
  [8] 4 Scope rationale and design  (part 3 of 3)  0/0/0  -> 0.00
  [9] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [10] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [11] 6 Implementation                             0/0/0  -> 0.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Use of `transform_view` and `zip_transform_view` can make it harder for implementations to parallelize `ranges` algorithms.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Revision history                           0/0/0  -> 0.00
  [4] 2 Motivation                                 0/0/0  -> 0.00
  [5] 3 Proposal summary                           1/1/1  -> 1.00
  [6] 4 Scope rationale and design  (part 1 of 3)  2/2/2  -> 2.00
  [7] 4 Scope rationale and design  (part 2 of 3)  0/0/0  -> 0.00
  [8] 4 Scope rationale and design  (part 3 of 3)  0/0/0  -> 0.00
  [9] 5 Specifying an identity for reductions a... 2/2/2  -> 2.00
  [10] 5 Specifying an identity for reductions a... 0/0/0  -> 0.00
  [11] 6 Implementation                             2/2/2  -> 2.00
  [12] 7 Wording                                    0/0/0  -> 0.00
  [13] 8 Acknowledgements                           0/0/0  -> 0.00
  [14] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The implementation experience is work-in-progress.
candidate 2 (found by 3 of 42 passes): [Here is a prototype](https://godbolt.org/z/hYq16PTob) that shows three different designs, including this one.
candidate 3 (found by 3 of 42 passes): The oneAPI DPC++ library ([oneDPL](https://github.com/uxlfoundation/oneDPL)) has a partial deployment experience.
candidate 4 (found by 2 of 42 passes): Here is an example (available on [Compiler Explorer](https://godbolt.org/z/vYnzGd3js) as well).

-->
