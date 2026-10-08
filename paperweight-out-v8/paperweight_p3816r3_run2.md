Verdict: Strong (8/14)

The paper offers a mixed case for its own standardization, with its strongest grounding in prior art, implementer feedback, and coordination concerns, but it leaves several central justifications asserted rather than demonstrated. The thinnest support concerns who would actually be affected by the facility and why existing library-level approaches cannot meet the need, which weakens the argument that standardization is necessary.

- The paper’s most concrete support comes from compiler implementers in Clang, EDG, and GCC, whose feedback anchors the proposal in real implementation experience and coordination.
- The discussion of prior art and alternatives is credited as established, particularly the connection to P2830’s acknowledged difficulty with `mp_unique` and the absence of an existing compile-time hash facility.
- The paper only claims, without fully establishing, why the feature matters and why it belongs in the standard rather than in a library, relying on general statements about future interfaces and unordered containers.
- The most glaring omission is the complete absence of any account of who is affected by the problem, leaving the motivating user base and practical impact unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.67   accumulate 9.00   max 9.00

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 1.50  insufficiency 0.50  implementation 1.67
sample agreement: 83 of 91 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.50 / 8.00 / 8.00   (all 3 samples: 7.67)
headings: h2 12
on threshold: coordination, implementation
splits: motivation[5] 0/1/1  motivation[6] 1/0/1  motivation[10] 2/1/1  prior_art[9] 2/1/2
        vehicle[3] 0/0/1  vehicle[6] 0/1/1  coordination[6] 2/0/0  implementation[7] 1/2/2
## END SUMMARY

## motivation - grade 1.17 (fired in 5 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Examples                                   0/1/1  -> 0.67
  [6] 5 Impact                                     1/0/1  -> 0.67
  [7] 6 Design decisions                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      2/1/1  -> 1.33
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Ultimately, the goal of this paper is to provide a robust way to hash values of type `meta::info`.
candidate 2 (found by 2 of 39 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys, and potentially with other types in future.
candidate 3 (found by 2 of 39 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection.
candidate 4 (found by 2 of 39 passes): It introduces the first example of a compile-time hash facility.

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

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 6)  (SHARED PASSAGE)
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
  [9] 8 Implementation experience                  2/1/2  -> 1.67
  [10] 9 Possible extensions of current design      2/2/2  -> 2.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 2/2/2  -> 2.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In [[P2830]](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2830r10.html) (7.3) the authors discuss the infeasibility of implementing `mp_unique` using value-based reflection. Our proposal provides a short and effective solution without needing to sort a list of reflected types.
candidate 2 (found by 3 of 39 passes): It introduces the first example of a compile-time hash facility.
candidate 3 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.
candidate 4 (found by 3 of 39 passes): Feedback from GCC and Clang implementers indicates that the most practical strategy is to reuse existing mangling infrastructure to implement the hashing.

## vehicle - grade 0.83 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
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
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A robust hash for `meta::info` requires compiler support, thus we believe such a facility belongs in the standard library.
candidate 2 (found by 2 of 39 passes): it enables future standard library features: new `consteval` functions may naturally require unordered containers as part of their interfaces, and `consteval_hash` provides the uniform mechanism needed to support such APIs.
candidate 3 (found by 1 of 39 passes): The purpose of this facility is to provide a standard interface for compile-time hashing, thereby allowing unordered containers such as `unordered_map` and `unordered_set` to be used with `meta::info` keys

## coordination - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Examples                                   0/0/0  -> 0.00
  [6] 5 Impact                                     2/0/0  -> 0.67
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
  [7] 6 Design decisions                           1/2/2  -> 1.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Implementation experience                  0/0/0  -> 0.00
  [10] 9 Possible extensions of current design      0/0/0  -> 0.00
  [11] 10 Acknowledgements                          0/0/0  -> 0.00
  [12] 11 Appendix: Alternate names for consteva... 0/0/0  -> 0.00
  [13] 12 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): During discussion of [R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p3816r2.html) of the paper, we received feedback from compiler developers working on C++26 reflection implementations in Clang, EDG, and GCC.

-->
