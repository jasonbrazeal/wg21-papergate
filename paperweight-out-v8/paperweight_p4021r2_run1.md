Verdict: Strong (9/14)

The paper offers a reasonably solid foundation for why a compile-time assertion facility would be useful and why existing library or attribute-based approaches fall short, but it leaves the case for standardization itself more asserted than demonstrated. The thinnest areas are the absence of any coordination or interoperability discussion and the lack of concrete evidence about who would be affected by adopting the feature.

- The strongest support is the implementation experience, with a reference implementation and use in codebases since 2023, alongside a macro approach that works across all three major compilers.
- The paper also convincingly establishes why a library solution will not do, pointing to the need for compiler-integrated control-flow analysis and the limitations of external static analysis tools.
- The case for prior art and alternatives is well grounded, citing existing compiler attributes and the distinction from `static_assert` and runtime `assert`.
- The most glaring omission is the complete absence of any coordination and interoperability discussion, leaving open how the feature would interact with existing tooling, standards, or compiler ecosystems.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 31. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 10.17   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.50  implementation 2.00
sample agreement: 208 of 217 section-criterion pairs unanimous (96%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 15 + bold numbered 15
on threshold: insufficiency, implementation
splits: motivation[5] 0/1/0  motivation[19] 1/1/2  motivation[26] 1/0/1  prior_art[13] 1/1/2
        vehicle[23] 0/0/1  insufficiency[15] 1/0/1  insufficiency[19] 1/0/0
        implementation[17] 2/1/1  implementation[20] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 31 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Design Goals and Non-Goals                0/1/0  -> 0.33
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
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           1/1/2  -> 1.33
  [20] 11. Sample examples and tests                0/0/0  -> 0.00
  [21] 12. Compilers supported                      0/0/0  -> 0.00
  [22] 13. Notes                                    1/1/1  -> 1.00
  [23] 14. Other approaches considered              2/2/2  -> 2.00
  [24] 15. Runtime vs compile-time constraints      2/2/2  -> 2.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              1/0/1  -> 0.67
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): This new keyword is used for bounds checking, avoiding nullptr dereferences, parameter validation and data validation at compile-time.
candidate 2 (found by 3 of 93 passes): There is no general mechanism that allows flexible compile-time assertions inside ordinary functions from regular compilers based on control-flow analysis.
candidate 3 (found by 3 of 93 passes): Modern compilers already eliminate unreachable branches and perform inter-procedural constant analysis. `compile_assert()` formalizes this capability into a portable language facility with a standardized keyword and syntax.
candidate 4 (found by 3 of 93 passes): It feels more rational for the programmer to simply put the `if(handle>=0)` in `api_function(int handle)` as best practice, LTO could then eliminate redundant checks.

## audience - grade 0.50 (fired in 1 of 31 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
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
candidate 1 (found by 3 of 93 passes): `compile_assert()`has had a reference implementation and has been used in codebases since 2023.

## prior_art - grade 2.00 (fired in 10 of 31 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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
  [13] Forward references                           1/1/2  -> 1.33
  [14] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [15] 7. Implementation Experience                 1/1/1  -> 1.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     2/2/2  -> 2.00
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
candidate 1 (found by 3 of 93 passes): All three major compilers (GCC, Clang, MSVC) are supported by a sample implementation macro I published in 2023 that works by re-purposing the Optimizer to identify failure branches that should be unreachable.
candidate 2 (found by 3 of 93 passes): C currently provides: `static_assert()` - requires constant expressions. `assert()` - a runtime check that calls abort() to terminate and may be disabled.
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
  [22] 13. Notes                                    0/0/0  -> 0.00
  [23] 14. Other approaches considered              0/0/1  -> 0.33
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              0/0/0  -> 0.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): Compilers may implement the keyword as a warning, with the option for it to be a hard compile error.
candidate 2 (found by 3 of 93 passes): Since the compiler generates the machine code, it is important that the compile-time assertion originates from the compiler; rather than a separate static analysis tool which may or may not determine control-flow the same way.
candidate 3 (found by 3 of 93 passes): Modern compilers already eliminate unreachable branches and perform inter-procedural constant analysis. `compile_assert()` formalizes this capability into a portable language facility with a standardized keyword and syntax.
candidate 4 (found by 1 of 93 passes): When `compile_assert()` is implemented as a macro, the reported file and line number are accurate.

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

## insufficiency - grade 1.50 (fired in 4 of 31 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
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
  [15] 7. Implementation Experience                 1/0/1  -> 0.67
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     0/0/0  -> 0.00
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           1/0/0  -> 0.33
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
candidate 1 (found by 2 of 93 passes): There is limited visibility of what static analysis tools detect, they would need unreachable dead code removal, and a way to output their analysis, as they do not output assembly like a compiler does.
candidate 2 (found by 2 of 93 passes): GCC has supported `__attribute__((error("message")))` since version 4.3 in 2008, since GCC 5 in 2015 `[[gnu::error(message)]]` support was added.
candidate 3 (found by 1 of 93 passes): Since the compiler generates the machine code, it is important that the compile-time assertion originates from the compiler; rather than a separate static analysis tool which may or may not determine control-flow the same way.
candidate 4 (found by 1 of 93 passes): GCC and Clang both support `__attribute__ ((error(message)))`, GCC since version 4.3 in 2008.

## implementation - grade 2.00  [binary: max] (fired in 10 of 31 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [15] 7. Implementation Experience                 1/1/1  -> 1.00
  [16] 8. Impact on the Standard                    0/0/0  -> 0.00
  [17] 9. Sample implementation                     2/1/1  -> 1.33
  [18] 10. Example source                           0/0/0  -> 0.00
  [19] 10. LTO – Link Time Optimization           2/2/2  -> 2.00
  [20] 11. Sample examples and tests                1/2/1  -> 1.33
  [21] 12. Compilers supported                      1/1/1  -> 1.00
  [22] 13. Notes                                    0/0/0  -> 0.00
  [23] 14. Other approaches considered              1/1/1  -> 1.00
  [24] 15. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [25] 16. Additional compiler implementations      0/0/0  -> 0.00
  [26] 17. Limitations                              1/1/1  -> 1.00
  [27] 18. Acknowledgments                          0/0/0  -> 0.00
  [28] 19. References                               0/0/0  -> 0.00
  [29] 21. External resources                       0/0/0  -> 0.00
  [30] 22. ChangeLog                                0/0/0  -> 0.00
  [31] 23. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 93 passes): All three major compilers (GCC, Clang, MSVC) are supported by a sample implementation macro I published in 2023 that works by re-purposing the Optimizer to identify failure branches that should be unreachable.
candidate 2 (found by 3 of 93 passes): `compile_assert()`has had a reference implementation and has been used in codebases since 2023.
candidate 3 (found by 3 of 93 passes): `compile_assert()` relies on the compiler's control-flow analysis in the sample implementation.
candidate 4 (found by 3 of 93 passes): A header-only implementation demonstrates this behavior by placing an ill-formed construct in a branch that the compiler determines to be reachable.

-->
