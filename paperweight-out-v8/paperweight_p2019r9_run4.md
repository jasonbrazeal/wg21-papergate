Verdict: Strong to Excellent (11/14)

The paper offers a reasonably strong case for standardization in several key areas, particularly in showing existing practice, implementation experience, and the difficulty of solving the problem outside the standard library. The support is thinnest when it comes to demonstrating who is concretely affected and why a non-standard library solution would be inadequate, where the argument leans on assertion rather than evidence.

- The strongest support comes from the documented existence of similar thread classes across major open source projects and a working prototype implementation, which grounds the proposal in real-world practice.
- The paper also convincingly establishes that setting attributes at thread creation forces a library to reimplement `std::thread` wholesale, making a standard-library solution the natural fit.
- The least established part is the claim about who is affected, since the paper names projects and use cases but does not substantiate the breadth or severity of the need beyond anecdotal and general statements.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 10.00   accumulate 13.17   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 1.00  implementation 2.00
sample agreement: 169 of 189 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.50 / 10.50 / 12.00   (all 3 samples: 11.00)
headings: h2 26
on threshold: vehicle, coordination, implementation
splits: motivation[4] 1/2/1  motivation[6] 2/0/2  motivation[8] 0/1/0  motivation[13] 1/0/0
        audience[6] 1/0/1  audience[7] 1/1/2  audience[12] 1/0/1  audience[16] 0/0/1
        prior_art[3] 0/0/2  prior_art[6] 0/2/0  prior_art[19] 1/0/1  vehicle[11] 0/1/1
        vehicle[16] 0/1/0  coordination[2] 0/0/1  coordination[6] 0/1/2  coordination[14] 0/0/1
        insufficiency[4] 1/0/1  insufficiency[7] 0/0/1  insufficiency[12] 1/0/1
        implementation[18] 0/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 13 of 27 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      1/2/1  -> 1.33
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   2/0/2  -> 1.33
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          0/1/0  -> 0.33
  [9] I don’t need that and don’t want to p... 1/1/1  -> 1.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 1/1/1  -> 1.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      1/0/0  -> 0.33
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  1/1/1  -> 1.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       1/1/1  -> 1.00
  [19] Implementation                               0/0/0  -> 0.00
  [20] Alternatives considered                      2/2/2  -> 2.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): The absence of these features make `std::thread` and `std::jthread` unfit or unsatisfactory for many use cases.
candidate 2 (found by 3 of 81 passes): Achieving the same result in C++20 requires duplicating the entire `std::thread` class, which would be difficult to fit in a Tony table.
candidate 3 (found by 3 of 81 passes): People working on AAA games told us that the lack of stack size support prevented them to use `std::thread`, which therefore fails to be a vocabulary type.
candidate 4 (found by 3 of 81 passes): On many implementations, including Linux, the space for the thread name is allocated re- gardless of whether it is used or not.

## audience - grade 1.00 (fired in 4 of 27 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   1/0/1  -> 0.67
  [7] Motivation for standardization               1/1/2  -> 1.33
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 1/0/1  -> 0.67
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   0/0/0  -> 0.00
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  0/0/1  -> 0.33
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       0/0/0  -> 0.00
  [19] Implementation                               0/0/0  -> 0.00
  [20] Alternatives considered                      0/0/0  -> 0.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): We found threads classes supporting names and stack size in many open source projects, including POCO, Chromium, Firefox, LLVM, Bloomberg Basic Development Environment, Folly, Intel TBB, Tensorflow...
candidate 2 (found by 2 of 81 passes): We also found multiple questions related to setting name thread on StackOverflow.
candidate 3 (found by 2 of 81 passes): This proposal will help more people use `std::thread`.
candidate 4 (found by 1 of 81 passes): It is also less generally useful and mostly used in HPC and embedded platforms, where there is the greatest variety of implementation.

## prior_art - grade 2.00 (fired in 13 of 27 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/2  -> 0.67
  [4] Example                                      1/1/1  -> 1.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/2/0  -> 0.67
  [7] Motivation for standardization               1/1/1  -> 1.00
  [8] FAQ                                          1/1/1  -> 1.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 1/1/1  -> 1.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      1/1/1  -> 1.00
  [16] What about other properties                  1/1/1  -> 1.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       2/2/2  -> 2.00
  [19] Implementation                               1/0/1  -> 0.67
  [20] Alternatives considered                      2/2/2  -> 2.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Achieving the same result in C++20 requires duplicating the entire `std::thread` class, which would be difficult to fit in a Tony table.
