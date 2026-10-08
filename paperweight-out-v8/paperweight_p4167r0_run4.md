Verdict: Adequate (6/14)

The paper offers only a narrow basis for its own standardization: it credibly positions itself against prior work and explains that it is exploring a different design, but it does little to show why the problem matters, who would be affected, or why standardization rather than a library solution is necessary. The thinnest support is in the areas that would normally carry the burden of a proposal—motivation, affected users, and the need for language or standard action—where the paper either says nothing or offers only a fragment of reasoning.

- The strongest support is the paper’s clear contrast with P2822R2 and its acknowledgment of existing discussion and prototype work, which establishes that the author has considered alternatives.
- The paper claims, without establishing, that the ADL-related responsibility placed on libraries is a significant problem, but it does not connect this to a concrete need for standardization.
- The paper offers no account of who is affected by the issue, leaving the practical stakes of the proposal unstated.
- The most glaring omission is the absence of any argument for why the standard should address this rather than leaving it to libraries, especially since the paper itself notes that a library-only prototype exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 4 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.33   accumulate 5.50   max 7.33

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 6.00 / 5.50   (all 3 samples: 5.50)
headings: h2 6
on threshold: motivation, coordination
splits: motivation[6] 0/0/1  prior_art[4] 1/1/0  prior_art[5] 0/0/1  implementation[4] 2/2/0
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/1  -> 0.33
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.
candidate 2 (found by 1 of 21 passes): But it puts a responsibility on library to be in sync with language algorithm to gather associated entities.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   1/1/0  -> 0.67
  [5] Implementation                               0/0/1  -> 0.33
  [6] Design options                               2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper is exploration of a different design than proposed by similar paper [P2822R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2822r2.pdf), major difference is this paper doesn't propose no new syntax and it uses existing annotation syntax.
candidate 2 (found by 3 of 21 passes): This is what I worded, it's the most powerful option. But it puts a responsibility on library to be in sync with language algorithm to gather associated entities.
candidate 3 (found by 2 of 21 passes): Mateusz Pusz [presented](https://github.com/train-it-eu/conf-slides/tree/a5c771c590814db9e8b59cf556af3ce81716d0e1/2026.03%20-%20Croydon) on an evening session in Croydon his [MP-Units library](https://github.com/mpusz/mp-units) paper
candidate 4 (found by 1 of 21 passes): Currently none, only prototype on godbolt to gather the associated entities with purely library code.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/0  -> 1.33
  [5] Implementation                               1/1/1  -> 1.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Currently none, only prototype on godbolt to gather the associated entities with purely library code.
candidate 2 (found by 2 of 21 passes): You can experiment with the example on [compiler explorer](https://compiler-explorer.com/z/Mxacx74r7).

-->
