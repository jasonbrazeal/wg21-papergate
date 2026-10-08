Verdict: Adequate to Strong (9/14)

The paper offers a solid foundation in direct implementation experience and a clear articulation of the problem, but its case for standardization rests heavily on assertions that active use, language-level necessity, and interoperability benefits exist without much supporting evidence. The strongest material concerns what has actually been built and observed, while the thinnest concerns the claims that only the standard can provide the needed hook and that the feature will deliver cross-model safety.

- The paper’s implementation experience is its most convincing support, with concrete libraries and an HTTP stack built on the proposed protocol.
- The discussion of prior art and alternatives is grounded in a reference implementation and a specific analysis of why existing designs fall short.
- The claim that the standard is necessary because C++ provides exactly one hook at the right time is asserted rather than demonstrated against plausible library-only workarounds.
- The most glaring omission is the lack of substantiation for the interoperability and allocator-policy benefits, which are described as important but not shown to require standardization or to work as claimed across foreign libraries.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 7 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 9.67   accumulate 8.83   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.83  coordination 1.00  insufficiency 0.67  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 11.00 / 8.50 / 7.00   (all 3 samples: 8.83)
headings: h2 8
on threshold: none
splits: motivation[4] 0/2/2  motivation[6] 0/1/0  audience[4] 2/0/0  prior_art[2] 1/0/0
        prior_art[10] 1/2/1  vehicle[2] 1/1/0  coordination[4] 2/0/1  coordination[5] 2/1/0
        insufficiency[5] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/2/2  -> 1.33
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               0/1/0  -> 0.33
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): We asked what happens when networking requirements drive the design of a coroutine execution model.
candidate 3 (found by 3 of 36 passes): When code calls a blocking read on a socket, the thread waits - doing nothing - while the network delivers data.
candidate 4 (found by 2 of 36 passes): I/O applications share four requirements: The application decides executor policy. A read operation should not need to know about executor policy.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/0/0  -> 0.67
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Both libraries are in active use.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               1/1/1  -> 1.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       1/1/1  -> 1.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       1/2/1  -> 1.33
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 2 (found by 3 of 36 passes): Derived promise types that need additional `await_transform` overloads should override `transform_awaitable` rather than `await_transform` itself.
candidate 3 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].
candidate 4 (found by 3 of 36 passes): Unlike the Networking TS executor requirements, this concept operates on `coroutine_handle<>` rather than arbitrary function objects.

## vehicle - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
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
candidate 2 (found by 1 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 3 (found by 1 of 36 passes): Their conjunction yields something no single property suggests: the optimal basis for byte-oriented I/O.

## coordination - grade 1.00 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/0/1  -> 1.00
  [5] 1. Introduction  (part 2 of 3)               2/1/0  -> 1.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): This is also an interoperability feature. In a world with multiple coexisting async models, a coroutine that accidentally `co_await` s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 2 (found by 2 of 36 passes): Applications can set a policy once via `set_frame_allocator` , and all coroutines launched with the default will use it - including those in foreign libraries, without propagating allocator template parameters or recompiling.

## insufficiency - grade 0.67 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               2/2/0  -> 1.33
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): C++ provides exactly one hook at the right time: `promise_type::operator new`. The compiler passes coroutine arguments directly to this overload, allowing the promise to inspect parameters and select a frame allocator.
candidate 2 (found by 1 of 36 passes): C++ provides exactly one hook at the right time: `promise_type::operator new` .

## implementation - grade 2.00  [binary: max] (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
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
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): [Capy](https://github.com/cppalliance/capy)[5] implements the IoAwaitable protocol. [Corosio](https://github.com/cppalliance/corosio)[6], built on Capy, provides sockets, timers, TLS, and DNS resolution on multiple platforms. Both libraries are in active use.
candidate 3 (found by 3 of 36 passes): [Boost.Http](https://github.com/cppalliance/http)[8], an HTTP library built on Capy, works entirely in terms of type-erased streams.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

-->
