Verdict: Strong (9/14)

The paper gives a reasonably concrete account of why the current restrictions are problematic and shows that the change is already live in major implementations, but it leans heavily on that implementation experience and on code-search evidence rather than fully developing the affected-user and standards-process arguments. The thinnest part is the absence of any discussion of why a library-only solution would be insufficient, which leaves a key part of the standardization case unaddressed.

- The strongest support is the implementation experience, with both libstdc++ and libc++ already accepting the relevant character types as an extension.
- The paper also clearly establishes the motivating defect by pointing to undefined behavior for `signed char` and `unsigned char` in `<random>`.
- The affected-user case is only claimed, resting on GitHub search counts and extension support rather than a fuller demonstration of widespread or unavoidable reliance.
- The most glaring omission is the lack of any established argument for why a library cannot solve the problem, leaving the need for a standard change incompletely justified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 6 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 8.67   accumulate 9.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 0.33  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 48 of 56 section-criterion pairs unanimous (86%)
single-sample totals would have been: 10.50 / 7.50 / 9.00   (all 3 samples: 8.67)
headings: h2 7
on threshold: audience
splits: motivation[3] 2/0/2  audience[3] 2/0/0  audience[5] 0/0/2  prior_art[2] 1/0/0
        vehicle[3] 1/1/0  coordination[3] 2/0/0  coordination[6] 2/0/2  implementation[5] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/0/2  -> 1.33
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The ability to generate random bytes or octets is extremely valuable for fuzz testing.
candidate 2 (found by 3 of 24 passes): The current restriction which forbids `unsigned char` is bad, but it's not obvious how much the restriction should be relaxed.
candidate 3 (found by 2 of 24 passes): Use of `signed char` or `unsigned char` in `&lt;random>` currently results in undefined behavior.
candidate 4 (found by 1 of 24 passes): Use of `signed char` or `unsigned char` in `<random>` currently results in undefined behavior.

## audience - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/0/0  -> 0.67
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/2  -> 0.67
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension.
candidate 2 (found by 1 of 24 passes): A GitHub code search for [`language:C++ /(?-i)uniform_int_distribution<((unsigned |signed |)char|(std::)?u?int8_t|i8|u8)>/`](https://github.com/search?q=language%3AC%2B%2B+%2F%28%3F-i%29uniform_int_distribution%3C%28%28unsigned+%7Csigned+%7C%29char%7C%28std%3A%3A%29%3Fu%3Fint8_t%7Ci8%7Cu8%29%3E%2F&type=code) shows 8.4K files already using e.g. `std::uniform_int_distribution<uint8_t>`.
candidate 3 (found by 1 of 24 passes): [GitHub code search](https://github.com/search?q=language%3AC%2B%2B+%2F(%3F-i)linear_congruential_engine%3C((unsigned+|signed+|)char|(std%3A%3A)%3Fu%3Fint8_t|i8|u8)%2F&type=code) finds uses of `linear_congruential_engine<uint8_t>`.

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Generating octets is effectively supported already. `uniform_int_distribution<unsigned int>(0, 255)` is functionally equivalent to `uniform_int_distribution<unsigned char>()`.
candidate 2 (found by 3 of 24 passes): While [[LWG4109]](https://cplusplus%2egithub%2eio/LWG/issue4109) offers the option to make the program ill-formed when the existing restrictions are not satisfied (Option B in the issue), it fails to mention that this would break thousands of files of existing code; see §1. Introduction.
candidate 3 (found by 3 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted
candidate 4 (found by 1 of 24 passes): NB comment [[RU-272]](https://github%2ecom/cplusplus/nbballot/issues/847) is resolved by this paper.

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/0  -> 0.67
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): This paper resolves all these known defects and discrepancies of [[rand.req.genl]](https://eel.is/c++draft/rand.req.genl) in one fell swoop.

## coordination - grade 1.00 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/0/0  -> 0.67
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 2/0/2  -> 1.33
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted; see: [https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49](https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49).
candidate 2 (found by 1 of 24 passes): A GitHub code search for [`language:C++ /(?-i)uniform_int_distribution<((unsigned |signed |)char|(std::)?u?int8_t|i8|u8)>/`](https://github.com/search?q=language%3AC%2B%2B+%2F%28%3F-i%29uniform_int_distribution%3C%28%28unsigned+%7Csigned+%7C%29char%7C%28std%3A%3A%29%3Fu%3Fint8_t%7Ci8%7Cu8%29%3E%2F&type=code) shows 8.4K files already using e.g. `std::uniform_int_distribution<uint8_t>`.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    2/0/2  -> 1.33
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is possible because both libstdc++ and libc++ support those types as an extension; see §4. Implementation experience.
candidate 2 (found by 2 of 24 passes): libc++ supports `signed char` and `unsigned char` as an extension. This is the minimum amount of support assuming this paper is accepted; see: https://github.com/llvm/llvm-project/blob/9d075d271ff15ec153ada3413d294540206a15ed/libcxx/include/__random/is_valid.h#L49
candidate 3 (found by 1 of 24 passes): GCC having support for this already (see §4. Implementation experience)
candidate 4 (found by 1 of 24 passes): despite GCC having support for this already (see §4. Implementation experience)

-->
