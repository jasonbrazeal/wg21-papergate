Verdict: Strong (8/14)

The paper offers a mixed case for its own standardization, with its strongest material concentrated in the rationale for a compile-time hash facility and the evidence of implementer engagement. The support becomes noticeably thinner when the paper moves from motivation to the specific necessity of standardization, particularly around demonstrating real implementation experience and ruling out a library-only solution.

- The paper most convincingly establishes why the feature matters and that relevant prior art and implementer feedback exist, especially through the connection to reflection and the reported discussions with Clang, EDG, and GCC developers.
- The case for coordination and interoperability is reasonably grounded in the need for compiler support and the reported agreement that hash values should be stable across translation units and compiler runs.
- The paper asserts but does not adequately establish who is affected, since the claim that the relevant types are widely used as keys is not backed by evidence.
- The most glaring omission is implementation experience, where the paper cites discussions with compiler developers but provides no actual prototype, usage data, or implementation results to substantiate feasibility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 7 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.00   accumulate 8.83   max 10.00

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 2.00  vehicle 0.67  coordination 1.50  insufficiency 0.50  implementation 1.33
sample agreement: 83 of 91 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.50 / 8.50 / 7.50   (all 3 samples: 7.83)
headings: h2 12
on threshold: motivation, coordination
splits: motivation[5] 2/1/0  motivation[7] 0/1/1  audience[10] 0/1/1  prior_art[5] 2/0/0
        prior_art[9] 1/2/2  vehicle[6] 1/0/0  coordination[6] 2/1/0  implementation[7] 1/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 6 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/1/0  -> 1.00
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           0/1/1  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      1/1/1  -> 1.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Enabling hash-based associative containers as a first step will improve the ergonomics of compile-time programming and bring it more in line with runtime code.
candidate 2 (found by 3 of 39 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 2 of 39 passes): Ultimately, the goal of this paper is to provide a robust way to hash values of type `meta::info`.
candidate 4 (found by 2 of 39 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [P3372] concerning `std::hash<T*>` having inconsistent values between compile-time and runtime.

## audience - grade 0.33 (fired in 1 of 13 sections, strong in 0)
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
  [10] 9 Possible extensions of current design      0/1/1  -> 0.67
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): These types are both widely used as keys in unordered associative containers and straightforward to support in a portable, implementation-independent manner.

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Examples                                   2/0/0  -> 0.67
  [6] 5 Impact                                     1/1/1  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  1/2/2  -> 1.67
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 2/2/2  -> 2.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): It introduces the first example of a compile-time hash facility.
candidate 2 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.
candidate 3 (found by 3 of 39 passes): Feedback from GCC and Clang implementers indicates that the most practical strategy is to reuse existing mangling infrastructure to implement the hashing.
candidate 4 (found by 2 of 39 passes): Notably, extending initial support to pointer types would help in resolving the implementation experience issues highlighted in [[P3372]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3372r3.html) concerning `std::hash<T*>` having inconsistent values between compile-time and runtime.

## vehicle - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
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
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 1 of 39 passes): It enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.

## coordination - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     2/1/0  -> 1.00
  [7] 6 Design decisions                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 3 of 39 passes): Clang developers agreed that hash values should be stable across translation units and compiler runs.
candidate 3 (found by 1 of 39 passes): The issue arises from the fact that we do not require hash values to remain consistent across different translation units.
candidate 4 (found by 1 of 39 passes): It introduces the first example of a compile-time hash facility.

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     0/0/0  -> 0.00
  [7] 6 Design decisions                           1/2/1  -> 1.33
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.

-->
