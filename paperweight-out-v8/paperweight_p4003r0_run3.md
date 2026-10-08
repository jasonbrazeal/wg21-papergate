Verdict: Adequate to Strong (8/14)

The paper offers solid grounding in direct implementation experience and a clear account of the design space, but its case for standardization leans heavily on assertion rather than demonstrated necessity. The thinnest support appears where the paper claims broad impact, interoperability benefits, and the impossibility of a library-only solution without showing evidence that these conditions actually hold.

- The strongest support comes from the reference implementation and working networking stack, which demonstrate that the proposed protocol has been exercised in real code.
- The paper also establishes that C++20 coroutines have properties making them uniquely suited to asynchronous I/O, and it situates the design against examined alternatives.
- The claim that both libraries are in active use is asserted but not substantiated with evidence of adoption or user base.
- The most glaring omission is the lack of demonstrated need for standardization itself, since the paper does not show why the working library implementation cannot remain a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 7 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.67   accumulate 8.00   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.67  coordination 0.67  insufficiency 0.17  implementation 2.00
sample agreement: 72 of 84 section-criterion pairs unanimous (86%)
single-sample totals would have been: 7.00 / 8.50 / 8.00   (all 3 samples: 7.83)
headings: h2 8
on threshold: none
splits: motivation[4] 0/0/2  motivation[6] 1/0/1  audience[4] 0/0/2  prior_art[8] 1/0/0
        prior_art[10] 2/2/1  vehicle[2] 0/1/1  vehicle[4] 0/0/1  vehicle[7] 0/1/1
        coordination[4] 1/2/0  coordination[5] 1/0/0  insufficiency[5] 0/1/0
        implementation[12] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/2  -> 0.67
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               1/0/1  -> 0.67
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): This approach works, but it violates encapsulation. The coroutine’s parameter list - which should describe the algorithm’s interface - is polluted with frame allocation machinery unrelated to its purpose.
candidate 3 (found by 3 of 36 passes): We asked what happens when networking requirements drive the design of a coroutine execution model.
candidate 4 (found by 3 of 36 passes): When code calls a blocking read on a socket, the thread waits - doing nothing - while the network delivers data.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/2  -> 0.67
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Both libraries are in active use.

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
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/1  -> 1.67
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): C++20 coroutines have five properties that, taken together, make them uniquely suited to asynchronous I/O
candidate 2 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 3 (found by 3 of 36 passes): Derived promise types that need additional `await_transform` overloads should override `transform_awaitable` rather than `await_transform` itself.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

## vehicle - grade 0.67 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/1  -> 0.33
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/1/1  -> 0.67
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Standards should follow implementations, not the reverse.
candidate 2 (found by 1 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 3 (found by 1 of 36 passes): C++20 coroutines have five properties that, taken together, make them uniquely suited to asynchronous I/O
candidate 4 (found by 1 of 36 passes): The protocol that emerged is small: two concepts, a type-erased executor, and a thread-local write-through cache that keeps frame allocator policy out of coroutine signatures - yet it is the foundation from which a complete networking stack can be built.

## coordination - grade 0.67 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               1/2/0  -> 1.00
  [5] 1. Introduction  (part 2 of 3)               1/0/0  -> 0.33
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): This is also an interoperability feature. In a world with multiple coexisting async models, a coroutine that accidentally `co_await` s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 2 (found by 1 of 36 passes): Applications can set a policy once via `set_frame_allocator` , and all coroutines launched with the default will use it - including those in foreign libraries, without propagating allocator template parameters or recompiling.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               0/1/0  -> 0.33
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
