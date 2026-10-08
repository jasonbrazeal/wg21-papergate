Verdict: Adequate to Strong (8/14)

The paper offers solid motivation for a standard compile-time hash and shows meaningful engagement with prior art and implementer feedback, but it does not adequately establish who is affected or demonstrate that the facility must be standardized rather than provided some other way. The thinnest parts are the absence of any identified user population and the lack of concrete implementation experience beyond a fork.

- The strongest support is the clear motivation that hash-based containers for `meta::info` would improve compile-time programming ergonomics and address a known limitation in value-based reflection.
- The paper also credibly establishes prior art and alternatives by citing compiler-developer feedback and linking the facility to existing mangling infrastructure and pointer-hash consistency issues.
- The case for why the standard is necessary rests almost entirely on an unsupported assertion that robust hashing requires compiler support, with no argument ruling out library or tooling alternatives.
- The most glaring omission is that the paper never identifies who is affected by the lack of this facility, leaving the need for standardization abstract rather than tied to concrete users or use cases.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.33   accumulate 7.67   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 1.33  insufficiency 0.50  implementation 1.33
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.50 / 8.50 / 7.00   (all 3 samples: 7.67)
headings: h2 12
on threshold: coordination
splits: prior_art[4] 2/0/2  prior_art[5] 0/2/0  coordination[4] 1/1/0  implementation[9] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/2/2  -> 2.00
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys
candidate 2 (found by 3 of 39 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 3 (found by 3 of 39 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection.
candidate 4 (found by 3 of 39 passes): Con: it adds randomness into the compiler that cannot be controlled by the user (hindering reproducibility). It would then be possible for repeated builds (such as a nightly job) to sporadically fail.

## audience - grade 0.00 (fired in 0 of 13 sections, strong in 0)
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
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/0/2  -> 1.33
  [5] 4 Examples                                   0/2/0  -> 0.67
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

## vehicle - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
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

## coordination - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/0  -> 0.67
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 2 of 39 passes): Clang developers agreed that hash values should be stable across translation units and compiler runs.
candidate 3 (found by 1 of 39 passes): Clang developers also raised concerns about making hash stability a strong ABI commitment.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  2/2/0  -> 1.33
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.
candidate 2 (found by 2 of 39 passes): We have implemented an [**unstable**](https://github.com/bloomberg/clang-p2996/pull/227) version and two **semi-stable** versions of the hash on Bloomberg’s Clang fork.

-->