candidate 2 (found by 3 of 81 passes): We found threads classes supporting names and stack size in many open source projects, including POCO, Chromium, Firefox, LLVM, Bloomberg Basic Development Environment, Folly, Intel TBB, Tensorflow...
candidate 3 (found by 3 of 81 passes): There exist a POSIX function that makes the wording more palatable.
candidate 4 (found by 3 of 81 passes): We spent resources standardizing 2 (!) thread classes, which are not used in many cases.

## vehicle - grade 1.50 (fired in 6 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Motivation for standardization               1/1/1  -> 1.00
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/1/1  -> 0.67
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  0/1/0  -> 0.33
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       0/0/0  -> 0.00
  [19] Implementation                               0/0/0  -> 0.00
  [20] Alternatives considered                      2/2/2  -> 2.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Like thread names, adding this support to `std::thread` would be standardizing existing practices.
candidate 2 (found by 3 of 81 passes): The cost of re-implementing classes similar to `std::thread` is great for the industry.
candidate 3 (found by 3 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.
candidate 4 (found by 2 of 81 passes): Setting a stack size insufficient for the correct execution of a well-formed program isn’t different than if the default stack size is insufficient ([intro.compliance])

## coordination - grade 1.50 (fired in 4 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/1/2  -> 1.00
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 0/0/0  -> 0.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   0/0/1  -> 0.33
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  0/0/0  -> 0.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       0/0/0  -> 0.00
  [19] Implementation                               0/0/0  -> 0.00
  [20] Alternatives considered                      0/0/0  -> 0.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): People working on AAA games told us that the lack of stack size support prevented them to use `std::thread`, which therefore fails to be a vocabulary type.
candidate 2 (found by 2 of 81 passes): Most operating systems, including real-time operating systems for embedded platforms, provide a way to name threads.
candidate 3 (found by 1 of 81 passes): The absence of these features make `std::thread` and `std::jthread` unfit or unsatisfactory for many use cases.
candidate 4 (found by 1 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.

## insufficiency - grade 1.00 (fired in 5 of 27 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      1/0/1  -> 0.67
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Motivation for standardization               0/0/1  -> 0.33
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 1/0/1  -> 0.67
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  0/0/0  -> 0.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       0/0/0  -> 0.00
  [19] Implementation                               0/0/0  -> 0.00
  [20] Alternatives considered                      1/1/1  -> 1.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.
candidate 2 (found by 3 of 81 passes): A standard library that targets a limited number of platforms can set the attributes more easily than a library that may desire to work in an environment where C++ is deployed.
candidate 3 (found by 2 of 81 passes): Achieving the same result in C++20 requires duplicating the entire `std::thread` class, which would be difficult to fit in a Tony table.
candidate 4 (found by 2 of 81 passes): The cost of re-implementing classes similar to `std::thread` is great for the industry.

## implementation - grade 2.00  [binary: max] (fired in 3 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Motivation for standardization               1/1/1  -> 1.00
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 0/0/0  -> 0.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   0/0/0  -> 0.00
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  0/0/0  -> 0.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       0/2/1  -> 1.00
  [19] Implementation                               2/2/2  -> 2.00
  [20] Alternatives considered                      0/0/0  -> 0.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): We found threads classes supporting names and stack size in many open source projects, including POCO, Chromium, Firefox, LLVM, Bloomberg Basic Development Environment, Folly, Intel TBB, Tensorflow...
candidate 2 (found by 3 of 81 passes): A [prototype implementation](https://github.com/cor3ntin/llvm-project/tree/corentin/thread_name_p2019) for libc++ (supporting only POSIX) threads has been created to validate the design.
candidate 3 (found by 2 of 81 passes): This is made slightly easier by pack indexing ([P2662R2](https://wg21.link/P2662R2) [3]) [[Compiler](https://compiler-explorer.com/z/n8vYb7Tar) [Explorer]](https://compiler-explorer.com/z/n8vYb7Tar).

-->
