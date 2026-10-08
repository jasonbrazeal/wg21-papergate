Verdict: Strong (9/14)

The paper offers meaningful support in the areas where it can point to concrete implementation experience and a clear account of existing practice, but its case is much thinner when it comes to showing that the problem requires a standard rather than a library or vendor solution, and it does not establish that at all. The weakest parts are the absence of any argument for why a library cannot suffice and the largely asserted, rather than demonstrated, claims about who is affected and how the feature would interoperate with existing standards machinery.

- The strongest support is the implementation experience, with shipping hardened configurations, Apple’s bounds safety and libc++ hardening, and a live prototype all credited as evidence.
- The paper also establishes why the problem matters by showing that no current sanitizer reliably catches all 58 cases and that the proposed shape matches what hardened production setups already ship.
- The prior art and alternatives section is established, including the comparison with P3100 and the C++ Alliance Clang fork’s partial enforcement.
- The most glaring omission is the complete lack of an established case for why a library will not do, leaving the central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 6 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 8.67   accumulate 9.67   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.17  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 106 of 119 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.50 / 10.00 / 8.50   (all 3 samples: 9.17)
headings: h2 16
on threshold: audience
splits: motivation[7] 0/0/1  motivation[10] 1/1/0  audience[11] 0/2/0  prior_art[13] 2/2/1
        prior_art[17] 2/1/0  vehicle[4] 1/1/0  vehicle[6] 1/2/1  coordination[6] 1/0/1
        coordination[9] 0/1/0  coordination[10] 2/0/0  implementation[6] 2/2/1
        implementation[13] 1/1/0  implementation[14] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 17 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. The Guarantee                             1/1/1  -> 1.00
  [6] 3. Activation and Response                   1/1/1  -> 1.00
  [7] 4. How to sever each case from the archit... 0/0/1  -> 0.33
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            1/1/1  -> 1.00
  [10] 7. Deployed Practice                         1/1/0  -> 0.67
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): The form of our solution: named checks, per-build activation, terminating response, is what ships today in hardened production setups.
candidate 2 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 3 (found by 3 of 51 passes): Under the profile, that question does not arise.
candidate 4 (found by 3 of 51 passes): ASan misses stack and global use-after-free. UBSan's vptr check misses non-polymorphic type errors.

## audience - grade 1.33 (fired in 2 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
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
  [11] 8. Potential Concerns                        0/2/0  -> 0.67
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): Google's 0.30% figure [10] measures library-precondition hardening, not core-language type-and-lifetime instrumentation.
candidate 2 (found by 1 of 51 passes): hardening libstdc++ | 2024 GCC 6, | preconditions library | trap ~0.30% diagnostic, | (Google) not separately | hundreds of millions of LoC default at `-O0`
candidate 3 (found by 1 of 51 passes): D4277R0 [6] reports prototype checks on GCC and Clang p3850 branches (38% of subcategories uncovered).

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
  [13] 10. Conclusion                               2/2/1  -> 1.67
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 2/1/0  -> 1.00
candidate 1 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 2 (found by 3 of 51 passes): D4277R0 [6] presents an alternative wording strategy for P3100R8 that may reduce the six-clause count; the count of six applies to P3100R8's primary wording as presented in R8.
candidate 3 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15]
candidate 4 (found by 3 of 51 passes): libc++ authors identify their trap as "precisely the quick-enforce evaluation semantic" of C++26 Contracts. [11]

## vehicle - grade 1.17 (fired in 3 of 17 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/0  -> 0.67
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   1/2/1  -> 1.33
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
candidate 1 (found by 3 of 51 passes): P3608R0 [9] (Dos Reis, Voutilainen, Wakely) proposed this shape for library hardening: "a concrete profile that switches on the standard library hardening, and makes the violations of hardened preconditions just terminate the program, without any additional flexibility for C++26,"
candidate 2 (found by 2 of 51 passes): There is consensus for the undefined behavior enumeration, and not the architecture.
candidate 3 (found by 2 of 51 passes): The scalar initialization precedent happened without implicit contract assertions and without routing through any violation handler.
candidate 4 (found by 1 of 51 passes): The profile adds rules on top via P3589R2 [3].

## coordination - grade 0.67 (fired in 3 of 17 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   1/0/1  -> 0.67
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            0/1/0  -> 0.33
  [10] 7. Deployed Practice                         2/0/0  -> 0.67
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): A deployment can route through the C++26 contract-violation handler as an interop path, but this reintroduces the Contracts dependency the design avoids.
candidate 2 (found by 1 of 51 passes): The ABI boundary for instrumented cases (shadow state, lifetime records) is inherent to the instrumentation, not to the routing.
candidate 3 (found by 1 of 51 passes): libc++ authors identify their trap as "precisely the quick-enforce evaluation semantic" of C++26 Contracts. [11]

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

## implementation - grade 2.00  [binary: max] (fired in 8 of 17 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   2/2/1  -> 1.67
  [7] 4. How to sever each case from the archit... 2/2/2  -> 2.00
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            0/0/0  -> 0.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               1/1/0  -> 0.67
  [14] 11. Disclosure                               1/0/0  -> 0.33
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): The form of our solution: named checks, per-build activation, terminating response, is what ships today in hardened production setups.
candidate 2 (found by 3 of 51 passes): Apple's `-fbounds-safety` and libc++ hardening ship this.
candidate 3 (found by 3 of 51 passes): The prototype (Section 5) demonstrates this case live on Compiler Explorer: https://godbolt.org/z/s5Exo86K6
candidate 4 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15] The prototype is available on Compiler Explorer as "clang (std::core_ub profile - P4317)".

-->
