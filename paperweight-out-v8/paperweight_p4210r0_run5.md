Verdict: Adequate (6/14)

The paper gives a partial account of why a `copy_on_write` wrapper would be useful and shows that comparable ideas exist in practice, but it leaves several essential parts of the standardization case unaddressed. The thinnest areas are the lack of a clear audience, the absence of a rationale for doing this in the standard rather than in a library, and the missing discussion of how the facility would interact with existing standard components.

- The strongest support comes from the explanation of the value-semantics and deferred-mutation model, which makes the motivating performance problem concrete.
- The paper also establishes relevant prior art by comparing the design with `std::indirect`, `shared_ptr<const T>`, and existing implementations such as Adobe’s `stlab`.
- The most glaring omission is that the paper does not establish who is affected or why the standard, rather than a library, is the right venue for this facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 7.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.50 / 6.00 / 6.50   (all 3 samples: 6.33)
headings: h2 12
on threshold: implementation
splits: motivation[5] 2/1/2  motivation[13] 2/1/1  implementation[6] 1/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design Requirements                          2/1/2  -> 1.67
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           1/1/1  -> 1.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        2/1/1  -> 1.33
candidate 1 (found by 3 of 39 passes): This gives efficient value semantics: copying is O(1) regardless of the size or complexity of `T`, and mutation is deferred until necessary.
candidate 2 (found by 3 of 39 passes): If `document` objects are copied frequently (passed by value, returned from functions, stored in containers) but modified rarely, eagerly copying all lines on every copy is unnecessarily expensive.
candidate 3 (found by 3 of 39 passes): Unlike `indirect<T>`, which has unique ownership, `copy_on_write<T>` uses shared, reference-counted ownership.
candidate 4 (found by 3 of 39 passes): The absence of a non-const `operator*` and `operator->` is the most distinctive aspect of `copy_on_write` compared to `indirect`.

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

## prior_art - grade 2.00 (fired in 3 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
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
candidate 3 (found by 3 of 39 passes): `copy_on_write<T>` has a similar ownership model to `shared_ptr<const T>`: multiple owners, atomic reference counting. It differs in several important respects:

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
candidate 1 (found by 3 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect<T>` or `polymorphic<T>` without adding an additional layer of indirection.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   1/0/1  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A C++20 reference implementation is available at https://github.com/purpleKarrot/copyon-write.
candidate 2 (found by 2 of 39 passes): Adobe’s `stlab` library provides a `copy_on_write` type along similar lines.

-->
