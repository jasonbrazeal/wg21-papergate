Verdict: Adequate (6/14)

The paper gives a reasonably clear account of the problem and of possible implementation directions, but it leaves several parts of its standardization case asserted rather than demonstrated. The thinnest support concerns why a standard change is needed at all, since the discussion of library workarounds, affected users, and implementation experience does not rise beyond claims.

- The strongest support is the explanation of why the degenerate `std::bit_cast` behavior matters and how the proposed change would only affect code that already has undefined behavior.
- The paper also establishes that prior art and alternatives exist, including compiler builtins and an earlier more ambitious revision.
- The case for affected users is weaker, resting mainly on a claimed frequent interaction with `_BitInt` rather than on demonstrated usage.
- The most glaring omission is the absence of an established argument for why this requires standardization rather than a compiler diagnostic, library facility, or other non-standard remedy.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 6 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 6.00   accumulate 5.50   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.17  implementation 1.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 5.00 / 5.50   (all 3 samples: 5.50)
headings: h2 9
on threshold: none
splits: audience[4] 1/0/0  coordination[4] 1/0/0  insufficiency[4] 0/0/1
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
candidate 2 (found by 3 of 30 passes): The proposed change only makes the degenerate form of `std::bit_cast` ill-formed, i.e. it raises an error in code that contained unconditional UB.
candidate 3 (found by 3 of 30 passes): The single-function solution is problematic because `std::bit_cast` can be used to convert padded types to a byte array without undefined behavior and with zero overhead.
candidate 4 (found by 2 of 30 passes): This behavior is a footgun, and is not very useful. If users wanted a function that always has UB, they should be writing `std::unreachable`, not `std::bit_cast`.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/0  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R3]]), considering that most `_BitInt` types (at least 7/8) have padding bits.

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R3]](https://wg21%2elink/p3666r3)), considering that most `_BitInt` types (at least 7/8) have padding bits.
candidate 2 (found by 3 of 30 passes): The most straight-forward implementation strategy is to add a check in the compiler's `__builtin_bit_cast` intrinsic for the degenerate form of `std::bit_cast`.
candidate 3 (found by 2 of 30 passes): R0 of this paper was more ambitious and presented two approaches:
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
  [4] 2. Introduction                              1/0/0  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Compilers also have no warning for the degenerate form at the time of writing.

## insufficiency - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/1  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): That makes it possible to implement a proper conversion from `long double` to `__int128`, although it requires multiple steps:

## implementation - grade 1.00  [binary: max] (fired in 1 of 10 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 0/0/0  -> 0.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): GCC compiles this code; Clang already rejects both assertions.

-->
