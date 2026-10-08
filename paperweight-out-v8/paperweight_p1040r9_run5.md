Verdict: Excellent (12/14)

The paper offers substantial support for its own standardization, with most of the necessary case laid out clearly and backed by implementation experience, performance data, and a survey of existing practice. The support is thinnest around coordination and interoperability, where the paper gestures at broad industry need but does not demonstrate how the feature would fit into the wider ecosystem or align with other standards and tooling.

- The strongest support comes from the demonstrated failure of existing library-only and tooling-based approaches, including concrete compiler performance and memory overhead numbers.
- The paper also establishes clear prior art, from `xxd` to earlier `F"..."` syntax proposals, and shows that multiple major implementations and real projects have already grappled with this problem.
- Implementation experience is well documented, with references to MongoDB’s custom tooling and a working implementation with published benchmarks.
- The most glaring omission is the coordination section, where the claim that many industries need the feature is asserted without evidence of engagement with those industries, adjacent standards bodies, or build-system maintainers.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 7 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 12.00   accumulate 12.17   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 0.50  insufficiency 2.00  implementation 2.00
sample agreement: 84 of 91 section-criterion pairs unanimous (92%)
single-sample totals would have been: 12.00 / 12.00 / 12.00   (all 3 samples: 12.00)
headings: h2 11
on threshold: audience
splits: motivation[5] 2/0/2  audience[9] 0/1/0  prior_art[10] 1/0/0  vehicle[6] 1/0/1
        vehicle[11] 2/1/0  insufficiency[5] 0/1/1  implementation[8] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                2/0/2  -> 1.33
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           2/2/2  -> 2.00
  [9] 6. Previous Implementations                  2/2/2  -> 2.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A proposal for a function that allows pulling resources at compile-time into a program, and a preprocessor directive to make finding those resources feasible for compilers and build systems.
candidate 2 (found by 3 of 39 passes): there were a small subsection of files on all deployed operating systems (Windows, Linux-based, and MacOS (both normal and Linux through Asahi Linux)) that needed users to be precise about the byte sequence used to address storage on disk.
candidate 3 (found by 3 of 39 passes): Forcing users to either adapt their code to play nice with this new C++ file system or maintaining a translation table to and from "C++ String Table" to "C++ File System" is an order of magnitude additional complexity.
candidate 4 (found by 2 of 39 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.

## audience - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  0/1/0  -> 0.33
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.
candidate 2 (found by 3 of 39 passes): All three major implementations were explored, plus an early implementation of this functionality in GCC.
candidate 3 (found by 1 of 39 passes): the author of this paper and almost 100% of the author’s clients do not use distributed anything to build their code

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           1/1/1  -> 1.00
  [9] 6. Previous Implementations                  2/2/2  -> 2.00
  [10] 7. Changes to the Standard                   1/0/0  -> 0.33
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time.
candidate 2 (found by 3 of 39 passes): Other techniques used include pre-processing data, link-time based tooling, and assembly-time runtime loading.
candidate 3 (found by 2 of 39 passes): many different tools and practices were adapted to handle this, as far back as 1995 with the `xxd` tool.
candidate 4 (found by 2 of 39 passes): As a backstop to the primary `std::u8string_view` template that we expect most users to employ with `u8""` string literals, we expect users to occasionally need to reach for `L""` (on fringe non-Windows and Windows machines) as well as `""`

## vehicle - grade 2.00 (fired in 5 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          1/0/1  -> 0.67
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  2/2/2  -> 2.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/1/0  -> 1.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This paper proposes `<embed>` to make this process much more efficient, portable, recursive, non-dependent on fixed preprocessor strings and streamlined.
candidate 2 (found by 3 of 39 passes): Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way?
candidate 3 (found by 3 of 39 passes): C++ does not need to make for itself a reputation of trying to be an extremely unique snowflake at the cost of usability and user friendliness.
candidate 4 (found by 2 of 39 passes): The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms.

## coordination - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           0/0/0  -> 0.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  0/0/0  -> 0.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Many industries need such functionality, including (but hardly limited to):

## insufficiency - grade 2.00 (fired in 3 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/1  -> 0.67
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  0/0/0  -> 0.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.
candidate 2 (found by 3 of 39 passes): This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully.
candidate 3 (found by 2 of 39 passes): It also absolutely destroys state-of-the-art compilers due to the extremely high memory overhead of producing an Abstract Syntax Tree for a braced initializer list of several tens of thousands of integral constants with numeric values at 255 or less.

## implementation - grade 2.00  [binary: max] (fired in 3 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           1/0/1  -> 0.67
  [9] 6. Previous Implementations                  0/0/0  -> 0.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): MongoDB uses a [custom python script](https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/jstoh.py), just to get their data into C++:
candidate 2 (found by 2 of 39 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable. We also scrutinize the performance, with numbers for both [memory overhead](https://github.com/ThePhD/embed#memory-size-results) and [speed overhead](https://github.com/ThePhD/embed#speed-results) available at the repository that houses the [current implementation](https://github.com/ThePhD/embed).
candidate 3 (found by 2 of 39 passes): Unfortunately, implementation experience attemping this found that there were a small subsection of files on all deployed operating systems
candidate 4 (found by 1 of 39 passes): For ease of access, the numbers as of January 2020 with the latest versions of the indicated compilers and tools are replicated below.

-->
