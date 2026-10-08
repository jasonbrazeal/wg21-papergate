Verdict: Weak (3/14)

The paper offers only a narrow foundation for its own standardization: it connects its ideas to prior work and to a recognized framing of safety and liveness, but it does not establish who would be affected, why the standard is the right venue, how the feature would interoperate, why a library cannot suffice, or whether anyone has implemented it. The thinnest support is around the core standardization questions, where the paper is largely silent.

- The strongest support is the acknowledgment of prior art, including a broader discussion in Teodorescu26 and Lamport’s safety/liveness distinction.
- The motivation is asserted in general terms about improving safety, liveness, and correctness, but it is not tied to concrete C++ users or use cases.
- The paper does not explain why standardization, rather than a library or existing practice, is necessary.
- The most glaring omission is the absence of any implementation experience or evidence of coordination and interoperability with existing C++ features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.00   accumulate 3.67   max 3.33

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 3.00 / 2.50   (all 3 samples: 2.67)
headings: h2 6
on threshold: prior_art
splits: motivation[2] 1/2/1
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        1/1/1  -> 1.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  1/1/1  -> 1.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Correctness is usually harder to discuss than the individual properties from which it is built.
candidate 2 (found by 3 of 21 passes): This makes our reasoning harder.
candidate 3 (found by 3 of 21 passes): These are small things that we can do to improve the safety, liveness and correctness of our C++ programs.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        0/0/0  -> 0.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 4 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 A pivot on liveness                        1/1/1  -> 1.00
  [5] 3 Correctness composability                  1/1/1  -> 1.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Some of these ideas are also discussed in a broader form in [[Teodorescu26]](https://lucteo.ro/2026/05/10/safety-refined-liveness/). This paper repeats and adapts them for the context of C++ standardization.
candidate 2 (found by 3 of 21 passes): For more details, please see [[Teodorescu26]](https://lucteo.ro/2026/05/10/safety-refined-liveness/).
candidate 3 (found by 3 of 21 passes): For example, we know that low-level synchronization with semaphores is prone to progress issues.
candidate 4 (found by 2 of 21 passes): Following Lamport’s division of correctness into safety and liveness [[Lamport77]](https://lamport.azurewebsites.net/pubs/proving.pdf)

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        0/0/0  -> 0.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        0/0/0  -> 0.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        0/0/0  -> 0.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        0/0/0  -> 0.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
