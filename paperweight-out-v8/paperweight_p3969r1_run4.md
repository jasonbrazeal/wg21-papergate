Verdict: Adequate (5/14)

The paper makes a credible start by explaining why the current behavior of `std::bit_cast` with padded types is a dangerous footgun, and it shows some awareness of alternatives and related cases, but it leaves most of the practical case for standardization unaddressed. The support is thinnest around who would actually be affected, why a language change rather than a library facility is necessary, and whether any implementation experience exists.

- The strongest support is the clear argument that bit-casting a padded type to a non-padded type currently produces unconditional undefined behavior and that making this ill-formed would only reject already-broken code.
- The paper also shows reasonable prior-art awareness by discussing `_BitInt` padding and the suggested `__builtin_clear_padding` alternative.
- The most glaring omission is the absence of any established audience or affected-user analysis, leaving the practical impact of the change unclear.
- The paper also fails to establish why the standard itself must act, since the library-based alternative is only asserted to be problematic rather than demonstrated as insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 3 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.00   accumulate 5.33   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 1.33  implementation 0.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 5.33)
headings: h2 9
on threshold: insufficiency
splits: motivation[5] 2/1/1  prior_art[4] 2/1/1  insufficiency[4] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/1/1  -> 1.33
  [6] 4. Impact on existing code                   1/1/1  -> 1.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): When bit-casting a type containing padding bits to a type with no padding bits, `std::bit_cast` degenerates into an alternative spelling for `std::unreachable` (some exceptions apply).
candidate 2 (found by 3 of 30 passes): The proposed change only makes the degenerate form of `std::bit_cast` ill-formed, i.e. it raises an error in code that contained unconditional UB.
candidate 3 (found by 3 of 30 passes): The single-function solution is problematic because `std::bit_cast` can be used to convert padded types to a byte array without undefined behavior and with zero overhead.
candidate 4 (found by 2 of 30 passes): This behavior is a footgun, and is not very useful. If users wanted a function that always has UB, they should be writing `std::unreachable`, not `std::bit_cast`.

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

## prior_art - grade 2.00 (fired in 3 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/1/1  -> 1.33
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R3]](https://wg21%2elink/p3666r3)), considering that most `_BitInt` types (at least 7/8) have padding bits.
candidate 2 (found by 3 of 30 passes): In the discussion of this proposal prior to publication, it was suggested to clear the padding *before* bit-casting. That is, standardizing [`__builtin_clear_padding`](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fclear_005fpadding) and using an idiom such as:
candidate 3 (found by 2 of 30 passes): R0 of this paper was more ambitious and presented two approaches:
candidate 4 (found by 1 of 30 passes): R0 of this paper was more ambitious and presented two approaches

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
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. Appendix: Single-function solution vs.... 2/2/2  -> 2.00
  [10] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This would likely mean that `constexpr std::clear_padding` is effectively unimplementable in current compilers.
candidate 2 (found by 2 of 30 passes): That makes it possible to implement a proper conversion from `long double` to `__int128`, although it requires multiple steps:

## implementation - grade 0.00  [binary: max] (fired in 0 of 10 sections, strong in 0)
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

-->
