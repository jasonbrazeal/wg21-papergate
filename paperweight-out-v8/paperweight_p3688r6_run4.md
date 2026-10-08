Verdict: Adequate to Strong (7/14)

The paper offers a mixed case for its own standardization, with its strongest material going to the existence of prior art, the limits of current standard facilities, and the availability of an implementation. The case is thinnest around coordination with existing library conventions and around why the work cannot be adequately served by a library, where the paper mostly asserts rather than demonstrates need.

- The paper clearly establishes that current `<cctype>` and `<locale>` facilities are locale-dependent, not `constexpr`, and unsuited to Unicode character types.
- It provides credible prior art and implementation experience through a linked partial implementation and discussion of alternative naming and locale-based approaches.
- The paper claims but does not establish that ASCII case handling is common enough to justify standardization, relying on general assertions rather than evidence of widespread need.
- It offers no meaningful discussion of coordination or interoperability with existing or proposed standard library facilities, leaving a significant gap in the standardization case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.67   accumulate 7.00   max 8.67

## SUMMARY
grades: motivation 1.50  audience 0.67  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 7.50 / 7.00   (all 3 samples: 7.00)
headings: h2 9
on threshold: motivation, implementation
splits: audience[5] 0/1/0  prior_art[8] 1/1/0  insufficiency[4] 0/1/1  implementation[10] 0/2/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The utilities in `<cctype>` or `<locale>` are locale-specific, not `constexpr`, and provide no support for Unicode character types.
candidate 2 (found by 3 of 30 passes): Unfortunately, these common and simple tasks are only supported through functions in the `<cctype>` and `<locale>` headers, such as:

## audience - grade 0.67 (fired in 2 of 10 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/1/0  -> 0.33
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): working with ASCII characters is such an overwhelmingly common use case that it's worth supporting in the standard library.
candidate 2 (found by 1 of 30 passes): Ignoring or transforming ASCII case in algorithms is a fairly common problem.

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Implementation experience                 1/1/1  -> 1.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      1/1/0  -> 0.67
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Many of these problems are resolved by the `std::locale` overloads in `<locale>`, but their locale dependence makes them unfit for what this proposal aims to achieve.
candidate 2 (found by 3 of 30 passes): A naive implementation of all proposed functions can be found at [[CompilerExplorer]](https://godbolt%2eorg/z/5nvWzdf8G), although these are implemented as function templates, not as overload sets (as proposed).
candidate 3 (found by 2 of 30 passes): The use of `ascii_to_upper` deliberately produces different results than Unicode comparisons because those would essentially involve a 128-character lookup table, whereas `ascii_case_insensitive_compare` is easily SIMD-parallelizable and requires no memory lookup.
candidate 4 (found by 1 of 30 passes): R4 and previous revisions of this paper used the naming scheme `is_ascii_*` rather than `is_ascii_*` for character rests.

## vehicle - grade 0.50 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Even if all proposed functions were trivial to implement, working with ASCII characters is such an overwhelmingly common use case that it's worth supporting in the standard library.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 0/0/0  -> 0.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): In the standard library, it can be efficiently implemented using a 128-bit or 256-bit bitset.

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Implementation experience                 2/2/2  -> 2.00
  [7] 5. Wording                                   0/0/0  -> 0.00
  [8] ASCII utilities [ascii]                      0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/2/0  -> 0.67
candidate 1 (found by 3 of 30 passes): A naive implementation of all proposed functions can be found at [[CompilerExplorer]](https://godbolt%2eorg/z/5nvWzdf8G), although these are implemented as function templates, not as overload sets (as proposed).
candidate 2 (found by 1 of 30 passes): [CompilerExplorer] Jan Schultke, Corentin Jabot. Partial implementation of character utilities https://godbolt.org/z/5nvWzdf8G

-->
