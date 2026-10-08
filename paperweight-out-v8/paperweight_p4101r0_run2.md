Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for its motivation and its relationship to prior reflection work, and it can point to a concrete implementation, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas are the absence of any discussion of coordination or interoperability and the lack of a case for why a library solution cannot suffice.

- The paper clearly establishes why the current type-based approach causes practical problems and why a value-level rule is worth pursuing.
- It also situates the proposal credibly against P2996 and P3603R1, and it reports implementation experience in a Clang fork.
- The claim that the standard is the right venue rests mainly on an assertion that the rule is simpler and more enforceable, without a developed argument.
- The paper does not address coordination with related features or interoperability concerns, and it never explains why a library-based approach would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.00   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 7.50 / 6.50 / 7.50   (all 3 samples: 7.17)
headings: h2 5
on threshold: implementation
splits: vehicle[4] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Issues with Consteval-only Types           2/2/2  -> 2.00
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): But we’ve run into issues and limitations with that approach, so we propose that, for C++26, we change instead to a consteval-only value model.
candidate 2 (found by 3 of 18 passes): This is a problem. Note also that class incompleteness might apply to members — rather than `S` being incomplete, `S` could have a member `U*` where `U` is incomplete.
candidate 3 (found by 3 of 18 passes): There is a different approach to restricting certain values to not persist until runtime: enforce the rules at a *value* level instead of a *type* level.

## audience - grade 0.50 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           1/1/1  -> 1.00
  [4] 3 Consteval-only Values                      0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): approximately everybody who uses reflection will run into needing this.

## prior_art - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   2/2/2  -> 2.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The Reflection design from [[P2996R13]](https://wg21.link/p2996r13) was based on a model of having consteval-only types to prevent reflections from leaking to runtime.
candidate 2 (found by 3 of 18 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 3 (found by 3 of 18 passes): unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.

## vehicle - grade 0.67 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      2/0/2  -> 1.33
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The consteval-only value rule gives us a way to keep reflections at compile-time with a simpler, more-easily-enforceable rule than the consteval-only type rule.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Barry implemented the consteval-only value approach in [his fork of the p2996 fork of clang](https://github.com/brevzin/llvm-project/compare/p2996...brevzin:llvm-project:consteval-only-values).

-->
