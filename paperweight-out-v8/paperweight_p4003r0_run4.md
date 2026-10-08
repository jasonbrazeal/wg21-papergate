Verdict: Strong (8/14)

The paper offers solid grounding in implementation experience and a clear account of the design space, but its case for standardization rests heavily on assertions about real-world usage, interoperability, and the necessity of language-level support that are not yet demonstrated. The thinnest support appears where the paper argues that only a standard facility can achieve its goals and that the affected ecosystem is broad enough to justify standardization.

- The strongest support comes from the concrete implementation experience with Capy, Corosio, and Boost.Http, which shows the protocol working across real networking and HTTP use cases.
- The paper also establishes meaningful prior art and alternatives by explaining why C++20 coroutines are uniquely suited to asynchronous I/O and by pointing to a reference implementation.
- The most glaring omission is the lack of evidence that the claimed active use and cross-library coordination benefits actually materialize in practice, since those claims are asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 7 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 9.00   accumulate 8.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.67  coordination 0.83  insufficiency 0.17  implementation 2.00
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 7.50 / 8.50   (all 3 samples: 8.00)
headings: h2 8
on threshold: none
splits: motivation[4] 2/2/0  audience[4] 1/0/1  prior_art[8] 1/0/0  vehicle[5] 0/0/1
        coordination[4] 0/2/0  coordination[5] 2/0/1  insufficiency[5] 0/0/1
        implementation[12] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/0  -> 1.33
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               1/1/1  -> 1.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The frame allocator becomes viral, infecting interfaces throughout the codebase.
candidate 2 (found by 3 of 36 passes): This mixin encapsulates the boilerplate that every IoRunnable-compatible promise type would otherwise duplicate.
candidate 3 (found by 3 of 36 passes): We asked what happens when networking requirements drive the design of a coroutine execution model.
candidate 4 (found by 2 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               1/0/1  -> 0.67
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Both libraries are in active use.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               1/1/1  -> 1.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     1/0/0  -> 0.33
  [9] 10. Thoughts on Wording  (part 1 of 2)       1/1/1  -> 1.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): C++20 coroutines have five properties that, taken together, make them uniquely suited to asynchronous I/O
candidate 2 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 3 (found by 3 of 36 passes): Derived promise types that need additional `await_transform` overloads should override `transform_awaitable` rather than `await_transform` itself.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               0/0/1  -> 0.33
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Standards should follow implementations, not the reverse.
candidate 2 (found by 1 of 36 passes): The standard library already accepted this tradeoff: `std::pmr::get_default_resource()` is a process-wide thread-local allocator channel, adopted in C++17.
candidate 3 (found by 1 of 36 passes): The IoAwaitable protocol is offered in that spirit: not as a theoretical construct, but as a distillation of patterns proven in practice.

## coordination - grade 0.83 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/2/0  -> 0.67
  [5] 1. Introduction  (part 2 of 3)               2/0/1  -> 1.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Applications can set a policy once via `set_frame_allocator` , and all coroutines launched with the default will use it - including those in foreign libraries, without propagating allocator template parameters or recompiling.
candidate 2 (found by 1 of 36 passes): This is also an interoperability feature. In a world with multiple coexisting async models, a coroutine that accidentally `co_await` s across model boundaries should fail at compile time, not silently misbehave at runtime.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               0/0/1  -> 0.33
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Thread-local propagation is the only approach that maintains clean interfaces while respecting the timing constraint.

## implementation - grade 2.00  [binary: max] (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                2/2/2  -> 2.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   2/0/2  -> 1.33
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): [Capy](https://github.com/cppalliance/capy)[5] implements the IoAwaitable protocol. [Corosio](https://github.com/cppalliance/corosio)[6], built on Capy, provides sockets, timers, TLS, and DNS resolution on multiple platforms. Both libraries are in active use.
candidate 3 (found by 3 of 36 passes): [Boost.Http](https://github.com/cppalliance/http)[8], an HTTP library built on Capy, works entirely in terms of type-erased streams.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

-->
