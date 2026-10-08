Verdict: Strong (8/14)

The paper offers a reasonably grounded case for the existence and feasibility of a compile-time hash facility, with its strongest support coming from concrete implementation experience and a clear account of prior art. The argument becomes thinner where it relies on assertions about compiler support, the need for a standard rather than a library solution, and the breadth of affected users, none of which are developed with evidence or analysis.

- The paper’s implementation experience is the most convincing element, since it reports both unstable and semi-stable versions of the hash on a real Clang fork.
- The prior art and alternatives section is well supported, particularly through its engagement with P3068 and P3372 and its positioning as the first compile-time hash facility.
- The claim that a robust hash for `meta::info` requires compiler support is repeated as the basis for standardization, but the paper does not establish why that support cannot be provided through a non-standard library or compiler extension.
- The most glaring omission is the lack of any established evidence about who is affected or how widely the proposed facility would be used, leaving the practical demand for standardization asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 7 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 9.67   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.83  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 9.00 / 8.00   (all 3 samples: 8.33)
headings: h2 11
on threshold: implementation
splits: motivation[6] 0/2/1  prior_art[3] 1/1/0  prior_art[5] 2/0/2  vehicle[4] 2/1/1
        vehicle[6] 0/1/0  vehicle[7] 0/1/0  coordination[4] 0/1/1  coordination[10] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   1/1/1  -> 1.00
  [6] 5 Impact                                     0/2/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 2 (found by 3 of 36 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.
candidate 3 (found by 2 of 36 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys, and potentially with other types in future.
candidate 4 (found by 2 of 36 passes): The following examples illustrate practical applications of `consteval_hash`.

## audience - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/0  -> 0.67
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   2/0/2  -> 1.33
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  1/1/1  -> 1.00
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 2 (found by 3 of 36 passes): [[P3068]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3068r2.html) has been approved for C++26, allowing exception throwing within constexpr, so it is meaningful to mark `consteval_hash<meta::info>::operator()` as `noexcept`.
candidate 3 (found by 3 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash<T*>` having inconsistent values between compile time and runtime.
candidate 4 (found by 2 of 36 passes): thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys, and potentially with other types in future.

## vehicle - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/1/1  -> 1.33
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/1/0  -> 0.33
  [7] 6 Design decisions                           0/1/0  -> 0.33
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 1 of 36 passes): Overall, this feels like the more complete and extensible solution, so it is the one we are proposing.

## coordination - grade 0.50 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/1/1  -> 0.67
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/1/0  -> 0.33
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 36 passes): extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [P3372] concerning `std::hash<T*>` having inconsistent values between compile time and runtime.

## insufficiency - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.

## implementation - grade 2.00  [binary: max] (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  2/2/2  -> 2.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We have implemented an [unstable](https://github.com/bloomberg/clang-p2996/pull/227) version and two semi-stable versions of the hash on Bloomberg’s Clang fork.

-->
