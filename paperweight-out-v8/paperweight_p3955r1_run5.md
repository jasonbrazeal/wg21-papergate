Verdict: Adequate to Strong (8/14)

The paper offers a solid foundation for why asynchronous scoping matters and shows meaningful engagement with prior art, but it leaves several essential parts of the standardization case asserted rather than demonstrated. The thinnest support is around who is actually affected, why the standard is the right venue, and whether a library solution would be insufficient.

- The strongest support is the clear explanation of the synchronous/asynchronous gap and the concrete limitations of existing `std::execution` idioms.
- The paper also credibly establishes prior art and alternatives, including the `let_async_scope` proposal and the broader observation that sender/receiver features are effectively language features in library form.
- The case for why a library will not do is largely asserted, resting on references to async scopes and examples that do not fully connect to the proposed design.
- The most glaring omission is implementation experience, where the paper claims an implementation exists but offers no evidence or detail to establish that the design has been tested in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 20. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.33   accumulate 7.67   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.00  coordination 0.67  insufficiency 0.83  implementation 1.00
sample agreement: 132 of 140 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.00 / 8.00 / 7.00   (all 3 samples: 7.67)
headings: h2 18
on threshold: none
splits: motivation[7] 2/2/0  motivation[10] 1/1/2  motivation[11] 2/0/0  audience[7] 0/1/0
        prior_art[14] 1/0/1  coordination[7] 1/2/1  insufficiency[11] 2/0/0
        implementation[10] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 20 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         2/2/0  -> 1.33
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 2/2/2  -> 2.00
  [10] Proposed Design                              1/1/2  -> 1.33
  [11] Examples                                     2/0/0  -> 0.67
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      1/1/1  -> 1.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 60 passes): Unfortunately C++ is a fundamentally synchronous language. Entering and leaving a scope, and therefore the power of RAII, is only available synchronously.
candidate 2 (found by 3 of 60 passes): The most serious issue with the previous design is that it requires that `async_construct` and `async_destruct` be invocable on const lvalue async objects.
candidate 3 (found by 3 of 60 passes): This utility provides a superior alternative to the idiom of `execution::just(...) |` `execution::let_value(...)` ([10] at 40:06) which is commonly used to place one or more objects in an operation state and thereby attach them to an asynchronous scope.
candidate 4 (found by 2 of 60 passes): This paper lays out an approach to achieving the same effect as regular, synchronous scopes in the asynchronous domain (i.e. `std::execution` [1]), including asynchronous construction and destruction of objects.

## audience - grade 0.17 (fired in 1 of 20 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         0/1/0  -> 0.33
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
candidate 1 (found by 1 of 60 passes): Two phase init could clearly be used here, but that is widely regarded as an antipattern in general (the Google style guide, for example, has historically been much-maligned for featuring/requiring it).

## prior_art - grade 2.00 (fired in 12 of 20 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    1/1/1  -> 1.00
  [6] What Is an “Asynchronous Object?”        1/1/1  -> 1.00
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
candidate 2 (found by 3 of 60 passes): An asynchronous simulacrum of itself, as another ([2] at §3): “It is becoming apparent that all the sender/receiver features are language features being implemented in library.”
candidate 3 (found by 3 of 60 passes): Similarly ([2] at §1.1): *“An* `async-object` *is an object [...] that has* `async-function`*s to construct and destruct the* *object.”*
candidate 4 (found by 3 of 60 passes): A narrow solution to the specific problem above has been proposed: `execution::let_async_scope` [5] (this will be returned to later in this paper), but we can do better.

## vehicle - grade 1.00 (fired in 2 of 20 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
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
candidate 1 (found by 3 of 60 passes): To evolve its asynchronous ecosystem and achieve parity with its synchronous ecosystem C++ needs not only asynchronous functions, but also asynchronous objects [2].
candidate 2 (found by 3 of 60 passes): POSIX system calls and io_uring are beyond the purview of the standard, however, and for justification of asynchronous destructors we need not look that far.

## coordination - grade 0.67 (fired in 1 of 20 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
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
candidate 1 (found by 3 of 60 passes): C++26 actually contains such a justification: Async scopes [4].

## insufficiency - grade 0.83 (fired in 2 of 20 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
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
  [11] Examples                                     2/0/0  -> 0.67
  [12] Proposed Wording  (part 1 of 2)              0/0/0  -> 0.00
  [13] Proposed Wording  (part 2 of 2)              0/0/0  -> 0.00
  [14] Implementation Experience                    0/0/0  -> 0.00
  [15] Additional Material                          0/0/0  -> 0.00
  [16] Suggested/Desired Polls                      0/0/0  -> 0.00
  [17] Review History                               0/0/0  -> 0.00
  [18] Revision History                             0/0/0  -> 0.00
  [19] Acknowledgements                             0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 60 passes): The scope is transitioned to the `joined` state by obtaining a sender via the scope’s `join` member function, connecting it, starting the resulting operation state, and allowing that asynchronous operation to run to completion.
candidate 2 (found by 1 of 60 passes): C++26 actually contains such a justification: Async scopes [4].
candidate 3 (found by 1 of 60 passes): Because in this example `file_descriptor` has been reimagined as a regular, synchronous object with a regular, synchronous destructor. Therefore the synchronous close syscall must be used for clean up rather than the asynchronous `IORING_OP_CLOSE`.

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
  [10] Proposed Design                              1/0/1  -> 0.67
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
candidate 2 (found by 2 of 60 passes): Note that in the author’s experience this has always been the desired use of `lifetime`.

-->
