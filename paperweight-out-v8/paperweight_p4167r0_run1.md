Verdict: Adequate (6/14)

The paper offers only partial support for its own standardization, with the strongest material concentrated in its acknowledgment of prior work and a small amount of implementation experimentation. The case is thinnest where it matters most: the paper does not establish why the standard should change or why a library cannot address the problem, and its central motivating claim about ADL is asserted rather than demonstrated.

- The paper’s treatment of prior art and alternatives is the most solid part, clearly situating the design against P2822R2 and existing annotation syntax.
- The implementation experience is real but minimal, consisting only of a Compiler Explorer prototype for gathering associated entities.
- The core motivation—that the `quantity` template’s value representation fails to add associated entities for ADL—is stated as a problem without evidence of who is affected or why it rises to the level of a standards change.
- The paper never establishes why the standard, as opposed to a library, is the right venue, nor does it address coordination and interoperability beyond repeating the same unsubstantiated ADL claim.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 5 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 6.00   accumulate 5.83   max 8.00

## SUMMARY
grades: motivation 1.00  audience 0.17  prior_art 1.83  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 1.67
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 4.50 / 6.00 / 6.50   (all 3 samples: 5.67)
headings: h2 6
on threshold: motivation, coordination, implementation
splits: audience[4] 0/0/1  prior_art[4] 1/2/1  prior_art[6] 1/2/2  implementation[4] 1/2/2
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## audience - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   0/0/1  -> 0.33
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.

## prior_art - grade 1.83 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   1/2/1  -> 1.33
  [5] Implementation                               1/1/1  -> 1.00
  [6] Design options                               1/2/2  -> 1.67
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper is exploration of a different design than proposed by similar paper [P2822R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2822r2.pdf), major difference is this paper doesn't propose no new syntax and it uses existing annotation syntax.
candidate 2 (found by 3 of 21 passes): One possible approach could be:
candidate 3 (found by 2 of 21 passes): Mateusz Pusz [presented](https://github.com/train-it-eu/conf-slides/tree/a5c771c590814db9e8b59cf556af3ce81716d0e1/2026.03%20-%20Croydon) on an evening session in Croydon his [MP-Units library](https://github.com/mpusz/mp-units) paper
candidate 4 (found by 2 of 21 passes): This is what I worded, it's the most powerful option. But it puts a responsibility on library to be in sync with language algorithm to gather associated entities.

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

## implementation - grade 1.67  [binary: max] (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   1/2/2  -> 1.67
  [5] Implementation                               1/1/1  -> 1.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): You can experiment with the example on [compiler explorer](https://compiler-explorer.com/z/Mxacx74r7).
candidate 2 (found by 3 of 21 passes): Currently none, only prototype on godbolt to gather the associated entities with purely library code.

-->
