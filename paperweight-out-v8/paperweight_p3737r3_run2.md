Verdict: Strong (8/14)

The paper offers solid support in the areas that anchor a proposal of this kind: it identifies a real specification problem, shows that two major implementations already converge on the intended behavior, and explains why the remaining latitude is not useful. The case is thinnest where it needs to show that the change belongs in the standard rather than in implementation documentation or a library solution, and it does not establish that a library-level fix would be inadequate.

- The strongest support is the implementation experience, since the paper documents that libstdc++ and libc++ already match the proposed behavior for zero-length `std::array`.
- The paper also establishes meaningful prior art and alternatives by framing the proposal as standardizing the common denominator of existing practice and by noting that MSVC’s divergent behavior is itself non-conforming.
- The weakest established area is the rationale for standardization itself, which rests on general claims about universal practice and the undesirability of implementation freedom rather than a specific standards-level need.
- The most glaring omission is the absence of any established argument for why a library cannot address the problem, leaving that required justification effectively unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 7.83   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.67  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.00 / 7.50 / 8.00   (all 3 samples: 7.83)
headings: h2 8
on threshold: coordination
splits: motivation[4] 0/2/0  audience[7] 1/0/0  prior_art[5] 0/1/0  vehicle[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/2/0  -> 0.67
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): However, its specification in the standard is considerably more permissive and should be simplified.
candidate 2 (found by 3 of 27 passes): It would be beneficial to the C++ community if the simplified explanation in §2. Introduction was what the standard actually said.
candidate 3 (found by 2 of 27 passes): Within [[array.zero]](https://eel.is/c++draft/array.zero), there are some long-standing issues going back to 2012.
candidate 4 (found by 1 of 27 passes): Notably, there are quite a couple of guarantees that are absent.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Impact on implementations                 1/0/0  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): For zero-length `std::array`s, libstdc++ and libc++ already comply with the proposed changes.

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/1/0  -> 0.33
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The `std::array` class template has established itself as a de-facto replacement for "builtin arrays" or "C-style arrays" in many code bases.
candidate 2 (found by 3 of 27 passes): The MSVC STL implements zero-length `std::array`s incorrectly and does not comply with C++26 (or any prior standard), and fixing this would require an ABI break.
candidate 3 (found by 1 of 27 passes): It seems like the vagueness in the specification serves no practical purpose; it is unclear what implementations could do with the additional freedom, other than pranking their users.
candidate 4 (found by 1 of 27 passes): The overall design strategy is to standardize the "greatest common denominator" of libc++ and libstdc++.

## vehicle - grade 0.67 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design considerations                     0/0/1  -> 0.33
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): If the remaining implementation freedom can only be used for evil, perhaps we should not grant it.
candidate 2 (found by 1 of 27 passes): it would be unusual for WG21 to shy away from standardizing universally existing practice and to recommend users to rely on non-standard implementation details
candidate 3 (found by 1 of 27 passes): The overall design strategy is to standardize the "greatest common denominator" of libc++ and libstdc++.

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
