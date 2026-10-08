Verdict: Strong (9/14)

The paper offers a solid foundation for why statement-expression syntax is needed and how it connects to existing work, but it leaves several parts of the standardization case underdeveloped, particularly around the affected audience and the impossibility of a library solution. The strongest support comes from its clear motivation and demonstrated implementation experience, while the thinnest areas concern coordination with other proposals and the absence of evidence about who would use the feature.

- The paper establishes a concrete motivating need by tying the feature to pattern matching and the desugaring of control-flow operators.
- It shows credible implementation experience through a working clang implementation available on Compiler Explorer.
- It documents prior art and alternative spellings, including reasons for rejecting earlier forms.
- It does not establish who is affected by the proposal or why a library-only approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 5 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 8.00   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.50  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 8.00 / 8.50 / 9.00   (all 3 samples: 8.50)
headings: h2 5
on threshold: vehicle, coordination, implementation
splits: vehicle[3] 0/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 do expressions  (part 1 of 2)              2/2/2  -> 2.00
  [5] 3 do expressions  (part 2 of 2)              2/2/2  -> 2.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Let’s take the example motivating case from [[P2561R2] (A control flow operator)](https://wg21.link/p2561r2) and compare implicit last expression to explicit return:
candidate 2 (found by 3 of 21 passes): The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator ([[P2561R2]](https://wg21.link/p2561r2)) into a `do` expression.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 do expressions  (part 1 of 2)              0/0/0  -> 0.00
  [5] 3 do expressions  (part 2 of 2)              0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 do expressions  (part 1 of 2)              2/2/2  -> 2.00
  [5] 3 do expressions  (part 2 of 2)              2/2/2  -> 2.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Other alternative spellings we’ve considered: - `do return` (in the previous revision of this paper, which has an ambiguity with `do ... while` loops) - `do_yield` (presented to EWG in Issaquah as the initial pre-publication draft of this proposal)
candidate 2 (found by 2 of 21 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add
candidate 3 (found by 1 of 21 passes): Indeed, as of [[P2688R5] (Pattern Matching: `match` Expression)](https://wg21.link/p2688r5), the `{ *statement* }` production is gone and the `*braced-init-list*` case is now supported. Pattern matching now relies upon `do` expressions to support multiple statements.
candidate 4 (found by 1 of 21 passes): Pattern matching now relies upon `do` expressions to support multiple statements.

## vehicle - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/2  -> 1.00
  [4] 3 do expressions  (part 1 of 2)              0/0/0  -> 0.00
  [5] 3 do expressions  (part 2 of 2)              2/2/2  -> 2.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add
candidate 2 (found by 1 of 21 passes): What pattern matching really needs here is a statement-expression syntax.
candidate 3 (found by 1 of 21 passes): What pattern matching really needs here is a statement-expression syntax. But it’s not just pattern matching that has a strong desire for statement-expressions, this would be a broadly useful facility, so we should have an orthogonal language feature

## coordination - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 do expressions  (part 1 of 2)              0/0/0  -> 0.00
  [5] 3 do expressions  (part 2 of 2)              0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): What pattern matching really needs here is a statement-expression syntax.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 do expressions  (part 1 of 2)              0/0/0  -> 0.00
  [5] 3 do expressions  (part 2 of 2)              0/0/0  -> 0.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 do expressions  (part 1 of 2)              0/0/0  -> 0.00
  [5] 3 do expressions  (part 2 of 2)              2/2/2  -> 2.00
  [6] 4 Wording                                    0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This is implemented in clang and can be seen on [compiler explorer](https://compiler-explorer.com/z/jcEGbEYnf).

-->
