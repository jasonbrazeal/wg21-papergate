Verdict: Strong (9/14)

The paper gives a reasonably solid account of why a compiler-integrated compile-time assertion mechanism would be useful and why existing library or tooling approaches fall short, but its case weakens considerably when it comes to showing who is concretely affected and how standardization would fit with existing committee and vendor efforts. The strongest material concerns the demonstrated limitations of current alternatives and the existence of a working macro-based implementation across major compilers.

- The paper clearly establishes that existing mechanisms such as `static_assert`, vendor attributes, and external link-time tricks do not provide the same control-flow-based, in-function compile-time checking that the proposal envisions.
- The implementation experience is the most concrete part of the paper, with a published macro approach used since 2023 and supported on GCC, Clang, and MSVC.
- The claim that a broad user population is affected rests mainly on the existence of the sample implementation rather than on demonstrated adoption, reported experience, or measured demand.
- The paper offers no meaningful discussion of coordination with other standardization efforts, vendor roadmaps, or interoperability concerns, leaving a significant gap in the standardization case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 6 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 31. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.00   accumulate 10.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 1.83  vehicle 1.00  coordination 0.00  insufficiency 1.50  implementation 2.00
sample agreement: 208 of 217 section-criterion pairs unanimous (96%)
single-sample totals would have been: 9.50 / 9.00 / 9.00   (all 3 samples: 9.17)
headings: h2 15 + bold numbered 15
on threshold: insufficiency
splits: motivation[15] 1/1/0  motivation[23] 0/0/2  motivation[26] 1/1/0  audience[3] 1/0/1
        prior_art[5] 0/0/1  prior_art[17] 2/2/1  vehicle[22] 0/1/0  implementation[15] 0/1/1
        implementation[23] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 31 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           1/1/1  -> 1.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 1/1/0  -> 0.67
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           1/1/1  -> 1.00
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    1/1/1  -> 1.00
  [23] 14. Other approaches considered              0/0/2  -> 0.67
  [24] 15. Runtime vs compile-time constraints      2/2/2  -> 2.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              1/1/0  -> 0.67
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): This new keyword is used for bounds checking, avoiding nullptr dereferences, parameter validation and data validation at compile-time.
candidate 2 (found by 3 of 93 passes): There is no general mechanism that allows flexible compile-time assertions inside ordinary functions from regular compilers based on control-flow analysis.
candidate 3 (found by 3 of 93 passes): Modern compilers already eliminate unreachable branches and perform inter-procedural constant analysis. `compile_assert()` formalizes this capability into a portable language facility with a standardized keyword and syntax.
candidate 4 (found by 3 of 93 passes): It feels more rational for the programmer to simply put the `if(handle>=0)` in `api_function(int handle)` as best practice, LTO could then eliminate redundant checks.

## audience - grade 0.83 (fired in 2 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/0/1  -> 0.67
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           0/0/0  -> 0.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 0/0/0  -> 0.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    0/0/0  -> 0.00
  [23] 14. Other approaches considered              0/0/0  -> 0.00
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): All three major compilers (GCC, Clang, MSVC) are supported by a sample implementation macro I published in 2023
candidate 2 (found by 2 of 93 passes): `compile_assert()`has had a reference implementation and has been used in codebases since 2023.

## prior_art - grade 1.83 (fired in 11 of 31 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/1  -> 0.33
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           1/1/1  -> 1.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 1/1/1  -> 1.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     2/2/1  -> 1.67
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           1/1/1  -> 1.00
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    1/1/1  -> 1.00
  [23] 14. Other approaches considered              2/2/2  -> 2.00
  [24] 15. Runtime vs compile-time constraints      1/1/1  -> 1.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): There is no general mechanism that allows flexible compile-time assertions inside ordinary functions from regular compilers based on control-flow analysis.
candidate 2 (found by 3 of 93 passes): `static_assert()` requires the condition to be a constant expression. `compile_assert()` is fundamentally different from `static_assert()`, which operates purely in the constant-evaluation mode defined by the language.
candidate 3 (found by 3 of 93 passes): GCC and Clang both support `__attribute__ ((error(message)))`, GCC since version 4.3 in 2008.
candidate 4 (found by 3 of 93 passes): Several alternative mechanisms exist for deliberately causing compilation or linkage failure in the presence of a violated constraint.

## vehicle - grade 1.00 (fired in 4 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           1/1/1  -> 1.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 0/0/0  -> 0.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    0/1/0  -> 0.33
  [23] 14. Other approaches considered              0/0/0  -> 0.00
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): The benefit of this approach is users get a standard keyword, however they do not get a full warranty that everything will be enforced.
candidate 2 (found by 3 of 93 passes): Since the compiler generates the machine code, it is important that the compile-time assertion originates from the compiler; rather than a separate static analysis tool which may or may not determine control-flow the same way.
candidate 3 (found by 3 of 93 passes): Modern compilers already eliminate unreachable branches and perform inter-procedural constant analysis. `compile_assert()` formalizes this capability into a portable language facility with a standardized keyword and syntax.
candidate 4 (found by 1 of 93 passes): C may standardize as `_Compile_assert()` which can then be defined as `compile_assert()`.

## coordination - grade 0.00 (fired in 0 of 31 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           0/0/0  -> 0.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 0/0/0  -> 0.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    0/0/0  -> 0.00
  [23] 14. Other approaches considered              0/0/0  -> 0.00
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.50 (fired in 2 of 31 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           0/0/0  -> 0.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 0/0/0  -> 0.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    0/0/0  -> 0.00
  [23] 14. Other approaches considered              2/2/2  -> 2.00
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): Since the compiler generates the machine code, it is important that the compile-time assertion originates from the compiler; rather than a separate static analysis tool which may or may not determine control-flow the same way.
candidate 2 (found by 2 of 93 passes): MSVC has `__assume()` and GCC has `__builtin_assume()`, neither offered any usable results.
candidate 3 (found by 1 of 93 passes): Calling an external error function that does not exist causes the linker to output the file and line location of the `compile_assert()` constraint failure.

## implementation - grade 2.00  [binary: max] (fired in 9 of 31 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] Syntax                                       0/0/0  -> 0.00
  [8] Constraints                                  0/0/0  -> 0.00
  [9] Semantics                                    0/0/0  -> 0.00
  [10] Outcomes                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Diagnostic output                            0/0/0  -> 0.00
  [13] Forward references                           1/1/1  -> 1.00
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 0/1/1  -> 0.67
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     1/1/1  -> 1.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           2/2/2  -> 2.00
  [20] 11. Sample examples and tests                2/2/2  -> 2.00
  [21] 12. Compilers supported                      1/1/1  -> 1.00
  [22] 13. Notes                                    0/0/0  -> 0.00
  [23] 14. Other approaches considered              1/0/0  -> 0.33
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): All three major compilers (GCC, Clang, MSVC) are supported by a sample implementation macro I published in 2023 that works by re-purposing the Optimizer to identify failure branches that should be unreachable.
candidate 2 (found by 3 of 93 passes): `compile_assert()`has had a reference implementation and has been used in codebases since 2023.
candidate 3 (found by 3 of 93 passes): `compile_assert()` relies on the compiler's control-flow analysis in the sample implementation.
candidate 4 (found by 3 of 93 passes): While there is no compiler supporting this feature directly, I created the following `compile_assert()` macro for GCC and Clang:

-->
