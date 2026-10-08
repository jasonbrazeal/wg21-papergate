Verdict: Adequate (7/14)

The paper gives a workable account of why mixed smart-pointer comparisons would be useful and shows that the change has been prototyped, but it does not build a complete case for standardization. The support is thinnest around the questions that matter most for a library extension of this kind: whether the problem is widespread enough to require a standard solution, how the change fits with existing comparison machinery, and why users cannot simply supply their own helpers.

- The strongest support is the concrete implementation experience, since a working prototype on GCC 13 demonstrates that the proposed change is technically feasible.
- The paper also establishes the motivating problem clearly, showing that mixed comparisons are currently ill-formed and that existing proposals do not already cover this need.
- The weakest part of the case is the absence of any coordination or interoperability discussion, leaving unclear how the change interacts with the broader comparison design already in the standard.
- The paper likewise does not establish why a library-level solution would be insufficient, which is a notable gap for a proposal whose effect could plausibly be achieved through user-defined comparison operators or small utility functions.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.33   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.50 / 7.00 / 6.50   (all 3 samples: 6.67)
headings: h2 10
on threshold: implementation
splits: motivation[5] 2/0/0  vehicle[5] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               2/2/2  -> 2.00
  [5] 3. Motivation and Scope                      2/0/0  -> 0.67
  [6] 4. Impact On The Standard                    1/1/1  -> 1.00
  [7] 5. Design Decisions                          2/2/2  -> 2.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): We propose to enable mixed comparisons for the Standard Library smart pointer class templates `unique_ptr` and `shared_ptr`, so that one can compare them against raw pointers.
candidate 2 (found by 3 of 33 passes): Code like this (predicates, etc.) may get duplicated all over the place where smart pointers are used in containers/algorithms.
candidate 3 (found by 3 of 33 passes): The impact is positive: code that was ill-formed before becomes well-formed.
candidate 4 (found by 3 of 33 passes): The motivating reason of this proposal is that this code should work:

## audience - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               0/0/0  -> 0.00
  [5] 3. Motivation and Scope                      1/1/1  -> 1.00
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          0/0/0  -> 0.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): the situation where one has to compare smart pointers and raw pointers commonly occurs in practice

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               2/2/2  -> 2.00
  [5] 3. Motivation and Scope                      1/1/1  -> 1.00
  [6] 4. Impact On The Standard                    2/2/2  -> 2.00
  [7] 5. Design Decisions                          2/2/2  -> 2.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): [P0919R3] does not provide a heterogeneous hasher for smart pointers, so a custom one is still needed
candidate 2 (found by 3 of 33 passes): Smart pointer classes are universally recognized as the idiomatic way to express ownership of a resource (very incomplete list: [Sutter], [Meyers], [R.20]).
candidate 3 (found by 3 of 33 passes): [P0805R2] matches the spirit of the current proposal, although comparing smart pointers and raw pointer does not require any algorithm, and does not have such a verbose syntax.
candidate 4 (found by 3 of 33 passes): [P1614R2] added support for `operator<=>` across the Standard Library. Notably, it *added* `operator<=>` for `unique_ptr`, leaving the other four ordering operators (`<`, `<=`, `>`, `>=`) untouched.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               0/0/0  -> 0.00
  [5] 3. Motivation and Scope                      0/1/0  -> 0.33
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          0/0/0  -> 0.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Allowing mixed comparisons isn’t merely a "semantic fixup"; the situation where one has to compare smart pointers and raw pointers commonly occurs in practice

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               0/0/0  -> 0.00
  [5] 3. Motivation and Scope                      0/0/0  -> 0.00
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          0/0/0  -> 0.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               0/0/0  -> 0.00
  [5] 3. Motivation and Scope                      0/0/0  -> 0.00
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          0/0/0  -> 0.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               0/0/0  -> 0.00
  [5] 3. Motivation and Scope                      0/0/0  -> 0.00
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          0/0/0  -> 0.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 2/2/2  -> 2.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): A working prototype of the changes proposed by this paper, done on top of GCC 13, is available in this GCC branch on GitHub.

-->
