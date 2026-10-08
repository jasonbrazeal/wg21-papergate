Verdict: Strong (10/14)

The paper gives solid support for standardizing case ranges by pointing to long-standing compiler implementations, C2y adoption, and the interoperability benefits for shared C and C++ code. The case is much thinner when it comes to showing who specifically needs this in standard C++ and why existing extensions or the C standard are not enough on their own.

- The strongest support is the implementation experience, with GCC and Clang shipping the feature for decades and C2y already specifying the behavior.
- The paper also clearly establishes prior art and alternatives by citing the C2y feature, the GNU extension history, and the consistency argument with P2864R2.
- The weakest established area is the rationale for why the standard must act, since the paper mostly asserts usefulness and C2y alignment without showing a distinct C++ standardization need.
- The most glaring omission is the complete absence of any argument for why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 6 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 9.00   accumulate 11.50   max 10.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.17  coordination 1.50  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 10.50 / 9.50 / 10.00   (all 3 samples: 9.83)
headings: h2 8
on threshold: coordination, implementation
splits: audience[7] 2/0/2  vehicle[2] 1/1/0  vehicle[6] 2/1/1  coordination[4] 0/1/1
        implementation[4] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): C2y added ranges in `case` labels, such as `case 0 ... 9:`. Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 2 (found by 3 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 3 (found by 3 of 27 passes): There is an obvious asymmetry here, decreasing readability.
candidate 4 (found by 3 of 27 passes): Standardizing case ranges legitimizes existing C++ code that relies on the GNU extension for case ranges by giving it behavior specified by the standard.

## audience - grade 1.17 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/0/2  -> 1.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 2 (found by 3 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 3 (found by 2 of 27 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.

## prior_art - grade 2.00 (fired in 5 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Also, [[P2864R2]](https://wg21%2elink/p2864r2) removed the (deprecated in C++20) ability to mix different enumeration types in comparisons (or generally, in usual arithmetic conversions), and disallowing enumeration mixing in `switch` statements would be consistent with that design.
candidate 2 (found by 3 of 27 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.
candidate 3 (found by 2 of 27 passes): C2y added ranges in `case` labels, such as `case 0 ... 9:`.
candidate 4 (found by 2 of 27 passes): In 2024, [[N3370]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3370%2ehtm) added support for `case` ranges to C2y.

## vehicle - grade 1.17 (fired in 4 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/1/1  -> 1.33
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 2 (found by 3 of 27 passes): In addition to the feature being generally useful in C++, as mentioned above, it is an existing C2y feature.
candidate 3 (found by 2 of 27 passes): This part should also be standardized because it is useful.
candidate 4 (found by 1 of 27 passes): This feature should be standardized for C++.

## coordination - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Case ranges can be used in code that is meant to compile in both C and C++, which is unlikely to ever be the case for pattern matching.
candidate 2 (found by 2 of 27 passes): Providing it to users would make it easier to port C code to C++ and vice versa.
candidate 3 (found by 1 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 4 (found by 1 of 27 passes): This feature is already implemented in GCC and Clang, not just for C but also for C++.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/2  -> 1.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 2 (found by 3 of 27 passes): This feature is already implemented in GCC and Clang, not just for C but also for C++.
candidate 3 (found by 3 of 27 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.
candidate 4 (found by 1 of 27 passes): the current behavior has existed in the C++ extension for many years and is the current C2y behavior

-->
