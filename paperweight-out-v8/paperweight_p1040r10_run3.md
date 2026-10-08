Verdict: Strong to Excellent (12/14)

The paper offers substantial support for standardizing `std::embed`, particularly in demonstrating why existing alternatives fail and why a library-only solution is impractical. The case is thinnest around who is actually affected and how the feature would coordinate with existing build and tooling ecosystems, where the paper asserts broad relevance without concrete evidence.

- The strongest support is the implementation experience, with working patches in LLVM/Clang and GCC trunks showing the feature is realizable in practice.
- The paper clearly establishes why a library will not do, citing compiler memory blowups and platform-specific workarounds that a standardized intrinsic could avoid.
- The discussion of prior art and alternatives is well grounded, especially in contrasting `std::embed` with the C++26 `#embed` preprocessor feature and third-party tools.
- The most glaring omission is the lack of established evidence about who is affected or how the feature would interoperate with existing build systems and data-processing workflows.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 12.00   accumulate 11.67   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 2.00  coordination 0.50  insufficiency 2.00  implementation 2.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 11.00 / 12.00 / 12.00   (all 3 samples: 11.67)
headings: h2 11
on threshold: implementation
splits: motivation[2] 1/0/1  motivation[5] 2/0/2  audience[7] 0/2/2  prior_art[9] 1/1/0
        vehicle[5] 1/2/1  implementation[8] 1/2/1  implementation[10] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                2/0/2  -> 1.33
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable.
candidate 2 (found by 3 of 36 passes): Binary data as C(++) arrays provide the overhead of having to comma-delimit every single byte present, it also requires that the compiler verify every entry in that array is a valid literal or entry according to the C++ language.
candidate 3 (found by 2 of 36 passes): A proposal for a function that allows pulling resources at compile-time into a program, and a preprocessor directive to make finding those resources feasible for compilers and build systems.
candidate 4 (found by 2 of 36 passes): One of the biggest benefits of `std::embed` is that it’s a normal, regular `consteval` function call.

## audience - grade 1.17 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 0/2/2  -> 1.33
  [8] 6. Design Decisions                          0/0/0  -> 0.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.
candidate 2 (found by 2 of 36 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   1/1/0  -> 0.67
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A simpler, C-friendly, preprocessor-only version of this functionality was standardized in C++26 and C23 with `#embed <file> params...`, which solved the problem for C and C-adjacent use cases.
candidate 2 (found by 3 of 36 passes): It was Circle’s conclusion that a generic API was unsuitable and suffered from the same performance pitfalls that currently plagued current-generation compilers today.
candidate 3 (found by 3 of 36 passes): There is a tool called [incbin] which is a 3rd party attempt at pulling files in at "assembly time". Its approach is incredibly similar to `ld`, with the caveat that files must be shipped with their binary.
candidate 4 (found by 2 of 36 passes): It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time.

## vehicle - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/2/1  -> 1.33
  [6] 4. Scope and Impact                          1/1/1  -> 1.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes `<embed>` to make this process much more efficient, portable, recursive, non-dependent on fixed preprocessor strings and streamlined.
candidate 2 (found by 3 of 36 passes): The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms.
candidate 3 (found by 3 of 36 passes): Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way?
candidate 4 (found by 3 of 36 passes): There is precedent for specifying library features that are implemented only through compile-time compiler intrinsics (`type_traits`, `source_location`, and similar utilities).

## coordination - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 0/0/0  -> 0.00
  [8] 6. Design Decisions                          0/0/0  -> 0.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Many, many more data formats and their resulting files need to be parsed and stitched together in part or in whole to be usable without a pre-determined build system step.

## insufficiency - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          1/1/1  -> 1.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It also absolutely destroys state-of-the-art compilers due to the extremely high memory overhead of producing an Abstract Syntax Tree for a braced initializer list of several tens of thousands of integral constants with numeric values at 255 or less.
candidate 2 (found by 3 of 36 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.
candidate 3 (found by 3 of 36 passes): This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully.
candidate 4 (found by 2 of 36 passes): This means that when processing data, it can be called recursively after reading the data from inside of the embedded file.

## implementation - grade 2.00  [binary: max] (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          1/2/1  -> 1.33
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/0/2  -> 1.33
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The current implementation uses `-fembed-path=some/path/here/` to indicate this, but when it is standardized there will probably be an `-RI` or `-resource-include` flag instead.
candidate 2 (found by 2 of 36 passes): a proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet. They can be viewed [here: https://github.com/ThePhD/embed/tree/main/patches](https://github.com/ThePhD/embed/tree/main/patches).
candidate 3 (found by 2 of 36 passes): MongoDB uses a [custom python script](https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/jstoh.py), just to get their data into C++:
candidate 4 (found by 1 of 36 passes): A proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet.

-->
