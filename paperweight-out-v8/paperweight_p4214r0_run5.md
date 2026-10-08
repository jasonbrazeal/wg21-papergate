Verdict: Weak (3/14)

The paper offers a narrow foundation for its standardization case: it connects its argument to prior work and to Lamport’s safety/liveness framing, but it does not establish who is affected, why the standard is the right venue, how the feature would interoperate, why a library cannot suffice, or that there is implementation experience. The strongest support is conceptual rather than practical, and the thinnest areas are the absence of a demonstrated need for standardization itself and any evidence from use.

- The paper’s clearest support comes from its grounding in Lamport’s safety/liveness distinction and its citation of related prior work.
- The paper claims that progress guarantees matter for correctness, but it does not show concretely who is affected or how widespread the problem is.
- The paper does not establish why this belongs in the C++ standard rather than in a library or guidance document.
- The most glaring omission is the lack of any implementation experience or interoperability discussion to show the proposal is ready for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 2.00   accumulate 4.00   max 3.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 2.50 / 2.50 / 3.00   (all 3 samples: 2.50)
headings: h2 6
on threshold: prior_art
splits: motivation[3] 0/0/2  motivation[5] 1/0/0
## END SUMMARY

## motivation - grade 1.00 (fired in 5 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               0/0/2  -> 0.67
  [4] 2 A pivot on liveness                        1/1/1  -> 1.00
  [5] 3 Correctness composability                  1/0/0  -> 0.33
  [6] 4 Takeaways                                  1/1/1  -> 1.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Correctness is usually harder to discuss than the individual properties from which it is built.
candidate 2 (found by 3 of 21 passes): These are small things that we can do to improve the safety, liveness and correctness of our C++ programs.
candidate 3 (found by 2 of 21 passes): This makes our reasoning harder.
candidate 4 (found by 1 of 21 passes): A program that never produces a wrong answer may still fail to produce any answer.

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
