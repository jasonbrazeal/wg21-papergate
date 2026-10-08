Verdict: Adequate (7/14)

The paper offers some useful motivation and situates the idea against existing practice, but it leaves the standardization case largely undeveloped where it matters most: audience, implementation experience, and the necessity of a language feature rather than a library facility.

- The strongest support is the clear explanation of why checking optimizer behavior matters and how the feature would fit alongside existing tools like `__builtin_constant_p` and `[[assume]]`.
- The argument that a library solution cannot adequately control side effects or undefined behavior is asserted, but the paper does not show concretely why a language feature is required.
- The paper claims implementation experience through a library prototype, but provides no evidence of that prototype’s use, limitations, or lessons.
- The most glaring omission is any account of who would be affected by the feature or how it would coordinate with existing implementations and toolchains.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 6.83   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 1.00  coordination 0.00  insufficiency 1.33  implementation 0.67
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.83)
headings: h2 10
on threshold: vehicle, insufficiency
splits: prior_art[2] 1/2/2  insufficiency[9] 1/1/0  implementation[10] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              2/2/2  -> 2.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  1/1/1  -> 1.00
  [6] 5 Unspecified behaviour                      1/1/1  -> 1.00
  [7] 6 Non optimizing modes                       1/1/1  -> 1.00
  [8] 7 Interaction with UB                        1/1/1  -> 1.00
  [9] 8 Side effects                               1/1/1  -> 1.00
  [10] 9 Implementation                             2/2/2  -> 2.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Having a way to check that the optimizer work as expected without resorting to reading assembler output can save many hours when fine tuning code or identifying regressions.
candidate 2 (found by 3 of 33 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 3 (found by 3 of 33 passes): many `constant_assert`s will need maximum optimizations. This mean that `constant_assert` will have to be wrapped and replaced with something else in unoptimized builds.
candidate 4 (found by 3 of 33 passes): This may cause some unwanted costs and add restrictions on where a `constant_assert` can be used, so this proposal suggest that evaluating a constant_assert do not produce any side effects at runtime.

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

## prior_art - grade 1.83 (fired in 2 of 11 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              1/2/2  -> 1.67
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               0/0/0  -> 0.00
  [10] 9 Implementation                             2/2/2  -> 2.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): A related feature `[[``assume``()]]` is sometimes used when we think we know the truth and want to make sure the optimizer know, hoping it will improve performance.
candidate 2 (found by 3 of 33 passes): Gcc implements a __builtin_constant_p(expr) [[constant_p]](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fconstant_005fp) that tells whether the expression has been constant folded by the optimizer or not.

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
candidate 1 (found by 3 of 33 passes): With a library solution it is hard to control that no side effects are produced and that it behave correctly with UB.

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

## insufficiency - grade 1.33 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 4                              0/0/0  -> 0.00
  [3] 2 Revisions                                  0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Use cases                                  0/0/0  -> 0.00
  [6] 5 Unspecified behaviour                      0/0/0  -> 0.00
  [7] 6 Non optimizing modes                       0/0/0  -> 0.00
  [8] 7 Interaction with UB                        0/0/0  -> 0.00
  [9] 8 Side effects                               1/1/0  -> 0.67
  [10] 9 Implementation                             2/2/2  -> 2.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This may cause some unwanted costs and add restrictions on where a `constant_assert` can be used, so this proposal suggest that evaluating a constant_assert do not produce any side effects at runtime.
candidate 2 (found by 2 of 33 passes): With a library solution it is hard to control that no side effects are produced and that it behave correctly with UB.
candidate 3 (found by 1 of 33 passes): __builtin_constant_p has some problems that we can avoid by doing `constant_assert` as a dedicated language feature.

## implementation - grade 0.67  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
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
  [10] 9 Implementation                             1/0/1  -> 0.67
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This let us implement a prototype as a library function.

-->
