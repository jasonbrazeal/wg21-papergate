Verdict: Adequate (7/14)

The paper offers a solid foundation for its proposal by clearly motivating the need for mixed smart-pointer comparisons and demonstrating both prior art and a working prototype, but it leaves several key arguments asserted rather than substantiated. The thinnest support concerns the practical prevalence of the problem and the absence of any discussion of why a library solution would be insufficient.

- The strongest support comes from the concrete motivating code and the availability of a GCC-based prototype, which together show the intended behavior and feasibility.
- The discussion of prior art and alternatives is well grounded, particularly the references to P0919R3 and P1614R2.
- The claim that mixed comparisons are commonly needed in practice is repeated but never backed by examples, user reports, or codebase evidence.
- The paper does not address why a library-level solution would not suffice, leaving a central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.33   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.83  vehicle 0.33  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 7.00 / 6.50   (all 3 samples: 6.50)
headings: h2 10
on threshold: implementation
splits: motivation[2] 1/1/0  motivation[6] 1/0/0  audience[5] 0/1/0  prior_art[4] 2/1/2
        vehicle[5] 0/1/1  coordination[5] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               2/2/2  -> 2.00
  [5] 3. Motivation and Scope                      2/2/2  -> 2.00
  [6] 4. Impact On The Standard                    1/0/0  -> 0.33
  [7] 5. Design Decisions                          2/2/2  -> 2.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Code like this (predicates, etc.) may get duplicated all over the place where smart pointers are used in containers/algorithms.
candidate 2 (found by 3 of 33 passes): Allowing mixed comparisons isn’t merely a "semantic fixup"; the situation where one has to compare smart pointers and raw pointers commonly occurs in practice
candidate 3 (found by 3 of 33 passes): The motivating reason of this proposal is that this code should work:
candidate 4 (found by 2 of 33 passes): We propose to enable mixed comparisons for the Standard Library smart pointer class templates `unique_ptr` and `shared_ptr`, so that one can compare them against raw pointers.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)
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

## prior_art - grade 1.83 (fired in 3 of 11 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               2/1/2  -> 1.67
  [5] 3. Motivation and Scope                      1/1/1  -> 1.00
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          2/2/2  -> 2.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): [P0919R3] does not provide a heterogeneous hasher for smart pointers, so a custom one is still needed
candidate 2 (found by 3 of 33 passes): [Sutter], [Meyers], [R.20]
candidate 3 (found by 3 of 33 passes): [P1614R2] added support for `operator<=>` across the Standard Library. Notably, it *added* `operator<=>` for `unique_ptr`, leaving the other four ordering operators (`<`, `<=`, `>`, `>=`) untouched.

## vehicle - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Tony Tables                               0/0/0  -> 0.00
  [5] 3. Motivation and Scope                      0/1/1  -> 0.67
  [6] 4. Impact On The Standard                    0/0/0  -> 0.00
  [7] 5. Design Decisions                          0/0/0  -> 0.00
  [8] 6. Technical Specifications                  0/0/0  -> 0.00
  [9] 7. Implementation experience                 0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): We propose to remove this inconsistency by defining the relational operators between the Standard Library owning smart pointer classes and raw pointers.

## coordination - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
