Verdict: Excellent (12/14)

The paper offers substantial support for standardizing thread attributes, with most of its case grounded in concrete industry use, existing practice, and implementation experience. The thinnest part is the argument that a library solution cannot suffice: the paper asserts this strongly but does not fully demonstrate why a portable library wrapper would be inadequate.

- The strongest support comes from implementation experience, including a prototype in libc++ and named thread classes in major open-source projects such as Chromium, Firefox, LLVM, and TBB.
- The paper clearly establishes why the feature matters and who is affected, citing AAA game developers, StackOverflow demand, and the failure of `std::thread` as a vocabulary type.
- Prior art and alternatives are well covered, with direct reference to LEWG feedback on P2019R3 and POSIX facilities that make the wording feasible.
- The most glaring omission is the claim that a library will not do, which is asserted through duplication cost and portability pain but never backed by a concrete demonstration that a non-standard library approach is unworkable.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 27. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 10.00   accumulate 13.67   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.67  insufficiency 1.00  implementation 2.00
sample agreement: 178 of 189 section-criterion pairs unanimous (94%)
single-sample totals would have been: 11.50 / 11.50 / 12.00   (all 3 samples: 11.67)
headings: h2 26
on threshold: audience, vehicle, coordination, implementation
splits: motivation[4] 2/1/1  motivation[14] 2/1/1  motivation[17] 0/0/1  audience[12] 0/1/1
        prior_art[6] 0/2/2  prior_art[7] 1/1/0  prior_art[15] 1/0/0  vehicle[4] 0/0/1
        coordination[7] 1/1/2  coordination[14] 1/0/0  insufficiency[7] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 14 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      2/1/1  -> 1.33
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   2/2/2  -> 2.00
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          1/1/1  -> 1.00
  [9] I don’t need that and don’t want to p... 1/1/1  -> 1.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 1/1/1  -> 1.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      1/1/1  -> 1.00
  [14] This belongs in a library?                   2/1/1  -> 1.33
  [15] What about GPU threads?                      0/0/0  -> 0.00
  [16] What about other properties                  1/1/1  -> 1.00
  [17] Proposed design                              0/0/1  -> 0.33
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
candidate 3 (found by 3 of 81 passes): More generally, such inconsistencies are a source of bugs and expensive testing.
candidate 4 (found by 3 of 81 passes): People working on AAA games told us that the lack of stack size support prevented them to use `std::thread`, which therefore fails to be a vocabulary type.

## audience - grade 1.50 (fired in 3 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   1/1/1  -> 1.00
  [7] Motivation for standardization               2/2/2  -> 2.00
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 0/1/1  -> 0.67
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
candidate 3 (found by 2 of 81 passes): This proposal will help more people use `std::thread`.

## prior_art - grade 2.00 (fired in 12 of 27 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    2/2/2  -> 2.00
  [4] Example                                      1/1/1  -> 1.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/2/2  -> 1.33
  [7] Motivation for standardization               1/1/0  -> 0.67
  [8] FAQ                                          1/1/1  -> 1.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 1/1/1  -> 1.00
  [12] This is not something that the committee ... 1/1/1  -> 1.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/1/1  -> 1.00
  [15] What about GPU threads?                      1/0/0  -> 0.33
  [16] What about other properties                  1/1/1  -> 1.00
  [17] Proposed design                              0/0/0  -> 0.00
  [18] Design                                       2/2/2  -> 2.00
  [19] Implementation                               0/0/0  -> 0.00
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
candidate 3 (found by 3 of 81 passes): Use cases for querying a thread name include printing stack traces [4]
candidate 4 (found by 3 of 81 passes): There exist a POSIX function that makes the wording more palatable.

## vehicle - grade 1.50 (fired in 5 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/1  -> 0.33
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
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
  [20] Alternatives considered                      1/1/1  -> 1.00
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

## coordination - grade 1.67 (fired in 3 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      0/0/0  -> 0.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   2/2/2  -> 2.00
  [7] Motivation for standardization               1/1/2  -> 1.33
  [8] FAQ                                          0/0/0  -> 0.00
  [9] I don’t need that and don’t want to p... 0/0/0  -> 0.00
  [10] It’s an ABI break ???                      0/0/0  -> 0.00
  [11] We cannot speak about stack size in the s... 0/0/0  -> 0.00
  [12] This is not something that the committee ... 0/0/0  -> 0.00
  [13] I cannot implement that on my platform?      0/0/0  -> 0.00
  [14] This belongs in a library?                   1/0/0  -> 0.33
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
candidate 1 (found by 3 of 81 passes): Most operating systems, including real-time operating systems for embedded platforms, provide a way to name threads.
candidate 2 (found by 3 of 81 passes): People working on AAA games told us that the lack of stack size support prevented them to use `std::thread`, which therefore fails to be a vocabulary type.
candidate 3 (found by 1 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.

## insufficiency - grade 1.00 (fired in 5 of 27 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revisions                                    0/0/0  -> 0.00
  [4] Example                                      1/1/1  -> 1.00
  [5] Previous Polls                               0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Motivation for standardization               1/1/0  -> 0.67
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
  [20] Alternatives considered                      1/1/1  -> 1.00
  [21] Wording                                      0/0/0  -> 0.00
  [22] ■                                          0/0/0  -> 0.00
  [23] ? Threads [thread.threads]                   0/0/0  -> 0.00
  [24] jthread                                      0/0/0  -> 0.00
  [25] Feature test macros                          0/0/0  -> 0.00
  [26] Acknowledgments                              0/0/0  -> 0.00
  [27] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 81 passes): Achieving the same result in C++20 requires duplicating the entire `std::thread` class, which would be difficult to fit in a Tony table.
candidate 2 (found by 3 of 81 passes): The cost of re-implementing classes similar to `std::thread` is great for the industry.
candidate 3 (found by 3 of 81 passes): Because the proposed attributes may need to be set during the thread creation, a library would have no choice but to reimplement all of `std::thread`.
candidate 4 (found by 3 of 81 passes): This solves the problem of having to rewrite an entire thread class just to set a stack size. However, it would still be painful to do so portably, as described in P0484.

## implementation - grade 2.00  [binary: max] (fired in 2 of 27 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [18] Design                                       0/0/0  -> 0.00
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

-->
