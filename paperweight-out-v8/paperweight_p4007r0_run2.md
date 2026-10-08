Verdict: Adequate to Strong (8/14)

The paper offers real support for its standardization case in the areas of prior art and implementation experience, but its argument thins considerably when it comes to showing why the standard is the right venue and why a library solution cannot suffice. The strongest material is concrete and external: production use at Citadel Securities and a working coroutine I/O implementation with benchmarks. The weakest material is the absence of any established case that a library would be inadequate, which leaves a central part of the standardization rationale unaddressed.

- The paper establishes meaningful implementation experience through reported production use and a coroutine-native I/O research implementation compiled on three toolchains with benchmarks and tests.
- The prior art and alternatives section is well supported, including a survey showing five of six major coroutine libraries use symmetric transfer and a research report demonstrating that coroutine-native I/O surfaces the relevant gaps naturally.
- The paper claims but does not establish that standard networking built on the sender model would force coroutine I/O users to bear the documented costs, since that causal claim is asserted rather than demonstrated.
- The most glaring omission is that the paper does not establish why a library will not do, leaving unanswered whether the proposed standardization is actually necessary rather than merely useful.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 8.00   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 1.83  vehicle 0.33  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.50 / 8.50 / 7.00   (all 3 samples: 7.83)
headings: h2 7
on threshold: audience, implementation
splits: audience[3] 0/2/0  prior_art[4] 2/0/0  prior_art[5] 1/2/2  vehicle[2] 1/1/0
        coordination[3] 2/0/0  implementation[3] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 9 sections, strong in 5)  (SHARED PASSAGE)
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

## audience - grade 1.33 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/2/0  -> 0.67
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”[36]
candidate 2 (found by 1 of 27 passes): [P4003R0](https://wg21.link/p4003r0)[25] (“Coroutines for I/O”) benchmarks a 4-deep coroutine call chain (2 million iterations):

## prior_art - grade 1.83 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              2/0/0  -> 0.67
  [5] 10. Conclusion                               1/2/2  -> 1.67
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): A coroutine-native I/O research report ([P4003R0](https://wg21.link/p4003r0)[25]) made the gaps visible by showing that partial results, error returns, cancellation, and frame allocator propagation emerge naturally when I/O is designed for coroutines.
candidate 2 (found by 3 of 27 passes): The SG4 poll (Kona 2023, SF:5/F:5/N:1/A:0/SA:1) presented two alternatives. A coroutine-native approach was not among the choices.
candidate 3 (found by 1 of 27 passes): [P2583R0](https://wg21.link/p2583r0)[63] (“Symmetric Transfer and Sender Composition”) surveys six major production coroutine libraries. Five of six use symmetric transfer.

## vehicle - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Mandating that standard networking be built on the sender model would force coroutine I/O users to pay these costs.

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              2/0/0  -> 0.67
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): The structural gaps documented in Sections 3-5 exist at the boundary where `std::execution` meets coroutines.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/2/2  -> 1.33
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”
candidate 2 (found by 2 of 27 passes): [P4003R0](https://wg21.link/p4003r0)[25] (“Coroutines for I/O”) is a research report drawn from a working implementation compiled on three toolchains, with benchmarks and unit tests.

-->
