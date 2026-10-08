Verdict: Strong (11/14)

The paper gives solid support for the core motivation, the inadequacy of existing alternatives, and the feasibility of a compiler-backed library approach, but it leaves the affected audience and the coordination story more asserted than demonstrated. The thinnest part is the claim about how widely this need is felt and how the feature would fit into existing build and tooling workflows.

- The strongest support is the concrete evidence that current compiler behavior and existing tools impose severe performance or portability costs for embedding binary data.
- The paper also clearly establishes that a library-only solution cannot meet the compile-time and cross-platform goals, and that implementation experience in major compilers exists.
- The least developed area is the claim that a very large number of programmers attempt to include non-C++ data directly, which is stated without supporting evidence.
- The most glaring omission is a convincing account of how this proposal coordinates with build systems, resource discovery, and existing preprocessing or toolchain conventions.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 12.00   accumulate 11.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 0.50  insufficiency 2.00  implementation 2.00
sample agreement: 81 of 84 section-criterion pairs unanimous (96%)
single-sample totals would have been: 11.00 / 11.00 / 11.00   (all 3 samples: 11.00)
headings: h2 11
on threshold: none
splits: prior_art[9] 1/1/0  insufficiency[5] 1/1/0  implementation[10] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A proposal for a function that allows pulling resources at compile-time into a program, and a preprocessor directive to make finding those resources feasible for compilers and build systems.
candidate 2 (found by 3 of 36 passes): Binary data as C(++) arrays provide the overhead of having to comma-delimit every single byte present, it also requires that the compiler verify every entry in that array is a valid literal or entry according to the C++ language.
candidate 3 (found by 2 of 36 passes): Many industries need such functionality, including (but hardly limited to): Financial Development, Game Development, Embedded Development, Application Development, Server Development, Static Analyzers.
candidate 4 (found by 2 of 36 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable.

## audience - grade 0.50 (fired in 1 of 12 sections, strong in 0)
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
candidate 1 (found by 3 of 36 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.

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
candidate 3 (found by 3 of 36 passes): It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time.
candidate 4 (found by 3 of 36 passes): There is a tool called [incbin] which is a 3rd party attempt at pulling files in at "assembly time". Its approach is incredibly similar to `ld`, with the caveat that files must be shipped with their binary.

## vehicle - grade 2.00 (fired in 5 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Scope and Impact                          1/1/1  -> 1.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms.
candidate 2 (found by 3 of 36 passes): Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way?
candidate 3 (found by 3 of 36 passes): There is precedent for specifying library features that are implemented only through compile-time compiler intrinsics (`type_traits`, `source_location`, and similar utilities).
candidate 4 (found by 2 of 36 passes): This paper proposes `<embed>` to make this process much more efficient, portable, recursive, non-dependent on fixed preprocessor strings and streamlined.

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

## insufficiency - grade 2.00 (fired in 3 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/0  -> 0.67
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          0/0/0  -> 0.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.
candidate 2 (found by 2 of 36 passes): It also absolutely destroys state-of-the-art compilers due to the extremely high memory overhead of producing an Abstract Syntax Tree for a braced initializer list of several tens of thousands of integral constants with numeric values at 255 or less.
candidate 3 (found by 2 of 36 passes): This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully.
candidate 4 (found by 1 of 36 passes): Because these declarations are `extern`, the values in the array cannot be accessed at compilation/translation-time.

## implementation - grade 2.00  [binary: max] (fired in 3 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/2/0  -> 0.67
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Finally, a proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet.
candidate 2 (found by 3 of 36 passes): The current implementation uses `-fembed-path=some/path/here/` to indicate this, but when it is standardized there will probably be an `-RI` or `-resource-include` flag instead.
candidate 3 (found by 1 of 36 passes): MongoDB uses a [custom python script](https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/jstoh.py), just to get their data into C++:

-->
