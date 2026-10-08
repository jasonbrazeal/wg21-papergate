Verdict: Adequate (5/14)

The paper offers a solid foundation for why a source-level always-enforce option matters and how it fits with prior committee direction, but it leaves several essential parts of the standardization case largely unargued. The strongest material concerns motivation and alignment with existing proposals, while the thinnest areas are interoperability, implementation experience, and the need for a standard rather than a library solution.

- The paper clearly establishes that users need a way to mark selected contract assertions as always enforced without duplicating logic, and that limiting this to preconditions would leave reliability gaps.
- It also establishes that the design is additive to C++26 Contracts and consistent with the post-C++26 direction described in P3400, with alternatives already removed following EWG guidance.
- The paper only claims, rather than demonstrates, that the affected audience is broad or representative, since the production examples are asserted but not substantiated.
- It offers no established case for coordination and interoperability, why a library cannot address the need, or any implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.67   accumulate 5.67   max 6.67

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 5.00 / 5.00 / 5.50   (all 3 samples: 5.00)
headings: h3 13   <- NOT h2, check the unit list
on threshold: motivation, audience
splits: motivation[2] 0/1/1  motivation[5] 0/0/1  motivation[8] 0/2/0  motivation[9] 0/1/0
        prior_art[6] 0/2/2  prior_art[9] 2/2/1  vehicle[2] 0/0/1  vehicle[6] 1/0/1
        vehicle[11] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 8 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/1  -> 0.33
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/2/0  -> 0.67
  [9] 4. Design choice 1: Should "always-enforc... 0/1/0  -> 0.33
  [10] 5. Design choice 2: What syntax should be... 1/1/1  -> 1.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/1/1  -> 1.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): programmers may write a contract assertion under an expectation of enforcement that is not guaranteed. Users who need "always-enforce" contract assertions are forced to duplicate logic between contract assertions and regular code.
candidate 2 (found by 3 of 42 passes): The Romanian NB requests only a narrow extension that allows a contract assertion to be marked as enforced in source code.
candidate 3 (found by 3 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 4 (found by 3 of 42 passes): Limiting always-enforced contract assertions to `pre` conditions would **leave gaps in reliability** because `post` conditions and `contract_assert` could still be ignored if different semantics are chosen separately.

## audience - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Below, we present a selection of representative, widely used examples that leverage non-continuing (terminating) enforcement semantics in production:

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/2/2  -> 1.33
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 2/2/1  -> 1.67
  [10] 5. Design choice 2: What syntax should be... 2/2/2  -> 2.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): We have removed options 2, 3, and 4 in accordance with EWG guidance and to increase consensus on the C++26 Contracts feature set.
candidate 2 (found by 2 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 3 (found by 2 of 42 passes): This design represents a balanced compromise: it preserves configurability while ensuring selected contract assertions are reliably checked.
candidate 4 (found by 2 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](http://wg21.link/P3835R0)[4], it appears there are three large, partially overlapping groups:

## vehicle - grade 0.50 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              1/0/1  -> 0.67
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/1  -> 0.33
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 2 (found by 1 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and in hardened libraries.
candidate 3 (found by 1 of 42 passes): By enabling a simple source-level choice among `enforce`, `quick-enforce`, or `terminating` semantics, the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries

## coordination - grade 0.00 (fired in 0 of 14 sections, strong in 0)
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

## implementation - grade 0.00  [binary: max] (fired in 0 of 14 sections, strong in 0)
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

-->
