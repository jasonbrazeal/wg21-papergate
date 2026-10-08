Verdict: Adequate to Strong (7/14)

The paper offers a solid foundation for its proposal by clearly motivating the need for mixed smart-pointer/raw-pointer comparisons and by demonstrating both prior art and a working prototype, but it leaves several important justifications asserted rather than shown. The thinnest areas are the absence of any argument for why a library solution would be insufficient and the repeated reliance on an unsupported claim about how common the situation is in practice.

- The strongest support comes from the concrete implementation experience, with a working GCC 13 prototype available for review.
- The paper also does well in establishing prior art and alternatives, showing how earlier proposals addressed adjacent problems without fully resolving this one.
- The case for why this belongs in the standard is weakened by resting on the same unsubstantiated claim about practical frequency rather than offering evidence or examples.
- The most glaring omission is the complete lack of any discussion of why a library-only solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.33   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.50  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.50 / 7.00   (all 3 samples: 7.17)
headings: h2 10
on threshold: implementation
splits: motivation[2] 1/1/0  motivation[6] 1/0/1  audience[5] 0/1/0  prior_art[5] 2/1/1
        prior_art[6] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               2/2/2  -> 2.00
  [5] 3. Motivation and Scope                      2/2/2  -> 2.00
  [6] 4. Impact On The Standard                    1/0/1  -> 0.67
  [7] 5. Design Decisions                          2/2/2  -> 2.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Code like this (predicates, etc.) may get duplicated all over the place where smart pointers are used in containers/algorithms.
candidate 2 (found by 3 of 33 passes): Allowing mixed comparisons isn’t merely a "semantic fixup"; the situation where one has to compare smart pointers and raw pointers commonly occurs in practice
candidate 3 (found by 3 of 33 passes): The motivating reason of this proposal is that this code should work:
candidate 4 (found by 2 of 33 passes): We propose to enable mixed comparisons for the Standard Library smart pointer class templates `unique_ptr` and `shared_ptr`, so that one can compare them against raw pointers.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 1 of 33 passes): the situation where one has to compare smart pointers and raw pointers commonly occurs in practice

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               2/2/2  -> 2.00
  [5] 3. Motivation and Scope                      2/1/1  -> 1.33
  [6] 4. Impact On The Standard                    2/0/2  -> 1.33
  [7] 5. Design Decisions                          2/2/2  -> 2.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): [P0919R3] does not provide a heterogeneous hasher for smart pointers, so a custom one is still needed
candidate 2 (found by 3 of 33 passes): [P1614R2] added support for `operator<=>` across the Standard Library. Notably, it *added* `operator<=>` for `unique_ptr`, leaving the other four ordering operators (`<`, `<=`, `>`, `>=`) untouched.
candidate 3 (found by 2 of 33 passes): Smart pointer classes are universally recognized as the idiomatic way to express ownership of a resource (very incomplete list: [Sutter], [Meyers], [R.20]).
candidate 4 (found by 2 of 33 passes): [P0805R2] matches the spirit of the current proposal, although comparing smart pointers and raw pointer does not require any algorithm, and does not have such a verbose syntax.

## vehicle - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 33 passes): We propose to remove this inconsistency by defining the relational operators between the Standard Library owning smart pointer classes and raw pointers.
candidate 2 (found by 1 of 33 passes): Allowing mixed comparisons isn’t merely a "semantic fixup"; the situation where one has to compare smart pointers and raw pointers commonly occurs in practice

## coordination - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 33 passes): Allowing mixed comparisons isn’t merely a "semantic fixup"; the situation where one has to compare smart pointers and raw pointers commonly occurs in practice
candidate 2 (found by 1 of 33 passes): the situation where one has to compare smart pointers and raw pointers commonly occurs in practice

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
