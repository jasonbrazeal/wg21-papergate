Verdict: Adequate to Strong (7/14)

The paper offers meaningful support in a few areas, particularly in identifying the problem and showing that a compiler warning already targets the same cases, but it leaves several essential standardization questions largely unaddressed. The thinnest parts concern why the standard itself must change and how the change would fit with existing rules and implementations.

- The strongest support is the clear explanation that bit-casting a type with padding bits to one without padding bits currently produces unconditional undefined behavior with little user benefit.
- The paper also establishes prior art and alternatives by pointing to an active Clang warning and discussing a padding-clearing builtin as a possible idiom.
- The most glaring omission is the absence of any established case for why the standard is the necessary venue, as opposed to relying on compiler diagnostics or library-level approaches.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.33   accumulate 7.50   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 1.33  implementation 2.00
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 7.50 / 7.50   (all 3 samples: 7.50)
headings: h2 9
on threshold: insufficiency, implementation
splits: audience[7] 0/0/1  prior_art[4] 2/2/0  prior_art[7] 2/1/1  insufficiency[4] 1/1/0
        implementation[4] 0/1/1
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

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/1  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/0  -> 1.33
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/1/1  -> 1.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.
candidate 2 (found by 3 of 30 passes): In the discussion of this proposal prior to publication, it was suggested to clear the padding *before* bit-casting. That is, standardizing [`__builtin_clear_padding`](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fclear_005fpadding) and using an idiom such as:
candidate 3 (found by 2 of 30 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R3]](https://wg21%2elink/p3666r3)), considering that most `_BitInt` types (at least 7/8) have padding bits.
candidate 4 (found by 2 of 30 passes): R0 of this paper was more ambitious and presented two approaches: 1. Make the degenerate form of `std::bit_cast` ill-formed. Also add a new `std::bit_cast_zero_padding` function... 2. Make `std::bit_cast` behave like `std::bit_cast_zero_padding` without adding any new function.

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

## insufficiency - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/0  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This would likely mean that `constexpr std::clear_padding` is effectively unimplementable in current compilers.
candidate 2 (found by 2 of 30 passes): That makes it possible to implement a proper conversion from `long double` to `__int128`, although it requires multiple steps:

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Compilers also have no warning for the degenerate form at the time of writing.
candidate 2 (found by 2 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning
candidate 3 (found by 1 of 30 passes): there is an active Clang Pull Request at [https://github.com/llvm/llvm-project/pull/200362](https://github.com/llvm/llvm-project/pull/200362) which adds a `-Wbit-cast-padding` warning which triggers in exactly the same scenarios that this proposal would make ill-formed.

-->
