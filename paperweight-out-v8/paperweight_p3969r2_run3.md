Verdict: Adequate (6/14)

The paper offers a narrow but real justification for changing `std::bit_cast` behavior around padding bits, but it leaves most of the case for standardization unargued. The strongest material concerns the nature of the problem and the existence of prior work, while the thinnest areas are the absence of any identified affected audience and the lack of a positive argument that the standard is the right venue.

- The paper establishes that bit-casting a type with padding bits to a type without them currently produces unconditional undefined behavior, and that making this ill-formed would convert a footgun into a diagnosable error.
- The paper establishes meaningful prior art and alternatives, including a Clang warning implementation and discussion of a `__builtin_clear_padding` idiom.
- The paper claims but does not establish that a library solution would be insufficient, resting on a single assertion about `constexpr` implementability.
- The paper does not establish who is affected by the problem or why standardization, rather than continued compiler diagnostics or other mechanisms, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 9
on threshold: insufficiency
splits: implementation[4] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   1/1/1  -> 1.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): When bit-casting a type containing padding bits to a type with no padding bits, `std::bit_cast` degenerates into an alternative spelling for `std::unreachable` (some exceptions apply).
candidate 2 (found by 3 of 30 passes): This behavior is a footgun, and is not very useful.
candidate 3 (found by 3 of 30 passes): Overall, this design sweeps the problem under the rug with little benefit to the user.
candidate 4 (found by 3 of 30 passes): The proposed change only makes the degenerate form of `std::bit_cast` ill-formed, i.e. it raises an error in code that contained unconditional UB.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): R0 of this paper was more ambitious and presented two approaches:
candidate 2 (found by 3 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.
candidate 3 (found by 2 of 30 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R3]](https://wg21%2elink/p3666r3)), considering that most `_BitInt` types (at least 7/8) have padding bits.
candidate 4 (found by 2 of 30 passes): It was suggested to clear the padding *before* bit-casting. That is, standardizing [`__builtin_clear_padding`](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fclear_005fpadding) and using an idiom such as:

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This would likely mean that `constexpr std::clear_padding` is effectively unimplementable in current compilers.

## implementation - grade 1.00  [binary: max] (fired in 2 of 10 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): However, there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.
candidate 2 (found by 2 of 30 passes): GCC compiles this code; Clang already rejects both assertions.

-->
