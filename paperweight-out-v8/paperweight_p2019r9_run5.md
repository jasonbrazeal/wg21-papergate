Verdict: Excellent (12/14)

The paper offers substantial support for the need to standardize thread attributes, particularly through its survey of existing practice and its prototype implementation. The case is thinnest where it argues that only standardization can solve the problem, since the claims about the necessity of a standard facility are asserted more than demonstrated.

- The strongest support comes from the breadth of prior art, with named thread and stack size support documented across major open source projects and a working libc++ prototype.
- The paper also clearly establishes who is affected, citing both industry reports and widespread community questions about thread naming.
- The weakest part of the argument is the claim that a library solution would be inadequate, which rests on assertions about duplication cost and portability without a fuller demonstration of why existing third-party libraries cannot serve.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 11.00   accumulate 13.83   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.33  coordination 2.00  insufficiency 1.00  implementation 2.00
sample agreement: 172 of 189 section-criterion pairs unanimous (91%)
single-sample totals would have been: 11.50 / 12.50 / 11.50   (all 3 samples: 11.83)
headings: h2 26
on threshold: audience, implementation
splits: motivation[6] 2/2/0  motivation[9] 1/1/0  motivation[13] 0/1/0  motivation[14] 1/2/2
        audience[2] 1/1/0  audience[12] 1/0/0  prior_art[6] 0/2/0  prior_art[9] 1/0/1
        prior_art[19] 1/0/1  vehicle[4] 0/1/0  vehicle[7] 1/2/1  vehicle[15] 0/0/1
        vehicle[20] 1/2/1  insufficiency[4] 1/1/0  insufficiency[7] 0/1/1
        insufficiency[12] 1/0/0  implementation[18] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 13 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      1/1/1  -> 1.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   2/2/0  -> 1.33
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          1/1/1  -> 1.00
  [9] I don’t need that and don’t want to p... 1/1/0  -> 0.67
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 1/1/1  -> 1.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/1/0  -> 0.33
  [14] This belongs in a library?                   1/2/2  -> 1.67
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
candidate 4 (found by 3 of 81 passes): It is rarely useful to query the stack size (except to assert that it is in a range acceptable to the application).

## audience - grade 1.50 (fired in 4 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   1/1/1  -> 1.00
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 1/0/0  -> 0.33
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   0/0/0  -> 0.00
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
candidate 1 (found by 3 of 81 passes): We also found multiple questions related to setting name thread on StackOverflow.
candidate 2 (found by 3 of 81 passes): We found threads classes supporting names and stack size in many open source projects, including POCO, Chromium, Firefox, LLVM, Bloomberg Basic Development Environment, Folly, Intel TBB, Tensorflow...
candidate 3 (found by 2 of 81 passes): both of which are, as we demonstrate, current practices in many domains.
candidate 4 (found by 1 of 81 passes): This proposal will help more people use `std::thread`.

## prior_art - grade 2.00 (fired in 13 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    2/2/2  -> 2.00
  [4] Example                                      1/1/1  -> 1.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/2/0  -> 0.67
  [7] Motivation for standardization               1/1/1  -> 1.00
  [8] FAQ                                          1/1/1  -> 1.00
  [9] I don’t need that and don’t want to p... 1/0/1  -> 0.67
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 1/1/1  -> 1.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      0/0/0  -> 0.00
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
candidate 1 (found by 3 of 81 passes): During the review of [P2019R3](https://wg21.link/P2019R3) [2], LEWG did not like the proposed `make_with_attributes` and said they would prefer a constructor that allows both attributes and arguments
candidate 2 (found by 3 of 81 passes): Achieving the same result in C++20 requires duplicating the entire `std::thread` class, which would be difficult to fit in a Tony table.
candidate 3 (found by 3 of 81 passes): We found threads classes supporting names and stack size in many open source projects, including POCO, Chromium, Firefox, LLVM, Bloomberg Basic Development Environment, Folly, Intel TBB, Tensorflow...
candidate 4 (found by 3 of 81 passes): Use cases for querying a thread name include printing stack traces [4]

## vehicle - grade 1.33 (fired in 6 of 27 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/1/0  -> 0.33
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Motivation for standardization               1/2/1  -> 1.33
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      0/0/1  -> 0.33
  [16] What about other properties                  0/0/0  -> 0.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       0/0/0  -> 0.00
  [19] Implementation                               0/0/0  -> 0.00
  [20] Alternatives considered                      1/2/1  -> 1.33
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): People working on AAA games told us that the lack of stack size support prevented them to use `std::thread`, which therefore fails to be a vocabulary type.
candidate 2 (found by 3 of 81 passes): The cost of re-implementing classes similar to `std::thread` is great for the industry.
candidate 3 (found by 3 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.
candidate 4 (found by 3 of 81 passes): We feel very strongly that such an approach fails to improve portability and only improves the status quo marginally.

## coordination - grade 2.00 (fired in 4 of 27 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   2/2/2  -> 2.00
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
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
candidate 2 (found by 3 of 81 passes): The cost of re-implementing classes similar to `std::thread` is great for the industry.
candidate 3 (found by 3 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.
candidate 4 (found by 2 of 81 passes): This non-exhaustive table shows that most platforms do in fact provide a way to set and often query a thread name.

## insufficiency - grade 1.00 (fired in 5 of 27 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      1/1/0  -> 0.67
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Motivation for standardization               0/1/1  -> 0.67
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 1/0/0  -> 0.33
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
candidate 2 (found by 2 of 81 passes): Achieving the same result in C++20 requires duplicating the entire `std::thread` class, which would be difficult to fit in a Tony table.
candidate 3 (found by 2 of 81 passes): We feel very strongly that such an approach fails to improve portability and only improves the status quo marginally.
candidate 4 (found by 1 of 81 passes): Libc++ `std::thread` implementation is (very approximately) 1000 lines of code. Because stack size needs to be set before thread creation, an application wishing to use a non-default stack size has to duplicate that effort.

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
  [18] Design                                       0/0/1  -> 0.33
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
candidate 3 (found by 1 of 81 passes): This is made slightly easier by pack indexing ([P2662R2](https://wg21.link/P2662R2) [3]) [[Compiler](https://compiler-explorer.com/z/n8vYb7Tar) [Explorer]](https://compiler-explorer.com/z/n8vYb7Tar).

-->
