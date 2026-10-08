Verdict: Adequate (6/14)

The paper offers a reasonably grounded case for why the feature matters, who would use it, and how it relates to existing directions, but it leaves several parts of the standardization argument more asserted than demonstrated. The thinnest support concerns why a library solution is insufficient and whether the proposed syntax has meaningful implementation experience behind it.

- The strongest support is the clear connection between the proposal and a specific national body concern, with a narrow, additive change that would resolve it.
- The paper also does well in situating the proposal against prior work and ongoing committee directions, making the path to standardization feel deliberate rather than isolated.
- The case for why this belongs in the standard rather than in a library is not established, leaving a central standardization question unanswered.
- The most glaring omission is the lack of demonstrated implementation experience for the proposed facility itself, despite references to similar syntax in other languages.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.00   accumulate 7.17   max 8.00

## SUMMARY
grades: motivation 1.50  audience 1.50  prior_art 2.00  vehicle 0.83  coordination 0.33  insufficiency 0.00  implementation 0.33
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.00 / 7.00 / 6.50   (all 3 samples: 6.50)
headings: h3 13   <- NOT h2, check the unit list
on threshold: motivation, audience
splits: motivation[7] 1/0/1  audience[2] 1/0/0  prior_art[2] 1/1/0  prior_art[5] 0/1/1
        prior_art[9] 2/1/1  vehicle[2] 0/1/1  coordination[6] 1/0/1  implementation[8] 0/1/0
        implementation[10] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 6 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/0/1  -> 0.67
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 1/1/1  -> 1.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/1/1  -> 1.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Either option presented in sections §4.1 or §4.2 (see below) would satisfy the Romanian NB’s concern.
candidate 2 (found by 3 of 42 passes): The Romanian NB requests only a narrow extension that allows a contract assertion to be marked as enforced in source code.
candidate 3 (found by 3 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 4 (found by 3 of 42 passes): Limiting always-enforced contract assertions to `pre` conditions would **leave gaps in reliability** because `post` conditions and `contract_assert` could still be ignored if different semantics are chosen separately.

## audience - grade 1.50 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Below, we present a selection of representative, widely used examples that leverage non-continuing (terminating) enforcement semantics in production:
candidate 2 (found by 2 of 42 passes): improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 3 (found by 1 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and in hardened libraries.
candidate 4 (found by 1 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/1/1  -> 0.67
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 2/1/1  -> 1.33
  [10] 5. Design choice 2: What syntax should be... 2/2/2  -> 2.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 2 (found by 3 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](http://wg21.link/P3835R0)[4], it appears there are three large, partially overlapping groups:
candidate 3 (found by 3 of 42 passes): This option follows the original strawman syntax in R0 of this paper (see [P3911R0](http://wg21.link/P3911R0)).
candidate 4 (found by 2 of 42 passes): Building on motivation from EWG Kona 2025, this paper proposes a minimal pure extension to the C++26 Contracts facility.

## vehicle - grade 0.83 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 2 (found by 2 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and in hardened libraries.

## coordination - grade 0.33 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              1/0/1  -> 0.67
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): It may also **address other NB concerns**, notably enabling the implementation of the C++26 hardened standard library using C++26 Contracts.

## insufficiency - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.33  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/1/0  -> 0.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/1/0  -> 0.33
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): There is a substantial body of existing practice that motivates "always-enforced" contract assertions, demonstrates their utility, and makes the model familiar to users.
candidate 2 (found by 1 of 42 passes): This follows existing use of the `!` suffix to connote the sense of "do not continue execution" (with halt or throw semantics) in other popular languages

-->
