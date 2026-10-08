Verdict: Adequate (6/14)

The paper gives a partial account of why the proposed rewrite rule would be useful, but it leaves several essential parts of the standardization case largely unaddressed. The strongest material concerns motivation and continuity with existing language rules, while the discussion of affected users, implementation experience, and coordination is essentially absent.

- The paper clearly establishes that the change matters by connecting it to long-standing proxy iterator problems and to the existing pattern of operator rewrite rules.
- It offers credible prior art by tracing the idea to P1046R2 and by comparing the proposal with the more complex comparison operator rewrites.
- The argument for why this must be a language rule rather than a library facility is only asserted, not developed beyond the bare claim that a rewrite rule offers an option library solutions lack.
- The paper says nothing about who would be affected, what implementation experience exists, or how the feature would coordinate with existing and proposed language features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 4 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 6.00   max 8.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 0.00
sample agreement: 77 of 77 section-criterion pairs unanimous (100%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 10
on threshold: motivation, vehicle, insufficiency
splits: none
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        1/1/1  -> 1.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             1/1/1  -> 1.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have.
candidate 2 (found by 3 of 33 passes): It is not possible to safely and consistently define `operator``->` for these types, so we do not always do so, but under this proposal they would all do the right thing.
candidate 3 (found by 2 of 33 passes): This solves many long-standing issues around proxy iterators that return by value.
candidate 4 (found by 1 of 33 passes): The first motivation of this paper is that users should have little or no reason to write their own version of `operator->` when they have already provided an appropriate `operator*`.

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

## prior_art - grade 2.00 (fired in 2 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        2/2/2  -> 2.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper was split off from [[P1046R2](https://wg21.link/p1046r2)]. That paper proposed generating many operators, this paper is just the arrow overloads.
candidate 2 (found by 2 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have. However, unlike the comparison operators this change is significantly simpler and less likely to have all the corner cases we’ve seen with `operator==` and `operator<=>`.
candidate 3 (found by 1 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have.

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs->rhs` as being equivalent to `(*lhs).rhs`.

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

## insufficiency - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs->rhs` as being equivalent to `(*lhs).rhs`.
candidate 2 (found by 1 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator``<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs``->``rhs` as being equivalent to `(*``lhs``).``rhs`.

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
