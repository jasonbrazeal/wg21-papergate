Verdict: Adequate to Strong (7/14)

The paper offers a solid foundation for why character-type support in `to_chars` and `from_chars` matters and shows meaningful implementation precedent, but it leaves several key arguments about standardization need asserted rather than demonstrated. The thinnest areas are the absence of a clearly identified affected audience and the underdeveloped case for why this must be standardized rather than delivered through a library.

- The strongest support comes from the established motivation around `char8_t` and UTF-8, where the paper shows concrete usability problems and real-world relevance to formats like JSON.
- The paper also credibly establishes prior art and alternatives, including stale proposals and the lack of existing transcoding facilities in the standard library.
- The most glaring omission is the failure to establish who is affected, leaving the scope and urgency of the problem largely undefined.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.33   accumulate 7.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.50  insufficiency 0.33  implementation 1.67
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 6.50   (all 3 samples: 7.17)
headings: h2 8
on threshold: implementation
splits: prior_art[8] 1/2/0  vehicle[4] 2/1/1  insufficiency[4] 0/1/1  implementation[7] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `std::to_chars` and `std::from_chars` currently only provide support for `char`, which causes several usability problems.
candidate 2 (found by 3 of 27 passes): Due to how common UTF-8 is and due to `char8_t` now regularly being used to represent UTF-8 text in C++ software, the motivation in §2. Introduction mostly refers to `char8_t`.
candidate 3 (found by 2 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere:
candidate 4 (found by 1 of 27 passes): File formats such as JSON require the use of Unicode character encodings, so an application that deals with JSON may want to use `char8_t` in its APIs and internally.

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

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   1/2/0  -> 1.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It is worth noting that there is a stale proposal [[P2584R0]](https://wg21%2elink/p2584r0) "A More Composable `from_chars`" which proposes additional overloads taking `std::span`, superseding the even more stale [[P2007R0]](https://wg21%2elink/p2007r0) "`std::from_chars` should work with `std::string_view`".
candidate 2 (found by 3 of 27 passes): libc++ supports EBCDIC and is used on z/OS (see [https://reviews.llvm.org/D114813](https://reviews.llvm.org/D114813)). Another library with EBCDIC support is the IBM XL C++ for z/OS, but according to [IBM's documentation](https://www.ibm.com/docs/en/zos/3.1.0?topic=files-xl-c-header), no `<charconv>` implementation exists yet.
candidate 3 (found by 2 of 27 passes): The user could use the `std::to_chars(char*, char*, int, int)` overload and then transcode to UTF-8 as `char8_t`, but the standard library provides no transcoding facilities yet.
candidate 4 (found by 1 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere:

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/1/1  -> 1.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere:
candidate 2 (found by 1 of 27 passes): The lack of support for `char8_t` (and other character types) severely limits what can be done elsewhere

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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

## insufficiency - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The user could use the `std::to_chars(char*, char*, int, int)` overload and then transcode to UTF-8 as `char8_t`, but the standard library provides no transcoding facilities yet.

## implementation - grade 1.67  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/2/1  -> 1.67
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Any existing implementation of `std::to_chars` and `std::from_chars` for a platform with ASCII-based `char` (Windows, POSIX, etc.) is *numerically* implementing what is proposed here.

-->
