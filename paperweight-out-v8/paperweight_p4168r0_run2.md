Verdict: Strong (10/14)

The paper offers solid support in several areas, particularly in documenting divergent implementation behavior, prior standardization attempts, and real implementation experience. The case is thinnest where it asserts rather than demonstrates the scale of user impact and the necessity of a standard-library rather than library-level solution.

- The strongest support is the concrete evidence that implementations already diverge from each other and from the standard’s wording, with years of shipping experience behind the proposed direction.
- The paper also clearly establishes the relevant prior art and alternatives, including earlier proposals and LWG issues that attempted or partially addressed the same problem.
- The most glaring omission is the lack of substantiation for the claim that changing `std::from_chars` behavior would break substantial amounts of existing code, which is asserted without supporting evidence.
- The paper likewise does not establish why a library solution such as `boost::from_chars_erange` is insufficient, beyond an arguable recommendation rather than a demonstrated need for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 10.67   accumulate 9.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.67  coordination 2.00  insufficiency 0.33  implementation 2.00
sample agreement: 50 of 56 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 9.50 / 10.00   (all 3 samples: 9.50)
headings: h2 7
on threshold: none
splits: vehicle[4] 1/2/1  coordination[2] 1/0/0  insufficiency[3] 0/0/2  implementation[2] 0/1/1
        implementation[3] 2/1/2  implementation[5] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The handling of floating-point overflow and underflow in `std::from_chars` is inconsistent; the implementations diverge from each other, and every implementation diverges from the wording in the standard.
candidate 2 (found by 3 of 24 passes): Changing the behavior of `std::from_chars` can break substantial amounts of existing code.
candidate 3 (found by 2 of 24 passes): This is an ineffective way to communicate the behavior of `std::from_chars` and should be rewritten so that the accepted pattern can be understood solely through [[charconv.from.chars]].
candidate 4 (found by 1 of 24 passes): This is an ineffective way to communicate the behavior of `std::from_chars` and should be rewritten so that the accepted pattern can be understood solely through [[charconv.from.chars]](https://eel.is/c++draft/charconv.from.chars).

## audience - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    1/1/1  -> 1.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Changing the behavior of `std::from_chars` can break substantial amounts of existing code.

## prior_art - grade 2.00 (fired in 6 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Editorial problems                        2/2/2  -> 2.00
  [7] 5. Wording                                   1/1/1  -> 1.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper supersedes [[P2827R1]](https://wg21%2elink/p2827r1) and fixes [[LWG3081]](https://wg21%2elink/LWG3081), [[LWG3082]](https://wg21%2elink/LWG3082), and [[LWG3456]](https://wg21%2elink/LWG3456).
candidate 2 (found by 3 of 24 passes): In 2023, [[P2827R1]](https://wg21%2elink/p2827r1) attempted to solve this issue, but died in LEWG eventually.
candidate 3 (found by 3 of 24 passes): [[LWG3456]](https://wg21%2elink/LWG3456) performs such a rewrite, but does not fully decouple `std::from_chars` from the C wording.
candidate 4 (found by 3 of 24 passes): The description deliberately uses code points to avoid ever spelling a character literal, in preparation for [[P3876R1]](https://wg21%2elink/p3876r1), which adds support for `char8_t` and other character types.

## vehicle - grade 0.67 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    1/2/1  -> 1.33
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): `std::from_chars` should have that same behavior to increase ISO/IEC 60559 conformance.
candidate 2 (found by 1 of 24 passes): Changing the behavior of `std::from_chars` can break substantial amounts of existing code.

## coordination - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): floating-point implementations of `std::from_chars` have already existed for years (MSVC STL since 2018, libstdc++ since 2021, libc++ since 2025). Changing the behavior of `std::from_chars` can break substantial amounts of existing code.
candidate 2 (found by 1 of 24 passes): The handling of floating-point overflow and underflow in `std::from_chars` is inconsistent; the implementations diverge from each other, and every implementation diverges from the wording in the standard.
candidate 3 (found by 1 of 24 passes): At the time of writing, implementations behave as shown in the table below when parsing a string as `float` (binary32).
candidate 4 (found by 1 of 24 passes): The wording is defective, implementations diverge, and users suffer from it to the point where `boost::from_chars_erange` should arguably be recommended to users over the standard feature; at least it is portable and well-specified.

## insufficiency - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/2  -> 0.67
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): users suffer from it to the point where `boost::from_chars_erange` ([[BoostCharConv]](https://www%2eboost%2eorg/doc/libs/latest/libs/charconv/doc/html/charconv%2ehtml)) should arguably be recommended to users over the standard feature; at least it is portable and well-specified.

## implementation - grade 2.00  [binary: max] (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1. Introduction                              2/1/2  -> 1.67
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/2/2  -> 1.67
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): At the time of writing, implementations behave as shown in the table below when parsing a string as `float` (binary32).
candidate 2 (found by 2 of 24 passes): The handling of floating-point overflow and underflow in `std::from_chars` is inconsistent; the implementations diverge from each other, and every implementation diverges from the wording in the standard.
candidate 3 (found by 2 of 24 passes): floating-point implementations of `std::from_chars` have already existed for years (MSVC STL since 2018, libstdc++ since 2021, libc++ since 2025).
candidate 4 (found by 2 of 24 passes): The proposed behavior has been released in MSVC STL and libc++, except that the behavior in §2.5. Further edge cases does not need to be implemented and only exists on paper for these implementations.

-->
