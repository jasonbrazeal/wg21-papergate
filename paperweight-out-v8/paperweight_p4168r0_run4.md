Verdict: Strong (10/14)

The paper offers solid grounding in the practical problem and the existing implementation landscape, but its case for standardization is uneven: it clearly documents divergence and prior work, while leaving the affected audience and the necessity of a standard-library fix more asserted than demonstrated.

- The strongest support comes from the concrete, credited account of implementation divergence and the history of prior attempts, which makes the need for clarified wording easy to see.
- The paper also establishes implementation experience well, since the proposed behavior is already released in major standard libraries.
- The thinnest support is around who is affected and why a library cannot suffice, where the paper relies on broad claims about breakage and user suffering without showing the scale or the limits of non-standard alternatives.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 11.00   accumulate 9.83   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 2.00  insufficiency 0.50  implementation 2.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 10.50 / 10.00 / 9.00   (all 3 samples: 9.83)
headings: h2 7
on threshold: none
splits: audience[5] 1/1/0  prior_art[7] 1/0/0  coordination[2] 0/1/0  insufficiency[3] 2/1/0
        implementation[4] 2/2/1
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
candidate 3 (found by 3 of 24 passes): This is an ineffective way to communicate the behavior of `std::from_chars` and should be rewritten so that the accepted pattern can be understood solely through [[charconv.from.chars]].

## audience - grade 0.83 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    1/1/1  -> 1.00
  [5] 3. Implementation experience                 1/1/0  -> 0.67
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Changing the behavior of `std::from_chars` can break substantial amounts of existing code.
candidate 2 (found by 2 of 24 passes): The proposed behavior has been released in MSVC STL and libc++
candidate 3 (found by 1 of 24 passes): floating-point implementations of `std::from_chars` have already existed for years (MSVC STL since 2018, libstdc++ since 2021, libc++ since 2025).

## prior_art - grade 2.00 (fired in 6 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Editorial problems                        2/2/2  -> 2.00
  [7] 5. Wording                                   1/0/0  -> 0.33
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper supersedes [[P2827R1]](https://wg21%2elink/p2827r1) and fixes [[LWG3081]](https://wg21%2elink/LWG3081), [[LWG3082]](https://wg21%2elink/LWG3082), and [[LWG3456]](https://wg21%2elink/LWG3456).
candidate 2 (found by 3 of 24 passes): In 2023, [[P2827R1]](https://wg21%2elink/p2827r1) attempted to solve this issue, but died in LEWG eventually.
candidate 3 (found by 3 of 24 passes): Neither [[LWG3081]](https://wg21%2elink/LWG3081) nor [[P2827R1]](https://wg21%2elink/p2827r1) fully resolve the defects in the wording. Each proposes a different value that should be written for overflow; the LWG issue proposes `numeric_limits<T>::max()`, and the paper proposes `1`.
candidate 4 (found by 3 of 24 passes): The proposed behavior has also been implemented as `boost::from_chars_erange`

## vehicle - grade 0.50 (fired in 1 of 8 sections, strong in 0)
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
candidate 1 (found by 2 of 24 passes): The choice of (correctly signed) zeros and infinities to signal underflow and overflow is far from arbitrary; `strtod` has that design, and correctly implements the ISO/IEC 60559 (or IEEE-754) operation convertFromDecimalCharacter for floating-point types.
candidate 2 (found by 1 of 24 passes): The choice of (correctly signed) zeros and infinities to signal underflow and overflow is far from arbitrary; `strtod` has that design, and correctly implements the ISO/IEC 60559 (or IEEE-754) operation convertFromDecimalCharacter for floating-point types

## coordination - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): libstdc++ leaves `x` unmodified, but libc++ and MSVC STL set it to ∞. `ec` is `std::errc::result_out_of_range` for all implementations, but the wording requires that `x` is set to ∞ and that `ec` is value-initialized, which no one implements.
candidate 2 (found by 2 of 24 passes): the MSVC STL and libc++ behavior is proposed, with additional wording clarifications.
candidate 3 (found by 1 of 24 passes): The handling of floating-point overflow and underflow in `std::from_chars` is inconsistent; the implementations diverge from each other, and every implementation diverges from the wording in the standard.
candidate 4 (found by 1 of 24 passes): libstdc++ leaves `x` unmodified, but libc++ and MSVC STL set it to ∞.

## insufficiency - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/1/0  -> 1.00
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): libstdc++ leaves `x` unmodified, but libc++ and MSVC STL set it to ∞. `ec` is `std::errc::result_out_of_range` for all implementations, but the wording requires that `x` is set to ∞ and that `ec` is value-initialized, which no one implements.
candidate 2 (found by 1 of 24 passes): users suffer from it to the point where `boost::from_chars_erange` ([[BoostCharConv]](https://www%2eboost%2eorg/doc/libs/latest/libs/charconv/doc/html/charconv%2ehtml)) should arguably be recommended to users over the standard feature; at least it is portable and well-specified.

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/1  -> 1.67
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): At the time of writing, implementations behave as shown in the table below when parsing a string as `float` (binary32).
candidate 2 (found by 3 of 24 passes): the MSVC STL and libc++ behavior is proposed, with additional wording clarifications.
candidate 3 (found by 2 of 24 passes): The proposed behavior has been released in MSVC STL and libc++, except that the behavior in §2.5. Further edge cases does not need to be implemented and only exists on paper for these implementations.
candidate 4 (found by 1 of 24 passes): The proposed behavior has been released in MSVC STL and libc++, except that the behavior in §2.5.

-->
