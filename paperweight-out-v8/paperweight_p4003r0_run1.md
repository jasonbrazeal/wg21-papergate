Verdict: Strong (8/14)

The paper offers credible grounding in direct implementation experience and a clear account of the problem it wants to solve, but its case for standardization is uneven: the strongest evidence concerns what has been built and observed, while the arguments about real-world adoption, the insufficiency of library-only solutions, and interoperability remain asserted rather than demonstrated.

- The paper’s implementation experience is its strongest support, with concrete libraries and an HTTP stack built on the proposed model.
- The motivation and prior art are well established, tying the design to existing executor practice and documented ecosystem constraints.
- The claims about active use and cross-library interoperability are plausible but not backed by evidence in the paper.
- The most glaring omission is any real argument for why a library cannot suffice, leaving the central standardization question unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 9.00   accumulate 8.00   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.50 / 7.50 / 8.00   (all 3 samples: 8.00)
headings: h2 8
on threshold: audience
splits: motivation[2] 1/2/1  motivation[6] 1/1/0  audience[4] 2/1/2  prior_art[2] 1/0/1
        prior_art[6] 0/1/1  prior_art[8] 0/0/1  coordination[4] 2/1/0  coordination[5] 0/0/1
        implementation[12] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               1/1/0  -> 0.67
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): We asked what happens when networking requirements drive the design of a coroutine execution model.
candidate 3 (found by 2 of 36 passes): The frame allocator becomes viral, infecting interfaces throughout the codebase.
candidate 4 (found by 2 of 36 passes): This mixin encapsulates the boilerplate that every IoRunnable-compatible promise type would otherwise duplicate.

## audience - grade 0.83 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/1/2  -> 1.67
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Both libraries are in active use.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               0/1/1  -> 0.67
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/1  -> 0.33
  [9] 10. Thoughts on Wording  (part 1 of 2)       1/1/1  -> 1.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This terminology honors Christopher Kohlhoff’s executor model in [Boost.Asio][3], which established the foundation for modern C++ asynchronous I/O.
candidate 2 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 3 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].
candidate 4 (found by 3 of 36 passes): Unlike the Networking TS executor requirements, this concept operates on `coroutine_handle<>` rather than arbitrary function objects.

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Standards should follow implementations, not the reverse.

## coordination - grade 0.67 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/1/0  -> 1.00
  [5] 1. Introduction  (part 2 of 3)               0/0/1  -> 0.33
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): This is also an interoperability feature. In a world with multiple coexisting async models, a coroutine that accidentally `co_await` s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 2 (found by 1 of 36 passes): Applications can set a policy once via `set_frame_allocator` , and all coroutines launched with the default will use it - including those in foreign libraries, without propagating allocator template parameters or recompiling.

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

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
  [12] References                                   0/2/0  -> 0.67
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): [Capy](https://github.com/cppalliance/capy)[5] implements the IoAwaitable protocol. [Corosio](https://github.com/cppalliance/corosio)[6], built on Capy, provides sockets, timers, TLS, and DNS resolution on multiple platforms. Both libraries are in active use.
candidate 3 (found by 3 of 36 passes): [Boost.Http](https://github.com/cppalliance/http)[8], an HTTP library built on Capy, works entirely in terms of type-erased streams.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

-->
