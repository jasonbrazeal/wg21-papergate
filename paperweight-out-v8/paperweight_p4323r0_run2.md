Verdict: Weak (2/14)

The paper offers only a partial case for its own standardization, with its strongest material going toward explaining why the feature matters and what alternatives exist, while leaving most of the procedural and evidentiary requirements entirely unaddressed. The thinnest areas are those that would show the problem is real for identifiable users, that standardization is the right venue, and that the design has been tested in practice.

- The paper’s most developed support is its argument that requiring `do_return` matters for consistency, teachability, and readability, though even this is asserted rather than demonstrated.
- It gestures at prior art by referencing P2806R4 and raising the question of omitting returns in lambdas or functions, but does not establish a substantive comparison or alternative analysis.
- The paper does not identify who is affected by the issue or provide any evidence of user impact.
- It offers no case for why the standard is the appropriate mechanism, why a library solution would not suffice, or what implementation experience exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.17/14)

Provisionally addressed: 2 of 7. Provisional points: 2.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.17   corroborated 2.00   accumulate 3.50   max 2.33

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.50 / 2.00   (all 3 samples: 2.17)
headings: h2 5
on threshold: none
splits: motivation[4] 2/2/0
## END SUMMARY

## motivation - grade 1.17 (fired in 4 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Problems with omitting doreturn           2/2/0  -> 1.33
  [5] 3. Conclusion                                1/1/1  -> 1.00
  [6] 4. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This paper argues against that feature for a variety of reasons.
candidate 2 (found by 3 of 18 passes): I argue that this is a bad idea, and that `do_return` should be required, for the reasons listed below.
candidate 3 (found by 2 of 18 passes): Consistency with other constructs, teachability, stylistic consistency, accessibility, visual and textual greppability, and other positives aspects of the language are affected where `do` expressions are used without `do_return`.
candidate 4 (found by 1 of 18 passes): C++ users have been taught for 30 years that ... control flow interactions (without which you flow off the end of a block) require a keyword like `if`, `return`, `break`, `co_yield`, etc.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Problems with omitting doreturn           0/0/0  -> 0.00
  [5] 3. Conclusion                                0/0/0  -> 0.00
  [6] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Problems with omitting doreturn           0/0/0  -> 0.00
  [5] 3. Conclusion                                1/1/1  -> 1.00
  [6] 4. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): [[P2806R4]](https://wg21%2elink/p2806r4) proposed to let the user omit the last semicolon in a `do` expression to yield a result.
candidate 2 (found by 3 of 18 passes): [[P2806R4]](https://wg21%2elink/p2806r4) proposes a new feature of `do` expressions, allowing the user to put statements inside of an expression.
candidate 3 (found by 2 of 18 passes): Consistency with other constructs, teachability, stylistic consistency, accessibility, visual and textual greppability, and other positives aspects of the language are affected where `do` expressions are used without `do_return`.
candidate 4 (found by 1 of 18 passes): Do we want to allow omitting the `return` statement in lambdas, and/or in functions, in general?

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Problems with omitting doreturn           0/0/0  -> 0.00
  [5] 3. Conclusion                                0/0/0  -> 0.00
  [6] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Problems with omitting doreturn           0/0/0  -> 0.00
  [5] 3. Conclusion                                0/0/0  -> 0.00
  [6] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Problems with omitting doreturn           0/0/0  -> 0.00
  [5] 3. Conclusion                                0/0/0  -> 0.00
  [6] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Problems with omitting doreturn           0/0/0  -> 0.00
  [5] 3. Conclusion                                0/0/0  -> 0.00
  [6] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

-->
