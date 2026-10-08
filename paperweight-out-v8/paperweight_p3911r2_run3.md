Verdict: Adequate to Strong (8/14)

The paper gives a reasonably clear account of why always-enforced contract assertions matter and who would use them, and it situates the proposal within recent committee discussion and prior implementations. The support becomes much thinner when the paper turns to the necessity of standardization itself: the arguments about duplication, library alternatives, and interoperability are asserted rather than demonstrated with concrete evidence or analysis.

- The strongest support is the motivation, which identifies a real reliability gap in C++26 contracts and ties it directly to a national body comment.
- The affected audience is also well grounded, with references to large codebases and hardened libraries that rely on terminating enforcement.
- The discussion of prior art and alternatives is credible, showing awareness of EWG feedback and narrowing the design space to two viable options.
- The most glaring omission is the lack of established evidence that a library solution cannot address the need, since the paper only claims duplication and performance concerns without substantiating them.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 9.00   max 9.67

## SUMMARY
grades: motivation 1.50  audience 1.50  prior_art 2.00  vehicle 1.33  coordination 0.17  insufficiency 0.50  implementation 0.67
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.00 / 9.00 / 7.00   (all 3 samples: 7.67)
headings: h3 13   <- NOT h2, check the unit list
on threshold: motivation, audience, vehicle
splits: motivation[2] 1/0/0  motivation[5] 0/1/0  motivation[10] 1/1/0  prior_art[9] 2/1/2
        vehicle[6] 1/2/2  vehicle[8] 0/1/1  coordination[2] 1/0/0  implementation[8] 1/0/0
        implementation[13] 0/2/0
## END SUMMARY

## motivation - grade 1.50 (fired in 7 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/1/0  -> 0.33
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 1/1/0  -> 0.67
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/1/1  -> 1.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Under the current C++26 model, such invariants cannot be expressed solely as contract assertions, because enforcement may be disabled or weakened by configuration.
candidate 2 (found by 3 of 42 passes): Either option presented in sections §4.1 or §4.2 (see below) would satisfy the Romanian NB’s concern.
candidate 3 (found by 3 of 42 passes): Limiting always-enforced contract assertions to `pre` conditions would **leave gaps in reliability** because `post` conditions and `contract_assert` could still be ignored if different semantics are chosen separately.
candidate 4 (found by 2 of 42 passes): The Romanian NB requests only a narrow extension that allows a contract assertion to be marked as enforced in source code.

## audience - grade 1.50 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): in large-scale, real-world codebases, some contract assertions represent invariants that are sufficiently critical that execution must not continue if they are violated.
candidate 2 (found by 3 of 42 passes): Below, we present a selection of representative, widely used examples that leverage non-continuing (terminating) enforcement semantics in production:
candidate 3 (found by 3 of 42 passes): improves the practical reliability of contract assertions in large codebases and hardened libraries

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        1/1/1  -> 1.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 2/1/2  -> 1.67
  [10] 5. Design choice 2: What syntax should be... 2/2/2  -> 2.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Building on motivation from EWG Kona 2025, this paper proposes a minimal pure extension to the C++26 Contracts facility.
candidate 2 (found by 3 of 42 passes): This paper presents two alternative extensions to the C++26 Contracts facility, either of which is sufficient to address the Romanian NB Comment:
candidate 3 (found by 3 of 42 passes): We have removed options 2, 3, and 4, which EWG deemed as unviable.
candidate 4 (found by 3 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](https://wg21.link/P3835R0) [4], it appears there are three large, partially overlapping groups:

## vehicle - grade 1.33 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              1/2/2  -> 1.67
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/1/1  -> 0.67
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): By enabling a simple source-level choice among `enforce`, `quick-enforce`, or `terminating` semantics, the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 2 (found by 2 of 42 passes): Absent such a facility, users must resort to duplicating logic:
candidate 3 (found by 2 of 42 passes): This design represents a balanced compromise: it preserves configurability while ensuring selected contract assertions are reliably checked.
candidate 4 (found by 1 of 42 passes): Absent such a facility, users must resort to duplicating logic

## coordination - grade 0.17 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
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
candidate 1 (found by 1 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and also in hardened libraries.

## insufficiency - grade 0.50 (fired in 1 of 14 sections, strong in 0)
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
candidate 2 (found by 1 of 42 passes): Because the contract assertions's evaluation semantics are intentionally not observable from source code, performance-conscious developers cannot elide the `if` in `transmogrify` even if the runtime environment is configured to always enforce the contract assertion.

## implementation - grade 0.67  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 1/0/0  -> 0.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/2/0  -> 0.67
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): Existing implementation experience for these proposals is discussed in section §8.14.
candidate 2 (found by 1 of 42 passes): P1429 model was [fully implemented in GCC](https://gcc.gnu.org/onlinedocs/gcc-15.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fcontracts)

-->
