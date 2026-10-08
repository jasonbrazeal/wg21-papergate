Verdict: Adequate (5/14)

The paper gives a reasonably clear account of the problem and a plausible precedent in Boost.Optional, but it leaves much of the standardization case implicit rather than argued. The thinnest support concerns the need for action by the committee specifically, as opposed to a library solution, and the absence of any demonstrated implementation experience or affected-user evidence.

- The strongest support is the motivation: the paper clearly identifies the awkwardness of extracting a raw pointer from `optional<T&>` or `optional<T>` when interfacing with C and legacy C++ APIs.
- The prior-art discussion is also concrete, since it points to Boost.Optional as an existing model and argues for following that precedent.
- The paper claims but does not establish coordination with existing standardization discussions, such as the `inplace_vector` return-type question, without showing how this proposal would resolve or align with those discussions.
- The most glaring omission is the lack of any evidence about who is affected or why a library-only approach would be insufficient, leaving the case for standardization itself largely unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 5.50   max 5.67

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 5.50 / 5.00   (all 3 samples: 5.33)
headings: h2 8
on threshold: none
splits: motivation[6] 2/2/1  coordination[4] 0/0/1  coordination[6] 1/1/0
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Motivation and Scope                       2/2/2  -> 2.00
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           2/2/1  -> 1.67
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

## coordination - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and Scope                       0/0/1  -> 0.33
  [5] 4 Impact On the Standard                     0/0/0  -> 0.00
  [6] 5 Design Decisions                           1/1/0  -> 0.67
  [7] 6 Technical Specifications                   0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The primary use case, as mentioned, is to use this with C APIs and legacy C++ APIs that use pointers because there is/was (C/C++) no suitable vocabulary type to use.
candidate 2 (found by 1 of 27 passes): During the discussion around changing the return type for `inplace_vector<T, N>::try_*_back()` from a `T*` to a `std::optional<T&>` , it was noted that there is no easy way to convert the `optional<T&>` returned to a `T*` .

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
