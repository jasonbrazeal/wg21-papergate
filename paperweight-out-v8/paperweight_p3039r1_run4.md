Verdict: Adequate (5/14)

The paper offers a partial case for its own standardization, with its clearest support coming from prior art and the lineage of the idea, but it leaves several essential questions about audience, implementation, and interoperability largely unaddressed. The argument is thinnest where it needs to show who would actually use the feature and whether it can be implemented and integrated without surprises.

- The strongest support is the paper’s grounding in prior work, including the split from P1046R2 and the parallel to the established rewrite rules for comparison operators.
- The discussion of why a library solution is insufficient is suggestive, particularly the point that a rewrite rule can avoid address-of and temporary-lifetime problems, but it is asserted rather than demonstrated.
- The motivation is only claimed, not established, because the paper does not show that users are actually writing their own `operator->` in problematic numbers or that existing proxy iterator issues are widespread enough to justify the change.
- The most glaring omission is the absence of any implementation experience or evidence about who is affected, leaving the proposal without a concrete demonstration that the feature is needed or feasible in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.00   accumulate 5.17   max 7.33

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 0.00  insufficiency 0.83  implementation 0.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.00 / 5.50 / 5.00   (all 3 samples: 5.00)
headings: h2 10
on threshold: motivation, vehicle, insufficiency
splits: motivation[5] 1/0/0  motivation[7] 0/1/1  prior_art[2] 0/2/0  prior_art[7] 0/2/2
        vehicle[4] 2/2/1  insufficiency[4] 1/2/2
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        1/0/0  -> 0.33
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/1/1  -> 0.67
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The first motivation of this paper is that users should have little or no reason to write their own version of `operator->` when they have already provided an appropriate `operator*`.
candidate 2 (found by 2 of 33 passes): It is not possible to safely and consistently define `operator``->` for these types, so we do not always do so, but under this proposal they would all do the right thing.
candidate 3 (found by 1 of 33 passes): This solves many long-standing issues around proxy iterators that return by value.
candidate 4 (found by 1 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have.

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         0/0/0  -> 0.00
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/2/0  -> 0.67
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        2/2/2  -> 2.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/2/2  -> 1.33
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper was split off from [[P1046R2](https://wg21.link/p1046r2)]. That paper proposed generating many operators, this paper is just the arrow overloads.
candidate 2 (found by 3 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have. However, unlike the comparison operators this change is significantly simpler and less likely to have all the corner cases we’ve seen with `operator==` and `operator<=>`.
candidate 3 (found by 1 of 33 passes): This proposal follows the lead of `operator``<=>` (see Consistent Comparison [P0515R3]) by generating rewrite rules if a particular operator does not exist in current code.
candidate 4 (found by 1 of 33 passes): All of these types that are adapter types define their `operator``->` as deferring to the base iterator’s `operator``->`.

## vehicle - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/1  -> 1.67
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs->rhs` as being equivalent to `(*lhs).rhs`.
candidate 2 (found by 1 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator``<=>`), not in terms of function calls.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         0/0/0  -> 0.00
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         1/2/2  -> 1.67
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs->rhs` as being equivalent to `(*lhs).rhs`.
candidate 2 (found by 1 of 33 passes): This neatly sidesteps all of the issues of library-only solutions (how do we get the address of the object? how do we handle temporaries?).

## implementation - grade 0.00  [binary: max] (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         0/0/0  -> 0.00
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

-->
