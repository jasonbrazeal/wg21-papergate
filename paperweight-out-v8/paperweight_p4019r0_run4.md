Verdict: Adequate (6/14)

The paper offers a clear and persuasive account of why a facility like `constant_assert` would be useful, but it leaves much of the surrounding case for standardization asserted rather than demonstrated. The thinnest support concerns coordination with existing features and evidence from actual implementation or use.

- The strongest part of the paper is its motivation, which explains concretely how checking optimizer behavior can save time and support correctness without reading assembly.
- The discussion of implementation experience is suggestive but weak, since it points to a related compiler builtin and admits the proposed feature has not been implemented anywhere.
- The paper does not establish how the feature would coordinate or interoperate with existing standard facilities, leaving that question essentially unaddressed.
- The most glaring omission is the absence of any demonstrated implementation experience with the proposed `constant_assert` itself, which makes the standardization case largely prospective.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 6 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.67   accumulate 6.17   max 9.00

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 0.83  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 5.00 / 6.50   (all 3 samples: 5.67)
headings: h2 6
on threshold: motivation, vehicle, insufficiency
splits: audience[3] 1/0/1  prior_art[1] 1/1/2  prior_art[3] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  1/1/1  -> 1.00
  [4] 4 Unspecified behaviour                      1/1/1  -> 1.00
  [5] 5 Non optimizing modes                       1/1/1  -> 1.00
  [6] 6 Implementation                             1/1/1  -> 1.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): What is lacking is a simple way for a programmer to interact with it.
candidate 2 (found by 3 of 21 passes): Having a way to check that the optimizer work as expected without resorting to reading assembler output can save many hours when fine tuning code.
candidate 3 (found by 3 of 21 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 4 (found by 3 of 21 passes): For `constant_assert` on the other hand, we want the optimizer to do whatever it takes to prove it, even if it is not going to use the result to optimize the code.

## audience - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  1/0/1  -> 0.67
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             0/0/0  -> 0.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Macros that assert in debug and assume in release is not uncommon

## prior_art - grade 0.83 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/2  -> 1.33
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/1  -> 0.33
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             0/0/0  -> 0.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): A related feature `[[``assume``()]]` is sometimes used when we think we know the truth and want to make sure the optimizer know, hoping it will improve performance.
candidate 2 (found by 1 of 21 passes): Macros that assert in debug and assume in release is not uncommon, and also not safe.

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

## insufficiency - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## implementation - grade 1.00  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             1/1/1  -> 1.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Gcc implements a __builtin_constant_p(expr) [[constant_p]](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fconstant_005fp) that tells whether the expression has been constant folded by the optimizer or not.
candidate 2 (found by 1 of 21 passes): *constant_assert* has not been added in any implementation yet, but such a check is already implementable in user code.

-->
