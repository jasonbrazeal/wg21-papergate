Verdict: Strong (9/14)

The paper offers meaningful support in the areas of motivation, prior art, coordination, and implementation experience, but its case is thinner when it comes to showing who is affected, why the standard is the right home, and why a library cannot suffice. The strongest material comes from direct engagement with compiler implementers, while the weakest parts rely on assertion rather than demonstration.

- The paper’s implementation experience is its strongest asset, grounded in feedback from Clang, EDG, and GCC developers during discussion of the prior revision.
- The motivation and coordination sections are well supported, particularly through the stated goal of enabling `meta::info` keys in unordered containers and the implementer agreement on cross-translation-unit hash stability.
- The claim that a robust hash for `meta::info` requires compiler support is asserted as the basis for standardization, but the paper does not establish why that support cannot be delivered through a non-standard library or a smaller compiler interface.
- The most glaring omission is the lack of evidence for the claim that the affected types are widely used as keys, leaving the breadth of the need unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 7 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 9.67   accumulate 9.17   max 10.67

## SUMMARY
grades: motivation 1.83  audience 0.50  prior_art 2.00  vehicle 0.83  coordination 1.50  insufficiency 0.50  implementation 1.67
sample agreement: 84 of 91 section-criterion pairs unanimous (92%)
single-sample totals would have been: 9.50 / 9.50 / 7.50   (all 3 samples: 8.83)
headings: h2 12
on threshold: coordination, implementation
splits: motivation[6] 0/1/1  motivation[7] 2/2/1  prior_art[4] 2/2/0  prior_art[5] 2/0/2
        vehicle[6] 1/1/0  coordination[6] 0/0/1  implementation[7] 2/2/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/1/1  -> 0.67
  [7] 6 Design decisions                           2/2/1  -> 1.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 2 (found by 3 of 39 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 3 (found by 2 of 39 passes): It introduces the first example of a compile-time hash facility.
candidate 4 (found by 2 of 39 passes): Ultimately, the goal of this paper is to provide a robust way to hash values of type `meta::info`.

## audience - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/0  -> 1.33
  [5] 4 Examples                                   2/0/2  -> 1.33
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  2/2/2  -> 2.00
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 2/2/2  -> 2.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): It introduces the first example of a compile-time hash facility.
candidate 2 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.
candidate 3 (found by 3 of 39 passes): Feedback from GCC and Clang implementers indicates that the most practical strategy is to reuse existing mangling infrastructure to implement the hashing.
candidate 4 (found by 3 of 39 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash<T*>` having inconsistent values between compile-time and runtime.

## vehicle - grade 0.83 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     1/1/0  -> 0.67
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 2 of 39 passes): It introduces the first example of a compile-time hash facility.

## coordination - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/1  -> 0.33
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 2 of 39 passes): Clang developers agreed that hash values should be stable across translation units and compiler runs.
candidate 3 (found by 1 of 39 passes): It introduces the first example of a compile-time hash facility.
candidate 4 (found by 1 of 39 passes): Clang developers also raised concerns about making hash stability a strong ABI commitment.

## insufficiency - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.

## implementation - grade 1.67  [binary: max] (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           2/2/1  -> 1.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.

-->
