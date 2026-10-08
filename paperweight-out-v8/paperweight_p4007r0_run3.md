Verdict: Adequate to Strong (7/14)

The paper offers meaningful support in some areas, particularly in articulating the structural problems and in showing implementation experience, but it leaves central parts of the standardization case unproven. The thinnest support is around why the standard itself must change and how the proposal would coordinate or interoperate with existing facilities.

- The paper most convincingly establishes that the gaps between `std::execution` and coroutines are real structural costs, and that a working implementation exists across multiple toolchains.
- It also establishes that the relevant prior art and alternatives were considered, including a recorded SG4 poll presenting two options.
- The paper claims, but does not establish, that a library-only solution is insufficient, resting that claim on the sender model’s compile-time analysis requirements rather than demonstrating it.
- The most glaring omission is the absence of any established case for why the standard is the necessary venue, with no credited support for standardization itself or for coordination and interoperability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.00   accumulate 7.17   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.00 / 7.50 / 7.00   (all 3 samples: 7.17)
headings: h2 7
on threshold: audience, prior_art
splits: motivation[6] 1/0/0  audience[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              2/2/2  -> 2.00
  [4] Revision History  (part 2 of 2)              2/2/2  -> 2.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    1/0/0  -> 0.33
  [7] Appendix A - The Three-Channel Model         2/2/2  -> 2.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The structural gaps documented in Sections 3-5 exist at the boundary where `std::execution` meets coroutines.
candidate 2 (found by 3 of 27 passes): The four gaps documented in Sections 3-6 are the cost of treating the sender model as the universal model of asynchronous computation.
candidate 3 (found by 3 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.
candidate 4 (found by 2 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0][63].

## audience - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               2/2/2  -> 2.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/1/0  -> 0.33
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”[36]
candidate 2 (found by 1 of 27 passes): Herb Sutter reported that Citadel Securities uses it in production: “[We already use](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) C++26’s `std::execution` [in production for an entire asset class, and as the foundation of our new messaging](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [infrastructure.](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work)”
candidate 3 (found by 1 of 27 passes): The partial success problem was raised independently, across multiple groups, by participants with different domain backgrounds, over a span of five years.

## prior_art - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               1/1/1  -> 1.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The SG4 poll (Kona 2023, SF:5/F:5/N:1/A:0/SA:1) presented two alternatives.
candidate 2 (found by 2 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0][63].
candidate 3 (found by 1 of 27 passes): This paper identifies four structural gaps where the sender model meets coroutines: three at the boundary - error reporting, error returns, and frame allocator propagation - and one inside the composition mechanism - the symmetric transfer gap documented in [P2583R0].

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

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History  (part 1 of 2)              0/0/0  -> 0.00
  [4] Revision History  (part 2 of 2)              0/0/0  -> 0.00
  [5] 10. Conclusion                               0/0/0  -> 0.00
  [6] 11. Suggested Straw Polls                    0/0/0  -> 0.00
  [7] Appendix A - The Three-Channel Model         0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Each gap is the cost of a property the sender model requires for compile-time analysis
candidate 2 (found by 1 of 27 passes): Each gap is the cost of a property the sender model requires for compile-time analysis ([P2300R10](https://wg21.link/p2300r10)[1], [P4014R0](https://wg21.link/p4014r0)[26]).

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
