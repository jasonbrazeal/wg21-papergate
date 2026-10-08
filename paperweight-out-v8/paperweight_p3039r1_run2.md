Verdict: Adequate (5/14)

The paper offers only partial support for its own standardization, with its strongest grounding in prior art and the acknowledged lineage from P1046R2. Beyond that, the case is largely asserted rather than demonstrated, and several essential dimensions—such as who would be affected, how the feature would interoperate, and whether any implementation experience exists—are simply absent.

- The paper does establish that the idea was split from P1046R2 and that it follows the lead of existing rewrite rules, which gives it a recognizable technical ancestry.
- The discussion of why a library solution will not do is present but rests on claims about sidestepping library-only issues rather than a worked demonstration of those issues.
- The paper does not establish who is affected by the change, leaving the practical scope and user impact unclear.
- The most glaring omission is the complete absence of implementation experience, which leaves the proposal without evidence that the rewrite rule behaves as intended in real compilers or codebases.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.00   accumulate 5.17   max 7.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 1.00  implementation 0.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 4.83)
headings: h2 10
on threshold: motivation, insufficiency
splits: motivation[5] 1/0/1  motivation[7] 0/1/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         2/2/2  -> 2.00
  [5] 4 Comparison with comparison rewrites        1/0/1  -> 0.67
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/1/1  -> 0.67
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This solves many long-standing issues around proxy iterators that return by value.
candidate 2 (found by 2 of 33 passes): It is not possible to safely and consistently define `operator``->` for these types, so we do not always do so, but under this proposal they would all do the right thing.
candidate 3 (found by 1 of 33 passes): Much of the complexity around the comparison operators has come from reversed candidates and dealing with potentially multiple arguments.
candidate 4 (found by 1 of 33 passes): However, unlike the comparison operators this change is significantly simpler and less likely to have all the corner cases we’ve seen with `operator==` and `operator<=>`.

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
candidate 2 (found by 2 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have.
candidate 3 (found by 1 of 33 passes): This change tries to follow the lead of the existing rewrite rules we have. However, unlike the comparison operators this change is significantly simpler and less likely to have all the corner cases we’ve seen with `operator==` and `operator<=>`.

## vehicle - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 10 References 7                              0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Design Motivations                         1/1/1  -> 1.00
  [5] 4 Comparison with comparison rewrites        0/0/0  -> 0.00
  [6] 5 Design                                     0/0/0  -> 0.00
  [7] 6 Library impact                             0/0/0  -> 0.00
  [8] 7 Proposed Wording                           0/0/0  -> 0.00
  [9] 8 Feature Test Macro                         0/0/0  -> 0.00
  [10] 9 Acknowledgements                           0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator<=>`), not in terms of function calls.
candidate 2 (found by 1 of 33 passes): This paper was split off from [[P1046R2](https://wg21.link/p1046r2)]. That paper proposed generating many operators, this paper is just the arrow overloads.

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

## insufficiency - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 1 of 33 passes): This neatly sidesteps all of the issues of library-only solutions (how do we get the address of the object? how do we handle temporaries?).
candidate 2 (found by 1 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator``<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs``->``rhs` as being equivalent to `(*``lhs``).``rhs`.
candidate 3 (found by 1 of 33 passes): This paper, however, traffics in rewrite rules (following the lead of `operator<=>`), not in terms of function calls. Because of this, we have one more option that the library-only solutions lack: we define `lhs->rhs` as being equivalent to `(*lhs).rhs`.

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
