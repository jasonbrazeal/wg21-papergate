Verdict: Strong (8/14)

The paper offers a mixed case for standardization, with its strongest material going to the existence of prior art and the limitations of current language facilities, but with several central claims about usage, implementation experience, and the need for a standard mechanism left asserted rather than demonstrated. The thinnest support appears where the paper needs to show that existing practice and the proposed facility actually require standardization rather than a library or tooling solution.

- The paper clearly establishes that current C++ mechanisms such as `static_assert`, `assert`, and contracts do not cover the intended compile-time checking inside ordinary functions, and it documents relevant compiler extensions and optimizer behavior.
- The paper’s claim that a standard keyword is needed rests mainly on the assertion that relying on non-standardized optimizer behavior is problematic, but it does not establish that this problem cannot be addressed through a portable library or existing compiler features.
- The paper asserts a reference implementation and use in code bases since 2023, but provides no evidence of adoption, scale, or lessons learned, leaving implementation experience unestablished.
- The paper does not address coordination and interoperability at all, leaving open how the proposed facility would interact with contracts, profiles, static analysis tools, or other standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 6 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 24. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.33   accumulate 9.00   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.33  implementation 1.33
sample agreement: 162 of 168 section-criterion pairs unanimous (96%)
single-sample totals would have been: 8.00 / 9.00 / 8.00   (all 3 samples: 8.17)
headings: h2 9 + bold numbered 14
on threshold: none
splits: motivation[3] 0/0/2  prior_art[7] 0/1/0  vehicle[3] 1/1/0  insufficiency[8] 1/2/1
        insufficiency[17] 2/0/2  implementation[13] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 24 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              0/0/2  -> 0.67
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           1/1/1  -> 1.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 1/1/1  -> 1.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Implementation                            0/0/0  -> 0.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           1/1/1  -> 1.00
  [13] 11. Sample examples and tests                0/0/0  -> 0.00
  [14] 12. Compilers supported                      0/0/0  -> 0.00
  [15] 14. Notes                                    1/1/1  -> 1.00
  [16] 15. Alternative keyword name instead of c... 0/0/0  -> 0.00
  [17] 15. Other approaches considered              2/2/2  -> 2.00
  [18] 16. Runtime vs compile-time constraints      2/2/2  -> 2.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 72 passes): There is no general mechanism that allows compile time assertions inside ordinary functions from regular compilers.
candidate 2 (found by 3 of 72 passes): Reliance on Optimizer, which in itself is not standardized is an issue.
candidate 3 (found by 3 of 72 passes): It feels more rational for the programmer just to put the if(handle>=0) in api_function(int handle) as best practice, the Optimizer could then eliminate redundant checks.
candidate 4 (found by 3 of 72 passes): compile_assert() isn't suited for everything. It doesn't always "drop in" to replace assert() and other required runtime checks.

## audience - grade 0.50 (fired in 1 of 24 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] 9. Implementation                            0/0/0  -> 0.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [13] 11. Sample examples and tests                0/0/0  -> 0.00
  [14] 12. Compilers supported                      0/0/0  -> 0.00
  [15] 14. Notes                                    0/0/0  -> 0.00
  [16] 15. Alternative keyword name instead of c... 0/0/0  -> 0.00
  [17] 15. Other approaches considered              0/0/0  -> 0.00
  [18] 16. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 72 passes): compile_assert() has had a reference implementation and been in use since 2023 in code bases.

## prior_art - grade 2.00 (fired in 11 of 24 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           1/1/1  -> 1.00
  [7] 6. Interaction With Existing Features        0/1/0  -> 0.33
  [8] 7. Implementation Experience                 1/1/1  -> 1.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Implementation                            2/2/2  -> 2.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           1/1/1  -> 1.00
  [13] 11. Sample examples and tests                0/0/0  -> 0.00
  [14] 12. Compilers supported                      0/0/0  -> 0.00
  [15] 14. Notes                                    0/0/0  -> 0.00
  [16] 15. Alternative keyword name instead of c... 1/1/1  -> 1.00
  [17] 15. Other approaches considered              2/2/2  -> 2.00
  [18] 16. Runtime vs compile-time constraints      1/1/1  -> 1.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 72 passes): All three major compilers (GCC, Clang, MSVC) are supported with a sample implementation.
candidate 2 (found by 3 of 72 passes): C++ currently provides: static_assert - requires constant expressions. assert - runtime check, calls abort() to terminate, optionally disabled. Contracts – runtime checks, in progress. Profiles – not yet standardized.
candidate 3 (found by 3 of 72 passes): This is fundamentally different from static_assert, which operates purely in the constantevaluation mode defined by the language.
candidate 4 (found by 3 of 72 passes): GCC and Clang both support __attribute__ ((error(message))), GCC since gcc-4.5.3 in 2011.

