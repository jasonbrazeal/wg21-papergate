Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of the problem it targets and the population affected, but its case for standardization rests heavily on asserted compatibility and reliability benefits rather than demonstrated necessity or experience. The thinnest parts are the absence of any implementation evidence and the lack of a serious argument for why the capability cannot be supplied outside the standard.

- The strongest support is the concrete usability hazard identified in C++26 Contracts when enforcement semantics are chosen after a contract is written.
- The paper also establishes a clear affected audience in production codebases and hardened libraries that rely on terminating enforcement.
- Its claim that the feature is purely additive and forward-compatible with P3400 is plausible but not backed by enough detail to count as established.
- The most glaring omission is the lack of implementation experience, leaving the proposal without practical validation of its design or costs.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 6.00   accumulate 7.83   max 8.33

## SUMMARY
grades: motivation 1.50  audience 1.50  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.50 / 7.50 / 7.00   (all 3 samples: 7.00)
headings: h3 13   <- NOT h2, check the unit list
on threshold: motivation, audience
splits: motivation[5] 0/1/0  motivation[9] 1/1/0  prior_art[5] 0/0/1  prior_art[10] 2/0/2
        vehicle[2] 1/1/0  coordination[6] 0/2/0  coordination[8] 1/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 7 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/1/0  -> 0.33
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/0  -> 0.67
  [10] 5. Design choice 2: What syntax should be... 1/1/1  -> 1.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/1/1  -> 1.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): limiting C++26 Contracts to enforcement semantics chosen post-definition introduces a usability hazard: programmers may write a contract assertion under an expectation of enforcement that is not guaranteed.
candidate 2 (found by 3 of 42 passes): The Romanian NB requests only a narrow extension that allows a contract assertion to be marked as enforced in source code.
candidate 3 (found by 3 of 42 passes): Limiting always-enforced contract assertions to `pre` conditions would **leave gaps in reliability** because `post` conditions and `contract_assert` could still be ignored if different semantics are chosen separately.
candidate 4 (found by 2 of 42 passes): This paper does not propose additional changes beyond providing a way to spell "always-enforced" contracts assertions in source code, which is enough to satisfy the Romanian NB's concern and which EWG encouraged.

## audience - grade 1.50 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
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
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Below, we present a selection of representative, widely used examples that leverage non-continuing (terminating) enforcement semantics in production:
candidate 2 (found by 3 of 42 passes): improves the practical reliability of contract assertions in large codebases and hardened libraries

## prior_art - grade 2.00 (fired in 7 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/1  -> 0.33
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 2/0/2  -> 1.33
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Building on motivation from EWG Kona 2025, this paper proposes a minimal pure extension to the C++26 Contracts facility.
candidate 2 (found by 3 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 3 (found by 3 of 42 passes): We have removed options 2, 3, and 4 in accordance with EWG guidance and to increase consensus on the C++26 Contracts feature set.
candidate 4 (found by 3 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](http://wg21.link/P3835R0)[4], it appears there are three large, partially overlapping groups:

## vehicle - grade 1.00 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 2 (found by 3 of 42 passes): By enabling a simple source-level choice among `enforce`, `quick-enforce`, or `terminating` semantics, the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 3 (found by 2 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and in hardened libraries.

## coordination - grade 1.00 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/2/0  -> 0.67
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 1/1/2  -> 1.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Many production codebases ship an always-on assertion (separate from `assert`, which is sometimes-on by means of the `NDEBUG` macro).
candidate 2 (found by 1 of 42 passes): It may also **address other NB concerns**, notably enabling the implementation of the C++26 hardened standard library using C++26 Contracts.

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
