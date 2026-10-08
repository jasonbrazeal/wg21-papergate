Verdict: Adequate (7/14)

The paper offers a partial case for standardization, with its clearest support concentrated in the motivation and the contrast with existing facilities, but it leaves several practical questions about users, portability, and implementation experience largely asserted rather than demonstrated. The thinnest areas are those that would show the feature works beyond a single compiler pattern and that the affected community has a real, portable need for a language change.

- The strongest support is the explanation of why compile-time assertions inside ordinary functions matter and how they differ from static_assert, assert, and contracts.
- The paper also credibly identifies existing compiler behavior and prior art, particularly GCC’s attribute error and current optimizer-driven patterns.
- The case weakens where it claims a reference implementation and use since 2023 without showing who uses it or how widely.
- The most glaring omission is the absence of any coordination or interoperability discussion, leaving unclear how such a facility would fit with existing diagnostics, build systems, or other standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.33   accumulate 7.50   max 8.33

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.50  vehicle 1.00  coordination 0.00  insufficiency 0.67  implementation 1.33
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.50)
headings: h2 7 + bold numbered 5
on threshold: motivation, prior_art
splits: prior_art[3] 1/0/1  prior_art[5] 1/0/0  prior_art[7] 0/1/1  insufficiency[8] 0/1/0
        implementation[10] 1/1/0  implementation[13] 2/0/2
## END SUMMARY

## motivation - grade 1.50 (fired in 6 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           1/1/1  -> 1.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 1/1/1  -> 1.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  0/0/0  -> 0.00
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 5 of 39 passes): compile_assert provides advanced asserts at compile time, not runtime. Used for bounds checking, parameter validation and data validation at compile time.
candidate 2 (found by 3 of 39 passes): This enables expressing preconditions and invariants inside ordinary functions to provide compile-time diagnostics without introducing runtime overhead.
candidate 3 (found by 3 of 39 passes): There is no mechanism that allows compile time assertions inside ordinary functions from regular compilers.
candidate 4 (found by 3 of 39 passes): Modern C++ compilers already eliminate unreachable branches and perform inter- procedural constant analysis. compile_assert() formalizes this capability into a portable language facility.

## audience - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 0/0/0  -> 0.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  0/0/0  -> 0.00
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): compile_assert() has had a reference implementation and been in use since 2023 in code bases.

## prior_art - grade 1.50 (fired in 8 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/0/1  -> 0.67
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                1/0/0  -> 0.33
  [6] 4. Proposed Design                           2/2/2  -> 2.00
  [7] 6. Interaction With Existing Features        0/1/1  -> 0.67
  [8] 7. Implementation Experience                 1/1/1  -> 1.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  0/0/0  -> 0.00
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The example implementation does this by using GCC’s attribute error.
candidate 2 (found by 3 of 39 passes): C++ currently provides: static_assert - requires constant expressions. assert - runtime check, calls abort() to terminate, optionally disabled. Contracts – runtime checks, in progress. Profiles – not yet standardized.
candidate 3 (found by 3 of 39 passes): This is fundamentally different from static_assert, which operates purely in the constantevaluation domain defined by the language.
candidate 4 (found by 3 of 39 passes): Existing compilers such as GCC and Clang support this pattern today.

## vehicle - grade 1.00 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           1/1/1  -> 1.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 0/0/0  -> 0.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  0/0/0  -> 0.00
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Given the compiler is generating the machine code, it’s important the compile time assert is output from the compiler, not a separate static analysis tool
candidate 2 (found by 3 of 39 passes): Modern C++ compilers already eliminate unreachable branches and perform inter- procedural constant analysis. compile_assert() formalizes this capability into a portable language facility.

## coordination - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 0/0/0  -> 0.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  0/0/0  -> 0.00
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.67 (fired in 2 of 13 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 0/1/0  -> 0.33
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  0/0/0  -> 0.00
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): I could not find a way to get MSVC to stop the build.
candidate 2 (found by 1 of 39 passes): Reliance on Optimizer, which in itself is not standardized is an issue.

## implementation - grade 1.33  [binary: max] (fired in 6 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 1/1/1  -> 1.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Examples                                  1/1/0  -> 0.67
  [11] 10. Notes                                    0/0/0  -> 0.00
  [12] 10. Acknowledgements                         0/0/0  -> 0.00
  [13] 11. References                               2/0/2  -> 1.33
candidate 1 (found by 3 of 39 passes): The example implementation does this by using GCC’s attribute error.
candidate 2 (found by 3 of 39 passes): compile_assert() has had a reference implementation and been in use since 2023 in code bases.
candidate 3 (found by 3 of 39 passes): There is an implementation with examples listed in the references section.
candidate 4 (found by 3 of 39 passes): A header-only implementation demonstrates this behaviour by placing an ill-formed construct in a branch that the optimizer determines to be reachable.

-->
