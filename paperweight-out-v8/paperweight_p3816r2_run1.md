Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why compile-time hashing for `meta::info` would be useful and shows awareness of related work, but it does not substantiate several central claims about the need for standardization, and it offers no implementation experience. The strongest material concerns motivation and prior art, while the case for standard-library placement, affected users, and interoperability rests largely on assertion.

- The paper establishes a concrete motivation by connecting `consteval_hash` to practical use of `meta::info` as a key in unordered containers.
- It situates the proposal credibly against prior work, including P2830 and P3372, and explains how the facility differs from `hash_of`.
- The claim that a robust hash requires compiler support is repeated as the main justification for standardization, but the paper does not establish why that support cannot be provided through a library or existing mechanisms.
- The paper provides no implementation experience, leaving the feasibility and portability of the proposed facility unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 7.67   accumulate 6.67   max 7.67

## SUMMARY
grades: motivation 1.83  audience 0.33  prior_art 2.00  vehicle 0.83  coordination 0.83  insufficiency 0.50  implementation 0.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 7.00 / 5.50   (all 3 samples: 6.33)
headings: h2 11
on threshold: none
splits: motivation[5] 2/1/1  motivation[7] 2/2/1  audience[10] 1/1/0  prior_art[9] 0/2/2
        vehicle[6] 1/1/0  coordination[6] 1/0/0  coordination[10] 0/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/1/1  -> 1.33
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/1  -> 1.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Hashing support was intentionally omitted, as it lies outside the core reflection feature.
candidate 2 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 2 of 36 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 4 (found by 2 of 36 passes): The following examples illustrate practical applications of `consteval_hash`.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
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
  [10] 9 Possible extensions of current design      1/1/0  -> 0.67
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/2/2  -> 2.00
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/2/2  -> 1.33
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection. Our proposal provides a short and effective solution without needing to sort a list of reflected types.
candidate 2 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 3 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash<T*>` having inconsistent values between compile time and runtime.
candidate 4 (found by 2 of 36 passes): It is similar to `hash_of`, but does not have the same drawback of suggesting that it is the single meaningful way to hash `meta::info`.

## vehicle - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 2 of 36 passes): Moreover, it enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.

## coordination - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     1/0/0  -> 0.33
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/1/1  -> 0.67
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 2 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [P3372] concerning `std::hash<T*>` having inconsistent values between compile time and runtime.
candidate 3 (found by 1 of 36 passes): It introduces the first example of a compile-time hash facility.

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

## implementation - grade 0.00  [binary: max] (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
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
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidates: (none validated)

-->
