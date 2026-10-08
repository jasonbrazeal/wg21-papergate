Verdict: Adequate (6/14)

The paper gives a clear sense of why a programmer would want a facility like `constant_assert`, but it does not build much of a case beyond that motivation. The support is thinnest around the people affected, interoperability with existing practice, and any real implementation experience, leaving the standardization argument largely asserted rather than demonstrated.

- The strongest part of the paper is its explanation of the practical value: checking optimizer behavior without reading assembly and using the optimizer as a correctness tool.
- The discussion of prior art and library limitations gestures at relevant problems, but it does not establish that existing approaches are inadequate enough to require a language feature.
- The paper offers no meaningful account of who is affected or how the feature would coordinate with existing language and tooling conventions.
- The most glaring omission is implementation experience, since the only credited statement says a prototype was possible as a library function, which does not establish experience with the proposed language feature itself.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 5 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.67   accumulate 6.17   max 7.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.17  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 5.50 / 5.50   (all 3 samples: 5.83)
headings: h2 10
on threshold: vehicle
splits: motivation[2] 2/2/1  motivation[10] 2/1/2  prior_art[2] 2/1/1  insufficiency[9] 0/1/1
        insufficiency[10] 2/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 7 of 11 sections, strong in 2)
under each rule: top2 1.67   corroborated 1.67   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              2/2/1  -> 1.67
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  1/1/1  -> 1.00
  [6] 5 Unspecified behaviour                      1/1/1  -> 1.00
  [7] 6 Non optimizing modes                       1/1/1  -> 1.00
  [8] 7 Interaction with UB                        1/1/1  -> 1.00
  [9] 8 Side effects                               1/1/1  -> 1.00
  [10] 9 Implementation                             2/1/2  -> 1.67
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): What is lacking is a simple way for a programmer to interact with it.
candidate 2 (found by 3 of 33 passes): Having a way to check that the optimizer work as expected without resorting to reading assembler output can save many hours when fine tuning code or identifying regressions.
candidate 3 (found by 3 of 33 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 4 (found by 3 of 33 passes): This mean that `constant_assert` will have to be wrapped and replaced with something else in unoptimized builds.

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/0/0  -> 0.00
  [10] 9 Implementation                             0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              2/1/1  -> 1.33
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      1/1/1  -> 1.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/0/0  -> 0.00
  [10] 9 Implementation                             0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): A related feature `[[``assume``()]]` is sometimes used when we think we know the truth and want to make sure the optimizer know, hoping it will improve performance.
candidate 2 (found by 3 of 33 passes): The part where the compiler figure out if the expression can be resolved at compiler time is not possible to specify.

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/0/0  -> 0.00
  [10] 9 Implementation                             2/2/2  -> 2.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): With a library solution it is hard to control that no side effects are produced and that it behave correctly with UB.
candidate 2 (found by 1 of 33 passes): __builtin_constant_p has some problems that we can avoid by doing `constant_assert` as a dedicated language feature.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/0/0  -> 0.00
  [10] 9 Implementation                             0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/1/1  -> 0.67
  [10] 9 Implementation                             2/1/1  -> 1.33
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This may cause some unwanted costs and add restrictions on where a `constant_assert` can be used, so this proposal suggest that evaluating a constant_assert do not produce any side effects at runtime.
candidate 2 (found by 2 of 33 passes): With a library solution it is hard to control that no side effects are produced and that it behave correctly with UB.
candidate 3 (found by 1 of 33 passes): __builtin_constant_p has some problems that we can avoid by doing `constant_assert` as a dedicated language feature.

## implementation - grade 1.00  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/0/0  -> 0.00
  [10] 9 Implementation                             1/1/1  -> 1.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This let us implement a prototype as a library function.

-->
