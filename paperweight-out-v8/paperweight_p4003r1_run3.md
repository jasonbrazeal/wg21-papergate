Verdict: Strong to Excellent (12/14)

The paper offers substantial support for most of the standardization case, with direct implementation experience, clear evidence of ecosystem fragmentation, and a credible argument that only a standard vocabulary can break the impasse. The support is thinnest where the paper needs to show that a library alone cannot solve the problem, since that claim is asserted rather than demonstrated.

- The strongest support comes from the reference implementation and the networking stack built on it, which show the model working across sockets, timers, TLS, DNS, and HTTP.
- The paper also establishes who is affected by citing the 2021 LEWG polls and the weak consensus against the Networking TS async model as a general-purpose basis.
- The most glaring omission is the failure to establish why a library will not do, since the paper asserts that every library invents its own model but does not show why a shared library outside the standard could not serve as the common vocabulary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 11.33   accumulate 11.67   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 0.17  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 12.50 / 11.00 / 11.50   (all 3 samples: 11.67)
headings: h2 7
on threshold: audience
splits: audience[8] 2/0/1  prior_art[2] 1/1/0  prior_art[10] 1/2/2  coordination[6] 0/0/1
        insufficiency[4] 1/0/0  implementation[10] 2/0/2
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
candidate 2 (found by 3 of 36 passes): C++ does not have this tower - and the ecosystem has had twenty years to build it.
candidate 3 (found by 3 of 36 passes): We asked what happens when networking requirements drive the design of a coroutine execution model.
candidate 4 (found by 3 of 36 passes): Each C++ networking library builds on a different async model. The higher layers of the abstraction tower - the layers that application developers need - have not emerged because the foundation is not shared.

## audience - grade 1.50 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/0/1  -> 1.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The 2021 LEWG polls[14][15] found weak consensus against the Networking TS async model as a general-purpose basis (5 SF, 10 WF, 6 N, 14 WA, 18 SA) and weak consensus that networking should be based on sender/receiver (17-11-10-4-6).
candidate 2 (found by 2 of 36 passes): The 2021 LEWG polls[15] found weak consensus against the Networking TS async model as a general-purpose basis (5 SF, 10 WF, 6 N, 14 WA, 18 SA)

## prior_art - grade 2.00 (fired in 8 of 12 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               2/2/2  -> 2.00
  [6] 1. Introduction  (part 3 of 3)               2/2/2  -> 2.00
  [7] 8. Conclusion                                1/1/1  -> 1.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         1/1/1  -> 1.00
  [10] 9. Evidence Framework  (part 3 of 3)         1/2/2  -> 1.67
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): An alternative design would place the environment in the promise type and let `await_suspend` discover it by templating on the promise: ... This has a timing problem.
candidate 2 (found by 3 of 36 passes): [P4007R0](https://wg21.link/p4007r0)[1] Section 6.4 examines why alternative designs require a second template parameter and what the ecosystem’s response has been.
candidate 3 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].
candidate 4 (found by 3 of 36 passes): Unlike the Networking TS executor requirements, this concept operates on `continuation&` rather than arbitrary function objects.

## vehicle - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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
candidate 1 (found by 3 of 36 passes): Standards should follow implementations, not the reverse.
candidate 2 (found by 3 of 36 passes): The ecosystem cannot converge on a common vocabulary without standardization, because the entire point of a vocabulary is that everyone can depend on it being there.
candidate 3 (found by 2 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 4 (found by 2 of 36 passes): The reason is that there is no standard foundation to build them on. Every async I/O library invents its own model. An HTTP library built on one model cannot compose with a database library built on another.

## coordination - grade 2.00 (fired in 3 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               2/2/2  -> 2.00
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/1  -> 0.33
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         2/2/2  -> 2.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Every async I/O library invents its own model. An HTTP library built on one model cannot compose with a database library built on another.
candidate 2 (found by 2 of 36 passes): The ecosystem cannot converge on a common vocabulary without standardization, because the entire point of a vocabulary is that everyone can depend on it being there.
candidate 3 (found by 1 of 36 passes): This enables separate compilation and ABI stability.
candidate 4 (found by 1 of 36 passes): Each C++ networking library builds on a different async model. The higher layers of the abstraction tower - the layers that application developers need - have not emerged because the foundation is not shared.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction  (part 1 of 3)               1/0/0  -> 0.33
  [5] 1. Introduction  (part 2 of 3)               0/0/0  -> 0.00
  [6] 1. Introduction  (part 3 of 3)               0/0/0  -> 0.00
  [7] 8. Conclusion                                0/0/0  -> 0.00
  [8] 9. Evidence Framework  (part 1 of 3)         0/0/0  -> 0.00
  [9] 9. Evidence Framework  (part 2 of 3)         0/0/0  -> 0.00
  [10] 9. Evidence Framework  (part 3 of 3)         0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Every async I/O library invents its own model. An HTTP library built on one model cannot compose with a database library built on another.

## implementation - grade 2.00  [binary: max] (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
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
  [10] 9. Evidence Framework  (part 3 of 3)         2/0/2  -> 1.33
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We used C++20 coroutines directly for I/O - timers, sockets, DNS, TLS, HTTP - and observed what the language already provides.
candidate 2 (found by 3 of 36 passes): [Capy](https://github.com/cppalliance/capy)[5] implements the IoAwaitable protocol. [Corosio](https://github.com/cppalliance/corosio)[6], built on Capy, provides sockets, timers, TLS, and DNS resolution on multiple platforms.
candidate 3 (found by 3 of 36 passes): [Http](https://github.com/cppalliance/http)[8], an HTTP library built on Capy, works entirely in terms of type-erased streams.
candidate 4 (found by 3 of 36 passes): A reference implementation is available as [Capy](https://github.com/cppalliance/capy)[5], with networking provided by [Corosio](https://github.com/cppalliance/corosio)[6].

-->
