Verdict: Strong (9/14)

The paper offers solid support in a few key areas—particularly in motivating the need for compile-time hashing and in showing implementation experience—but much of the case for standardization rests on assertions that are not yet backed by evidence or detailed argument. The thinnest support appears where the paper needs to show why this belongs in the standard rather than in a library, and how it coordinates with existing or proposed facilities.

- The strongest support is the concrete implementation experience on Bloomberg’s Clang fork, which demonstrates feasibility and surfaces practical design considerations.
- The paper clearly establishes why compile-time hashing matters for reflection-based programming and future standard library interfaces.
- The argument that a robust hash for `meta::info` requires compiler support is asserted, but the paper does not establish why a library solution cannot provide it.
- The most glaring omission is the lack of established evidence for who is affected and how the proposed facility interoperates with existing standardization efforts, beyond general statements about unordered containers and `meta::info`.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 7 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 8.83   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.00  coordination 0.67  insufficiency 0.67  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 8.50 / 8.00   (all 3 samples: 8.50)
headings: h2 11
on threshold: implementation
splits: audience[10] 1/0/0  prior_art[3] 0/1/0  prior_art[4] 2/0/2  vehicle[6] 1/0/0
        vehicle[7] 2/1/0  coordination[3] 0/0/1  coordination[4] 1/0/1  coordination[10] 0/1/1
        insufficiency[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/2/2  -> 2.00
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 2 (found by 3 of 36 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 3 (found by 3 of 36 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection.
candidate 4 (found by 3 of 36 passes): It enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.

## audience - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [10] 9 Possible extensions of current design      1/0/0  -> 0.33
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/1/0  -> 0.33
  [4] 3 Motivation                                 2/0/2  -> 1.33
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 2 (found by 3 of 36 passes): It is similar to `hash_of`, but does not have the same drawback of suggesting that it is the single meaningful way to hash `meta::info`.
candidate 3 (found by 3 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash<T*>` having inconsistent values between compile time and runtime.
candidate 4 (found by 1 of 36 passes): thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys

## vehicle - grade 1.00 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     1/0/0  -> 0.33
  [7] 6 Design decisions                           2/1/0  -> 1.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 1 of 36 passes): Because of the runtime requirements on `hash<T>`, existing specializations cannot be made `constexpr`, meaning we would end up with some specializations of `std::hash<T>` being consteval-only, while others are runtime-only.
candidate 4 (found by 1 of 36 passes): Ultimately, the goal of this paper is to provide a robust way to hash values of type `meta::info.`

## coordination - grade 0.67 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/1  -> 0.33
  [4] 3 Motivation                                 1/0/1  -> 0.67
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/1/1  -> 0.67
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 2 (found by 1 of 36 passes): This creates a usage for compile-time hashing, including support for `meta::info` and other consteval-only types as keys.
candidate 3 (found by 1 of 36 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 4 (found by 1 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [P3372] concerning `std::hash<T*>` having inconsistent values between compile time and runtime.

## insufficiency - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/1/0  -> 0.33
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 36 passes): Because of the runtime requirements on `hash<T>`, existing specializations cannot be made `constexpr`, meaning we would end up with some specializations of `std::hash<T>` being consteval-only, while others are runtime-only.

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
