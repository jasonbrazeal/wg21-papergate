Verdict: Adequate to Strong (7/14)

The paper offers meaningful support in the areas of motivation, prior art, and implementation experience, but its case for standardization is uneven: the arguments for why this belongs in the standard rather than in a library, and for how it coordinates with existing practice, rest on a single assertion about compiler support that is not developed into a demonstration. The thinnest area is the complete absence of any account of who is affected by the problem or the proposed solution.

- The strongest support comes from the concrete implementation experience on Bloomberg’s Clang fork, including unstable and semi-stable versions.
- The paper also establishes clear motivation by showing how compile-time hashing enables `meta::info` keys in unordered containers and addresses a known infeasibility in value-based reflection.
- The discussion of prior art and alternatives is well grounded, including the contrast with pointer hashing inconsistencies and the lack of a natural ordering for reflections.
- The most glaring omission is the failure to identify who is affected, leaving the audience and impact of the proposal entirely unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 7.67   max 9.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 7.50 / 7.50   (all 3 samples: 7.33)
headings: h2 11
on threshold: motivation, implementation
splits: motivation[4] 0/2/2  motivation[7] 1/2/1  prior_art[5] 2/0/2  prior_art[9] 0/1/1
        vehicle[6] 1/0/0  implementation[7] 1/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 6 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 0/2/2  -> 1.33
  [5] 4 Examples                                   2/2/2  -> 2.00
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           1/2/1  -> 1.33
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 2 (found by 3 of 36 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection.
candidate 3 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 4 (found by 3 of 36 passes): Con: it adds randomness into the compiler that cannot be controlled by the user (hindering reproducability). It would then be possible for repeated builds (such as a nightly job) to sporadically fail.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/0/2  -> 1.33
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/1/1  -> 0.67
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It introduces the first example of a compile-time hash facility.
candidate 2 (found by 3 of 36 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash&lt;T*>` having inconsistent values between compile time and runtime.
candidate 3 (found by 2 of 36 passes): it is natural to also ask what meaning, if any, should be assigned to `map<meta::info, T>` and `set<meta::info>`... reflections do not admit a natural or semantically meaningful total ordering.
candidate 4 (found by 2 of 36 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection. Our proposal provides a short and effective solution without needing to sort a list of reflected types.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
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
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 36 passes): It enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.

## coordination - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           1/1/0  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  2/2/2  -> 2.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We have implemented an [unstable](https://github.com/bloomberg/clang-p2996/pull/227) version and two semi-stable versions of the hash on Bloomberg’s Clang fork.
candidate 2 (found by 2 of 36 passes): We attempted to find a middle ground that captures the best of both worlds.

-->
