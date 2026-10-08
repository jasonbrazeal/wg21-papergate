Verdict: Adequate (6/14)

The paper gives a partial but uneven account of why its proposed change belongs in the standard, with the strongest material concentrated in motivation, prior art, and implementation experience, while the case for standardization itself remains largely unaddressed.

- The paper clearly establishes why the current type-based approach causes problems and why a value-level model is worth pursuing.
- It also shows meaningful engagement with prior work and reports concrete implementation experience in a fork of Clang.
- Its claim that nearly all reflection users will need this is asserted rather than demonstrated with evidence or examples.
- The most glaring omissions are the absence of any argument for why this requires a standard change, how it coordinates with existing features, or why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 5
on threshold: implementation
splits: audience[3] 0/0/1
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
candidate 2 (found by 3 of 18 passes): There is a different approach to restricting certain values to not persist until runtime: enforce the rules at a *value* level instead of a *type* level.
candidate 3 (found by 2 of 18 passes): However, Jakub Jelinek pointed out in January 2026 that whether a type is consteval-only is not actually a static property.
candidate 4 (found by 1 of 18 passes): This is a problem. Note also that class incompleteness might apply to members — rather than `S` being incomplete, `S` could have a member `U*` where `U` is incomplete.

## audience - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/1  -> 0.33
  [4] 3 Consteval-only Values                      0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): approximately everybody who uses reflection will run into needing this.

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
candidate 3 (found by 2 of 18 passes): unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 4 (found by 1 of 18 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

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
