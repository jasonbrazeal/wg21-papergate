Verdict: Adequate (5/14)

The paper gives a partial account of why a constant assertion facility would be useful, but it leaves several parts of the standardization case largely unargued, especially around affected users, implementation experience, and coordination with existing features. The strongest material concerns motivation and known alternatives, while the thinnest concerns the need for a standard facility rather than a library or macro solution.

- The paper clearly establishes the practical motivation: checking optimizer behavior without reading assembly and using constant evaluation as a correctness tool.
- It also credibly identifies prior art and alternatives such as GCC’s `__builtin_constant_p`, `assert`, and `assume`.
- The argument for why this must be standardized rather than implemented as a macro or library is only asserted, not developed.
- The paper offers no meaningful account of who is affected, how the feature would coordinate with existing or proposed facilities, or whether there is implementation experience to support the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 5 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.67   accumulate 6.17   max 7.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 1.00  coordination 0.00  insufficiency 0.50  implementation 0.67
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 5.50 / 4.50   (all 3 samples: 5.33)
headings: h2 6
on threshold: motivation, prior_art, vehicle
splits: motivation[6] 2/1/1  implementation[6] 1/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 5 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  1/1/1  -> 1.00
  [4] 4 Unspecified behaviour                      1/1/1  -> 1.00
  [5] 5 Non optimizing modes                       1/1/1  -> 1.00
  [6] 6 Implementation                             2/1/1  -> 1.33
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): What is lacking is a simple way for a programmer to interact with it.
candidate 2 (found by 3 of 21 passes): Having a way to check that the optimizer work as expected without resorting to reading assembler output can save many hours when fine tuning code.
candidate 3 (found by 3 of 21 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 4 (found by 3 of 21 passes): many `constant_assert`s will need maximum optimizations. This mean that `constant_assert` will have to be wrapped and replaced with something else in unoptimized builds.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             0/0/0  -> 0.00
  [7] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  1/1/1  -> 1.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             2/2/2  -> 2.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): As a contract semantic, this will unlock some really powerful uses for both safety and performance as contracts can be forced to resolve at compile time.
candidate 2 (found by 3 of 21 passes): Gcc implements a __builtin_constant_p(expr) [[constant_p]](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fconstant_005fp) that tells whether the expression has been constant folded by the optimizer or not.
candidate 3 (found by 2 of 21 passes): A related feature `[[``assume``()]]` is sometimes used when we think we know the truth and want to make sure the optimizer know, hoping it will improve performance.
candidate 4 (found by 1 of 21 passes): We already have `assert``()` that verify a statement at runtime. It is costly performance wise and introduces possible terminations into the application.

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             2/2/2  -> 2.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): To extract the expression and present it in the compile output it would need be a macro, and we would need better ways to produce error messages.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             0/0/0  -> 0.00
  [7] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             1/1/1  -> 1.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): To extract the expression and present it in the compile output it would need be a macro, and we would need better ways to produce error messages.

## implementation - grade 0.67  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             1/1/0  -> 0.67
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): *constant_assert* has not been added in any implementation yet, but such a check is already implementable in user code.

-->
