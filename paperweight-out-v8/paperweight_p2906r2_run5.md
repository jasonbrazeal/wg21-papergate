Verdict: Adequate (7/14)

The paper offers a solid foundation for its standardization case in some areas, particularly in showing that the feature has prior art, a working implementation, and a clear reason to preserve compile-time extents. However, the support thins considerably when it comes to explaining who is affected, how the feature coordinates with existing standards, and why the work cannot be done in a library.

- The strongest support comes from the demonstrated implementation experience and the clear explanation of why discarding static extent information would be lossy and undesirable.
- The paper also establishes prior art and alternatives by connecting the proposal to `std::extents`, `std::mdspan`, and `std::constant_wrapper`.
- The case for why the standard is needed, rather than a library solution, is only claimed and not backed by sufficient reasoning.
- The most glaring omission is the absence of any established discussion of who is affected or how the proposal coordinates and interoperates with existing standards.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.67   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 6.50 / 7.00 / 7.00   (all 3 samples: 6.83)
headings: h2 9
on threshold: implementation
splits: insufficiency[7] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       2/2/2  -> 2.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           2/2/2  -> 2.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 2/2/2  -> 2.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Demoting static extents to runtime values would be lossy, with no way for user code to recover the compile-time nature afterwards.
candidate 2 (found by 3 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.
candidate 3 (found by 2 of 30 passes): However, `std::extents` behaves very little like an array. A notable missing feature are structured bindings, which would come in handy if the extents of the individual dimensions need to be extracted:
candidate 4 (found by 1 of 30 passes): A notable missing feature are structured bindings, which would come in handy if the extents of the individual dimensions need to be extracted:

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       2/2/2  -> 2.00
  [4] 3 Impact On the Standard                     1/1/1  -> 1.00
  [5] 4 Design Decisions                           2/2/2  -> 2.00
  [6] 5 Proposed implementation                    1/1/1  -> 1.00
  [7] 6 Alternative considered: demote static e... 2/2/2  -> 2.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.
candidate 2 (found by 2 of 30 passes): [[P0009R18]](https://wg21.link/p0009r18) proposed `std::mdspan`, which was approved for C++23. It comes with the utility class template `std::extents` to describe the integral extents of a multidimensional index space.
candidate 3 (found by 2 of 30 passes): This proposal providing a tuple interface so that users can decompose extents with structured bindings, and the dimensions now have meaningful names.
candidate 4 (found by 2 of 30 passes): This paper proposes to **retain the compile-time nature of static extents** by exposing them as `std::constant_wrapper` instances ([[P2781R9]](https://wg21.link/p2781r9)), while dynamic extents are exposed as plain values of `IndexType`.

## vehicle - grade 0.50 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     1/1/1  -> 1.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This proposal providing a tuple interface so that users can decompose extents with structured bindings, and the dimensions now have meaningful names.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/1/1  -> 0.67
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    2/2/2  -> 2.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): An example of such an implementation using libstdc++/libc++ trunk’s implementation of `<mdspan>` with `-std=c++26` on Godbolt is provided here: [Compiler Explorer](https://godbolt.org/z/dYocKf8cs).

-->
