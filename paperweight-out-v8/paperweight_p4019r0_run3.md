Verdict: Adequate (6/14)

The paper offers a clear motivation for why a facility like `constant_assert` would be useful to developers relying on optimizer behavior, but it leaves most of the practical case for standardization unproven. The thinnest areas are the absence of any identified affected audience, any coordination or interoperability analysis, and any implementation experience beyond a claim that something similar is already possible in user code.

- The strongest support is the motivation section, which credibly explains the time-saving and correctness-checking value of confirming optimizer behavior without reading assembly.
- The discussion of prior art gestures at related features like `__builtin_constant_p` and `[[assume()]]`, but it does not establish how those fall short in a way that requires a new standard facility.
- The argument for why a library or macro cannot suffice rests on a single assertion about extracting expressions into compile output, without demonstrating that this is a real limitation in practice.
- The most glaring omission is the complete lack of evidence about who would use this feature, how it would interact with existing tooling or contracts, or whether any implementation experience supports the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 5 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.00   accumulate 6.67   max 8.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.17  vehicle 1.17  coordination 0.00  insufficiency 0.83  implementation 1.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 6.00 / 6.00 / 6.50   (all 3 samples: 5.83)
headings: h2 6
on threshold: motivation, vehicle, insufficiency
splits: motivation[1] 0/2/0  motivation[3] 1/1/2  prior_art[6] 0/2/2  vehicle[5] 1/0/0
        insufficiency[6] 2/1/2
## END SUMMARY

## motivation - grade 1.67 (fired in 5 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/2/0  -> 0.67
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  1/1/2  -> 1.33
  [4] 4 Unspecified behaviour                      1/1/1  -> 1.00
  [5] 5 Non optimizing modes                       1/1/1  -> 1.00
  [6] 6 Implementation                             2/2/2  -> 2.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Having a way to check that the optimizer work as expected without resorting to reading assembler output can save many hours when fine tuning code.
candidate 2 (found by 3 of 21 passes): The idea here is to tap into the ingeniousness of the unconstrained optimizer and use it as a tool for correctness.
candidate 3 (found by 2 of 21 passes): many `constant_assert`s will need maximum optimizations. This mean that `constant_assert` will have to be wrapped and replaced with something else in unoptimized builds.
candidate 4 (found by 2 of 21 passes): For `constant_assert` on the other hand, we want the optimizer to do whatever it takes to prove it, even if it is not going to use the result to optimize the code.

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

## prior_art - grade 1.17 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  1/1/1  -> 1.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             0/2/2  -> 1.33
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): A related feature `[[``assume``()]]` is sometimes used when we think we know the truth and want to make sure the optimizer know, hoping it will improve performance.
candidate 2 (found by 2 of 21 passes): Gcc implements a __builtin_constant_p(expr) [[constant_p]](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fconstant_005fp) that tells whether the expression has been constant folded by the optimizer or not.
candidate 3 (found by 1 of 21 passes): Macros that assert in debug and assume in release is not uncommon, and also not safe.
candidate 4 (found by 1 of 21 passes): As a contract semantic, this will unlock some really powerful uses for both safety and performance as contracts can be forced to resolve at compile time.

## vehicle - grade 1.17 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       1/0/0  -> 0.33
  [6] 6 Implementation                             2/2/2  -> 2.00
  [7] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): To extract the expression and present it in the compile output it would need be a macro, and we would need better ways to produce error messages.
candidate 2 (found by 1 of 21 passes): `constant_assert` should be seen as a primary optimization driver and the optimizer should start with proving these checks on all levels of optimizations.
candidate 3 (found by 1 of 21 passes): Secondly, we do not want to base this on the constant expression query. It already has uses as a way to check if code is optimized and if not replace with something else.

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

## insufficiency - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Use cases                                  0/0/0  -> 0.00
  [4] 4 Unspecified behaviour                      0/0/0  -> 0.00
  [5] 5 Non optimizing modes                       0/0/0  -> 0.00
  [6] 6 Implementation                             2/1/2  -> 1.67
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
candidate 1 (found by 3 of 21 passes): *constant_assert* has not been added in any implementation yet, but such a check is already implementable in user code.

-->
