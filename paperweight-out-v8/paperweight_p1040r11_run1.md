Verdict: Strong to Excellent (11/14)

The paper offers substantial support for several core elements of its standardization case, particularly in demonstrating prior art, the need for a standard rather than a library-only solution, and the existence of implementation experience. The thinnest parts concern who is affected and how the feature would coordinate or interoperate with existing build and resource-handling practices, where the paper asserts relevance and breadth without fully backing those claims.

- The strongest support is the concrete implementation experience in LLVM/Clang and GCC trunks, which shows the feature is more than a design sketch.
- The paper also clearly establishes why a library-only approach is insufficient, citing performance advantages and the limitations of tool-based and platform-specific workarounds.
- The case for prior art and alternatives is well grounded, including the relationship to the already-standardized `#embed` and earlier syntax proposals.
- The most glaring omission is a substantiated account of who is affected and how widely the problem occurs, since the paper claims a very large affected population but does not establish that reach.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 11.67   accumulate 11.33   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 0.33  insufficiency 2.00  implementation 2.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 12.00 / 10.50 / 11.50   (all 3 samples: 11.33)
headings: h2 11
on threshold: none
splits: motivation[2] 1/0/1  audience[5] 1/1/0  audience[7] 2/0/2  vehicle[10] 0/2/0
        coordination[5] 1/0/1  insufficiency[7] 1/2/2  implementation[8] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
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
candidate 1 (found by 3 of 36 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable.
candidate 2 (found by 3 of 36 passes): One of the biggest benefits of `std::embed` is that it’s a normal, regular `consteval` function call.
candidate 3 (found by 3 of 36 passes): There are problems with the `xxd -i` or similar tool-based approach. Lexing and Parsing data-as-source-code adds an enormous overhead to actually reading and making that data available.
candidate 4 (found by 2 of 36 passes): A proposal for a function that allows pulling resources at compile-time into a program, and a preprocessor directive to make finding those resources feasible for compilers and build systems.

## audience - grade 1.00 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/0  -> 0.67
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/0/2  -> 1.33
  [8] 6. Design Decisions                          0/0/0  -> 0.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.
candidate 2 (found by 1 of 36 passes): The file is of the size specified at the top of the column. Files are kept the same between strategies and tests.
candidate 3 (found by 1 of 36 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
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
  [9] 7. Changes to the Standard                   1/1/1  -> 1.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A simpler, C-friendly, preprocessor-only version of this functionality was standardized in C++26 and C23 with `#embed <file> params...`, which solved the problem for C and C-adjacent use cases.
candidate 2 (found by 3 of 36 passes): It was Circle’s conclusion that a generic API was unsuitable and suffered from the same performance pitfalls that currently plagued current-generation compilers today.
candidate 3 (found by 3 of 36 passes): It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time.
candidate 4 (found by 2 of 36 passes): The implementation-defined conversion of the `resource_identifier` to an appropriate sequence of characters to both search for the resource and perform the input dependency check allows for robust checking of resource names identified by the quote research source.

## vehicle - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
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
  [10] 8. Appendix                                  0/2/0  -> 0.67
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms.
candidate 2 (found by 3 of 36 passes): Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way?
candidate 3 (found by 3 of 36 passes): There is precedent for specifying library features that are implemented only through compile-time compiler intrinsics (`type_traits`, `source_location`, and similar utilities).
candidate 4 (found by 2 of 36 passes): A simpler, C-friendly, preprocessor-only version of this functionality was standardized in C++26 and C23 with `#embed <file> params...`, which solved the problem for C and C-adjacent use cases.

## coordination - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/0/1  -> 0.67
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 0/0/0  -> 0.00
  [8] 6. Design Decisions                          0/0/0  -> 0.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Many, many more data formats and their resulting files need to be parsed and stitched together in part or in whole to be usable without a pre-determined build system step.

## insufficiency - grade 2.00 (fired in 4 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 1/2/2  -> 1.67
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.
candidate 2 (found by 3 of 36 passes): This means that when processing data, it can be called recursively after reading the data from inside of the embedded file.
candidate 3 (found by 3 of 36 passes): This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully.
candidate 4 (found by 2 of 36 passes): Many different tools and practices were adapted to handle this, as far back as 1995 with the `xxd` tool.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/1  -> 1.67
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The current implementation uses `-fembed-path=some/path/here/` to indicate this, but when it is standardized there will probably be an `-RI` or `-resource-include` flag instead.
candidate 2 (found by 1 of 36 passes): a proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet. They can be viewed [here: https://github.com/ThePhD/embed/tree/main/patches](https://github.com/ThePhD/embed/tree/main/patches).
candidate 3 (found by 1 of 36 passes): a proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet. They can be viewed here: https://github.com/ThePhD/embed/tree/main/patches
candidate 4 (found by 1 of 36 passes): A proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet.

-->
