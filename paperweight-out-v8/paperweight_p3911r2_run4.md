Verdict: Adequate to Strong (8/14)

The paper offers a reasonably grounded case in its opening motivation and in its evidence of prior implementation, but the argument thins considerably when it turns to who is actually affected and why the feature must be in the standard rather than supplied by ordinary code or a library. The strongest material concerns the problem’s relevance and the existence of working prior art, while the weakest areas are interoperability and any concrete demonstration of affected users.

- The paper clearly establishes why reliable enforcement matters for large codebases and hardened libraries under the current C++26 contracts model.
- It also provides credible prior art and implementation experience, including the fully implemented P1429 model in GCC.
- The claim that representative, widely used examples depend on terminating enforcement is asserted but not backed by concrete evidence.
- The most glaring omission is any treatment of coordination and interoperability, which the paper does not address at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 8.50   max 10.33

## SUMMARY
grades: motivation 1.67  audience 1.00  prior_art 1.67  vehicle 0.83  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 87 of 98 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.00 / 7.00 / 8.00   (all 3 samples: 7.67)
headings: h3 13   <- NOT h2, check the unit list
on threshold: motivation, audience, prior_art, implementation
splits: motivation[5] 0/1/1  motivation[7] 1/0/1  motivation[10] 0/0/1  motivation[13] 1/1/2
        prior_art[6] 0/0/2  prior_art[9] 1/1/2  prior_art[10] 0/0/2  vehicle[6] 2/1/1
        vehicle[8] 1/0/0  vehicle[11] 1/0/0  implementation[8] 2/0/0
## END SUMMARY

## motivation - grade 1.67 (fired in 8 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/1/1  -> 0.67
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/0/1  -> 0.67
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 0/0/1  -> 0.33
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/1/2  -> 1.33
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and also in hardened libraries.
candidate 2 (found by 3 of 42 passes): Under the current C++26 model, such invariants cannot be expressed solely as contract assertions, because enforcement may be disabled or weakened by configuration.
candidate 3 (found by 3 of 42 passes): Either option presented in sections §4.1 or §4.2 (see below) would satisfy the Romanian NB’s concern.
candidate 4 (found by 3 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries

## audience - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
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

## prior_art - grade 1.67 (fired in 6 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/2  -> 0.67
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/2  -> 1.33
  [10] 5. Design choice 2: What syntax should be... 0/0/2  -> 0.67
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Building on motivation from EWG Kona 2025, this paper proposes a minimal pure extension to the C++26 Contracts facility.
candidate 2 (found by 3 of 42 passes): We have removed options 2, 3, and 4, which EWG deemed as unviable.
candidate 3 (found by 2 of 42 passes): This design represents a balanced compromise: it preserves configurability while ensuring selected contract assertions are reliably checked.
candidate 4 (found by 2 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](https://wg21.link/P3835R0) [4], it appears there are three large, partially overlapping groups:

## vehicle - grade 0.83 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              2/1/1  -> 1.33
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 1/0/0  -> 0.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                1/0/0  -> 0.33
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Absent such a facility, users must resort to duplicating logic
candidate 2 (found by 1 of 42 passes): Absent such a facility, users must resort to duplicating logic:
candidate 3 (found by 1 of 42 passes): This design represents a balanced compromise: it preserves configurability while ensuring selected contract assertions are reliably checked.
candidate 4 (found by 1 of 42 passes): By enabling a simple source-level choice among `enforce`, `quick-enforce`, or `terminating` semantics, the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries

## coordination - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
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

## insufficiency - grade 0.50 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Such code repeats vital checks once as contract assertions for specification and tooling purposes, and again as ordinary control flow to guarantee termination when said requirements are not met.
candidate 2 (found by 1 of 42 passes): Absent such a facility, users must resort to duplicating logic

## implementation - grade 2.00  [binary: max] (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/0/0  -> 0.67
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                2/2/2  -> 2.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): P1429 model was [fully implemented in GCC](https://gcc.gnu.org/onlinedocs/gcc-15.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fcontracts)
candidate 2 (found by 1 of 42 passes): Existing implementation experience for these proposals is discussed in section §8.14.

-->
