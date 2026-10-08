Verdict: Strong (10/14)

The paper offers meaningful support in the areas of motivation, prior art, and implementation experience, but its case is much thinner when it comes to showing who is affected, why the standard is the right venue, how the feature interoperates, and why a library solution is insufficient. The strongest evidence is practical and grounded in working code, while the weakest parts rely on assertions that are not backed by detail or demonstration.

- The paper clearly establishes why the problem matters by describing concrete I/O requirements and the encapsulation failure caused by leaking frame-allocation machinery into coroutine interfaces.
- It also establishes implementation experience through Capy, Corosio, and Boost.Http, showing the protocol and supporting libraries in real use.
- The most glaring omission is the lack of established argument for why a library cannot solve the problem, since the paper identifies `promise_type::operator new` as the single language hook but does not establish that this hook is insufficient outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.67/14)

Provisionally addressed: 7 of 7. Provisional points: 9.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.67   corroborated 10.00   accumulate 9.67   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.67  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 9.00 / 11.00   (all 3 samples: 9.67)
headings: h2 8
on threshold: audience, insufficiency
splits: motivation[6] 0/1/1  prior_art[2] 1/0/0  prior_art[6] 0/1/1  prior_art[8] 1/0/0
        prior_art[10] 2/1/1  vehicle[2] 0/0/1  coordination[4] 1/0/2  coordination[5] 0/1/2
        implementation[12] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               0/1/1  -> 0.67
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): When code calls a blocking read on a socket, the thread waits - doing nothing - while the network delivers data.
candidate 3 (found by 2 of 36 passes): I/O applications share four requirements: The application decides executor policy. The application sends stop signals. The application decides frame allocation. The execution context owns its I/O objects.
candidate 4 (found by 2 of 36 passes): This approach works, but it violates encapsulation. The coroutine’s parameter list - which should describe the algorithm’s interface - is polluted with frame allocation machinery unrelated to its purpose.

## audience - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Both libraries are in active use.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               0/1/1  -> 0.67
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Suggested Straw Polls                     1/0/0  -> 0.33
  [9] 10. Thoughts on Wording  (part 1 of 2)       1/1/1  -> 1.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       2/1/1  -> 1.33
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 2 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].
candidate 3 (found by 3 of 36 passes): Unlike the Networking TS executor requirements, this concept operates on `coroutine_handle<>` rather than arbitrary function objects.
candidate 4 (found by 3 of 36 passes): The concepts presented here draw heavily from Christopher Kohlhoff’s pioneering work on Boost.Asio, which has served the C++ community for over two decades, and from Gor Nishanov’s C++ coroutines that now enable elegant expression of asynchronous control flow.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
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

## coordination - grade 1.00 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               1/0/2  -> 1.00
  [5] 1. Introduction  (part 2 of 3)               0/1/2  -> 1.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): This is also an interoperability feature. In a world with multiple coexisting async models, a coroutine that accidentally `co_await` s across model boundaries should fail at compile time, not silently misbehave at runtime.
candidate 2 (found by 2 of 36 passes): Applications can set a policy once via `set_frame_allocator` , and all coroutines launched with the default will use it - including those in foreign libraries, without propagating allocator template parameters or recompiling.

## insufficiency - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/0  -> 0.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [9] 10. Thoughts on Wording  (part 1 of 2)       0/0/0  -> 0.00
  [10] 10. Thoughts on Wording  (part 2 of 2)       0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): C++ provides exactly one hook at the right time: `promise_type::operator new` . The compiler passes coroutine arguments directly to this overload, allowing the promise to inspect parameters and select a frame allocator.
candidate 2 (found by 1 of 36 passes): C++ provides exactly one hook at the right time: `promise_type::operator new` .

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
