Verdict: Adequate (6/14)

The paper offers some useful context and a concrete prototype, but its central argument for standardization rests on repeated assertions rather than demonstrated need. The thinnest support is around the actual problem being solved, the affected audience, and why existing or library-level mechanisms are insufficient.

- The strongest support is the availability of a Compiler Explorer prototype, which at least shows the idea can be explored in code.
- The paper does establish that it is consciously exploring a different design from P2822R2 and explains one alternative it chose not to pursue.
- The core motivating claim about `quantity` and ADL is asserted several times but never substantiated with examples, user impact, or evidence of a real-world failure.
- The paper does not establish why the standard should change, nor why a library solution would not be adequate, leaving the standardization rationale largely unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.67   accumulate 6.33   max 8.33

## SUMMARY
grades: motivation 1.17  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.83  insufficiency 0.17  implementation 2.00
sample agreement: 42 of 49 section-criterion pairs unanimous (86%)
single-sample totals would have been: 6.50 / 6.00 / 6.50   (all 3 samples: 6.33)
headings: h2 6
on threshold: motivation, coordination, implementation
splits: motivation[6] 0/0/1  audience[4] 1/0/0  prior_art[4] 0/2/1  prior_art[5] 0/1/1
        prior_art[7] 1/1/0  coordination[4] 2/2/1  insufficiency[4] 0/0/1
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

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   0/2/1  -> 1.00
  [5] Implementation                               0/1/1  -> 0.67
  [6] Design options                               2/2/2  -> 2.00
  [7] Wording                                      1/1/0  -> 0.67
candidate 1 (found by 3 of 21 passes): This paper is exploration of a different design than proposed by similar paper [P2822R2](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2822r2.pdf), major difference is this paper doesn't propose no new syntax and it uses existing annotation syntax.
candidate 2 (found by 2 of 21 passes): This is what I worded, it's the most powerful option. But it puts a responsibility on library to be in sync with language algorithm to gather associated entities.
candidate 3 (found by 2 of 21 passes): If T has an annotation of type associated_entities_override, associated entities are provided only by iterating the annnotation object to get their reflection in form of objects of type std::meta.
candidate 4 (found by 1 of 21 passes): This paper *doesn't propose adding adding CNTTP* (class nontype template parameters) *to ADL*, that would be breaking change.

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

## coordination - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Disclaimer                                   0/0/0  -> 0.00
  [4] Motivation                                   2/2/1  -> 1.67
  [5] Implementation                               0/0/0  -> 0.00
  [6] Design options                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Major problem here is that `quantity` template is using value representation `awesomeness/s` which is not adding associated entities to ADL based overload resolution.

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
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
