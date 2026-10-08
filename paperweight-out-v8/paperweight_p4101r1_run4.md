Verdict: Adequate to Strong (6/14)

The paper gives a mixed account of its own readiness: it grounds the problem and the proposed direction in concrete implementation experience, but it leaves several parts of the standardization argument asserted rather than demonstrated. The thinnest support is around the need for a standard mechanism specifically, as opposed to a library or implementation strategy, and around how the change would fit with existing or adjacent standardization work.

- The strongest support comes from implementation experience, with both GCC cost reports and a Clang implementation of the consteval-only value approach cited.
- The paper also establishes why the issue matters for C++26 and shows meaningful engagement with prior art, particularly P3603R1.
- The claim that the consteval-only value rule is simpler and more enforceable than the consteval-only type rule is asserted, but the paper does not establish it as a standardization rationale.
- The most glaring omission is the lack of any established case for why a library solution cannot address the need or how the proposal coordinates with related standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.00 / 6.00 / 7.50   (all 3 samples: 6.50)
headings: h2 7
on threshold: implementation
splits: motivation[6] 2/1/2  audience[4] 0/0/1  vehicle[5] 0/0/2  implementation[5] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Issues with Consteval-only Types           2/2/2  -> 2.00
  [5] 4 Consteval-only Values                      2/2/2  -> 2.00
  [6] 5 Options for C++26                          2/1/2  -> 1.67
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This example is ill-formed today. The linked paper has a longer description, but basically `fptrs` is a `constexpr` variable that is initialized to an array of pointers to consteval functions. That is disallowed today.
candidate 2 (found by 2 of 24 passes): But we’ve run into issues and limitations with that approach, so we propose that, for C++26, we change instead to a consteval-only value model.
candidate 3 (found by 2 of 24 passes): Additionally, early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 4 (found by 2 of 24 passes): This is a problem we have to resolve for C++26.

## audience - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/1  -> 0.33
  [5] 4 Consteval-only Values                      0/0/0  -> 0.00
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): approximately everybody who uses reflection will run into needing this.

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 3)
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
candidate 2 (found by 3 of 24 passes): The hybrid approach was initially suggested due to implementation concerns of allowing `meta::info` to persist to runtime, but those concerns are no longer strongly held.
candidate 3 (found by 2 of 24 passes): unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.
candidate 4 (found by 1 of 24 passes): Note that unlike [[P3603R1]](https://wg21.link/p3603r1), this paper does not propose the ability to *explicitly* declare an immediate variable.

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           0/0/0  -> 0.00
  [5] 4 Consteval-only Values                      0/0/2  -> 0.67
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Issues with Consteval-only Types           2/2/2  -> 2.00
  [5] 4 Consteval-only Values                      0/0/2  -> 0.67
  [6] 5 Options for C++26                          0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Additionally, early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 2 (found by 1 of 24 passes): early experience from GCC ([#124925](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124925), [#125179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=125179)) indicate quite a bit of compile-time cost to having consteval-only types to begin with
candidate 3 (found by 1 of 24 passes): Barry implemented the consteval-only value approach in [his fork of the p2996 fork of clang](https://github.com/brevzin/llvm-project/commit/bb8ddc4050333bbc22e6646820062a4788fb70d8).

-->
