Verdict: Weak (3/14)

The paper offers a clear and well-developed argument for why `do_return` should be required, but it does not build a comparable case for standardization itself. The strongest support concerns the motivation and the problems with the alternative, while the rest of the standardization rationale is largely absent.

- The paper establishes why the issue matters by articulating concrete problems with omitting `do_return` and arguing against that feature.
- The discussion of prior art and alternatives is present but underdeveloped, since it references P2806R4 without fully establishing how the proposed approach compares to or improves on existing practice.
- The paper does not establish who is affected, why the standard is the right venue, how the feature coordinates with existing or future work, why a library solution is insufficient, or whether there is implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 2.00   accumulate 3.50   max 3.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.50 / 2.50   (all 3 samples: 2.50)
headings: h2 5
on threshold: motivation
splits: motivation[2] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Problems with omitting doreturn           2/2/2  -> 2.00
  [5] 3. Conclusion                                1/1/1  -> 1.00
  [6] 4. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): I argue that this is a bad idea, and that `do_return` should be required, for the reasons listed below.
candidate 2 (found by 3 of 18 passes): The ability to omit keywords like `return` which would yield results from expressions is a staple of other languages, such as Kotlin and Rust.
candidate 3 (found by 3 of 18 passes): The discussion above shows that there are many serious problems with omitting `do_return` in `do` expressions.
candidate 4 (found by 1 of 18 passes): This paper argues against that feature for a variety of reasons.

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

## prior_art - grade 1.00 (fired in 3 of 6 sections, strong in 0)
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
candidate 3 (found by 3 of 18 passes): Consistency with other constructs, teachability, stylistic consistency, accessibility, visual and textual greppability, and other positives aspects of the language are affected where `do` expressions are used without `do_return`.

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
