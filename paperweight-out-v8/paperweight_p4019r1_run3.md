Verdict: Adequate (7/14)

The paper gives a partial account of why a language feature might be useful, but it leaves several essential parts of the standardization case largely unargued, especially around affected users, interoperability, and real implementation experience. The strongest material concerns the motivation and the need for a language-level mechanism, while the thinnest concerns evidence that a library cannot suffice or that the feature has been tried in practice.

- The paper establishes a clear motivation by connecting `constant_assert` to optimizer interaction and the practical difficulty of verifying optimization without reading assembly.
- The paper establishes why standardization is needed by pointing to limitations of `__builtin_constant_p` and the desire for defined, side-effect-free evaluation.
- The paper does not establish who is affected, leaving the intended user community and its scale unspecified.
- The paper does not establish implementation experience, since the only credited statement says a prototype was possible as a library function rather than demonstrating experience with the proposed language feature.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.00   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.00  vehicle 1.50  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 6.00 / 6.50   (all 3 samples: 6.50)
headings: h2 10
on threshold: vehicle, insufficiency
splits: motivation[5] 2/1/1  vehicle[2] 0/1/0  vehicle[9] 1/0/0  insufficiency[9] 1/0/0
        insufficiency[10] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              2/2/2  -> 2.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  2/1/1  -> 1.33
  [6] 5 Unspecified behaviour                      1/1/1  -> 1.00
  [7] 6 Non optimizing modes                       1/1/1  -> 1.00
  [8] 7 Interaction with UB                        1/1/1  -> 1.00
  [9] 8 Side effects                               1/1/1  -> 1.00
  [10] 9 Implementation                             2/2/2  -> 2.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): What is lacking is a simple way for a programmer to interact with it.
candidate 2 (found by 3 of 33 passes): Having a way to check that the optimizer work as expected without resorting to reading assembler output can save many hours when fine tuning code or identifying regressions.
candidate 3 (found by 3 of 33 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 4 (found by 3 of 33 passes): This may cause some unwanted costs and add restrictions on where a `constant_assert` can be used

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

## prior_art - grade 1.00 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              1/1/1  -> 1.00
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
candidate 2 (found by 2 of 33 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 3 (found by 1 of 33 passes): This is how we want it. The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.

## vehicle - grade 1.50 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/1/0  -> 0.33
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       1/1/1  -> 1.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               1/0/0  -> 0.33
  [10] 9 Implementation                             2/2/2  -> 2.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `constant_assert` should be seen as a primary optimization driver and the optimizer should start with proving these checks on all levels of optimizations.
candidate 2 (found by 2 of 33 passes): __builtin_constant_p has some problems that we can avoid by doing `constant_assert` as a dedicated language feature.
candidate 3 (found by 1 of 33 passes): What is lacking is a simple way for a programmer to interact with it.
candidate 4 (found by 1 of 33 passes): this proposal suggest that evaluating a constant_assert do not produce any side effects at runtime.

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

## insufficiency - grade 1.00 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               1/0/0  -> 0.33
  [10] 9 Implementation                             2/1/2  -> 1.67
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): With a library solution it is hard to control that no side effects are produced and that it behave correctly with UB.
candidate 2 (found by 1 of 33 passes): This may cause some unwanted costs and add restrictions on where a `constant_assert` can be used, so this proposal suggest that evaluating a constant_assert do not produce any side effects at runtime.
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
