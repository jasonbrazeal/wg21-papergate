Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for why the problem matters, what alternatives were considered, and that the approach has been implemented, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support is around the need for a standard mechanism rather than a library solution, and around how the proposal would coordinate with existing or in-flight features.

- The strongest support is the implementation experience, with a working implementation in a Clang fork credited directly.
- The paper also establishes prior art and alternatives by connecting the proposal to P3603R1 and the reflection design in P2996R13.
- The claim that the standard is the right venue is only asserted, without a developed argument for why standardization is necessary here.
- The most glaring omission is coordination and interoperability, where the paper offers no established account of how the feature would fit with the broader language and library ecosystem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.67   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.50 / 6.50 / 7.50   (all 3 samples: 6.83)
headings: h2 5
on threshold: implementation
splits: prior_art[2] 0/0/1  prior_art[3] 2/2/0  vehicle[4] 0/0/2
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
candidate 2 (found by 3 of 18 passes): However, Jakub Jelinek pointed out in January 2026 that whether a type is consteval-only is not actually a static property.
candidate 3 (found by 3 of 18 passes): This example is ill-formed today. The linked paper has a longer description, but basically `fptrs` is a `constexpr` variable that is initialized to an array of pointers to consteval functions. That is disallowed today.

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

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/1  -> 0.33
  [3] 2 Issues with Consteval-only Types           2/2/0  -> 1.33
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   2/2/2  -> 2.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 2 (found by 3 of 18 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 3 (found by 2 of 18 passes): One suggested approach of how to resolve these issues (the incompleteness issue and the extra-instantiation issue) was to borrow from the closest analogue we have to this problem in C++ today: abstract class types.
candidate 4 (found by 1 of 18 passes): The Reflection design from [[P2996R13]](https://wg21.link/p2996r13) was based on a model of having consteval-only types to prevent reflections from leaking to runtime.

## vehicle - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      0/0/2  -> 0.67
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): The consteval-only value rule gives us a way to keep reflections at compile-time with a simpler, more-easily-enforceable rule than the consteval-only type rule.

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