## vehicle - grade 1.00 (fired in 3 of 24 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/0  -> 0.67
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           1/1/1  -> 1.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 0/0/0  -> 0.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Implementation                            0/0/0  -> 0.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [13] 11. Sample examples and tests                0/0/0  -> 0.00
  [14] 12. Compilers supported                      0/0/0  -> 0.00
  [15] 14. Notes                                    0/0/0  -> 0.00
  [16] 15. Alternative keyword name instead of c... 0/0/0  -> 0.00
  [17] 15. Other approaches considered              0/0/0  -> 0.00
  [18] 16. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 2 of 72 passes): The benefit of this approach is users get a standard keyword, however they do not get a full warranty that everything will be enforced.
candidate 2 (found by 2 of 72 passes): There is no general mechanism that allows compile time assertions inside ordinary functions from regular compilers.
candidate 3 (found by 2 of 72 passes): Modern optimizing C++ compilers already eliminate unreachable branches and perform inter-procedural constant analysis. compile_assert() formalizes this capability into a portable language facility with a standardized keyword.
candidate 4 (found by 1 of 72 passes): Given the compiler is generating the machine code, it’s important the compile time assert is output from the compiler, not a separate static analysis tool that may or may not determine control flow the same way.

## coordination - grade 0.00 (fired in 0 of 24 sections, strong in 0)
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
  [10] 9. Implementation                            0/0/0  -> 0.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [13] 11. Sample examples and tests                0/0/0  -> 0.00
  [14] 12. Compilers supported                      0/0/0  -> 0.00
  [15] 14. Notes                                    0/0/0  -> 0.00
  [16] 15. Alternative keyword name instead of c... 0/0/0  -> 0.00
  [17] 15. Other approaches considered              0/0/0  -> 0.00
  [18] 16. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.33 (fired in 3 of 24 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 1/2/1  -> 1.33
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Implementation                            0/0/0  -> 0.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [13] 11. Sample examples and tests                0/0/0  -> 0.00
  [14] 12. Compilers supported                      0/0/0  -> 0.00
  [15] 14. Notes                                    0/0/0  -> 0.00
  [16] 15. Alternative keyword name instead of c... 0/0/0  -> 0.00
  [17] 15. Other approaches considered              2/0/2  -> 1.33
  [18] 16. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 72 passes): Reliance on Optimizer, which in itself is not standardized is an issue.
candidate 2 (found by 2 of 72 passes): Given the compiler is generating the machine code, it’s important the compile time assert is output from the compiler, not a separate static analysis tool that may or may not determine control flow the same way.
candidate 3 (found by 2 of 72 passes): Calling an external error function that does not exist causes the linker to output the file and line location of the compile_assert constraint failure.
candidate 4 (found by 1 of 72 passes): There’s limited visibility of what static analysis tools detect, they would need a dead code removal optimization too, as they do not output assembly like a compiler does.

## implementation - grade 1.33  [binary: max] (fired in 6 of 24 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Design Goals and Non-Goals                0/0/0  -> 0.00
  [6] 4. Proposed Design                           0/0/0  -> 0.00
  [7] 6. Interaction With Existing Features        0/0/0  -> 0.00
  [8] 7. Implementation Experience                 1/1/1  -> 1.00
  [9] 8. Impact on the Standard                    0/0/0  -> 0.00
  [10] 9. Implementation                            1/1/1  -> 1.00
  [11] 10. Example source                           0/0/0  -> 0.00
  [12] 10. LTO – Link Time Optimization           0/0/0  -> 0.00
  [13] 11. Sample examples and tests                1/2/1  -> 1.33
  [14] 12. Compilers supported                      1/1/1  -> 1.00
  [15] 14. Notes                                    0/0/0  -> 0.00
  [16] 15. Alternative keyword name instead of c... 0/0/0  -> 0.00
  [17] 15. Other approaches considered              0/0/0  -> 0.00
  [18] 16. Runtime vs compile-time constraints      0/0/0  -> 0.00
  [19] 17. Additional compiler implementations      0/0/0  -> 0.00
  [20] 17. Acknowledgments                          0/0/0  -> 0.00
  [21] 18. References                               0/0/0  -> 0.00
  [22] 19. External resources                       0/0/0  -> 0.00
  [23] 20. ChangeLog                                0/0/0  -> 0.00
  [24] 21. Revision history                         0/0/0  -> 0.00
candidate 1 (found by 3 of 72 passes): All three major compilers (GCC, Clang, MSVC) are supported with a sample implementation.
candidate 2 (found by 3 of 72 passes): compile_assert() has had a reference implementation and been in use since 2023 in code bases.
candidate 3 (found by 3 of 72 passes): A header-only implementation demonstrates this behavior by placing an ill-formed construct in a branch that the optimizer determines to be reachable.
candidate 4 (found by 3 of 72 passes): While there is no compiler supporting this feature directly, I created the following compile_assert macro for GCC and Clang:

-->
