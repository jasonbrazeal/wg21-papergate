Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates real implementation experience, engages seriously with prior art, and explains clearly why a common standard foundation is needed. The support is thinnest where the paper reaches beyond its own experiments to make claims about the broader ecosystem, particularly regarding who is affected and why a library solution cannot suffice.

- The strongest support comes from the concrete implementation experience, with Capy, Corosio, and the HTTP library all built and exercised against the proposed model.
- The paper also establishes its case well on prior art and alternatives, situating the work against Boost.Asio and sender/receiver rather than ignoring them.
- The reasoning about why standardization is necessary is grounded in the observed fragmentation of async I/O models and the impossibility of composing libraries built on different foundations.
- The most glaring omission is the unestablished claim about who is affected, since the paper asserts wide production use and committee sentiment without sufficient evidence to back those assertions.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 11.33   accumulate 11.50   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 0.17  implementation 2.00
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 11.50 / 11.00 / 12.00   (all 3 samples: 11.50)
headings: h2 7
on threshold: audience
splits: motivation[6] 2/1/2  audience[8] 1/0/1  prior_art[9] 2/2/1  prior_art[10] 1/2/2
        vehicle[2] 0/1/0  vehicle[5] 0/0/1  insufficiency[4] 0/0/1  implementation[5] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               2/1/2  -> 1.67
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): This approach works, but it violates encapsulation. The coroutine’s parameter list - which should describe the algorithm’s interface - is polluted with frame allocation machinery unrelated to its purpose.
candidate 3 (found by 3 of 36 passes): We asked what happens when networking requirements drive the design of a coroutine execution model.
candidate 4 (found by 3 of 36 passes): When code calls a blocking read on a socket, the thread waits - doing nothing - while the network delivers data.

## audience - grade 1.33 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         1/0/1  -> 0.67
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The 2021 LEWG polls[14][15] found weak consensus against the Networking TS async model as a general-purpose basis (5 SF, 10 WF, 6 N, 14 WA, 18 SA) and weak consensus that networking should be based on sender/receiver (17-11-10-4-6).
candidate 2 (found by 1 of 36 passes): Boost.Asio has been available for over twenty years.
candidate 3 (found by 1 of 36 passes): The most widely deployed C++ async I/O model, with over twenty years of production use.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               2/2/2  -> 2.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         2/2/1  -> 1.67
  [10] 9. Evidence Framework  (part 3 of 3)         1/2/2  -> 1.67
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This terminology honors Christopher Kohlhoff’s executor model in [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html)[3], which established the foundation for modern C++ asynchronous I/O.
candidate 2 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 3 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].
candidate 4 (found by 3 of 36 passes): Sender/receiver ([P2300R10](https://wg21.link/p2300r10)[12]). The committee-adopted framework for structured asynchronous execution. Its advantages are real: generality across I/O, GPU, and parallel workloads; a formal algebra of sender composition; strong structured-concurrency guarantees; and significant investment from NVIDIA, Meta, and Bloomberg.

## vehicle - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/1  -> 0.33
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Standards should follow implementations, not the reverse.
candidate 2 (found by 3 of 36 passes): The ecosystem cannot converge on a common vocabulary without standardization, because the entire point of a vocabulary is that everyone can depend on it being there.
candidate 3 (found by 2 of 36 passes): The reason is that there is no standard foundation to build them on. Every async I/O library invents its own model. An HTTP library built on one model cannot compose with a database library built on another.
candidate 4 (found by 1 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.

## coordination - grade 2.00 (fired in 3 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               2/2/2  -> 2.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Every async I/O library invents its own model. An HTTP library built on one model cannot compose with a database library built on another.
candidate 2 (found by 2 of 36 passes): It ships as a compiled library with stable ABI.
candidate 3 (found by 2 of 36 passes): An HTTP library built on cppcoro cannot compose with a database driver built on libcoro. Without a shared protocol, each library is an island.
candidate 4 (found by 1 of 36 passes): The HTTP library depends on Capy’s type-erased abstractions. It ships as a compiled library with stable ABI.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/0/1  -> 0.33
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         0/0/0  -> 0.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The reason is that there is no standard foundation to build them on. Every async I/O library invents its own model.

## implementation - grade 2.00  [binary: max] (fired in 7 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/1/0  -> 0.33
  [6] 1. Introduction  (part 3 of 3)               2/2/2  -> 2.00
  [7] 8. Conclusion                                2/2/2  -> 2.00
  [8] 9. Evidence Framework  (part 1 of 3)         1/1/1  -> 1.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): [Capy](https://github.com/cppalliance/capy)[5] implements the IoAwaitable protocol. [Corosio](https://github.com/cppalliance/corosio)[6], built on Capy, provides sockets, timers, TLS, and DNS resolution on multiple platforms.
candidate 3 (found by 3 of 36 passes): [Http](https://github.com/cppalliance/http)[8], an HTTP library built on Capy, works entirely in terms of type-erased streams.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

-->
