Verdict: Weak to Adequate (3/14)

The paper offers some conceptual grounding for its position, but it does not yet make a persuasive case that this idea is ready for standardization. The strongest support is the connection to prior work and Lamport’s safety/liveness framework, while the case for who is affected, why the standard is the right venue, and what implementation experience exists is essentially absent.

- The paper’s engagement with prior art, particularly Lamport’s safety/liveness distinction and the cited broader discussion in Teodorescu26, gives it a recognizable intellectual foundation.
- The argument that C++ standardization should treat progress guarantees as part of correctness contracts is asserted, but the paper does not establish why this belongs in the standard rather than in guidance or libraries.
- The paper does not identify a concrete audience or set of users whose work would be improved by standardization.
- There is no implementation experience, interoperability analysis, or demonstration that a library solution would be insufficient, leaving the practical case for standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.33   accumulate 4.17   max 3.67

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.50  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.50 / 2.50 / 2.50   (all 3 samples: 2.83)
headings: h2 6
on threshold: prior_art
splits: motivation[2] 2/1/1  vehicle[2] 1/0/0
## END SUMMARY

## motivation - grade 1.17 (fired in 4 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/1  -> 1.33
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        1/1/1  -> 1.00
  [5] 3 Correctness composability                  1/1/1  -> 1.00
  [6] 4 Takeaways                                  1/1/1  -> 1.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Correctness is usually harder to discuss than the individual properties from which it is built.
candidate 2 (found by 3 of 21 passes): We usually think of liveness as completely separate from safety. This makes our reasoning harder.
candidate 3 (found by 3 of 21 passes): In practice, we rarely have complete proofs that a component is partially correct.
candidate 4 (found by 3 of 21 passes): These are small things that we can do to improve the safety, liveness and correctness of our C++ programs.

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
candidate 1 (found by 3 of 21 passes): Following Lamport’s division of correctness into safety and liveness [[Lamport77]](https://lamport.azurewebsites.net/pubs/proving.pdf), this paper argues that C++ standardization should treat progress guarantees as part of the correctness contract of concurrency facilities.
candidate 2 (found by 3 of 21 passes): Some of these ideas are also discussed in a broader form in [[Teodorescu26]](https://lucteo.ro/2026/05/10/safety-refined-liveness/). This paper repeats and adapts them for the context of C++ standardization.
candidate 3 (found by 3 of 21 passes): For more details, please see [[Teodorescu26]](https://lucteo.ro/2026/05/10/safety-refined-liveness/).
candidate 4 (found by 3 of 21 passes): For example, we know that low-level synchronization with semaphores is prone to progress issues.

## vehicle - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 A pivot on liveness                        0/0/0  -> 0.00
  [5] 3 Correctness composability                  0/0/0  -> 0.00
  [6] 4 Takeaways                                  0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): This paper argues that C++ standardization should treat progress guarantees as part of the correctness contract of concurrency facilities.

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
