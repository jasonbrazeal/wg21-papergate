Verdict: Strong (10/14)

The paper gives solid support for much of its standardization case, particularly around existing practice, C compatibility, and the need for a language feature rather than a library solution. The thinnest parts are the absence of any argument for why a library cannot address the need and only a general, unquantified claim about who is affected.

- The strongest support is the implementation experience, with decades of GCC and Clang support and a clear basis in the C2y feature.
- The paper also establishes why the standard is the right venue, since standardizing the extension would legitimize existing code and ease C and C++ portability.
- Prior art and alternatives are well covered, including the C2y adoption and the contrast with pattern matching.
- The most glaring omission is that the paper never explains why a library solution would be inadequate for case ranges.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.33/14, close to Excellent)

Provisionally addressed: 6 of 7. Provisional points: 10.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.33   corroborated 9.00   accumulate 11.50   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 0.00  implementation 2.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 10.50 / 10.00 / 10.50   (all 3 samples: 10.33)
headings: h2 7
on threshold: audience, vehicle, coordination, implementation
splits: audience[2] 0/0/1  audience[6] 2/1/2  implementation[3] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 2 (found by 3 of 24 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 3 (found by 3 of 24 passes): Many scoped enumerations organize enumerations into blocks, such as success statuses and error statuses, and case ranges allow for selecting such blocks.
candidate 4 (found by 2 of 24 passes): While it would also be possible to handle case ranges using an `if` statement, this often requires splitting off some cases from the `switch`.

## audience - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 2/1/2  -> 1.67
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.
candidate 2 (found by 2 of 24 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 3 (found by 1 of 24 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 4 (found by 1 of 24 passes): This feature is already implemented in GCC and Clang, not just for C but also for C++.

## prior_art - grade 2.00 (fired in 5 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 1/1/1  -> 1.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 2 (found by 3 of 24 passes): In 2024, [[N3370]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3370%2ehtm) added support for `case` ranges to C2y.
candidate 3 (found by 3 of 24 passes): In addition to the feature being generally useful in C++, as mentioned above, it is an existing C2y feature.
candidate 4 (found by 3 of 24 passes): Pattern matching provides very similar functionality:

## vehicle - grade 1.50 (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): In addition to the feature being generally useful in C++, as mentioned above, it is an existing C2y feature.
candidate 2 (found by 3 of 24 passes): Standardizing case ranges legitimizes existing C++ code that relies on the GNU extension for case ranges by giving it behavior specified by the standard.
candidate 3 (found by 2 of 24 passes): This feature should be standardized for C++.
candidate 4 (found by 2 of 24 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.

## coordination - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Since it is useful and widely supported, we should standardize existing practice and make it available to users in standard C++.
candidate 2 (found by 3 of 24 passes): it is an existing C2y feature. Providing it to users would make it easier to port C code to C++ and vice versa.
candidate 3 (found by 3 of 24 passes): Case ranges can be used in code that is meant to compile in both C and C++, which is unlikely to ever be the case for pattern matching.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/1/1  -> 1.33
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Design                                    1/1/1  -> 1.00
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Such case ranges have also been supported as a C++ compiler extension for many years.
candidate 2 (found by 3 of 24 passes): This feature is already implemented in GCC and Clang, not just for C but also for C++.
candidate 3 (found by 3 of 24 passes): There is no obvious reason to deviate from the existing semantics of the C2y feature and of the C++ compiler extension; all these choices seem adequate.
candidate 4 (found by 3 of 24 passes): Case ranges were first implemented in GCC 2.0 (1992) and Clang 1.0 (2007), albeit as a GNU extension, not as a standard C2y feature.

-->
