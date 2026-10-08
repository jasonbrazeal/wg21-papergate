Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why character-type support in `to_chars` and `from_chars` would be useful, and it does better than many proposals at situating itself against prior work, but it leaves several parts of its standardization case asserted rather than demonstrated. The thinnest areas are the absence of evidence about who is affected, why a library solution would be insufficient, and whether there is meaningful implementation experience beyond an inference from existing numeric behavior.

- The strongest support is the established motivation that the current `char`-only interface creates real usability limits, especially for `char8_t` and UTF-8 text.
- The paper also credibly establishes prior art and alternatives, including stale related proposals and the relevance of EBCDIC-supporting implementations.
- The claim that standardization is necessary because the lack of character-type support “severely limits what can be done elsewhere” is repeated but not backed by concrete examples or affected users.
- The most glaring omission is the absence of any established case for why a library cannot address the problem, leaving a central question about the need for a standard change unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 5 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 7.00   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 4.50 / 7.00   (all 3 samples: 5.83)
headings: h2 8
on threshold: none
splits: motivation[5] 2/1/2  prior_art[6] 0/1/1  prior_art[8] 1/2/2  implementation[7] 1/0/2
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/1/2  -> 1.67
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `std::to_chars` and `std::from_chars` currently only provide support for `char`, which causes several usability problems.
candidate 2 (found by 3 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere
candidate 3 (found by 3 of 27 passes): Due to how common UTF-8 is and due to `char8_t` now regularly being used to represent UTF-8 text in C++ software, the motivation in §2. Introduction mostly refers to `char8_t`.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/1/1  -> 0.67
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   1/2/2  -> 1.67
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It is worth noting that there is a stale proposal [[P2584R0]](https://wg21%2elink/p2584r0) "A More Composable `from_chars`" which proposes additional overloads taking `std::span`, superseding the even more stale [[P2007R0]](https://wg21%2elink/p2007r0) "`std::from_chars` should work with `std::string_view`".
candidate 2 (found by 3 of 27 passes): libc++ supports EBCDIC and is used on z/OS (see [https://reviews.llvm.org/D114813](https://reviews.llvm.org/D114813)). Another library with EBCDIC support is the IBM XL C++ for z/OS, but according to [IBM's documentation](https://www.ibm.com/docs/en/zos/3.1.0?topic=files-xl-c-header), no `<charconv>` implementation exists yet.
candidate 3 (found by 2 of 27 passes): Support for `char8_t` and other Unicode character types in `std::to_chars` and `std::from_chars` is clearly useful.
candidate 4 (found by 2 of 27 passes): The proposal is a pure extension of the `std::to_chars` and `std::from_chars` overload sets.

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere:
candidate 2 (found by 1 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): File formats such as JSON require the use of Unicode character encodings, so an application that deals with JSON may want to use `char8_t` in its APIs and internally.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/0/2  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Any existing implementation of `std::to_chars` and `std::from_chars` for a platform with ASCII-based `char` (Windows, POSIX, etc.) is *numerically* implementing what is proposed here.

-->
