Verdict: Adequate (5/14)

The paper offers only a narrow basis for standardization: it demonstrates that one implementation exists and that a compiler extension once allowed the syntax, but it does not build a case that the language change is needed, that affected users are widespread, or that standardization is the right venue. The support is thinnest around the core questions of why the standard should change and why a library solution cannot address the problem.

- The strongest support is the implementation experience, since both GCC’s historical extension and a Clang prototype show the feature is technically feasible.
- The paper claims some real-world breakage during a C++20 upgrade, but it does not establish how broad or significant that impact is.
- The discussion of prior art and alternatives is present but remains asserted rather than demonstrated as a reason to prefer this design.
- The most glaring omission is the absence of any established argument for why the standard, rather than a library or tooling change, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 5 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 5.33   max 8.00

## SUMMARY
grades: motivation 1.00  audience 0.83  prior_art 0.67  vehicle 0.00  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 5.00 / 5.00   (all 3 samples: 5.33)
headings: h2 6
on threshold: motivation, audience, coordination
splits: audience[3] 2/2/1  prior_art[3] 0/0/2  prior_art[4] 2/0/0  coordination[3] 2/2/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): However, the two do not mix: a designated initializer can currently only refer to a direct non-static data members.
candidate 2 (found by 1 of 21 passes): While I can initialize an `A` like `A{.a=1}`, I cannot designated-initialize `B`.

## audience - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/1  -> 1.67
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): gcc in `-std=c++17` mode — still to this day on trunk — supports `B{{.a=1}, .b=2}`. We actually had some code break while upgrading to C++20 that initialized aggregates in this way.
candidate 2 (found by 1 of 21 passes): We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## prior_art - grade 0.67 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/2  -> 0.67
  [4] 3 Proposal                                   2/0/0  -> 0.67
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): A previous revision of this paper proposed allowing only `b1` — coming up with a way to name the base class. This revision eschews that approach entirely.
candidate 2 (found by 1 of 21 passes): The original revisions of this paper dealt with how to name the `A` base class of `B`, and what this means for more complicated base classes (such at those with template parameters). This revision eschews that approach entirely

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/1  -> 1.67
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   2/2/2  -> 2.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): gcc in `-std=c++17` mode — still to this day on trunk — supports `B{{.a=1}, .b=2}`.
candidate 2 (found by 3 of 21 passes): I implemented this [in clang](https://github.com/llvm/llvm-project/compare/main...brevzin:llvm-project:p2287?expand=1) in a very literal way — by synthesizing a new designated-initializer-list to initialize the base classes in the situations where that comes up.

-->
