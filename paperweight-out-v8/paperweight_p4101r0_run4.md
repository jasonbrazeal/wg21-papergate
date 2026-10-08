Verdict: Adequate to Strong (6/14)

The paper offers solid support in the areas that anchor the proposal’s motivation and feasibility, particularly its explanation of why the current model causes problems and its report of implementation experience. The case is much thinner, however, when it comes to showing that the problem is widespread, that standardization is the right venue, and that a library solution would not suffice.

- The strongest support is the concrete implementation experience, which demonstrates that the proposed consteval-only value approach has been tried in a compiler fork.
- The paper also clearly establishes prior art and alternatives, including the earlier consteval-only type model and the abstract-class analogy.
- The thinnest support is the absence of any coordination or interoperability discussion, leaving the proposal’s relationship to existing and adjacent features unexamined.
- The paper also fails to establish why a library solution cannot address the problem, which is a notable gap for a language-change proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.67   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 1.67  audience 0.50  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 6.50 / 6.00   (all 3 samples: 6.50)
headings: h2 5
on threshold: motivation, implementation
splits: motivation[3] 2/2/0  prior_art[2] 0/0/1  vehicle[4] 2/0/0
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Issues with Consteval-only Types           2/2/0  -> 1.33
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): But we’ve run into issues and limitations with that approach, so we propose that, for C++26, we change instead to a consteval-only value model.
candidate 2 (found by 3 of 18 passes): The consteval-only value rule gives us a way to keep reflections at compile-time with a simpler, more-easily-enforceable rule than the consteval-only type rule.
candidate 3 (found by 1 of 18 passes): This is a problem. Note also that class incompleteness might apply to members — rather than `S` being incomplete, `S` could have a member `U*` where `U` is incomplete.
candidate 4 (found by 1 of 18 passes): However, Jakub Jelinek pointed out in January 2026 that whether a type is consteval-only is not actually a static property.

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

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/1  -> 0.33
  [3] 2 Issues with Consteval-only Types           2/2/2  -> 2.00
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   2/2/2  -> 2.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): One suggested approach of how to resolve these issues (the incompleteness issue and the extra-instantiation issue) was to borrow from the closest analogue we have to this problem in C++ today: abstract class types.
candidate 2 (found by 3 of 18 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 3 (found by 3 of 18 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 4 (found by 1 of 18 passes): The Reflection design from [[P2996R13]](https://wg21.link/p2996r13) was based on a model of having consteval-only types to prevent reflections from leaking to runtime.

## vehicle - grade 0.33 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           0/0/0  -> 0.00
  [4] 3 Consteval-only Values                      2/0/0  -> 0.67
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
