Verdict: Excellent (13/14)

The paper offers substantial support for standardizing `std::embed`, with its strongest material covering motivation, affected users, prior art, the need for a standard facility, and implementation experience. The case is thinnest around coordination and interoperability, where the paper asserts relationships with build systems, resource paths, and recursive processing but does not fully establish how those interactions would work in practice.

- The paper convincingly demonstrates that existing `#include` and tool-based approaches impose severe compile-time and memory costs, and that `std::embed` as a `consteval` function avoids those pitfalls.
- Prior art is well covered, including the C and C++ `#embed` directive and earlier Circle syntax, which helps situate the proposal within an ongoing standardization conversation.
- Implementation experience is established through completed LLVM/Clang and GCC patches, lending credibility to the feasibility of the design.
- The most glaring omission is a clear account of how `std::embed` coordinates with build systems and resource lookup paths, since the paper claims such integration but leaves the mechanics largely unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.83/14)

Provisionally addressed: 7 of 7. Provisional points: 12.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.83   corroborated 12.00   accumulate 12.83   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 1.33  insufficiency 2.00  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 12.50 / 13.00 / 13.00   (all 3 samples: 12.83)
headings: h2 11
on threshold: audience, coordination, implementation
splits: motivation[2] 1/0/1  vehicle[6] 0/1/1  vehicle[8] 2/1/1  coordination[5] 0/1/1
        insufficiency[5] 0/1/1  implementation[8] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable.
candidate 2 (found by 3 of 36 passes): There are problems with the `xxd -i` or similar tool-based approach. Lexing and Parsing data-as-source-code adds an enormous overhead to actually reading and making that data available.
candidate 3 (found by 2 of 36 passes): A proposal for a function that allows pulling resources at compile-time into a program, and a preprocessor directive to make finding those resources feasible for compilers and build systems.
candidate 4 (found by 2 of 36 passes): One of the biggest benefits of `std::embed` is that it’s a normal, regular `consteval` function call.

## audience - grade 1.50 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          0/0/0  -> 0.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.
candidate 2 (found by 2 of 36 passes): Below are timing results for a file of random bytes using a specific strategy.
candidate 3 (found by 1 of 36 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.

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
  [9] 7. Changes to the Standard                   1/1/1  -> 1.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A simpler, C-friendly, preprocessor-only version of this functionality was standardized in C++26 and C23 with `#embed <file> params...`, which solved the problem for C and C-adjacent use cases.
candidate 2 (found by 3 of 36 passes): It was Circle’s conclusion that a generic API was unsuitable and suffered from the same performance pitfalls that currently plagued current-generation compilers today.
candidate 3 (found by 3 of 36 passes): It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time.
candidate 4 (found by 3 of 36 passes): The wording also explicitly disallows the usage of the function outside of a core constant expression by marking it `consteval`

## vehicle - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Scope and Impact                          0/1/1  -> 0.67
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/1/1  -> 1.33
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes `<embed>` to make this process much more efficient, portable, recursive, non-dependent on fixed preprocessor strings and streamlined.
candidate 2 (found by 3 of 36 passes): Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way?
candidate 3 (found by 3 of 36 passes): There is precedent for specifying library features that are implemented only through compile-time compiler intrinsics (`type_traits`, `source_location`, and similar utilities).
candidate 4 (found by 2 of 36 passes): The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms.

## coordination - grade 1.33 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/1  -> 0.67
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 0/0/0  -> 0.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Many, many more data formats and their resulting files need to be parsed and stitched together in part or in whole to be usable without a pre-determined build system step.
candidate 2 (found by 1 of 36 passes): This means that when processing data, it can be called recursively after reading the data from inside of the embedded file.
candidate 3 (found by 1 of 36 passes): This is because one is for resources that are found only on the system / implementation paths similar to `-I` and `-isystem`, and then one that uses local look up plus the aforementioned resource paths.
candidate 4 (found by 1 of 36 passes): One of the biggest benefits of `std::embed` is that it’s a normal, regular `consteval` function call.

## insufficiency - grade 2.00 (fired in 4 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/1  -> 0.67
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Implementation Experience & Current Pr... 2/2/2  -> 2.00
  [8] 6. Design Decisions                          2/2/2  -> 2.00
  [9] 7. Changes to the Standard                   0/0/0  -> 0.00
  [10] 8. Appendix                                  2/2/2  -> 2.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.
candidate 2 (found by 3 of 36 passes): This means that when processing data, it can be called recursively after reading the data from inside of the embedded file.
candidate 3 (found by 2 of 36 passes): It also absolutely destroys state-of-the-art compilers due to the extremely high memory overhead of producing an Abstract Syntax Tree for a braced initializer list of several tens of thousands of integral constants with numeric values at 255 or less.
candidate 4 (found by 2 of 36 passes): Because these declarations are `extern`, the values in the array cannot be accessed at compilation/translation-time.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
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
  [10] 8. Appendix                                  0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The current implementation uses `-fembed-path=some/path/here/` to indicate this, but when it is standardized there will probably be an `-RI` or `-resource-include` flag instead.
candidate 2 (found by 2 of 36 passes): A proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet.
candidate 3 (found by 1 of 36 passes): A proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet. They can be viewed here: https://github.com/ThePhD/embed/tree/main/patches.

-->
