Verdict: Adequate (7/14)

The paper offers solid grounding for its core motivation, prior art, and the existence of implementation experience, but it leaves several important parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who is actually affected, why the standard is the right venue, and why a library solution would not suffice.

- The strongest support is the clear explanation of why copy-on-write value semantics matter and how the proposed type differs from existing ownership models.
- The paper also credibly establishes prior art and alternatives by situating the design against `std::indirect`, `shared_ptr<const T>`, and shared storage approaches.
- Implementation experience is reasonably documented through a reference implementation, Adobe’s `stlab`, and Qt’s `QSharedDataPointer`.
- The most glaring omission is the absence of any established case for coordination and interoperability with other standard library components or proposals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.00/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 8.00   accumulate 7.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 12
on threshold: implementation
splits: motivation[5] 2/1/1  audience[6] 1/1/0  prior_art[4] 0/1/0  prior_art[5] 0/2/2
        vehicle[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design Requirements                          2/1/1  -> 1.33
  [6] Prior Work                                   0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           2/2/2  -> 2.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        1/1/1  -> 1.00
candidate 1 (found by 3 of 39 passes): This gives efficient value semantics: copying is O(1) regardless of the size or complexity of `T`, and mutation is deferred until necessary.
candidate 2 (found by 3 of 39 passes): If `document` objects are copied frequently (passed by value, returned from functions, stored in containers) but modified rarely, eagerly copying all lines on every copy is unnecessarily expensive.
candidate 3 (found by 3 of 39 passes): Unlike `indirect<T>`, which has unique ownership, `copy_on_write<T>` uses shared, reference-counted ownership.
candidate 4 (found by 3 of 39 passes): The absence of a non-const `operator*` and `operator->` is the most distinctive aspect of `copy_on_write` compared to `indirect`.

## audience - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   1/1/0  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Qt’s `QSharedDataPointer` (Qt 4.0, 2005) pioneered a reusable COW pointer type in a major C++ framework.

## prior_art - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Design Requirements                          0/2/2  -> 1.33
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
candidate 4 (found by 1 of 39 passes): Sharing the underlying storage (e.g. with `std::shared_ptr`) avoids copies but can compromise value semantics.

## vehicle - grade 0.17 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   0/0/1  -> 0.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): This proposal standardises a modern, allocator-aware formulation aligned with the design of `std::indirect` [P3019].

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
candidate 1 (found by 2 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect<T>` or `polymorphic<T>` without adding an additional layer of indirection.
candidate 2 (found by 1 of 39 passes): Implementing copy-on-write behaviour requires intrusion into the details of object ownership and is not possible to implement for `indirect&lt;T>` or `polymorphic&lt;T>` without adding an additional layer of indirection.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] copyonwrite: A Vocabulary Type for Lazily-   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design Requirements                          0/0/0  -> 0.00
  [6] Prior Work                                   1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Technical Specifications                     0/0/0  -> 0.00
  [9] Design Discussions                           0/0/0  -> 0.00
  [10] Reference Implementation                     2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
  [13] Appendix A: Before and After Examples        0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A C++20 reference implementation is available at https://github.com/purpleKarrot/copyon-write.
candidate 2 (found by 2 of 39 passes): Adobe’s `stlab` library provides a `copy_on_write` type along similar lines.
candidate 3 (found by 1 of 39 passes): Qt’s `QSharedDataPointer` (Qt 4.0, 2005) pioneered a reusable COW pointer type in a major C++ framework.

-->
