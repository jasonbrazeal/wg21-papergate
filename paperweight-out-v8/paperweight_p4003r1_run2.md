Verdict: Strong to Excellent (12/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates real implementation experience, engages seriously with prior art, and explains clearly why a standard foundation is necessary for ecosystem convergence. The support is thinnest where the paper needs to show who is affected and why a library alone cannot solve the problem—both are asserted rather than demonstrated with evidence.

- The strongest support comes from the implementation experience, with multiple working libraries built on the proposed abstractions and used for real I/O workloads.
- The paper also establishes why the standard is needed by showing that without a shared vocabulary, independently developed async libraries cannot compose.
- The most glaring omission is the failure to establish who is affected beyond citing inconclusive poll results and a general claim about production use.
- The claim that a library will not do rests on a single sentence asserting there is no standard foundation, without showing why a non-standard shared library could not serve the same role.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 11.67   accumulate 11.50   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 0.33  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 11.00 / 11.50 / 12.00   (all 3 samples: 11.50)
headings: h2 7
on threshold: audience
splits: audience[8] 0/0/1  prior_art[2] 0/0/1  prior_art[9] 2/1/1  insufficiency[4] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               1/1/1  -> 1.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): The frame allocator becomes viral, infecting interfaces throughout the codebase.
candidate 3 (found by 3 of 36 passes): The reason TLS is involved at all is `operator new` ’s fixed signature.
candidate 4 (found by 3 of 36 passes): In that time, the ecosystem has not produced a standard HTTP framework, a standard WebSocket library, or a web application framework comparable to what other language ecosystems provide.

## audience - grade 1.17 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         0/0/1  -> 0.33
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The 2021 LEWG polls[14][15] found weak consensus against the Networking TS async model as a general-purpose basis (5 SF, 10 WF, 6 N, 14 WA, 18 SA) and weak consensus that networking should be based on sender/receiver (17-11-10-4-6).
candidate 2 (found by 1 of 36 passes): The most widely deployed C++ async I/O model, with over twenty years of production use.

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               2/2/2  -> 2.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         2/1/1  -> 1.33
  [10] 9. Evidence Framework  (part 3 of 3)         1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This terminology honors Christopher Kohlhoff’s executor model in [Boost.Asio](https://www.boost.org/doc/libs/release/doc/html/boost_asio.html)[3], which established the foundation for modern C++ asynchronous I/O.
candidate 2 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 3 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].
candidate 4 (found by 3 of 36 passes): Unlike the Networking TS executor requirements, this concept operates on `continuation&` rather than arbitrary function objects.

## vehicle - grade 2.00 (fired in 3 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The reason is that there is no standard foundation to build them on. Every async I/O library invents its own model. An HTTP library built on one model cannot compose with a database library built on another.
candidate 2 (found by 3 of 36 passes): Standards should follow implementations, not the reverse.
candidate 3 (found by 3 of 36 passes): The ecosystem cannot converge on a common vocabulary without standardization, because the entire point of a vocabulary is that everyone can depend on it being there.

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
candidate 3 (found by 2 of 36 passes): Each C++ networking library builds on a different async model. The higher layers of the abstraction tower - the layers that application developers need - have not emerged because the foundation is not shared.
candidate 4 (found by 1 of 36 passes): The HTTP library depends on Capy’s type-erased abstractions. It ships as a compiled library with stable ABI.

## insufficiency - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               0/1/1  -> 0.67
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         0/0/0  -> 0.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The reason is that there is no standard foundation to build them on.

## implementation - grade 2.00  [binary: max] (fired in 6 of 12 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               2/2/2  -> 2.00
  [7] 8. Conclusion                                2/2/2  -> 2.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         2/2/2  -> 2.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): [Capy](https://github.com/cppalliance/capy)[5] implements the IoAwaitable protocol. [Corosio](https://github.com/cppalliance/corosio)[6], built on Capy, provides sockets, timers, TLS, and DNS resolution on multiple platforms.
candidate 3 (found by 3 of 36 passes): [Http](https://github.com/cppalliance/http)[8], an HTTP library built on Capy, works entirely in terms of type-erased streams.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

-->
