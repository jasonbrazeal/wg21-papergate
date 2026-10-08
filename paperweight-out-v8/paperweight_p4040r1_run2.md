Verdict: Strong (9/14)

The paper offers solid support for standardizing case ranges by pointing to existing C2y precedent, long-standing compiler implementations, and the value of legitimizing widely used extension code. The case is thinnest where it needs to show who specifically is affected and how standardization would coordinate with the C feature beyond general portability claims, and it does not address why a library solution would be insufficient.

- The strongest support comes from implementation experience, with GCC and Clang shipping the feature for decades and the paper acknowledging the breaking-change implications of that history.
- The paper also clearly establishes prior art and alternatives through the C2y adoption and the documented GNU extension lineage.
- The rationale for why the standard rather than a library is needed is not established at all.
- The most glaring omission is the absence of any discussion of who is concretely affected or how interoperability with C would work in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.33/14)

Provisionally addressed: 6 of 7. Provisional points: 9.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.33   corroborated 8.00   accumulate 10.67   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 1.67  vehicle 1.50  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.00 / 9.00 / 9.50   (all 3 samples: 9.33)
headings: h2 8
on threshold: prior_art, vehicle, coordination
splits: audience[2] 1/0/1  audience[7] 1/0/0  prior_art[6] 2/2/0  vehicle[2] 0/1/0
        coordination[4] 0/1/1  coordination[6] 2/1/2  implementation[2] 0/1/1
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
candidate 1 (found by 3 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 2 (found by 3 of 27 passes): There is an obvious asymmetry here, decreasing readability.
candidate 3 (found by 2 of 27 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 4 (found by 2 of 27 passes): Standardizing case ranges legitimizes existing C++ code that relies on the GNU extension for case ranges by giving it behavior specified by the standard.

## audience - grade 0.83 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/0/0  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 2 (found by 2 of 27 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 3 (found by 1 of 27 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.

## prior_art - grade 1.67 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/2/0  -> 1.33
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): it is an existing C2y feature. Providing it to users would make it easier to port C code to C++ and vice versa.
candidate 2 (found by 3 of 27 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.
candidate 3 (found by 2 of 27 passes): C2y added ranges in `case` labels, such as `case 0 ... 9:`.
candidate 4 (found by 2 of 27 passes): In 2024, [[N3370]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3370%2ehtm) added support for `case` ranges to C2y.

## vehicle - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In addition to the feature being generally useful in C++, as mentioned above, it is an existing C2y feature.
candidate 2 (found by 3 of 27 passes): Standardizing case ranges legitimizes existing C++ code that relies on the GNU extension for case ranges by giving it behavior specified by the standard.
candidate 3 (found by 2 of 27 passes): This feature is already implemented in GCC and Clang, not just for C but also for C++. Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 4 (found by 1 of 27 passes): This feature should be standardized for C++.

## coordination - grade 1.33 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design                                    2/1/2  -> 1.67
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Providing it to users would make it easier to port C code to C++ and vice versa.
candidate 2 (found by 3 of 27 passes): Standardizing case ranges legitimizes existing C++ code that relies on the GNU extension for case ranges by giving it behavior specified by the standard.
candidate 3 (found by 2 of 27 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This feature is already implemented in GCC and Clang, not just for C but also for C++.
candidate 2 (found by 3 of 27 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.
candidate 3 (found by 2 of 27 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 4 (found by 1 of 27 passes): the proposed feature is an ancient extension, so we make a breaking change whether we restrict the behavior now or in a few years.

-->
