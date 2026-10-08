Verdict: Strong (10/14)

The paper offers substantial evidence that the restriction on character types in `<random>` is already being ignored in practice, with real code and major standard library implementations treating the current undefined behavior as an accepted extension. Its case is strongest on existing usage and implementation experience, while the thinnest part is the argument for why standardization—rather than continued reliance on library extensions—is necessary.

- The paper clearly establishes that thousands of files already use `uniform_int_distribution` with character types despite the undefined behavior, and that both libc++ and libstdc++ support these types as extensions.
- The paper shows a concrete path to implementation by pointing to existing support in major standard libraries, including specific code references.
- The paper does not establish why a library-level solution would be insufficient, leaving the necessity of standardization itself unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.67/14)

Provisionally addressed: 6 of 7. Provisional points: 9.67 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.67   corroborated 9.33   accumulate 9.83   max 10.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 1.83  vehicle 0.17  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 9.00 / 10.50 / 9.50   (all 3 samples: 9.67)
headings: h2 8
on threshold: coordination
splits: audience[6] 0/2/0  prior_art[7] 2/2/1  vehicle[4] 0/1/0  coordination[4] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The ability to generate random bytes or octets is extremely valuable for fuzz testing.
candidate 2 (found by 3 of 27 passes): The current restriction which forbids `unsigned char` is bad, but it's not obvious how much the restriction should be relaxed.
candidate 3 (found by 2 of 27 passes): Use of `signed char` or `unsigned char` in `&lt;random>` currently results in undefined behavior.
candidate 4 (found by 1 of 27 passes): Use of `signed char` or `unsigned char` in `<random>` currently results in undefined behavior.

## audience - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/2/0  -> 0.67
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): A GitHub code search for [`language:C++ /(?-i)uniform_int_distribution<((unsigned |signed |)char|(std::)?u?int8_t|i8|u8)>/`](https://github.com/search?q=language%3AC%2B%2B+%2F%28%3F-i%29uniform_int_distribution%3C%28%28unsigned+%7Csigned+%7C%29char%7C%28std%3A%3A%29%3Fu%3Fint8_t%7Ci8%7Cu8%29%3E%2F&type=code) shows 8.4K files already using e.g. `std::uniform_int_distribution<uint8_t>`.
candidate 2 (found by 3 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension.
candidate 3 (found by 1 of 27 passes): [GitHub code search](https://github.com/search?q=language%3AC%2B%2B+%2F(%3F-i)linear_congruential_engine%3C((unsigned+|signed+|)char|(std%3A%3A)%3Fu%3Fint8_t|i8|u8)%2F&type=code) finds uses of `linear_congruential_engine<uint8_t>`.

## prior_art - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 2/2/1  -> 1.67
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Generating octets is effectively supported already. `uniform_int_distribution<unsigned int>(0, 255)` is functionally equivalent to `uniform_int_distribution<unsigned char>()`.
candidate 2 (found by 3 of 27 passes): While [[LWG4109]](https://cplusplus%2egithub%2eio/LWG/issue4109) offers the option to make the program ill-formed when the existing restrictions are not satisfied (Option B in the issue), it fails to mention that this would break thousands of files of existing code; see §2. Introduction.
candidate 3 (found by 2 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted
candidate 4 (found by 1 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension.

## vehicle - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This paper resolves all these known defects and discrepancies of [[rand.req.genl]](https://eel.is/c++draft/rand.req.genl) in one fell swoop.

## coordination - grade 1.67 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/2/2  -> 1.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): A GitHub code search for [`language:C++ /(?-i)uniform_int_distribution<((unsigned |signed |)char|(std::)?u?int8_t|i8|u8)>/`](https://github.com/search?q=language%3AC%2B%2B+%2F%28%3F-i%29uniform_int_distribution%3C%28%28unsigned+%7Csigned+%7C%29char%7C%28std%3A%3A%29%3Fu%3Fint8_t%7Ci8%7Cu8%29%3E%2F&type=code) shows 8.4K files already using e.g. `std::uniform_int_distribution<uint8_t>`.
candidate 2 (found by 1 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension.
candidate 3 (found by 1 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted
candidate 4 (found by 1 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted;

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This is possible because both libstdc++ and libc++ support those types as an extension; see §5. Implementation experience.
candidate 2 (found by 3 of 27 passes): libstdc++ permits `__int128` in most of `<random>`, but rejects `linear_congruential_engine<__int128>` using:
candidate 3 (found by 2 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted; see: https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49
candidate 4 (found by 1 of 27 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted; see: [https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49](https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49).

-->
