Verdict: Strong (9/14)

The paper offers solid grounding in implementation divergence, prior standardization attempts, and real-world deployment experience, but its case thins considerably when it comes to demonstrating who is concretely harmed and why only a standard change can address that harm. The strongest support is factual and comparative; the weakest support is motivational and evidentiary.

- The paper clearly establishes that existing implementations and the current wording disagree about floating-point overflow and underflow in `std::from_chars`, and that this has persisted across multiple shipped standard libraries.
- It also establishes a credible standardization history by linking the proposal to superseded papers and open LWG issues, and by showing that the proposed behavior is already released in major implementations.
- The paper claims but does not establish that changing `std::from_chars` would break substantial amounts of existing code, leaving the affected population and the scale of impact unspecified.
- Most glaringly, the paper does not establish why a library-level solution is insufficient, offering only an unsupported assertion that users suffer enough to prefer a Boost alternative over the standard feature.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 7 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 9.33   accumulate 8.67   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.17  coordination 2.00  insufficiency 0.17  implementation 2.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.50 / 8.50 / 8.00   (all 3 samples: 8.67)
headings: h2 7
on threshold: none
splits: audience[4] 1/1/0  prior_art[7] 1/1/0  vehicle[4] 1/0/0  insufficiency[3] 1/0/0
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

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    1/1/0  -> 0.67
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Changing the behavior of `std::from_chars` can break substantial amounts of existing code.

## prior_art - grade 2.00 (fired in 6 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Editorial problems                        2/2/2  -> 2.00
  [7] 5. Wording                                   1/1/0  -> 0.67
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper supersedes [[P2827R1]](https://wg21%2elink/p2827r1) and fixes [[LWG3081]](https://wg21%2elink/LWG3081), [[LWG3082]](https://wg21%2elink/LWG3082), and [[LWG3456]](https://wg21%2elink/LWG3456).
candidate 2 (found by 3 of 24 passes): In 2023, [[P2827R1]](https://wg21%2elink/p2827r1) attempted to solve this issue, but died in LEWG eventually.
candidate 3 (found by 3 of 24 passes): [[LWG3456]](https://wg21%2elink/LWG3456) performs such a rewrite, but does not fully decouple `std::from_chars` from the C wording.
candidate 4 (found by 2 of 24 passes): Neither of these behaviors standardizes existing practice in standard libraries, is particularly well-motivated, or matches the behavior of other functions such as `std::strtod`.

## vehicle - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    1/0/0  -> 0.33
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): There seem to be only two plausible options with sufficiently low impact

## coordination - grade 2.00 (fired in 2 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): libstdc++ leaves `x` unmodified, but libc++ and MSVC STL set it to ∞.
candidate 2 (found by 2 of 24 passes): floating-point implementations of `std::from_chars` have already existed for years (MSVC STL since 2018, libstdc++ since 2021, libc++ since 2025).
candidate 3 (found by 1 of 24 passes): floating-point implementations of `std::from_chars` have already existed for years (MSVC STL since 2018, libstdc++ since 2021, libc++ since 2025). Changing the behavior of `std::from_chars` can break substantial amounts of existing code.

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/0  -> 0.33
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): users suffer from it to the point where `boost::from_chars_erange` should arguably be recommended to users over the standard feature; at least it is portable and well-specified.

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Editorial problems                        0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): At the time of writing, implementations behave as shown in the table below when parsing a string as `float` (binary32).
candidate 2 (found by 3 of 24 passes): floating-point implementations of `std::from_chars` have already existed for years (MSVC STL since 2018, libstdc++ since 2021, libc++ since 2025).
candidate 3 (found by 2 of 24 passes): The proposed behavior has been released in MSVC STL and libc++, except that the behavior in §2.5.
candidate 4 (found by 1 of 24 passes): The proposed behavior has been released in MSVC STL and libc++, except that the behavior in §2.5. Further edge cases does not need to be implemented and only exists on paper for these implementations.

-->
