Verdict: Weak (2/14)

The paper offers only a narrow basis for its own standardization: it shows awareness of nearby proposals and a related core issue, but it does not build a case that the feature is needed, that users are affected, or that standardization is the right vehicle. The thinnest support is around motivation and fit, where the paper is essentially silent.

- The strongest support is the discussion of prior art, which situates the proposal against P2841R7, P2989R2, and CWG3027.
- The implementation experience is asserted only as confidence about Clang, with no actual implementation offered.
- The paper does not establish why the problem matters or who is affected by it.
- It also leaves unaddressed why the standard, rather than a library or other mechanism, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.17/14)

Provisionally addressed: 2 of 7. Provisional points: 2.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.17   corroborated 1.67   accumulate 2.17   max 2.67

## SUMMARY
grades: motivation 0.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 2.50 / 1.50 / 2.50   (all 3 samples: 2.17)
headings: h2 9
on threshold: prior_art
splits: implementation[3] 1/0/1
## END SUMMARY

## motivation - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               1/1/1  -> 1.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Both [P2841R7](https://wg21.link/P2841R7) [3] and [P2989R2](https://wg21.link/P2989R2) [2] were in flight, and it was not clear to me if either these papers would impact the indexing of packs of template-names.
candidate 2 (found by 2 of 30 passes): [*Editor’s* *note:* Both the black and green text below presumes that [CWG3027](https://wg21.link/CWG3027) [1] has been approved and applied]
candidate 3 (found by 1 of 30 passes): It turns out that [P2841R7](https://wg21.link/P2841R7) [3] has no impact on the design of this paper except that indexing a pack of concept template parameter just works - and [P2989R2](https://wg21.link/P2989R2) [2] was not approved for C++26.
candidate 4 (found by 1 of 30 passes): Both the black and green text below presumes that CWG3027 [1] has been approved and applied

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.67  [binary: max] (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   1/0/1  -> 0.67
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): This paper has not been implemented, but I am confident this can be implemented in Clang without trouble.

-->
