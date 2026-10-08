Verdict: Adequate (7/14)

The paper offers solid grounding for the value of copy-on-write semantics and for the existence of prior art, but it leaves the standardization case thin in several places where a proposal normally needs to show who is affected and how the feature fits with the rest of the library.

- The strongest support is the clear motivation: the paper explains the performance problem with eager copying and shows how `copy_on_write` addresses it in a concrete document-model example.
- The paper also establishes meaningful prior art and implementation experience, including a reference implementation and a comparison to `std::indirect` and `shared_ptr<const T>`.
- The most glaring omission is the absence of any identified user population or affected codebase, leaving the audience for the feature unclear.
- The paper likewise does not establish coordination with related facilities or interoperability concerns, and its claim that the feature cannot be provided adequately as a library is asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.67   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.50 / 6.50 / 7.00   (all 3 samples: 6.67)
headings: h2 12
on threshold: implementation
splits: motivation[9] 2/1/2  prior_art[3] 1/0/0  vehicle[5] 0/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design Requirements                          1/1/1  -> 1.00
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           2/1/2  -> 1.67
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        1/1/1  -> 1.00
candidate 1 (found by 3 of 39 passes): This gives efficient value semantics: copying is O(1) regardless of the size or complexity of `T`, and mutation is deferred until necessary.
candidate 2 (found by 3 of 39 passes): If `document` objects are copied frequently (passed by value, returned from functions, stored in containers) but modified rarely, eagerly copying all lines on every copy is unnecessarily expensive.
candidate 3 (found by 3 of 39 passes): We show how `copy_on_write` simplifies composite class design and reduces copy overhead in a text-editor document model.
candidate 4 (found by 2 of 39 passes): The absence of a non-const `operator*` and `operator->` is the most distinctive aspect of `copy_on_write` compared to `indirect`.

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

## prior_art - grade 2.00 (fired in 4 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     1/0/0  -> 0.33
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
candidate 1 (found by 3 of 39 passes): This proposal standardises a modern, allocator-aware formulation aligned with the design of `std::indirect` [P3019].
candidate 2 (found by 2 of 39 passes): Unlike `indirect<T>`, which has unique ownership, `copy_on_write<T>` uses shared, reference-counted ownership.
candidate 3 (found by 2 of 39 passes): `copy_on_write<T>` has a similar ownership model to `shared_ptr<const T>`: multiple owners, atomic reference counting. It differs in several important respects:
candidate 4 (found by 1 of 39 passes): This gives efficient value semantics: copying is O(1) regardless of the size or complexity of `T`, and mutation is deferred until necessary.

## vehicle - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/1/1  -> 0.67
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect<T>` or `polymorphic<T>` without adding an additional layer of indirection.

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

## insufficiency - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect<T>` or `polymorphic<T>` without adding an additional layer of indirection.
candidate 2 (found by 1 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect&lt;T>` or `polymorphic&lt;T>` without adding an additional layer of indirection.

## implementation - grade 2.00  [binary: max] (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
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
  [10] Reference Implementation                     2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A C++20 reference implementation is available at https://github.com/purpleKarrot/copyon-write.

-->
