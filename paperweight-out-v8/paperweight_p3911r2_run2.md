Verdict: Strong (9/14)

The paper offers solid support for the motivating problem, the affected audience, and the existence of prior art and alternatives, but its case thins considerably when it turns to why standardization is necessary, how the feature interoperates with existing practice, why a library cannot suffice, and whether there is meaningful implementation experience. The strongest material concerns the real-world need for always-enforced contract assertions and the narrowing of design options through committee feedback; the weakest material relies on assertions about duplication, mixed-semantics codebases, and compiler behavior that are stated rather than demonstrated.

- The paper clearly establishes that critical invariants in large codebases and hardened libraries need an always-enforced contract assertion, and that prior committee discussion has narrowed the viable design space.
- The paper identifies a concrete affected population and gives representative production examples of non-continuing enforcement semantics.
- The paper does not establish that the standard is the right venue, since the claimed duplication of logic and reliability gains are asserted without evidence that existing or library-level mechanisms are inadequate.
- The most glaring omission is implementation experience: the only cited implementation is for a different model, and no evidence shows the proposed syntax or semantics have been tried in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 8.33   accumulate 10.33   max 11.00

## SUMMARY
grades: motivation 1.67  audience 1.50  prior_art 2.00  vehicle 1.17  coordination 1.00  insufficiency 0.50  implementation 1.33
sample agreement: 88 of 98 section-criterion pairs unanimous (90%)
single-sample totals would have been: 10.50 / 10.00 / 7.50   (all 3 samples: 9.17)
headings: h3 13   <- NOT h2, check the unit list
on threshold: motivation, audience
splits: motivation[2] 0/1/1  motivation[5] 1/0/1  motivation[13] 2/1/1  prior_art[5] 0/1/0
        vehicle[6] 1/1/2  vehicle[8] 0/2/1  vehicle[11] 1/0/1  coordination[2] 1/0/1
        coordination[8] 2/2/0  implementation[13] 2/2/0
## END SUMMARY

## motivation - grade 1.67 (fired in 7 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        1/0/1  -> 0.67
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 0/0/0  -> 0.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 1/1/1  -> 1.00
  [11] 6. Conclusion                                1/1/1  -> 1.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                2/1/1  -> 1.33
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Under the current C++26 model, such invariants cannot be expressed solely as contract assertions, because enforcement may be disabled or weakened by configuration.
candidate 2 (found by 3 of 42 passes): The Romanian NB requests only a narrow extension that allows a contract assertion to be marked as enforced in source code.
candidate 3 (found by 3 of 42 passes): the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 4 (found by 3 of 42 passes): Limiting always-enforced contract assertions to `pre` conditions would **leave gaps in reliability** because `post` conditions and `contract_assert` could still be ignored if different semantics are chosen separately.

## audience - grade 1.50 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 2 (found by 3 of 42 passes): improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 3 (found by 2 of 42 passes): Many production codebases ship an always-on assertion (separate from `assert`, which is sometimes-on by means of the `NDEBUG` macro).
candidate 4 (found by 1 of 42 passes): Below, we present a selection of representative, widely used examples that leverage non-continuing (terminating) enforcement semantics in production:

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/1/0  -> 0.33
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     1/1/1  -> 1.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/2  -> 2.00
  [9] 4. Design choice 1: Should "always-enforc... 1/1/1  -> 1.00
  [10] 5. Design choice 2: What syntax should be... 2/2/2  -> 2.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): We have removed options 2, 3, and 4, which EWG deemed as unviable.
candidate 2 (found by 3 of 42 passes): During the EWG discussion and on-time papers in Kona, such as [P3835R0](https://wg21.link/P3835R0) [4], it appears there are three large, partially overlapping groups:
candidate 3 (found by 2 of 42 passes): Building on motivation from EWG Kona 2025, this paper proposes a minimal pure extension to the C++26 Contracts facility.
candidate 4 (found by 2 of 42 passes): This option follows the original strawman syntax in R0 of this paper (see [P3911R0](https://wg21.link/P3911R0)).

## vehicle - grade 1.17 (fired in 3 of 14 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/2  -> 1.33
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 0/2/1  -> 1.00
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                1/0/1  -> 0.67
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Absent such a facility, users must resort to duplicating logic
candidate 2 (found by 2 of 42 passes): By enabling a simple source-level choice among `enforce`, `quick-enforce`, or `terminating` semantics, the proposal improves the practical reliability of contract assertions in large codebases and hardened libraries
candidate 3 (found by 1 of 42 passes): Absent such a facility, users must resort to duplicating logic:
candidate 4 (found by 1 of 42 passes): This proposal stipulates that `pre!` is **an enforcement, not an assumption**. An implementation is not permitted, for the purposes of caller-side compilation, to treat violation of an "always-enforced" contract assertion as implying that execution cannot continue past a function call.

## coordination - grade 1.00 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Acknowledgments                              0/0/0  -> 0.00
  [5] TL;DR                                        0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. Scope                                     0/0/0  -> 0.00
  [8] 3. Proposal: Add source syntax for minima... 2/2/0  -> 1.33
  [9] 4. Design choice 1: Should "always-enforc... 0/0/0  -> 0.00
  [10] 5. Design choice 2: What syntax should be... 0/0/0  -> 0.00
  [11] 6. Conclusion                                0/0/0  -> 0.00
  [12] 7. Wording                                   0/0/0  -> 0.00
  [13] 8. Frequently Asked Questions                0/0/0  -> 0.00
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): This addition to the C++26 Contracts facility allows reliable use of enforced contract assertions in large codebases with mixed contract semantics and also in hardened libraries.
candidate 2 (found by 2 of 42 passes): Many production codebases ship an always-on assertion (separate from `assert`, which is sometimes-on by means of the `NDEBUG` macro).

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
candidate 1 (found by 2 of 42 passes): Because the contract assertions's evaluation semantics are intentionally not observable from source code, performance-conscious developers cannot elide the `if` in `transmogrify` even if the runtime environment is configured to always enforce the contract assertion.
candidate 2 (found by 1 of 42 passes): Such code repeats vital checks once as contract assertions for specification and tooling purposes, and again as ordinary control flow to guarantee termination when said requirements are not met.

## implementation - grade 1.33  [binary: max] (fired in 1 of 14 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
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
  [13] 8. Frequently Asked Questions                2/2/0  -> 1.33
  [14] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): P1429 model was [fully implemented in GCC](https://gcc.gnu.org/onlinedocs/gcc-15.1.0/gcc/C_002b_002b-Dialect-Options.html#index-fcontracts)

-->
