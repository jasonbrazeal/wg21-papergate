Verdict: Adequate (7/14)

The paper gives a reasonably grounded account of why the current consteval-only type approach is causing trouble and what alternatives have been considered, but it leaves several parts of the standardization case more asserted than demonstrated. The strongest material concerns implementation experience and the identification of real language-design friction, while the thinnest parts involve coordination with existing features, why a library solution is insufficient, and who exactly is affected.

- The paper establishes meaningful implementation experience through a Clang fork and early GCC reports of compile-time cost with consteval-only types.
- The discussion of prior art and alternatives is well supported, including the contrast with P2996R13 and P3603R1.
- The claim that the consteval-only value rule is simpler and more enforceable than the consteval-only type rule is stated, but the paper does not establish it as a standardization need.
- The paper does not establish coordination and interoperability with the rest of the standard, nor does it show why a library-only approach would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.33   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.83)
headings: h2 7
on threshold: none
splits: audience[4] 0/1/0  vehicle[5] 2/0/2  implementation[4] 1/2/2  implementation[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 24 passes): But we’ve run into issues and limitations with that approach, so we propose that, for C++26, we change instead to a consteval-only value model.
candidate 2 (found by 2 of 24 passes): However, Jakub Jelinek pointed out in January 2026 that whether a type is consteval-only is not actually a static property.
candidate 3 (found by 2 of 24 passes): We do not currently have an answer to [[CWG3150]](https://cplusplus.github.io/CWG/issues/3150.html). Similarly, [[CWG3117]](https://wg21.link/cwg3117)/[[LWG4513]](https://wg21.link/lwg4513) needs to be resolved.
candidate 4 (found by 1 of 24 passes): Additionally, early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with

## audience - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/1/0  -> 0.33
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): approximately everybody who uses reflection will run into needing this.

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          2/2/2  -> 2.00
  [7] 6 Proposal                                   2/2/2  -> 2.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The Reflection design from [[P2996R13]](https://wg21.link/p2996r13) was based on a model of having consteval-only types to prevent reflections from leaking to runtime.
candidate 2 (found by 3 of 24 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 3 (found by 3 of 24 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 4 (found by 2 of 24 passes): We think the right approach is (2). We already have the notion of consteval-only values in the language today, a consteval-only type rule would be incomplete without them.

## vehicle - grade 0.67 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      2/0/2  -> 1.33
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): The consteval-only value rule gives us a way to keep reflections at compile-time with a simpler, more-easily-enforceable rule than the consteval-only type rule.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           1/2/2  -> 1.67
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          0/0/1  -> 0.33
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Barry implemented the consteval-only value approach in [his fork of the p2996 fork of clang](https://github.com/brevzin/llvm-project/commit/bb8ddc4050333bbc22e6646820062a4788fb70d8).
candidate 2 (found by 2 of 24 passes): Additionally, early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 3 (found by 1 of 24 passes): early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 4 (found by 1 of 24 passes): The hybrid approach was initially suggested due to implementation concerns of allowing `meta::info` to persist to runtime, but those concerns are no longer strongly held.

-->
