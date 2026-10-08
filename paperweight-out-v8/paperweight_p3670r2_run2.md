Verdict: Weak (2/14)

The paper offers a narrow but real foundation in its discussion of prior art and alternatives, yet it leaves most of the case for standardization unstated. The thinnest areas are the basic motivating questions—why the feature matters, why it belongs in the standard, and whether a library could suffice—along with any evidence of implementation experience or coordination with adjacent work.

- The strongest support is the paper’s engagement with related proposals and existing syntax, which grounds the design in known precedent.
- The claim that “we got very positive feedback” gestures at affected users but offers no concrete community or use-case evidence.
- The paper does not establish why the feature matters in the first place, leaving the core motivation implicit.
- Most glaringly, it offers no argument for why standardization is necessary or why a library solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.67/14)

Provisionally addressed: 2 of 7. Provisional points: 1.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.67   corroborated 1.33   accumulate 2.17   max 2.33

## SUMMARY
grades: motivation 0.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 2.00 / 1.50 / 1.50   (all 3 samples: 1.67)
headings: h2 9
on threshold: prior_art
splits: audience[3] 1/0/0
## END SUMMARY

## motivation - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   1/0/0  -> 0.33
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): we got very positive feedback

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Design                                       1/1/1  -> 1.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               1/1/1  -> 1.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The syntax for indexing a pack of template-name is similar to the syntax to the syntax used to index a pack of types or expressions.
candidate 2 (found by 3 of 30 passes): [*Editor’s* *note:* Both the black and green text below presumes that [CWG3027](https://wg21.link/CWG3027) [1] has been approved and applied]
candidate 3 (found by 2 of 30 passes): It turns out that [P2841R7](https://wg21.link/P2841R7) [3] has no impact on the design of this paper except that indexing a pack of concept template parameter just works - and [P2989R2](https://wg21.link/P2989R2) [2] was not approved for C++26.
candidate 4 (found by 1 of 30 passes): Both [P2841R7](https://wg21.link/P2841R7) [3] and [P2989R2](https://wg21.link/P2989R2) [2] were in flight, and it was not clear to me if either these papers would impact the indexing of packs of template-names.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

-->
