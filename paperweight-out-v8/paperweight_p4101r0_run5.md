Verdict: Adequate (6/14)

The paper offers a solid foundation in places, particularly in showing that the current model has real limitations and that a concrete implementation exists, but it leaves several essential parts of the standardization case largely unargued. The thinnest support is around why this needs to be in the standard at all, how it coordinates with existing features, and why a library solution cannot suffice.

- The strongest support is the implementation experience, with a working implementation in a Clang fork demonstrating the consteval-only value approach.
- The paper also establishes prior art and alternatives by connecting the proposal to earlier work on consteval-only values and the reflection design discussions.
- The most glaring omission is the absence of any established argument for why the standard is the right venue, or why a library approach would not work.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.67   accumulate 6.33   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.50 / 6.50 / 6.00   (all 3 samples: 6.33)
headings: h2 5
on threshold: implementation
splits: audience[3] 1/1/0  prior_art[2] 1/0/1  prior_art[3] 2/2/0
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
candidate 1 (found by 3 of 18 passes): However, Jakub Jelinek pointed out in January 2026 that whether a type is consteval-only is not actually a static property.
candidate 2 (found by 2 of 18 passes): But we’ve run into issues and limitations with that approach, so we propose that, for C++26, we change instead to a consteval-only value model.
candidate 3 (found by 2 of 18 passes): This example is ill-formed today. The linked paper has a longer description, but basically `fptrs` is a `constexpr` variable that is initialized to an array of pointers to consteval functions. That is disallowed today.
candidate 4 (found by 1 of 18 passes): we’ve run into issues and limitations with that approach

## audience - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Issues with Consteval-only Types           1/1/0  -> 0.67
  [4] 3 Consteval-only Values                      0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): approximately everybody who uses reflection will run into needing this
candidate 2 (found by 1 of 18 passes): approximately everybody who uses reflection will run into needing this.

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/0/1  -> 0.67
  [3] 2 Issues with Consteval-only Types           2/2/0  -> 1.33
  [4] 3 Consteval-only Values                      2/2/2  -> 2.00
  [5] 4 Proposal                                   2/2/2  -> 2.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 2 (found by 3 of 18 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 3 (found by 2 of 18 passes): The Reflection design from [[P2996R13]](https://wg21.link/p2996r13) was based on a model of having consteval-only types to prevent reflections from leaking to runtime.
candidate 4 (found by 2 of 18 passes): One suggested approach of how to resolve these issues (the incompleteness issue and the extra-instantiation issue) was to borrow from the closest analogue we have to this problem in C++ today: abstract class types.

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
