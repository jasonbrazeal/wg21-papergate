Verdict: Weak (2/14)

The paper offers only a narrow basis for its own standardization, centered on its relationship to prior and in-flight work; most of the case for why this feature should be standardized is left implicit or unargued. The thinnest support concerns the motivating problem, the affected users, and any evidence that the feature is implementable or cannot be achieved through a library.

- The strongest support is the paper’s engagement with prior art and related proposals, showing awareness of how the design fits with existing and pending work.
- The paper claims a user base by pointing to positive feedback on pack indexing, but it does not substantiate who is affected or why their experience matters here.
- The paper does not establish why the problem is important enough to warrant standardization in the first place.
- The most glaring omission is the absence of any implementation experience, leaving the practical viability of the proposal entirely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.67/14)

Provisionally addressed: 2 of 7. Provisional points: 1.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.67   corroborated 1.33   accumulate 1.83   max 2.33

## SUMMARY
grades: motivation 0.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 1.50 / 1.50 / 2.00   (all 3 samples: 1.67)
headings: h2 11
on threshold: prior_art
splits: audience[3] 0/0/1  prior_art[4] 0/1/0
## END SUMMARY

## motivation - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## audience - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   0/0/1  -> 0.33
  [4] Design                                       0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): We added the ability to index packs of types and expressions in C++26 through P2662R3 [4]. (P2662R3 [4] is now implemented in Clang and GCC, and we got very positive feedback).

## prior_art - grade 1.50 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Design                                       0/1/0  -> 0.33
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [8] ? Type equivalence [temp.type]               1/1/1  -> 1.00
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): It turns out that [P2841R7](https://wg21.link/P2841R7) [3] has no impact on the design of this paper except that indexing a pack of concept template parameter just works - and [P2989R2](https://wg21.link/P2989R2) [2] was not approved for C++26.
candidate 2 (found by 2 of 36 passes): Both the black and green text below presumes that CWG3027 has been approved and applied
candidate 3 (found by 1 of 36 passes): Both [P2841R7](https://wg21.link/P2841R7) [3] and [P2989R2](https://wg21.link/P2989R2) [2] were in flight, and it was not clear to me if either these papers would impact the indexing of packs of template-names.
candidate 4 (found by 1 of 36 passes): The syntax for indexing a pack of template-name is similar to the syntax to the syntax used to index a pack of types or expressions.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 12 sections, strong in 0)
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
  [9] ■                                          0/0/0  -> 0.00
  [10] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [11] Feature test macros                          0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

-->
