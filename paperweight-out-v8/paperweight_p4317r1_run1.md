Verdict: Strong (10/14)

The paper offers substantial support for its standardization case in the areas that matter most for practical adoption: it demonstrates real implementation experience, identifies the affected users and failure modes clearly, and situates itself against prior art with enough specificity to justify a distinct approach. The support is thinnest where the proposal needs to show that a library solution cannot suffice and that the standard itself—rather than vendor extensions or existing sanitizer infrastructure—is the necessary home for this work.

- The strongest support comes from the implementation experience, including live prototypes on Compiler Explorer and shipping production configurations that already use the named-check, per-build activation, terminating-response shape the paper proposes.
- The paper clearly establishes why the problem matters and who is affected, with concrete examples of compiler optimizations deleting null checks and sanitizer gaps that leave stack and global use-after-free undetected.
- The prior-art discussion is well grounded, particularly in identifying how P3100R8’s bundling of wording with an architecture claim creates the problem this paper seeks to avoid.
- The most glaring omission is the absence of any established argument for why a library cannot provide the same guarantees, leaving a central question about the necessity of standardization unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.33   accumulate 9.67   max 10.33

## SUMMARY
grades: motivation 1.83  audience 2.00  prior_art 2.00  vehicle 0.33  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 108 of 119 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.00 / 10.00 / 9.50   (all 3 samples: 9.50)
headings: h2 16
on threshold: coordination
splits: motivation[4] 1/2/1  motivation[6] 1/2/2  motivation[7] 1/0/1  prior_art[6] 0/2/2
        prior_art[13] 1/2/1  prior_art[17] 2/0/0  vehicle[6] 0/1/0  vehicle[7] 0/1/0
        coordination[9] 1/0/1  implementation[4] 1/0/0  implementation[14] 2/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 7 of 17 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/2/1  -> 1.33
  [5] 2. The Guarantee                             1/1/1  -> 1.00
  [6] 3. Activation and Response                   1/2/2  -> 1.67
  [7] 4. How to sever each case from the archit... 1/0/1  -> 0.67
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            1/1/1  -> 1.00
  [10] 7. Deployed Practice                         0/0/0  -> 0.00
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): The same 77 runtime-checkable cases of core-language undefined behavior, enumerated by Doumler and Berne in P3100R8, are brought together under a single profile with zero foundational wording changes and no handler dependency.
candidate 2 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 3 (found by 3 of 51 passes): A null `this` cannot happen, so at `-O2` the compiler deletes the test. The failure arrives with a compiler upgrade, not a code change.
candidate 4 (found by 3 of 51 passes): ASan misses stack and global use-after-free. UBSan's vptr check misses non-polymorphic type errors.

## audience - grade 2.00 (fired in 2 of 17 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   0/0/0  -> 0.00
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            0/0/0  -> 0.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Google's 0.30% figure [10] measures library-precondition hardening, not core-language type-and-lifetime instrumentation.
candidate 2 (found by 3 of 51 passes): D4277R0 [6] reports prototype checks on GCC and Clang p3850 branches (38% of subcategories uncovered).

## prior_art - grade 2.00 (fired in 12 of 17 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. The Guarantee                             2/2/2  -> 2.00
  [6] 3. Activation and Response                   0/2/2  -> 1.33
  [7] 4. How to sever each case from the archit... 2/2/2  -> 2.00
  [8] 5. Prototype                                 1/1/1  -> 1.00
  [9] 6. Checking Tiers and Composition            2/2/2  -> 2.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               1/1/1  -> 1.00
  [13] 10. Conclusion                               1/2/1  -> 1.33
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 2/0/0  -> 0.67
candidate 1 (found by 3 of 51 passes): P4297R1 [1] identifies the bundling problem with this approach: P3100R8 ties wording for 77 cases to an architecture claim.
candidate 2 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 3 (found by 3 of 51 passes): D4277R0 [6] presents an alternative wording strategy for P3100R8 that may reduce the six-clause count; the count of six applies to P3100R8's primary wording as presented in R8.
candidate 4 (found by 3 of 51 passes): Case identifiers are from P3100R8 Appendix A.

## vehicle - grade 0.33 (fired in 2 of 17 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   0/1/0  -> 0.33
  [7] 4. How to sever each case from the archit... 0/1/0  -> 0.33
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            0/0/0  -> 0.00
  [10] 7. Deployed Practice                         0/0/0  -> 0.00
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 1 of 51 passes): P3608R0 [9] (Dos Reis, Voutilainen, Wakely) proposed this shape for library hardening: "a concrete profile that switches on the standard library hardening, and makes the violations of hardened preconditions just terminate the program, without any additional flexibility for C++26,"
candidate 2 (found by 1 of 51 passes): The scalar initialization precedent happened without implicit contract assertions and without routing through any violation handler.

## coordination - grade 1.33 (fired in 2 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   2/2/2  -> 2.00
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            1/0/1  -> 0.67
  [10] 7. Deployed Practice                         0/0/0  -> 0.00
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): A deployment can route through the C++26 contract-violation handler as an interop path, but this reintroduces the Contracts dependency the design avoids.
candidate 2 (found by 2 of 51 passes): The ABI boundary for instrumented cases (shadow state, lifetime records) is inherent to the instrumentation, not to the routing.

## insufficiency - grade 0.00 (fired in 0 of 17 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   0/0/0  -> 0.00
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            0/0/0  -> 0.00
  [10] 7. Deployed Practice                         0/0/0  -> 0.00
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 8 of 17 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/0/0  -> 0.33
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   2/2/2  -> 2.00
  [7] 4. How to sever each case from the archit... 2/2/2  -> 2.00
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            0/0/0  -> 0.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               2/1/1  -> 1.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): The form of our solution: named checks, per-build activation, terminating response, is what ships today in hardened production setups.
candidate 2 (found by 3 of 51 passes): Apple's `-fbounds-safety` and libc++ hardening ship this.
candidate 3 (found by 3 of 51 passes): The prototype (Section 5) demonstrates this case live on Compiler Explorer: https://godbolt.org/z/s5Exo86K6
candidate 4 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15] The prototype is available on Compiler Explorer as "clang (std::core_ub profile - P4317)".

-->
