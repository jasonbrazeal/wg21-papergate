Verdict: Strong (9/14)

The paper offers solid grounding in prior discussion and implementation experience, but its case for standardization rests heavily on asserted real-world practice rather than demonstrated need. The thinnest support is in the areas where the proposal claims widespread production impact, duplication of logic, and interoperability benefits without concrete evidence.

- The paper clearly establishes that the requested extension has been narrowed to address a specific national body concern and that prior alternatives were already rejected by EWG.
- The paper establishes real implementation experience through the GCC implementation of the P1429 model.
- The paper claims but does not establish that many production codebases ship always-on assertions or that critical invariants are widespread enough to justify standardization.
- The paper claims but does not establish why a library solution is insufficient, relying on a single sentence about duplicated checks without showing actual examples or scale.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 7 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 19. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 8.67   accumulate 9.50   max 11.00

## SUMMARY
grades: motivation 1.83  audience 0.83  prior_art 1.50  vehicle 0.83  coordination 1.33  insufficiency 0.33  implementation 2.00
sample agreement: 88 of 98 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.00 / 8.50 / 9.00   (all 3 samples: 8.67)
headings: h3 13   <- NOT h2, check the unit list
on threshold: prior_art, coordination, implementation
splits: motivation[5] 1/0/0  motivation[7] 1/0/0  motivation[13] 1/2/2  audience[6] 1/0/0
        audience[8] 2/1/1  vehicle[11] 1/0/1  coordination[2] 0/0/1  coordination[6] 0/2/0
        insufficiency[6] 1/0/1  implementation[8] 2/0/2
## END SUMMARY

## motivation - grade 1.83 (fired in 7 of 14 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        1/0/0  -> 0.33
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/0/0  -> 0.33
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 1/1/1  -> 1.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                1/2/2  -> 1.67
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Under the current C++26 model, such invariants cannot be expressed solely as contract assertions, because enforcement may be disabled or weakened by configuration.
candidate 2 (found by 3 of 42 passes): Either option presented in sections §4.1 or §4.2 (see below) would satisfy the Romanian NB’s concern.
candidate 3 (found by 3 of 42 passes): The Romanian NB requests only a narrow extension that allows a contract assertion to be marked as enforced in source code.
candidate 4 (found by 3 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries

## audience - grade 0.83 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              1/0/0  -> 0.33
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/1/1  -> 1.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Many production codebases ship an always-on assertion (separate from `assert`, which is sometimes-on by means of the `NDEBUG` macro).
candidate 2 (found by 1 of 42 passes): in large-scale, real-world codebases, some contract assertions represent invariants that are sufficiently critical that execution must not continue if they are violated.

## prior_art - grade 1.50 (fired in 5 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        1/1/1  -> 1.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): We have removed options 2, 3, and 4, which EWG deemed as unviable.
candidate 2 (found by 3 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](https://wg21.link/P3835R0) [4], it appears there are three large, partially overlapping groups:
candidate 3 (found by 2 of 42 passes): This paper's narrow extension is both necessary and sufficient to address the Romanian NB's concern.
candidate 4 (found by 2 of 42 passes): This paper presents two alternative extensions to the C++26 Contracts facility, either of which is sufficient to address the Romanian NB Comment:

## vehicle - grade 0.83 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
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
  [11] 6. Conclusion                                1/0/1  -> 0.67
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Absent such a facility, users must resort to duplicating logic
candidate 2 (found by 2 of 42 passes): By enabling a simple source-level choice among `enforce`, `quick-enforce`, or `terminating` semantics, the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 3 (found by 1 of 42 passes): This proposal allows authors to state which assumptions are semantic requirements rather than configurable hints.

## coordination - grade 1.33 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              0/2/0  -> 0.67
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Many production codebases ship an always-on assertion (separate from `assert`, which is sometimes-on by means of the `NDEBUG` macro).
candidate 2 (found by 1 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and also in hardened libraries.
candidate 3 (found by 1 of 42 passes): It may also **address other NB concerns**, notably enabling the implementation of the C++26 hardened standard library using C++26 Contracts.

## insufficiency - grade 0.33 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              1/0/1  -> 0.67
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Such code repeats vital checks once as contract assertions for specification and tooling purposes, and again as ordinary control flow to guarantee termination when said requirements are not met.

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
  [8] 3. Proposal: Add source syntax for minima... 2/0/2  -> 1.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                2/2/2  -> 2.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): P1429 model was [fully implemented in GCC](https://gcc.gnu.org/onlinedocs/gcc-15.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fcontracts)
candidate 2 (found by 2 of 42 passes): Existing implementation experience for these proposals is discussed in section §8.14.

-->
