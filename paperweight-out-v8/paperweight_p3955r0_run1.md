Verdict: Adequate to Strong (7/14)

The paper offers a solid conceptual foundation for why asynchronous objects and destructors matter, and it engages seriously with prior work, but it does not yet make a persuasive case that this needs to be in the standard rather than a library. The strongest support is in the motivation and the survey of alternatives; the thinnest is in the absence of concrete evidence about users, implementation experience, or interoperability with existing facilities.

- The paper clearly establishes the core problem: RAII and scoped lifetimes are synchronous, and asynchronous code lacks an equivalent mechanism.
- It credibly identifies and critiques prior art, including Kirk Shoop’s work and `let_async_scope`, showing where existing approaches fall short.
- The claim that a library solution is insufficient rests mainly on general distaste for two-phase initialization, without demonstrating that a library cannot adequately address the need.
- The paper offers no published implementation or user experience, leaving its practical viability and demand largely unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.00   accumulate 7.17   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.83  coordination 0.33  insufficiency 0.83  implementation 1.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.50 / 7.00 / 8.00   (all 3 samples: 7.17)
headings: h2 13
on threshold: none
splits: motivation[6] 0/0/1  motivation[11] 2/1/2  audience[7] 0/0/1  vehicle[3] 1/0/1
        coordination[7] 0/0/2  insufficiency[7] 1/1/0  insufficiency[11] 0/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/1  -> 0.33
  [7] Why Are Asynchronous Objects Needed?         0/0/0  -> 0.00
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 2/2/2  -> 2.00
  [10] Proposal                                     2/2/2  -> 2.00
  [11] Examples                                     2/1/2  -> 1.67
  [12] Implementation Experience                    0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper lays out an approach to achieving the same effect as regular, synchronous scopes in the asynchronous domain (i.e. `std::execution` [1]), including asynchronous construction and destruction of objects.
candidate 2 (found by 3 of 42 passes): Unfortunately C++ is a fundamentally synchronous language. Entering and leaving a scope, and therefore the power of RAII, is only available synchronously.
candidate 3 (found by 3 of 42 passes): The most serious issue with the previous design is that it requires that `async_construct` and `async_destruct` be invocable on const lvalue async objects.
candidate 4 (found by 3 of 42 passes): It does not require that the object(s) be movable (ibid.)

## audience - grade 0.17 (fired in 1 of 14 sections, strong in 0)
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
  [10] Proposal                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Implementation Experience                    0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): Two phase init could clearly be used here, but that is widely regarded as an antipattern in general (the Google style guide, for example, has historically been much-maligned for featuring/requiring it).

## prior_art - grade 2.00 (fired in 9 of 14 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    1/1/1  -> 1.00
  [6] What Is an “Asynchronous Object?”        1/1/1  -> 1.00
  [7] Why Are Asynchronous Objects Needed?         2/2/2  -> 2.00
  [8] Prior Design                                 2/2/2  -> 2.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposal                                     2/2/2  -> 2.00
  [11] Examples                                     2/2/2  -> 2.00
  [12] Implementation Experience                    1/1/1  -> 1.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): An asynchronous simulacrum of itself, as another ([2] at §3):
candidate 2 (found by 3 of 42 passes): Kirk Shoop has previously explored this space [2].
candidate 3 (found by 3 of 42 passes): Similarly ([2] at §1.1): *“An* `async-object` *is an object [...] that has* `async-function`*s to construct and destruct the* *object.”*
candidate 4 (found by 3 of 42 passes): A narrow solution to the specific problem above has been proposed: `execution::let_async_scope` [5] (this will be returned to later in this paper), but we can do better.

## vehicle - grade 0.83 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/0/1  -> 0.67
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         1/1/1  -> 1.00
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposal                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Implementation Experience                    0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): POSIX system calls and io_uring are beyond the purview of the standard, however, and for justification of asynchronous destructors we need not look that far.
candidate 2 (found by 2 of 42 passes): To evolve its asynchronous ecosystem and achieve parity with its synchronous ecosystem C++ needs not only asynchronous functions, but also asynchronous objects [2].

## coordination - grade 0.33 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         0/0/2  -> 0.67
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposal                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Implementation Experience                    0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): C++26 actually contains such a justification: Async scopes [4]. Consider the functionality of the synchronous destructor of `execution::simple_counting_scope` (§33.14.2.2.2 [exec.simple.counting.ctor])

## insufficiency - grade 0.83 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Prior Art                                    0/0/0  -> 0.00
  [6] What Is an “Asynchronous Object?”        0/0/0  -> 0.00
  [7] Why Are Asynchronous Objects Needed?         1/1/0  -> 0.67
  [8] Prior Design                                 0/0/0  -> 0.00
  [9] Issues With the Prior Design                 0/0/0  -> 0.00
  [10] Proposal                                     0/0/0  -> 0.00
  [11] Examples                                     0/2/1  -> 1.00
  [12] Implementation Experience                    0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Two phase init could clearly be used here, but that is widely regarded as an antipattern in general
candidate 2 (found by 1 of 42 passes): Because in this example `file_descriptor` has been reimagined as a regular, synchronous object with a regular, synchronous destructor. Therefore the synchronous close syscall must be used for clean up rather than the asynchronous `IORING_OP_CLOSE`.
candidate 3 (found by 1 of 42 passes): In the status quo this would be difficult to workaround but `execution::sync_object` provides a solution:

## implementation - grade 1.00  [binary: max] (fired in 1 of 14 sections, strong in 0)
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
  [10] Proposal                                     0/0/0  -> 0.00
  [11] Examples                                     0/0/0  -> 0.00
  [12] Implementation Experience                    1/1/1  -> 1.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The author has implemented this design on top of nVidia’s stdexec [13]. The implementation is not yet published.

-->
