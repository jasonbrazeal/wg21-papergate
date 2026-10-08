Verdict: Weak (2/14)

The paper’s support for its own standardization is uneven: it situates the proposal against relevant prior work, but leaves most of the burden of justification unaddressed. The thinnest areas are the absence of any demonstrated user impact, the lack of a rationale for why the core language rather than a library is the right venue, and the absence of implementation evidence beyond the author’s confidence.

- The strongest support is the discussion of prior art, which credibly establishes how related proposals and a core issue interact with the design.
- The claim that the feature matters rests only on the assertion that there is “no good reason” for the current limitation, without showing concrete use cases or affected users.
- The most glaring omission is the lack of any implementation experience, since the paper explicitly says it has not been implemented and offers only an expectation that Clang could support it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.17/14)

Provisionally addressed: 3 of 7. Provisional points: 2.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.17   corroborated 2.00   accumulate 2.17   max 3.00

## SUMMARY
grades: motivation 0.33  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 2.50 / 1.50 / 2.50   (all 3 samples: 2.17)
headings: h2 9
on threshold: prior_art
splits: motivation[3] 2/0/0  implementation[3] 0/0/1
## END SUMMARY

## motivation - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revisions                                    0/0/0  -> 0.00
  [3] Motivation                                   2/0/0  -> 0.67
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Names of template specializations [temp... 0/0/0  -> 0.00
  [6] ? Type equivalence [temp.type]               0/0/0  -> 0.00
  [7] ■                                          0/0/0  -> 0.00
  [8] ? Keywords [gram.key]                        0/0/0  -> 0.00
  [9] Feature test macros                          0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): However, [P2662R3](https://wg21.link/P2662R3) [4] does not allow the indexing of a pack of templates. There is no good reason for that.

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
candidate 1 (found by 2 of 30 passes): It turns out that [P2841R7](https://wg21.link/P2841R7) [3] has no impact on the design of this paper except that indexing a pack of concept template parameter just works - and [P2989R2](https://wg21.link/P2989R2) [2] was not approved for C++26.
candidate 2 (found by 1 of 30 passes): Both [P2841R7](https://wg21.link/P2841R7) [3] and [P2989R2](https://wg21.link/P2989R2) [2] were in flight, and it was not clear to me if either these papers would impact the indexing of packs of template-names.
candidate 3 (found by 1 of 30 passes): [*Editor’s* *note:* Both the black and green text below presumes that [CWG3027](https://wg21.link/CWG3027) [1] has been approved and applied]
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
