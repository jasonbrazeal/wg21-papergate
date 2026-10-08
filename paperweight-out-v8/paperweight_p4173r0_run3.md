Verdict: Adequate to Strong (7/14)

The paper gives a partial account of why an iterator-based accessor would be useful, but it leaves several core justifications asserted rather than demonstrated. The strongest material concerns the conceptual relationship between `default_accessor` and a more general iterator model, along with a concrete implementation, while the case for affected users, standardization need, interoperability, and why a library solution is insufficient remains thin.

- The paper establishes that `default_accessor` is effectively a pointer-specific case of a broader iterator-based design, which supports the motivation for generalizing it.
- The implementation experience is concrete, with a working example based on libstdc++ and a stated preference for a constant-iterator concept.
- The paper does not establish who is affected by the current design or the practical scale of the ergonomic barrier it describes.
- The most glaring omission is the lack of support for why this cannot be adequately provided as a library rather than through standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 7.17   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.33  coordination 0.67  insufficiency 0.17  implementation 2.00
sample agreement: 49 of 56 section-criterion pairs unanimous (88%)
single-sample totals would have been: 7.50 / 6.50 / 6.50   (all 3 samples: 6.83)
headings: h3 7   <- NOT h2, check the unit list
on threshold: prior_art, implementation
splits: motivation[4] 2/0/0  prior_art[4] 1/1/2  vehicle[2] 1/0/0  vehicle[4] 1/0/0
        coordination[5] 1/0/0  insufficiency[2] 0/1/0  implementation[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   2/0/0  -> 0.67
  [5] Design                                       2/2/2  -> 2.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Since a range knows its own size, `mdspan` can now automatically check if the dimensions fit, catching errors early at compile-time or during runtime.
candidate 2 (found by 2 of 24 passes): A critical requirement of `mdspan` is that its first template argument, `ElementType`, must match the accessor's `element_type`.
candidate 3 (found by 1 of 24 passes): By default, `mdspan` provides accessors optimized for contiguous memory via raw pointers. Although designed as a general-purpose view, the standard `default_accessor` and `aligned_accessor` are strictly coupled with pointer-based data handles.
candidate 4 (found by 1 of 24 passes): This creates a significant ergonomic barrier: developers cannot easily leverage CTAD to deduce the `element_type` and `extents_type` while simultaneously selecting a different layout, such as `layout_left` or `layout_stride`.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   1/1/2  -> 1.33
  [5] Design                                       2/2/2  -> 2.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The standard `default_accessor<T>` is conceptually and functionally equivalent to `iterator_accessor<T*>`, which suggests that `default_accessor` is a specialization of a more general *iterator*-based model, rather than a fundamentally distinct *pointer*-based design.
candidate 2 (found by 2 of 24 passes): Standard `mdspan` accessors, such as `default_accessor`, are specialized for use with raw pointers.
candidate 3 (found by 1 of 24 passes): While `mdspan`'s design allows for custom accessors, providing a standardized iterator-based accessor simplifies integration with ranges such as views and containers.
candidate 4 (found by 1 of 24 passes): By following this precedent, `from_range_t` allows `mdspan` to function as a powerful multi-dimensional type eraser similar to `span`, which provides a consistent interface while still maintaining the high performance and high-level safety, as the constructor has performed the necessary checks:

## vehicle - grade 0.33 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   1/0/0  -> 0.33
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): This paper proposes `iterator_accessor`, which leverages `random_access_iterator` to decouple multi-dimensional views from physical memory continuity.
candidate 2 (found by 1 of 24 passes): This provides a standardized mechanism to bridge abstract data sequences with multi-dimensional indexing, eliminating the need to reinvent access logic.

## coordination - grade 0.67 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Design                                       1/0/0  -> 0.33
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): This paper proposes `iterator_accessor`, which leverages `random_access_iterator` to decouple multi-dimensional views from physical memory continuity.
candidate 2 (found by 1 of 24 passes): providing a standardized iterator-based accessor simplifies integration with ranges such as views and containers.
candidate 3 (found by 1 of 24 passes): This creates a significant ergonomic barrier: developers cannot easily leverage CTAD to deduce the `element_type` and `extents_type` while simultaneously selecting a different layout, such as `layout_left` or `layout_stride`.

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): This paper proposes `iterator_accessor`, which leverages `random_access_iterator` to decouple multi-dimensional views from physical memory continuity.

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Design                                       1/0/0  -> 0.33
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Proposed change                              0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The author implemented `iterator_accessor` and `from_range_t` constructor based on libstdc++ along with the above example. See [godbolt link](https://godbolt.org/z/6c4zeed6b) for details.
candidate 2 (found by 1 of 24 passes): The author prefers using the `*constant-iterator*` concept as it more accurately captures the semantic intent of read-only access.

-->
