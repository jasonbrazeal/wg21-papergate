Verdict: Adequate (7/14)

The paper offers a solid motivation for addressing the degenerate `std::bit_cast` case and shows meaningful engagement with prior art and alternatives, but it leaves several essential standardization questions largely unanswered. The thinnest areas are the absence of a clear audience analysis, a justification for why this belongs in the standard rather than in compiler diagnostics or a library facility, and concrete implementation experience beyond a single in-progress warning.

- The strongest support is the clear explanation of why the current behavior is a footgun and how the proposed change would only affect code already containing undefined behavior.
- The paper also credibly establishes prior art and alternatives, including the Clang warning effort and the `__builtin_clear_padding` idiom.
- The most glaring omission is the lack of any established account of who is affected by the change, which weakens the case for urgency and scope.
- The paper also does not establish why the standard is the right venue, since the problem could plausibly be addressed through compiler warnings or a library facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.67   accumulate 6.50   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 1.00  implementation 1.33
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 6.50 / 7.00   (all 3 samples: 6.50)
headings: h2 9
on threshold: insufficiency
splits: prior_art[4] 1/2/2  coordination[4] 0/1/0  implementation[4] 0/1/1
        implementation[7] 1/1/2
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
candidate 1 (found by 3 of 30 passes): This behavior is a footgun, and is not very useful.
candidate 2 (found by 3 of 30 passes): The proposed change only makes the degenerate form of `std::bit_cast` ill-formed, i.e. it raises an error in code that contained unconditional UB.
candidate 3 (found by 3 of 30 passes): The single-function solution is problematic because `std::bit_cast` can be used to convert padded types to a byte array without undefined behavior and with zero overhead.
candidate 4 (found by 2 of 30 passes): When bit-casting a type containing padding bits to a type with no padding bits, `std::bit_cast` degenerates into an alternative spelling for `std::unreachable` (some exceptions apply).

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

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/2/2  -> 1.67
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R3]](https://wg21%2elink/p3666r3)), considering that most `_BitInt` types (at least 7/8) have padding bits.
candidate 2 (found by 3 of 30 passes): R0 of this paper was more ambitious and presented two approaches:
candidate 3 (found by 3 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.
candidate 4 (found by 2 of 30 passes): it was suggested to clear the padding *before* bit-casting. That is, standardizing [`__builtin_clear_padding`](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fclear_005fpadding) and using an idiom such as:

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

## coordination - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Compilers also have no warning for the degenerate form at the time of writing.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/2  -> 1.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): GCC compiles this code; Clang already rejects both assertions.
candidate 2 (found by 2 of 30 passes): However, there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.
candidate 3 (found by 1 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.

-->
