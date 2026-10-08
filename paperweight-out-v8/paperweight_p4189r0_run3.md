Verdict: Adequate (5/14)

The paper offers a narrow but genuine foundation for its standardization case, centered on a clearly articulated interoperability problem and a named precedent in Boost.Optional. The support is thinnest where it matters most for a standards-track change: the paper does not show who is affected, why a library solution is insufficient, or that the feature has been implemented and used.

- The strongest support is the concrete statement that there is no easy way to retrieve a pointer from `optional<T&>` or `optional<T>`, which grounds the proposal in a real usability gap.
- The paper also establishes prior art by explicitly following the precedent set by Boost.Optional.
- A notable weakness is that the paper claims but does not establish why the standard is the right venue, since the same C API interoperability argument could point toward a library helper.
- The most glaring omission is the absence of any demonstrated implementation experience beyond the Boost precedent, leaving the proposal without evidence of practical use or refinement.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 5 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.67   accumulate 5.00   max 5.67

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.83  vehicle 0.17  coordination 0.33  insufficiency 0.00  implementation 0.67
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.50 / 3.50 / 5.50   (all 3 samples: 4.83)
headings: h2 8
on threshold: none
splits: motivation[6] 2/1/2  prior_art[4] 2/1/2  vehicle[6] 0/0/1  coordination[4] 1/1/0
        implementation[4] 1/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Motivation and Scope                       2/2/2  -> 2.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           2/1/2  -> 1.67
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): There is no easy, obvious way to retrieve the pointer stored in an `optional<T&>` , nor a pointer to the object in an `optional<T>`
candidate 2 (found by 3 of 27 passes): When calling a C or a legacy C++ API, a raw pointer is often used instead of an `optional<T&>` (in the case of C or pre-C++26 APIs) or an `optional<T>` (in the case of C or pre-C++17 APIs).
candidate 3 (found by 3 of 27 passes): The primary use case, as mentioned, is to use this with C APIs and legacy C++ APIs that use pointers because there is/was (C/C++) no suitable vocabulary type to use.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       0/0/0  -> 0.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/0  -> 0.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.83 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       2/1/2  -> 1.67
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           2/2/2  -> 2.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes following the precedent set by Boost.Optional.
candidate 2 (found by 3 of 27 passes): Of those, the best fit is making the same choice as Boost.Optional.

## vehicle - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       0/0/0  -> 0.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/1  -> 0.33
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): The primary use case, as mentioned, is to use this with C APIs and legacy C++ APIs that use pointers because there is/was (C/C++) no suitable vocabulary type to use.

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       1/1/0  -> 0.67
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/0  -> 0.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): During the discussion around changing the return type for `inplace_vector<T, N>::try_*_back()` from a `T*` to a `std::optional<T&>` , it was noted that there is no easy way to convert the `optional<T&>` returned to a `T*` .

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       0/0/0  -> 0.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/0  -> 0.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.67  [binary: max] (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       1/0/1  -> 0.67
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/0  -> 0.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This paper proposes following the precedent set by Boost.Optional.

-->
