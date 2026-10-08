Verdict: Adequate to Strong (7/14)

The paper offers a solid conceptual motivation for a compile-time hash facility and useful engagement with prior work, but its case for standardization rests heavily on assertion rather than demonstrated need. The thinnest areas are those that would normally justify putting something in the standard rather than shipping it as a library: affected users, implementation experience, and why a library solution is insufficient.

- The strongest support is the clear explanation of why the feature matters for compile-time programming and the recognition that it introduces the first compile-time hash facility.
- The discussion of prior art and alternatives is also well grounded, particularly the contrast with `std::hash<meta::info>` and the infeasibility of value-based reflection for `mp_unique`.
- The paper claims but does not establish that a robust hash for `meta::info` requires compiler support, leaving the central argument for standardization underdeveloped.
- The most glaring omission is implementation experience, where the paper mentions an unstable and two semi-stable versions but provides no evidence about usability, portability, or lessons learned.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 8.00   max 8.33

## SUMMARY
grades: motivation 1.67  audience 0.17  prior_art 2.00  vehicle 1.17  coordination 0.83  insufficiency 0.50  implementation 0.67
sample agreement: 72 of 84 section-criterion pairs unanimous (86%)
single-sample totals would have been: 6.50 / 7.50 / 8.50   (all 3 samples: 7.00)
headings: h2 11
on threshold: motivation
splits: motivation[5] 0/0/1  motivation[7] 2/1/1  audience[10] 0/1/0  prior_art[5] 2/2/0
        prior_art[8] 0/0/1  vehicle[4] 1/1/2  vehicle[6] 1/0/1  coordination[3] 0/0/1
        coordination[6] 0/1/1  coordination[10] 1/0/0  implementation[7] 0/1/1
        implementation[9] 0/0/2
## END SUMMARY

## motivation - grade 1.67 (fired in 6 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   0/0/1  -> 0.33
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/1/1  -> 1.33
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 2 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 3 of 36 passes): Con: it adds randomness into the compiler that cannot be controlled by the user (hindering reproducability). It would then be possible for repeated builds (such as a nightly job) to sporadically fail.
candidate 4 (found by 3 of 36 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## audience - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] 9 Possible extensions of current design      0/1/0  -> 0.33
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/2/0  -> 1.33
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/1  -> 0.33
  [9] 8 Implementation experience                  1/1/1  -> 1.00
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 2 (found by 3 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash&lt;T*>` having inconsistent values between compile time and runtime.
candidate 3 (found by 2 of 36 passes): A straightforward approach would be to specialize `hash<meta::info>`, but `hash<T>` in general is not constexpr-friendly due to its runtime requirements, so it would be inconsistent with compile-time hashing of other types.
candidate 4 (found by 2 of 36 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection. Our proposal provides a short and effective solution without needing to sort a list of reflected types.

## vehicle - grade 1.17 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/2  -> 1.33
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     1/0/1  -> 0.67
  [7] 6 Design decisions                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 3 of 36 passes): More crucially, if we provide users with functionality that they need to wrap themselves, we should just standardize the boilerplate instead.
candidate 3 (found by 1 of 36 passes): Moreover, it enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.
candidate 4 (found by 1 of 36 passes): It enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.

## coordination - grade 0.83 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/1  -> 0.33
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/1/1  -> 0.67
  [7] 6 Design decisions                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/0/0  -> 0.33
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 36 passes): thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 3 (found by 1 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 4 (found by 1 of 36 passes): it enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.

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

## implementation - grade 0.67  [binary: max] (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           0/1/1  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/2  -> 0.67
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): We attempted to find a middle ground that captures the best of both worlds.
candidate 2 (found by 1 of 36 passes): We have implemented an [unstable](https://github.com/bloomberg/clang-p2996/pull/227) version and two semi-stable versions of the hash on Bloomberg’s Clang fork.

-->
