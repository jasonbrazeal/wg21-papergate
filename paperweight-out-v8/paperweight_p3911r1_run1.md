Verdict: Adequate to Strong (7/14)

The paper offers solid motivation for the problem and identifies a plausible audience, but its case for standardization rests heavily on assertion rather than demonstration. The thinnest parts are the absence of any argument for why a library solution cannot meet the need and the lack of concrete implementation experience beyond a single external codebase.

- The paper clearly establishes why always-enforced contract assertions matter for reliability in mixed-semantics codebases and hardened libraries.
- It identifies affected users through widely used production patterns and ties the work to prior EWG discussion and existing directions.
- The claims about why this belongs in the standard and how it coordinates with other facilities are asserted but not substantiated with evidence or analysis.
- The paper does not address why a library-based mechanism would be insufficient, leaving a central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.33   accumulate 7.67   max 8.67

## SUMMARY
grades: motivation 1.83  audience 1.50  prior_art 1.83  vehicle 0.50  coordination 0.83  insufficiency 0.00  implementation 0.67
sample agreement: 86 of 98 section-criterion pairs unanimous (88%)
single-sample totals would have been: 6.50 / 6.00 / 9.00   (all 3 samples: 7.17)
headings: h3 13   <- NOT h2, check the unit list
on threshold: audience
splits: motivation[9] 1/0/1  motivation[10] 1/1/0  motivation[13] 1/2/2  audience[6] 0/1/0
        prior_art[6] 2/2/0  prior_art[8] 2/2/0  prior_art[9] 2/2/1  vehicle[2] 0/0/1
        vehicle[6] 1/0/1  coordination[6] 0/1/0  coordination[8] 2/0/2  implementation[8] 0/0/2
## END SUMMARY

## motivation - grade 1.83 (fired in 6 of 14 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 1/0/1  -> 0.67
  [10] 5. Design choice 2: What syntax should be... 1/1/0  -> 0.67
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/2/2  -> 1.67
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): limiting C++26 Contracts to enforcement semantics chosen post-definition introduces a usability hazard: programmers may write a contract assertion under an expectation of enforcement that is not guaranteed.
candidate 2 (found by 3 of 42 passes): This paper proposes a pure extension to the C++26 Contracts facility from the post-Kona C++ Working Draft.
candidate 3 (found by 3 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 4 (found by 3 of 42 passes): Limiting always-enforced contract assertions to `pre` conditions would **leave gaps in reliability** because `post` conditions and `contract_assert` could still be ignored if different semantics are chosen separately.

## audience - grade 1.50 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/1/0  -> 0.33
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
candidate 3 (found by 1 of 42 passes): This paper was prompted by the concern raised in RO 2-056 that limiting C++26 Contracts to enforcement semantics chosen post-definition introduces a usability hazard

## prior_art - grade 1.83 (fired in 6 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/0  -> 1.33
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/0  -> 1.33
  [9] 4. Design choice 1: Should "always-enforc... 2/2/1  -> 1.67
  [10] 5. Design choice 2: What syntax should be... 2/2/2  -> 2.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Building on motivation from EWG Kona 2025, this paper proposes a minimal pure extension to the C++26 Contracts facility.
candidate 2 (found by 3 of 42 passes): We have removed options 2, 3, and 4 in accordance with EWG guidance and to increase consensus on the C++26 Contracts feature set.
candidate 3 (found by 2 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 4 (found by 2 of 42 passes): Such mechanisms, commonly named `CHECK`, `VERIFY`, or `ALWAYS_ASSERT` in existing codebases, provide run-time validation of key conditions even in production: they verify the condition and do not continue execution if it does not hold.

## vehicle - grade 0.50 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
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
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): It is purely additive to C++26 Contracts, and pulls forward into C++26 one specific capability from the post-C++26 direction described in P3400 that addresses the current concerns, and does so in a forward-compatible way with P3400.
candidate 2 (found by 1 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and in hardened libraries.

## coordination - grade 0.83 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/1/0  -> 0.33
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/0/2  -> 1.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Many production codebases ship an always-on assertion (separate from `assert`, which is sometimes-on by means of the `NDEBUG` macro).
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

## implementation - grade 0.67  [binary: max] (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] 0. TL;DR                                     0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/2  -> 0.67
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): **Google Abseil**'s [CHECK](https://abseil.io/docs/cpp/guides/logging#CHECK) ("terminates the process" in all builds; paired with debug-only `DCHECK`) is used in a plethora of Google and third-party projects, notably including **Protocol Buffers**, **glog**, **gRPC**, **Chromium**, and **TensorFlow**.

-->
