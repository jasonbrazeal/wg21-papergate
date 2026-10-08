Verdict: Adequate (5/14)

The paper offers some grounding for its proposal in a recognized practical problem and an existing library precedent, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas concern who specifically needs the feature, why it belongs in the standard rather than in a library, and whether there is any implementation experience beyond pointing to Boost.

- The strongest support is the identification of a concrete conversion gap when interacting with C and legacy C++ APIs that use raw pointers.
- The paper also establishes a reasonable prior-art basis by following the precedent set by Boost.Optional.
- The discussion of coordination and interoperability gestures at the C and legacy API use case but does not develop it into a clear interoperability argument.
- The most glaring omission is the absence of any established case for why this cannot be provided by a library or why standardization is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 4.67   accumulate 5.17   max 5.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 0.67
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 4.00 / 5.00 / 5.50   (all 3 samples: 4.83)
headings: h2 8
on threshold: motivation
splits: motivation[6] 1/1/2  implementation[4] 0/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Motivation and Scope                       2/2/2  -> 2.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           1/1/2  -> 1.33
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): There is no easy, obvious way to retrieve the pointer stored in an `optional<T&>` , nor a pointer to the object in an `optional<T>`
candidate 2 (found by 3 of 27 passes): The primary use case, as mentioned, is to use this with C APIs and legacy C++ APIs that use pointers because there is/was (C/C++) no suitable vocabulary type to use.
candidate 3 (found by 2 of 27 passes): When calling a C or a legacy C++ API, a raw pointer is often used instead of an `optional<T&>` (in the case of C or pre-C++26 APIs) or an `optional<T>` (in the case of C or pre-C++17 APIs).
candidate 4 (found by 1 of 27 passes): During the discussion around changing the return type for `inplace_vector<T, N>::try_*_back()` from a `T*` to a `std::optional<T&>` , it was noted that there is no easy way to convert the `optional<T&>` returned to a `T*` .

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

## prior_art - grade 2.00 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       2/2/2  -> 2.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           2/2/2  -> 2.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes following the precedent set by Boost.Optional.
candidate 2 (found by 3 of 27 passes): Of those, the best fit is making the same choice as Boost.Optional.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       0/0/0  -> 0.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           1/1/1  -> 1.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The primary use case, as mentioned, is to use this with C APIs and legacy C++ APIs that use pointers because there is/was (C/C++) no suitable vocabulary type to use.

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
  [4] 3 Motivation and Scope                       0/1/1  -> 0.67
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/0  -> 0.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This paper proposes following the precedent set by Boost.Optional.

-->
