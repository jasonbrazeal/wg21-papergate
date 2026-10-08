Verdict: Strong (9/14)

The paper offers a solid foundation for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several supporting arguments asserted rather than demonstrated, and one required element entirely unaddressed. The thinnest support concerns the need for a standard library solution rather than a user-space one, which the paper does not establish at all.

- The strongest support comes from the concrete implementation table and the observation that libstdc++ and libc++ already conform to the proposed behavior, showing real-world experience.
- The paper clearly establishes why the change matters by pointing to permissiveness in the current specification and implementation divergence in the zero-length case.
- The discussion of prior art is well grounded in the de-facto replacement role of `std::array` and the documented MSVC STL non-conformance.
- The most glaring omission is the absence of any argument for why a library cannot provide the desired guarantees, leaving a required part of the standardization case unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 8.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 8.50 / 8.50 / 8.50   (all 3 samples: 8.50)
headings: h2 8
on threshold: audience, coordination
splits: motivation[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 0/0/1  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): However, its specification in the standard is considerably more permissive and should be simplified.
candidate 2 (found by 3 of 27 passes): The zero-length case is also where we see some implementation divergence in size and alignment of the array.
candidate 3 (found by 2 of 27 passes): It would be beneficial to the C++ community if the simplified explanation in §2. Introduction was what the standard actually said.
candidate 4 (found by 1 of 27 passes): A stricter specification would provide additional useful guarantees such as `std::array<T, N>` being trivially copyable when `T` is trivially copyable.

## audience - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Impact on implementations                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): For zero-length `std::array`s, libstdc++ and libc++ already comply with the proposed changes.

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The `std::array` class template has established itself as a de-facto replacement for "builtin arrays" or "C-style arrays" in many code bases.
candidate 2 (found by 3 of 27 passes): The MSVC STL implements zero-length `std::array`s incorrectly and does not comply with C++26 (or any prior standard), and fixing this would require an ABI break.
candidate 3 (found by 1 of 27 passes): The "greatest common denominator" between these implementations (excluding MSVC STL) should be standardized, which is:
candidate 4 (found by 1 of 27 passes): The "greatest common denominator" between these implementations (excluding MSVC STL) should be standardized, which is: - `std::array<T, 0>` is trivially copyable.

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): If the remaining implementation freedom can only be used for evil, perhaps we should not grant it.
candidate 2 (found by 1 of 27 passes): it would be unusual for WG21 to shy away from standardizing universally existing practice and to recommend users to rely on non-standard implementation details, simply because those implementation details are widespread.

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The following table shows how major standard libraries implement zero-length `std::array`.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The following table shows how major standard libraries implement zero-length `std::array`.
candidate 2 (found by 3 of 27 passes): For zero-length `std::array`s, libstdc++ and libc++ already comply with the proposed changes.

-->
