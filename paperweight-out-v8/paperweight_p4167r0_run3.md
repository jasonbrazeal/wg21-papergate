Verdict: Adequate (6/14)

The paper offers only partial support for its own standardization, with its strongest material concerning prior art and a small amount of implementation experience. The case is thinnest around the core rationale: why the problem matters, who is affected, why the standard is the right venue, and why a library solution cannot suffice are either asserted without adequate support or left unaddressed.

- The paper does establish that it is exploring a design distinct from P2822R2 and that a prototype exists on Compiler Explorer.
- The paper claims, but does not establish, that the `quantity` template’s value representation creates an ADL problem affecting users.
- The paper does not establish why standardization is necessary rather than a library-only approach.
- The paper offers no coordination or interoperability discussion beyond the same unestablished ADL claim.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 5 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 6.33   accumulate 5.83   max 7.33

## SUMMARY
grades: motivation 1.17  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 6.00 / 6.00 / 5.50   (all 3 samples: 5.83)
headings: h2 6
on threshold: motivation, implementation
splits: motivation[6] 1/0/0  audience[4] 1/0/0  prior_art[4] 2/2/0  prior_art[7] 0/0/1
        coordination[4] 0/2/1
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               1/0/0  -> 0.33
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.
candidate 2 (found by 1 of 21 passes): This is currently not worded, as I worded replacement.

## audience - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   1/0/0  -> 0.33
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/0  -> 1.33
  [5] Implementation                               1/1/1  -> 1.00
  [6] Design options                               2/2/2  -> 2.00
  [7] Wording                                      0/0/1  -> 0.33
candidate 1 (found by 3 of 21 passes): This paper is exploration of a different design than proposed by similar paper [P2822R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2822r2.pdf), major difference is this paper doesn't propose no new syntax and it uses existing annotation syntax.
candidate 2 (found by 3 of 21 passes): This is what I worded, it's the most powerful option. But it puts a responsibility on library to be in sync with language algorithm to gather associated entities.
candidate 3 (found by 2 of 21 passes): Currently none, only prototype on godbolt to gather the associated entities with purely library code.
candidate 4 (found by 1 of 21 passes): This paper *doesn't propose adding adding CNTTP* (class nontype template parameters) *to ADL*, that would be breaking change. This paper proposes adding ability to add other associated entity via a custom annotation.

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

## coordination - grade 0.50 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   0/2/1  -> 1.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Implementation                               1/1/1  -> 1.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): You can experiment with the example on [compiler explorer](https://compiler-explorer.com/z/Mxacx74r7).
candidate 2 (found by 3 of 21 passes): Currently none, only prototype on godbolt to gather the associated entities with purely library code.

-->
