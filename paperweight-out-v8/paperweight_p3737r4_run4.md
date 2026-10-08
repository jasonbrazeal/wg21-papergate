Verdict: Strong (8/14)

The paper offers solid grounding for its proposal in existing implementation practice, particularly through its comparison of major standard libraries and the observation that two of them already conform to the intended behavior. The case is thinnest where it needs to explain why a library-level solution would be insufficient and why the standard itself must change, since that argument is essentially absent.

- The strongest support comes from the implementation experience table, which shows libstdc++ and libc++ already matching the proposed zero-length behavior and gives the paper concrete existing practice to standardize.
- The motivation is also well established, since the paper identifies missing guarantees and permissiveness in the current specification that lead to real divergence and lost properties like trivial copyability.
- The paper claims but does not establish that users are broadly affected, since it gestures at affected code without demonstrating the scope or impact of that population.
- The most glaring omission is the absence of any argument for why a library cannot address the problem, leaving the necessity of a standard change unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 6 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 7.67   accumulate 8.50   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.67  vehicle 0.83  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.50 / 9.00 / 7.50   (all 3 samples: 8.17)
headings: h2 8
on threshold: prior_art, coordination
splits: motivation[7] 0/0/1  audience[6] 0/2/0  audience[7] 1/1/0  prior_art[6] 0/2/2
        vehicle[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Impact on implementations                 0/0/1  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): However, its specification in the standard is considerably more permissive and should be simplified.
candidate 2 (found by 3 of 27 passes): Notably, there are quite a couple of guarantees that are absent.
candidate 3 (found by 3 of 27 passes): A stricter specification would provide additional useful guarantees such as `std::array<T, N>` being trivially copyable when `T` is trivially copyable.
candidate 4 (found by 3 of 27 passes): The zero-length case is also where we see some implementation divergence in size and alignment of the array.

## audience - grade 0.67 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     0/2/0  -> 0.67
  [7] 5. Impact on implementations                 1/1/0  -> 0.67
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): For zero-length `std::array`s, libstdc++ and libc++ already comply with the proposed changes.
candidate 2 (found by 1 of 27 passes): The following table shows how major standard libraries implement zero-length `std::array`.

## prior_art - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design considerations                     0/2/2  -> 1.33
  [7] 5. Impact on implementations                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The `std::array` class template has established itself as a de-facto replacement for "builtin arrays" or "C-style arrays" in many code bases.
candidate 2 (found by 3 of 27 passes): The MSVC STL implements zero-length `std::array`s incorrectly and does not comply with C++26 (or any prior standard), and fixing this would require an ABI break.
candidate 3 (found by 2 of 27 passes): The "greatest common denominator" between these implementations (excluding MSVC STL) should be standardized, which is:

## vehicle - grade 0.83 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design considerations                     2/0/0  -> 0.67
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): it would be unusual for WG21 to shy away from standardizing universally existing practice and to recommend users to rely on non-standard implementation details
candidate 2 (found by 1 of 27 passes): If the remaining implementation freedom can only be used for evil, perhaps we should not grant it.
candidate 3 (found by 1 of 27 passes): it would be unusual for WG21 to shy away from standardizing universally existing practice and to recommend users to rely on non-standard implementation details, simply because those implementation details are widespread.
candidate 4 (found by 1 of 27 passes): The "greatest common denominator" between these implementations (excluding MSVC STL) should be standardized, which is:

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
