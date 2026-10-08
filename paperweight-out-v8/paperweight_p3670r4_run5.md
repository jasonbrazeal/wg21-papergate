Verdict: Weak (2/14)

The paper offers very little support for its own standardization, resting almost entirely on brief references to related proposals and an expression of confidence about implementability. Its thinnest areas are the basic questions of why the feature matters, who it would affect, and why it belongs in the standard rather than in a library.

- The strongest support is the paper’s engagement with related in-flight proposals, though even that is presented as unresolved rather than as evidence of a clear path.
- The only other positive claim is the author’s confidence that Clang implementation would be straightforward, but no implementation experience is actually reported.
- The paper does not establish the problem’s significance or identify any affected users or use cases.
- Most glaringly, it offers no argument for why standardization is necessary or why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.50/14)

Provisionally addressed: 2 of 7. Provisional points: 1.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.50   corroborated 1.33   accumulate 1.50   max 2.33

## SUMMARY
grades: motivation 0.00  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 1.50 / 1.00 / 2.00   (all 3 samples: 1.50)
headings: h2 9
on threshold: prior_art
splits: prior_art[6] 1/0/0  implementation[3] 0/0/1
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

## prior_art - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               1/0/0  -> 0.33
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): It turns out that [P2841R7](https://wg21.link/P2841R7) [3] has no impact on the design of this paper except that indexing a pack of concept template parameter just works - and [P2989R2](https://wg21.link/P2989R2) [2] was not approved for C++26.
candidate 2 (found by 1 of 30 passes): Both [P2841R7](https://wg21.link/P2841R7) [3] and [P2989R2](https://wg21.link/P2989R2) [2] were in flight, and it was not clear to me if either these papers would impact the indexing of packs of template-names.
candidate 3 (found by 1 of 30 passes): Both the black and green text below presumes that [CWG3027](https://wg21.link/CWG3027) [1] has been approved and applied

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

## implementation - grade 0.33  [binary: max] (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/1  -> 0.33
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): This paper has not been implemented, but I am confident this can be implemented in Clang without trouble.

-->
