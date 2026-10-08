Verdict: Strong (10/14)

The paper’s strongest support lies in its prior-art and implementation-experience sections, which show that the core idea has been enumerated, prototyped, and shipped in production configurations. Its case is thinnest where it needs to connect those experiences to the specific need for a standard: the affected-population evidence is borrowed from adjacent domains, and the arguments for why the standard—rather than a library or existing tooling—must act are asserted more than demonstrated.

- The paper clearly establishes that the undefined-behavior enumeration and the basic profile shape already exist in prior work and in at least one live implementation.
- It also establishes credible implementation experience through production hardening features and a working prototype on Compiler Explorer.
- The most glaring omission is a direct, quantified account of who is affected by the core-language type-and-lifetime gaps this profile targets, since the cited figures measure something else.
- The paper also leaves the standardization necessity largely asserted, without showing why the same coverage cannot be achieved through existing sanitizer, vendor, or library mechanisms.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.67   accumulate 10.17   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 0.83  coordination 1.00  insufficiency 0.33  implementation 2.00
sample agreement: 107 of 119 section-criterion pairs unanimous (90%)
single-sample totals would have been: 10.00 / 9.50 / 10.00   (all 3 samples: 9.50)
headings: h2 16
on threshold: audience, coordination
splits: motivation[12] 0/1/0  audience[9] 2/0/0  audience[11] 0/0/1  audience[13] 1/0/0
        prior_art[17] 0/0/1  vehicle[4] 1/1/0  vehicle[6] 1/0/1  insufficiency[5] 0/1/1
        implementation[2] 1/1/0  implementation[6] 2/1/2  implementation[9] 1/0/0
        implementation[14] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 17 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. The Guarantee                             1/1/1  -> 1.00
  [6] 3. Activation and Response                   1/1/1  -> 1.00
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            1/1/1  -> 1.00
  [10] 7. Deployed Practice                         0/0/0  -> 0.00
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/1/0  -> 0.33
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): The form of our solution: named checks, per-build activation, terminating response, is what ships today in hardened production setups.
candidate 2 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 3 (found by 3 of 51 passes): ASan misses stack and global use-after-free. UBSan's vptr check misses non-polymorphic type errors.
candidate 4 (found by 2 of 51 passes): There is consensus for the undefined behavior enumeration, and not the architecture. By separating the two, a profile inherits this consensus without the architecture that rides along with it.

## audience - grade 1.33 (fired in 4 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   0/0/0  -> 0.00
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            2/0/0  -> 0.67
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        0/0/1  -> 0.33
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               1/0/0  -> 0.33
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Google's 0.30% figure [10] measures library-precondition hardening, not core-language type-and-lifetime instrumentation.
candidate 2 (found by 1 of 51 passes): D4277R0 [6] reports 38% of subcategories with no checks on either prototype compiler.
candidate 3 (found by 1 of 51 passes): Apple `-fbounds-safety`, Android IntSan/BoundSan, and Chrome CFI check core-language subsets in production.
candidate 4 (found by 1 of 51 passes): `std::core_ub` guards the 77 cases with a single profile under P3589R2 [3].

## prior_art - grade 2.00 (fired in 11 of 17 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. The Guarantee                             2/2/2  -> 2.00
  [6] 3. Activation and Response                   0/0/0  -> 0.00
  [7] 4. How to sever each case from the archit... 2/2/2  -> 2.00
  [8] 5. Prototype                                 1/1/1  -> 1.00
  [9] 6. Checking Tiers and Composition            2/2/2  -> 2.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               1/1/1  -> 1.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/1  -> 0.33
candidate 1 (found by 3 of 51 passes): The same 77 runtime-checkable cases of core-language undefined behavior, enumerated by Doumler and Berne in P3100R8 [2], are brought together under a single profile with zero foundational wording changes and no handler dependency.
candidate 2 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 3 (found by 3 of 51 passes): D4277R0 [6] presents an alternative wording strategy for P3100R8 that may reduce the six-clause count; the count of six applies to P3100R8's primary wording as presented in R8.
candidate 4 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15]

## vehicle - grade 0.83 (fired in 3 of 17 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/0  -> 0.67
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   1/0/1  -> 0.67
  [7] 4. How to sever each case from the archit... 1/1/1  -> 1.00
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
candidate 1 (found by 3 of 51 passes): The scalar initialization precedent happened without implicit contract assertions and without routing through any violation handler.
candidate 2 (found by 2 of 51 passes): There is consensus for the undefined behavior enumeration, and not the architecture.
candidate 3 (found by 1 of 51 passes): P3608R0 [9] (Dos Reis, Voutilainen, Wakely) proposed this shape for library hardening: "a concrete profile that switches on the standard library hardening, and makes the violations of hardened preconditions just terminate the program, without any additional flexibility for C++26,"
candidate 4 (found by 1 of 51 passes): All three candidates provide the check identifier and source location to the response mechanism (crash reporter, diagnostic stream, or handler argument), giving deployment tooling enough to locate the violated constraint.

## coordination - grade 1.00 (fired in 1 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   2/2/2  -> 2.00
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
candidate 1 (found by 3 of 51 passes): A deployment can route through the C++26 contract-violation handler as an interop path, but this reintroduces the Contracts dependency the design avoids.

## insufficiency - grade 0.33 (fired in 1 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/1/1  -> 0.67
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
candidate 1 (found by 2 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.

## implementation - grade 2.00  [binary: max] (fired in 9 of 17 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   2/1/2  -> 1.67
  [7] 4. How to sever each case from the archit... 2/2/2  -> 2.00
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            1/0/0  -> 0.33
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               1/1/1  -> 1.00
  [14] 11. Disclosure                               1/2/2  -> 1.67
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Apple's `-fbounds-safety` and libc++ hardening ship this.
candidate 2 (found by 3 of 51 passes): The prototype (Section 5) demonstrates this case live on Compiler Explorer: https://godbolt.org/z/s5Exo86K6
candidate 3 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15] The prototype is available on Compiler Explorer as "clang (std::core_ub profile - P4317)".
candidate 4 (found by 3 of 51 passes): Section 5 demonstrates the profile's own prototype: 7 locally-checkable cases enforced under `std::core_ub`, with live Compiler Explorer links.

-->
