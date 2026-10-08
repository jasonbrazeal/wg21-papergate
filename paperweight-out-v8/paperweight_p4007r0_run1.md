Verdict: Strong (8/14)

The paper offers a solid foundation for why the problem matters and what alternatives exist, but it leaves several key justifications asserted rather than demonstrated. The thinnest support is around who is concretely affected, why this belongs in the standard rather than a library, and how the proposal would coordinate with existing practice.

- The strongest support is the documented structural gap between `std::execution` and coroutines, backed by prior art and a working implementation.
- The paper also establishes that coroutine-only and sender-only designs each fail to cover the full space, which grounds the need for something beyond either.
- The weakest area is the claim that a library solution cannot suffice, which is asserted through design observations but not shown against realistic alternatives.
- Most glaringly, the paper does not establish who is affected beyond a single production report and a survey of coroutine libraries, leaving the breadth of the problem largely unproven.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 7 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.33   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 1.67  vehicle 0.67  coordination 0.17  insufficiency 0.50  implementation 2.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 8.00 / 7.50   (all 3 samples: 8.00)
headings: h2 7
on threshold: prior_art
splits: audience[4] 2/0/0  audience[5] 2/1/1  prior_art[3] 2/2/0  vehicle[5] 1/0/0
        coordination[2] 0/1/0  insufficiency[2] 0/1/0  insufficiency[3] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 9 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 2)              2/2/2  -> 2.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         2/2/2  -> 2.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The structural gaps documented in Sections 3-5 exist at the boundary where `std::execution` meets coroutines.
candidate 2 (found by 3 of 27 passes): Senders get the allocator they do not need. Coroutines need the frame allocator they do not get.
candidate 3 (found by 3 of 27 passes): The four gaps documented in Sections 3-6 are the cost of treating the sender model as the universal model of asynchronous computation.
candidate 4 (found by 3 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.

## audience - grade 1.00 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              2/0/0  -> 0.67
  [5] 10. Conclusion                               2/1/1  -> 1.33
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”
candidate 2 (found by 1 of 27 passes): [P2583R0](https://wg21.link/p2583r0)[63] (“Symmetric Transfer and Sender Composition”) surveys six major production coroutine libraries. Five of six use symmetric transfer.
candidate 3 (found by 1 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production

## prior_art - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              2/2/0  -> 1.33
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               1/1/1  -> 1.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The SG4 poll (Kona 2023, SF:5/F:5/N:1/A:0/SA:1) presented two alternatives.
candidate 2 (found by 2 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0][63].
candidate 3 (found by 2 of 27 passes): The authors developed [P4003R0](https://wg21.link/p4003r0)[25] (“Coroutines for I/O”). A coroutine-only design cannot express compile-time work graphs, does not support heterogeneous dispatch, and assumes a cooperative runtime.
candidate 4 (found by 1 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0].

## vehicle - grade 0.67 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               1/0/0  -> 0.33
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Mandating that standard networking be built on the sender model would force coroutine I/O users to pay these costs.
candidate 2 (found by 1 of 27 passes): `std::execution` has earned its place.

## coordination - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Mandating that standard networking be built on the sender model would force coroutine I/O users to pay these costs.

## insufficiency - grade 0.50 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History  (part 1 of 2)              0/0/2  -> 0.67
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Each gap is the cost of a property the sender model requires for compile-time analysis
candidate 2 (found by 1 of 27 passes): The frame allocator is set once at the launch site and reaches every operation automatically. However… Nothing here allocates. Used as intended, the operation state is a single concrete type with no heap allocation.

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): [P4003R0](https://wg21.link/p4003r0)[25] (“Coroutines for I/O”) is a research report drawn from a working implementation compiled on three toolchains, with benchmarks and unit tests.
candidate 2 (found by 3 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”

-->
