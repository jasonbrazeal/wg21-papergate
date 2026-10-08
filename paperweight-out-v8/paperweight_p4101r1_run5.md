Verdict: Adequate (7/14)

The paper gives a partial but uneven account of why this work belongs in the standard, with its strongest material concentrated in prior art and early implementation feedback. The case thins considerably around who is affected, how the feature would coordinate with existing or in-flight work, and why a library solution cannot suffice.

- The paper most convincingly grounds itself in existing proposals and GCC implementation experience, showing both a lineage for the idea and concrete signals about compile-time cost.
- The motivation is supported by a concrete ill-formed example and an open core issue, though the explanation remains narrowly tied to that example.
- The argument for standardization rather than a library approach is asserted through a single sentence about simplicity and enforceability, without enough surrounding reasoning to establish it.
- The paper does not establish who is affected or how the proposal interoperates with adjacent standardization efforts, leaving the practical audience and coordination picture unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.67   accumulate 6.67   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.00 / 6.00   (all 3 samples: 6.67)
headings: h2 7
on threshold: vehicle, implementation
splits: prior_art[3] 1/0/1  implementation[4] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Issues with Consteval-only Types           2/2/2  -> 2.00
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): However, Jakub Jelinek pointed out in January 2026 that whether a type is consteval-only is not actually a static property.
candidate 2 (found by 3 of 24 passes): We do not currently have an answer to [[CWG3150]](https://cplusplus.github.io/CWG/issues/3150.html).
candidate 3 (found by 2 of 24 passes): we’ve run into issues and limitations with that approach
candidate 4 (found by 2 of 24 passes): This example is ill-formed today. The linked paper has a longer description, but basically `fptrs` is a `constexpr` variable that is initialized to an array of pointers to consteval functions. That is disallowed today.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          2/2/2  -> 2.00
  [7] 6 Proposal                                   2/2/2  -> 2.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 2 (found by 3 of 24 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 3 (found by 2 of 24 passes): The Reflection design from [[P2996R13]](https://wg21.link/p2996r13) was based on a model of having consteval-only types to prevent reflections from leaking to runtime.
candidate 4 (found by 2 of 24 passes): We think the right approach is (2). We already have the notion of consteval-only values in the language today, a consteval-only type rule would be incomplete without them.

## vehicle - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The consteval-only value rule gives us a way to keep reflections at compile-time with a simpler, more-easily-enforceable rule than the consteval-only type rule.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.67  [binary: max] (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           2/2/1  -> 1.67
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 2 (found by 1 of 24 passes): Additionally, early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with

-->
