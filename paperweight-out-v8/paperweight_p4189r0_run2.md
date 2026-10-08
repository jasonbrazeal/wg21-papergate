Verdict: Adequate (6/14)

The paper gives a partial account of why a pointer accessor for `optional` would be useful, but it leaves several essential parts of the standardization case largely unaddressed, particularly around affected users, the need for a standard solution, and evidence that a library approach is insufficient.

- The strongest support is the motivation, which clearly identifies friction when converting `optional<T&>` or `optional<T>` to raw pointers for C and legacy C++ APIs.
- The paper also credibly grounds its design choice in prior art by pointing to Boost.Optional as an existing precedent.
- The discussion of coordination with other standardization work is only asserted through the `inplace_vector` example, without showing how this proposal fits into the broader committee context.
- The most glaring omission is the absence of any established case for why this must be standardized rather than provided as a library facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 4 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 6.00   accumulate 5.83   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.83  insufficiency 0.00  implementation 1.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.50 / 5.50 / 5.50   (all 3 samples: 5.83)
headings: h2 8
on threshold: none
splits: coordination[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Motivation and Scope                       2/2/2  -> 2.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           2/2/2  -> 2.00
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

## coordination - grade 0.83 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       1/1/1  -> 1.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           2/0/0  -> 0.67
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): During the discussion around changing the return type for `inplace_vector<T, N>::try_*_back()` from a `T*` to a `std::optional<T&>` , it was noted that there is no easy way to convert the `optional<T&>` returned to a `T*` .
candidate 2 (found by 1 of 27 passes): The primary use case, as mentioned, is to use this with C APIs and legacy C++ APIs that use pointers because there is/was (C/C++) no suitable vocabulary type to use.

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       1/1/1  -> 1.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           0/0/0  -> 0.00
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes following the precedent set by Boost.Optional.

-->
