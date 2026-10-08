Verdict: Strong (9/14)

The paper gives a reasonably solid account of existing practice and real-world usage, but it leaves the affirmative case for standardization incomplete because it does not show why the standard itself must change or why a library solution would be inadequate. The strongest material concerns implementation experience and interoperability, while the thinnest concerns the necessity of standardizing the behavior at all.

- The paper establishes widespread existing use and implementation support, including libc++ and libstdc++ extensions and thousands of code files already relying on the behavior.
- It also shows coordination with prior national-body comments and library issue discussions, making clear that the change would align the standard with de facto practice.
- The most glaring omission is the absence of an established reason why the standard, rather than a library or continued implementation extension, is the right vehicle for the change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 5 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 8.00   accumulate 9.67   max 10.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 1.50  vehicle 0.00  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.50 / 8.50 / 9.50   (all 3 samples: 9.17)
headings: h2 7
on threshold: prior_art, coordination
splits: audience[4] 1/1/0  audience[6] 0/2/0  prior_art[4] 1/0/1  coordination[3] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Use of `signed char` or `unsigned char` in `<random>` currently results in undefined behavior.
candidate 2 (found by 3 of 24 passes): The ability to generate random bytes or octets is extremely valuable for fuzz testing.
candidate 3 (found by 3 of 24 passes): The current restriction which forbids `unsigned char` is bad, but it's not obvious how much the restriction should be relaxed.

## audience - grade 2.00 (fired in 4 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Motivation                                1/1/0  -> 0.67
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 0/2/0  -> 0.67
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): A GitHub code search for [`language:C++ /(?-i)uniform_int_distribution<((unsigned |signed |)char|(std::)?u?int8_t|i8|u8)>/`](https://github.com/search?q=language%3AC%2B%2B+%2F%28%3F-i%29uniform_int_distribution%3C%28%28unsigned+%7Csigned+%7C%29char%7C%28std%3A%3A%29%3Fu%3Fint8_t%7Ci8%7Cu8%29%3E%2F&type=code) shows 8.4K files already using e.g. `std::uniform_int_distribution<uint8_t>`.
candidate 2 (found by 3 of 24 passes): [GitHub code search](https://github.com/search?q=language%3AC%2B%2B+%2F(%3F-i)linear_congruential_engine%3C((unsigned+|signed+|)char|(std%3A%3A)%3Fu%3Fint8_t|i8|u8)%2F&type=code) finds uses of `linear_congruential_engine<uint8_t>`.
candidate 3 (found by 2 of 24 passes): Support for `unsigned char` and `signed char` in distributions would be useful.
candidate 4 (found by 1 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension.

## prior_art - grade 1.50 (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                1/0/1  -> 0.67
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 1/1/1  -> 1.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): NB comment [[RU-272]](https://github%2ecom/cplusplus/nbballot/issues/847) is resolved by this paper.
candidate 2 (found by 3 of 24 passes): While [[LWG4109]](https://cplusplus%2egithub%2eio/LWG/issue4109) offers the option to make the program ill-formed when the existing restrictions are not satisfied (Option B in the issue), it fails to mention that this would break thousands of files of existing code; see §1. Introduction.
candidate 3 (found by 3 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension.
candidate 4 (found by 1 of 24 passes): `uniform_int_distribution<unsigned int>(0, 255)` is functionally equivalent to `uniform_int_distribution<unsigned char>()`.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.67 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/0/2  -> 1.33
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): A GitHub code search for [`language:C++ /(?-i)uniform_int_distribution<((unsigned |signed |)char|(std::)?u?int8_t|i8|u8)>/`](https://github.com/search?q=language%3AC%2B%2B+%2F%28%3F-i%29uniform_int_distribution%3C%28%28unsigned+%7Csigned+%7C%29char%7C%28std%3A%3A%29%3Fu%3Fint8_t%7Ci8%7Cu8%29%3E%2F&type=code) shows 8.4K files already using e.g. `std::uniform_int_distribution<uint8_t>`.
candidate 2 (found by 1 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted
candidate 3 (found by 1 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted; see: [https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49](https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49).
candidate 4 (found by 1 of 24 passes): The MSVC STL has a `static_assert` which prevents instantiation of `std::uniform_int_distribution<unsigned char>`... libc++ supports `signed char` and `unsigned char` as an extension... libstdc++ supports any integral type as an extension.

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is possible because both libstdc++ and libc++ support those types as an extension; see §4. Implementation experience.
candidate 2 (found by 3 of 24 passes): libstdc++ permits `__int128` in most of `<random>`, but rejects `linear_congruential_engine<__int128>` using:
candidate 3 (found by 3 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted; see: https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49

-->
