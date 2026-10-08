Verdict: Adequate (6/14)

The paper offers a solid foundation for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several essential justifications largely unaddressed. The thinnest support concerns the people affected by the problem, the reason a standard library facility is necessary, and how the proposal would coordinate with existing or planned standard components.

- The paper clearly establishes why copy-on-write value semantics matter for performance-sensitive code that copies frequently but mutates rarely.
- It credibly situates the proposal against existing practice, including `std::indirect`, `shared_ptr<const T>`, and Adobe’s `stlab` implementation.
- The argument that this cannot be done adequately as a library is asserted but not demonstrated, leaving a central standardization question open.
- The paper does not establish who is affected by the absence of a standard `copy_on_write`, nor why the standard itself—rather than a widely available library—is the right home for the facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.50 / 6.00 / 6.00   (all 3 samples: 6.17)
headings: h2 12
on threshold: motivation, implementation
splits: motivation[9] 2/1/1  prior_art[4] 0/0/1  implementation[6] 1/0/0
## END SUMMARY

## motivation - grade 1.67 (fired in 5 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design Requirements                          1/1/1  -> 1.00
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           2/1/1  -> 1.33
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        1/1/1  -> 1.00
candidate 1 (found by 3 of 39 passes): This gives efficient value semantics: copying is O(1) regardless of the size or complexity of `T`, and mutation is deferred until necessary.
candidate 2 (found by 3 of 39 passes): If `document` objects are copied frequently (passed by value, returned from functions, stored in containers) but modified rarely, eagerly copying all lines on every copy is unnecessarily expensive.
candidate 3 (found by 3 of 39 passes): The absence of a non-const `operator*` and `operator->` is the most distinctive aspect of `copy_on_write` compared to `indirect`.
candidate 4 (found by 3 of 39 passes): We show how `copy_on_write` simplifies composite class design and reduces copy overhead in a text-editor document model.

## audience - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 13 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/1  -> 0.33
  [5] Design Requirements                          2/2/2  -> 2.00
  [6] Prior Work                                   2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           2/2/2  -> 2.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Unlike `indirect<T>`, which has unique ownership, `copy_on_write<T>` uses shared, reference-counted ownership.
candidate 2 (found by 3 of 39 passes): This proposal standardises a modern, allocator-aware formulation aligned with the design of `std::indirect` [P3019].
candidate 3 (found by 2 of 39 passes): `copy_on_write<T>` has a similar ownership model to `shared_ptr<const T>`: multiple owners, atomic reference counting. It differs in several important respects:
candidate 4 (found by 1 of 39 passes): Sharing the underlying storage (e.g. with `std::shared_ptr`) avoids copies but can compromise value semantics.

## vehicle - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          1/1/1  -> 1.00
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect&lt;T>` or `polymorphic&lt;T>` without adding an additional layer of indirection.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   1/0/0  -> 0.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A C++20 reference implementation is available at https://github.com/purpleKarrot/copyon-write.
candidate 2 (found by 1 of 39 passes): Adobe’s `stlab` library provides a `copy_on_write` type along similar lines.

-->
