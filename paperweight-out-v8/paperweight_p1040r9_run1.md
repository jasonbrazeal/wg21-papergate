Verdict: Excellent (12/14)

The paper gives substantial support for standardizing this facility, with its strongest material covering the practical need, the affected audience, the failure of library-only approaches, and the existence of implementation experience. The support is thinnest where the paper gestures at coordination and interoperability across industries and toolchains but does not actually demonstrate how the proposed facility would fit into those broader ecosystems.

- The paper convincingly establishes why the problem matters and that a very large number of C and C++ programmers encounter it when embedding non-C++ data.
- It also makes a strong case that existing tool-based and library-based alternatives impose unacceptable compilation overhead or platform-specific complexity.
- The most glaring omission is the lack of concrete evidence for the claimed coordination and interoperability benefits, which remain asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.33/14)

Provisionally addressed: 7 of 7. Provisional points: 12.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.33   corroborated 12.00   accumulate 13.00   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 0.83  insufficiency 2.00  implementation 2.00
sample agreement: 80 of 91 section-criterion pairs unanimous (88%)
single-sample totals would have been: 13.50 / 12.50 / 12.00   (all 3 samples: 12.33)
headings: h2 11
on threshold: audience, implementation
splits: motivation[5] 0/2/2  motivation[8] 0/1/0  audience[9] 1/0/0  audience[11] 2/0/0
        prior_art[10] 0/1/0  vehicle[11] 2/0/2  coordination[7] 0/1/0  coordination[11] 2/0/0
        insufficiency[5] 1/2/1  implementation[8] 1/0/0  implementation[11] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/2/2  -> 1.33
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/1/0  -> 0.33
  [9] 6. Previous Implementations                  2/2/2  -> 2.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Forcing users to either adapt their code to play nice with this new C++ file system or maintaining a translation table to and from "C++ String Table" to "C++ File System" is an order of magnitude additional complexity.
candidate 2 (found by 2 of 39 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.
candidate 3 (found by 2 of 39 passes): This is problematic because it turns binary data in C++ source. In many cases, this results in a larger file due to having to restructure the data to fit grammar requirements.
candidate 4 (found by 2 of 39 passes): There are problems with the `xxd -i` or similar tool-based approach. Lexing and Parsing data-as-source-code adds an enormous overhead to actually reading and making that data available.

## audience - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  1/0/0  -> 0.33
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/0/0  -> 0.67
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code.
candidate 2 (found by 3 of 39 passes): All three major implementations were explored, plus an early implementation of this functionality in GCC.
candidate 3 (found by 1 of 39 passes): the author of this paper and almost 100% of the author’s clients do not use distributed anything to build their code
candidate 4 (found by 1 of 39 passes): MongoDB uses a [custom python script](https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/jstoh.py), just to get their data into C++:

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
  [10] 7. Changes to the Standard                   0/1/0  -> 0.33
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): many different tools and practices were adapted to handle this, as far back as 1995 with the `xxd` tool.
candidate 2 (found by 3 of 39 passes): It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time.
candidate 3 (found by 3 of 39 passes): This implementation idea was floated twice, once during SG-7 discussion at the November 2019 Belfast meeting and again during the February 2020 Prague meeting.
candidate 4 (found by 3 of 39 passes): Other techniques used include pre-processing data, link-time based tooling, and assembly-time runtime loading.

## vehicle - grade 2.00 (fired in 5 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          1/1/1  -> 1.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  2/2/2  -> 2.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/0/2  -> 1.33
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This paper proposes `<embed>` to make this process much more efficient, portable, recursive, non-dependent on fixed preprocessor strings and streamlined.
candidate 2 (found by 3 of 39 passes): The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms.
candidate 3 (found by 3 of 39 passes): Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way?
candidate 4 (found by 2 of 39 passes): C++ does not need to make for itself a reputation of trying to be an extremely unique snowflake at the cost of usability and user friendliness.

## coordination - grade 0.83 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           0/1/0  -> 0.33
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  0/0/0  -> 0.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/0/0  -> 0.67
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Many industries need such functionality, including (but hardly limited to):
candidate 2 (found by 1 of 39 passes): This hurts the portability and interop story of C++ with other tools and languages.
candidate 3 (found by 1 of 39 passes): This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully.

## insufficiency - grade 2.00 (fired in 3 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                1/2/1  -> 1.33
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           0/0/0  -> 0.00
  [9] 6. Previous Implementations                  0/0/0  -> 0.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/2/2  -> 2.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): It also absolutely destroys state-of-the-art compilers due to the extremely high memory overhead of producing an Abstract Syntax Tree for a braced initializer list of several tens of thousands of integral constants with numeric values at 255 or less.
candidate 2 (found by 3 of 39 passes): This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully.
candidate 3 (found by 2 of 39 passes): This is problematic because it turns binary data in C++ source. In many cases, this results in a larger file due to having to restructure the data to fit grammar requirements.
candidate 4 (found by 1 of 39 passes): The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers.

## implementation - grade 2.00  [binary: max] (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Relevant Polls                            0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Scope and Impact                          0/0/0  -> 0.00
  [7] 5. Design Decisions  (part 1 of 2)           2/2/2  -> 2.00
  [8] 5. Design Decisions  (part 2 of 2)           1/0/0  -> 0.33
  [9] 6. Previous Implementations                  0/0/0  -> 0.00
  [10] 7. Changes to the Standard                   0/0/0  -> 0.00
  [11] 8. Appendix                                  2/0/0  -> 0.67
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable. We also scrutinize the performance, with numbers for both [memory overhead](https://github.com/ThePhD/embed#memory-size-results) and [speed overhead](https://github.com/ThePhD/embed#speed-results) available at the repository that houses the [current implementation](https://github.com/ThePhD/embed).
candidate 2 (found by 1 of 39 passes): Unfortunately, implementation experience attemping this found that there were a small subsection of files on all deployed operating systems
candidate 3 (found by 1 of 39 passes): MongoDB uses a [custom python script](https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/jstoh.py), just to get their data into C++:

-->
