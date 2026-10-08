Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why the current consteval-only type model is problematic and why a consteval-only value model is being considered, and it points to concrete implementation experience. The support is thinnest around the case for standardization itself: it does not show who is affected, how the feature would coordinate with existing or in-flight work, or why a library solution cannot address the problem.

- The strongest support comes from the established motivation, including concrete ill-formed examples and reported compile-time costs from GCC.
- The paper also establishes prior art and alternatives by discussing the earlier consteval-only values proposal and the hybrid approach.
- The argument for why this needs to be in the standard is only claimed, resting on a simpler and more easily enforceable rule without further demonstration.
- The most glaring omissions are the absence of any established affected audience, coordination and interoperability analysis, or explanation of why a library will not do.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 7
on threshold: implementation
splits: vehicle[5] 0/0/1  implementation[2] 0/1/0
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
candidate 1 (found by 3 of 24 passes): But we’ve run into issues and limitations with that approach, so we propose that, for C++26, we change instead to a consteval-only value model.
candidate 2 (found by 2 of 24 passes): This example is ill-formed today. The linked paper has a longer description, but basically `fptrs` is a `constexpr` variable that is initialized to an array of pointers to consteval functions. That is disallowed today.
candidate 3 (found by 1 of 24 passes): Additionally, early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 4 (found by 1 of 24 passes): This is a problem. Note also that class incompleteness might apply to members — rather than `S` being incomplete, `S` could have a member `U*` where `U` is incomplete. We cannot say definitively whether a type is consteval-only or not.

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

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          2/2/2  -> 2.00
  [7] 6 Proposal                                   2/2/2  -> 2.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We already explored this idea of consteval-only values in [[P3603R1] (Consteval-only Values and Consteval Variables)](https://wg21.link/p3603r1), but what if we generalized the notion we have today and combined it with reflections?
candidate 2 (found by 2 of 24 passes): The hybrid approach was initially suggested due to implementation concerns of allowing `meta::info` to persist to runtime, but those concerns are no longer strongly held.
candidate 3 (found by 2 of 24 passes): unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 4 (found by 1 of 24 passes): We believe that there are four options: 1. Stick with the consteval-only type model... 2. Switch to the consteval-only value model... 3. Switch to the consteval-only value model... 4. A hybrid approach...

## vehicle - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      0/0/1  -> 0.33
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The consteval-only value rule gives us a way to keep reflections at compile-time with a simpler, more-easily-enforceable rule than the consteval-only type rule.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/1/0  -> 0.33
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           2/2/2  -> 2.00
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          1/1/1  -> 1.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 2 (found by 3 of 24 passes): The hybrid approach was initially suggested due to implementation concerns of allowing `meta::info` to persist to runtime, but those concerns are no longer strongly held.
candidate 3 (found by 1 of 24 passes): linked to implementation on compiler explorer

-->
