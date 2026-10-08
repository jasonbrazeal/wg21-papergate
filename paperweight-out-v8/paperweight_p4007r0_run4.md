Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for its central technical observations, with implementation experience and prior-art analysis that make the structural gaps credible, but it does not yet make a persuasive case that standardization is the necessary response. The support is thinnest where the paper needs to show that a library cannot address the problem and that the standard is the right venue.

- The strongest support comes from the working implementation and production use cited, which establish that the paper is grounded in real systems rather than speculation.
- The prior-art and alternatives section is well developed, showing that the gaps were not invented for this paper and that existing approaches leave them open.
- The case for why the standard should act rests mainly on a single conditional claim about mandating the sender model, without establishing that such a mandate is actually proposed or likely.
- The paper offers no argument at all for why a library solution would be insufficient, leaving a central justification for standardization entirely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 6.67   accumulate 8.00   max 8.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 1.67  vehicle 0.17  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.50 / 8.50 / 6.50   (all 3 samples: 7.33)
headings: h2 7
on threshold: audience, prior_art
splits: audience[3] 0/2/0  audience[4] 0/2/0  audience[7] 1/1/0  prior_art[5] 1/2/1
        vehicle[2] 0/1/0  coordination[2] 1/0/0
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
candidate 2 (found by 3 of 27 passes): The four gaps documented in Sections 3-6 are the cost of treating the sender model as the universal model of asynchronous computation.
candidate 3 (found by 3 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.
candidate 4 (found by 2 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0][63].

## audience - grade 1.33 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/2/0  -> 0.67
  [4] Revision History  (part 2 of 2)              0/2/0  -> 0.67
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         1/1/0  -> 0.67
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”[36]
candidate 2 (found by 2 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.
candidate 3 (found by 1 of 27 passes): [P4003R0](https://wg21.link/p4003r0)[25] (“Coroutines for I/O”) benchmarks a 4-deep coroutine call chain (2 million iterations):
candidate 4 (found by 1 of 27 passes): [P2583R0](https://wg21.link/p2583r0)[63] (“Symmetric Transfer and Sender Composition”) surveys six major production coroutine libraries. Five of six use symmetric transfer.

## prior_art - grade 1.67 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               1/2/1  -> 1.33
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The SG4 poll (Kona 2023, SF:5/F:5/N:1/A:0/SA:1) presented two alternatives. A coroutine-native approach was not among the choices.
candidate 2 (found by 2 of 27 passes): A coroutine-native I/O research report ([P4003R0](https://wg21.link/p4003r0)[25]) made the gaps visible by showing that partial results, error returns, cancellation, and frame allocator propagation emerge naturally when I/O is designed for coroutines.
candidate 3 (found by 1 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0].

## vehicle - grade 0.17 (fired in 1 of 9 sections, strong in 0)
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

## coordination - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)
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
