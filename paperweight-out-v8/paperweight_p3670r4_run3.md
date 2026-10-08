Verdict: Weak (2/14)

The paper offers very little support for its own standardization, resting almost entirely on a brief statement about implementability and a passing discussion of related proposals. Its thinnest areas are the basic motivating questions: why the feature matters, who it affects, and why the standard is the right place for it.

- The strongest support is the author’s confidence that the feature can be implemented in Clang without trouble, though no actual implementation is reported.
- The paper gestures at prior art and alternatives by mentioning two related proposals and a core issue, but it does not establish how they bear on the design.
- The paper does not establish why the feature matters or who would be affected by it.
- The most glaring omission is the absence of any case for why the standard should address this rather than a library or other mechanism.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.00   accumulate 2.33   max 3.00

## SUMMARY
grades: motivation 0.00  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 2.00 / 2.50 / 2.50   (all 3 samples: 2.33)
headings: h2 9
on threshold: prior_art
splits: prior_art[6] 0/1/1
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

## prior_art - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/1/1  -> 0.67
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): It turns out that [P2841R7](https://wg21.link/P2841R7) [3] has no impact on the design of this paper except that indexing a pack of concept template parameter just works - and [P2989R2](https://wg21.link/P2989R2) [2] was not approved for C++26.
candidate 2 (found by 1 of 30 passes): Both [P2841R7](https://wg21.link/P2841R7) [3] and [P2989R2](https://wg21.link/P2989R2) [2] were in flight, and it was not clear to me if either these papers would impact the indexing of packs of template-names.
candidate 3 (found by 1 of 30 passes): Both the black and green text below presumes that CWG3027 has been approved and applied
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

## implementation - grade 1.00  [binary: max] (fired in 1 of 10 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper has not been implemented, but I am confident this can be implemented in Clang without trouble.

-->
