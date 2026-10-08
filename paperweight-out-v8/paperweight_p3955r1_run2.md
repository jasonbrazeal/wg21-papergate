Verdict: Strong (8/14)

The paper offers solid grounding for the problem it addresses and for the existence of prior work, but its case for standardization rests largely on assertions rather than demonstrated need, with the weakest support around why a library solution is insufficient and how the proposal coordinates with existing facilities.

- The strongest support is the clear framing of asynchronous scopes as the natural counterpart to synchronous RAII and the acknowledgment of prior exploration by Kirk Shoop.
- The paper also establishes that existing idioms like `just(...) | let_value(...)` are awkward enough to motivate a better mechanism.
- The thinnest support is the claim that a library cannot adequately solve the problem, since the examples given involve synchronous objects and system calls outside the standard’s scope.
- The most glaring omission is any concrete demonstration of implementation experience or interoperability with the async facilities already slated for C++26.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 7 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.33   accumulate 8.00   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.17  coordination 0.50  insufficiency 1.17  implementation 1.00
sample agreement: 131 of 140 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 8.00 / 8.50   (all 3 samples: 8.00)
headings: h2 18
on threshold: insufficiency
splits: motivation[10] 1/2/2  motivation[11] 0/2/0  motivation[16] 1/1/2  audience[7] 0/0/1
        prior_art[6] 1/0/1  prior_art[14] 1/0/1  vehicle[7] 1/2/1  insufficiency[7] 0/0/1
        implementation[10] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 20 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         2/2/2  -> 2.00
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 2/2/2  -> 2.00
  [10] Proposed Design                              1/2/2  -> 1.67
  [11] Examples                                     0/2/0  -> 0.67
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      1/1/2  -> 1.33
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): This paper lays out an approach to achieving the same effect as regular, synchronous scopes in the asynchronous domain (i.e. `std::execution` [1]), including asynchronous construction and destruction of objects.
candidate 2 (found by 3 of 60 passes): Unfortunately C++ is a fundamentally synchronous language. Entering and leaving a scope, and therefore the power of RAII, is only available synchronously.
candidate 3 (found by 3 of 60 passes): The most serious issue with the previous design is that it requires that `async_construct` and `async_destruct` be invocable on const lvalue async objects.
candidate 4 (found by 3 of 60 passes): This utility provides a superior alternative to the idiom of `execution::just(...) |` `execution::let_value(...)` ([10] at 40:06) which is commonly used to place one or more objects in an operation state and thereby attach them to an asynchronous scope.

## audience - grade 0.17 (fired in 1 of 20 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         0/0/1  -> 0.33
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposed Design                              0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      0/0/0  -> 0.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 60 passes): Two phase init could clearly be used here, but that is widely regarded as an antipattern in general

## prior_art - grade 2.00 (fired in 12 of 20 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    1/1/1  -> 1.00
  [6] What Is an “Asynchronous Object?”        1/0/1  -> 0.67
  [7] Why Are Asynchronous Objects Needed?         2/2/2  -> 2.00
  [8] Prior Design                                 2/2/2  -> 2.00
  [9] Issues With the Prior Design                 2/2/2  -> 2.00
  [10] Proposed Design                              2/2/2  -> 2.00
  [11] Examples                                     2/2/2  -> 2.00
  [12] Proposed Wording  (part 1 of 2)              1/1/1  -> 1.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    1/0/1  -> 0.67
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      2/2/2  -> 2.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): This paper lays out an approach to achieving the same effect as regular, synchronous scopes in the asynchronous domain (i.e. `std::execution` [1])
candidate 2 (found by 3 of 60 passes): An asynchronous simulacrum of itself, as another ([2] at §3):
candidate 3 (found by 3 of 60 passes): Kirk Shoop has previously explored this space [2]. With his permission the author of this paper is continuing that exploration.
candidate 4 (found by 3 of 60 passes): A narrow solution to the specific problem above has been proposed: `execution::let_async_scope` [5] (this will be returned to later in this paper), but we can do better.

## vehicle - grade 1.17 (fired in 2 of 20 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         1/2/1  -> 1.33
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposed Design                              0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      0/0/0  -> 0.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): To evolve its asynchronous ecosystem and achieve parity with its synchronous ecosystem C++ needs not only asynchronous functions, but also asynchronous objects [2].
candidate 2 (found by 3 of 60 passes): POSIX system calls and io_uring are beyond the purview of the standard, however, and for justification of asynchronous destructors we need not look that far.

## coordination - grade 0.50 (fired in 1 of 20 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         1/1/1  -> 1.00
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposed Design                              0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      0/0/0  -> 0.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): C++26 actually contains such a justification: Async scopes [4].

## insufficiency - grade 1.17 (fired in 2 of 20 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         0/0/1  -> 0.33
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposed Design                              0/0/0  -> 0.00
  [11] Examples                                     2/2/2  -> 2.00
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      0/0/0  -> 0.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Because in this example `file_descriptor` has been reimagined as a regular, synchronous object with a regular, synchronous destructor. Therefore the synchronous close syscall must be used for clean up rather than the asynchronous `IORING_OP_CLOSE`.
candidate 2 (found by 1 of 60 passes): C++26 actually contains such a justification: Async scopes [4].

## implementation - grade 1.00  [binary: max] (fired in 2 of 20 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         0/0/0  -> 0.00
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposed Design                              0/1/0  -> 0.33
  [11] Examples                                     0/0/0  -> 0.00
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    1/1/1  -> 1.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      0/0/0  -> 0.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): The author has implemented this design on top of nVidia’s stdexec [18].
candidate 2 (found by 1 of 60 passes): Note that in the author’s experience this has always been the desired use of `lifetime`.

-->
