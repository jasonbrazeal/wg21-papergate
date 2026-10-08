Verdict: Strong (8/14)

The paper offers substantial evidence that the problems it identifies are real, widely encountered, and already addressed in production practice, but it does not close the case for why standardization is the necessary remedy or why a library solution cannot suffice. The strongest material concerns implementation experience and the breadth of affected users, while the argument thins considerably around the institutional and interoperability justifications for a standard.

- The paper’s strongest support comes from documented production use and a working implementation compiled on multiple toolchains, which grounds the problem in real practice rather than speculation.
- The claim that the gaps affect a broad population is well supported by survey evidence showing five of six major coroutine libraries rely on symmetric transfer and by reports of production deployment at Citadel Securities.
- The paper establishes that the sender model and coroutine model collide in specific, structural ways, and that alternatives have been considered in committee.
- The most glaring omission is the absence of any established argument for why the standard must act, as opposed to a library or ecosystem-level solution, and the interoperability rationale remains asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 5 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.83   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 1.50  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.00 / 9.00 / 8.00   (all 3 samples: 8.33)
headings: h2 7
on threshold: prior_art
splits: motivation[6] 1/0/1  audience[5] 2/2/1  prior_art[4] 2/0/0  coordination[2] 0/1/0
        coordination[3] 0/0/2  coordination[7] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 2)              2/2/2  -> 2.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    1/0/1  -> 0.67
  [7] Appendix A - The Three-Channel Model         2/2/2  -> 2.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The structural gaps documented in Sections 3-5 exist at the boundary where `std::execution` meets coroutines.
candidate 2 (found by 3 of 27 passes): The four gaps documented in Sections 3-6 are the cost of treating the sender model as the universal model of asynchronous computation.
candidate 3 (found by 3 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.
candidate 4 (found by 2 of 27 passes): Senders get the allocator they do not need. Coroutines need the frame allocator they do not get.

## audience - grade 1.83 (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              2/2/2  -> 2.00
  [5] 10. Conclusion                               2/2/1  -> 1.67
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): [P2583R0](https://wg21.link/p2583r0)[63] (“Symmetric Transfer and Sender Composition”) surveys six major production coroutine libraries. Five of six use symmetric transfer.
candidate 2 (found by 2 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”
candidate 3 (found by 1 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              2/0/0  -> 0.67
  [5] 10. Conclusion                               1/1/1  -> 1.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0][63].
candidate 2 (found by 3 of 27 passes): The SG4 poll (Kona 2023, SF:5/F:5/N:1/A:0/SA:1) presented two alternatives.
candidate 3 (found by 1 of 27 passes): [P2583R0](https://wg21.link/p2583r0)[63] documents the full mechanism, surveys production practice, and argues the gap is architectural: sender algorithms are structs with void-returning completions.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History  (part 1 of 2)              0/0/2  -> 0.67
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         2/2/0  -> 1.33
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.
candidate 2 (found by 1 of 27 passes): Mandating that standard networking be built on the sender model would force coroutine I/O users to pay these costs.
candidate 3 (found by 1 of 27 passes): The structural gaps documented in Sections 3-5 exist at the boundary where `std::execution` meets coroutines.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

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
candidate 2 (found by 2 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”[36]
candidate 3 (found by 1 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”

-->
