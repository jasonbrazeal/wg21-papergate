Verdict: Strong (10/14)

The paper offers substantial support for its standardization case in the areas that matter most practically: it demonstrates real implementation experience, identifies affected users with concrete data, and situates itself credibly against prior art and existing sanitizers. The support thins considerably when the paper turns to the standard’s own role, where the arguments for why this belongs in the standard rather than a library, and how it coordinates with existing standardization efforts, remain asserted rather than shown.

- The strongest support is implementation experience, with working prototypes on Compiler Explorer and shipping enforcement in Apple’s toolchain and libc++ hardening.
- The paper also establishes who is affected and why the problem matters, citing concrete gaps in current sanitizers and measurable coverage shortfalls.
- The case for why the standard is the right venue rests on precedent and claimed consensus, but does not yet establish that the proposed shape belongs in the standard itself.
- The most glaring omission is the absence of any established argument for why a library solution will not do, leaving the central standardization question unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 10.33   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.33  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 108 of 119 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.00 / 10.50 / 9.00   (all 3 samples: 9.50)
headings: h2 16
on threshold: audience, vehicle
splits: motivation[6] 1/0/1  motivation[12] 0/1/0  motivation[13] 0/1/1  audience[9] 1/2/0
        audience[11] 0/2/0  prior_art[11] 2/2/0  prior_art[17] 2/0/0  vehicle[6] 1/2/2
        coordination[6] 1/2/1  implementation[2] 1/0/1  implementation[6] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 17 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. The Guarantee                             1/1/1  -> 1.00
  [6] 3. Activation and Response                   1/0/1  -> 0.67
  [7] 4. How to sever each case from the archit... 1/1/1  -> 1.00
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            1/1/1  -> 1.00
  [10] 7. Deployed Practice                         0/0/0  -> 0.00
  [11] 8. Potential Concerns                        0/0/0  -> 0.00
  [12] 9. Questions for the Committee               0/1/0  -> 0.33
  [13] 10. Conclusion                               0/1/1  -> 0.67
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 2 (found by 3 of 51 passes): ASan misses stack and global use-after-free. UBSan's vptr check misses non-polymorphic type errors.
candidate 3 (found by 2 of 51 passes): The form of our solution: named checks, per-build activation, terminating response, is what ships today in hardened production setups.
candidate 4 (found by 2 of 51 passes): There is consensus for the undefined behavior enumeration, and not the architecture.

## audience - grade 1.50 (fired in 3 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   0/0/0  -> 0.00
  [7] 4. How to sever each case from the archit... 0/0/0  -> 0.00
  [8] 5. Prototype                                 0/0/0  -> 0.00
  [9] 6. Checking Tiers and Composition            1/2/0  -> 1.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        0/2/0  -> 0.67
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Google's 0.30% figure [10] measures library-precondition hardening, not core-language type-and-lifetime instrumentation.
candidate 2 (found by 2 of 51 passes): D4277R0 [6] reports 38% of subcategories with no checks on either prototype compiler.
candidate 3 (found by 1 of 51 passes): A prototype covers 7 locally-checkable cases (Section 5), available on Compiler Explorer.

## prior_art - grade 2.00 (fired in 11 of 17 sections, strong in 6)  (SHARED PASSAGE)
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
  [11] 8. Potential Concerns                        2/2/0  -> 1.33
  [12] 9. Questions for the Committee               1/1/1  -> 1.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 2/0/0  -> 0.67
candidate 1 (found by 3 of 51 passes): No current sanitizer catches all 58 reliably; this paper and P3100 face the same instrumentation limits.
candidate 2 (found by 3 of 51 passes): D4277R0 [6] presents an alternative wording strategy for P3100R8 that may reduce the six-clause count; the count of six applies to P3100R8's primary wording as presented in R8.
candidate 3 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15]
candidate 4 (found by 3 of 51 passes): P3100R8 faces identical limits.

## vehicle - grade 1.33 (fired in 3 of 17 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   1/2/2  -> 1.67
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
candidate 2 (found by 3 of 51 passes): The scalar initialization precedent happened without implicit contract assertions and without routing through any violation handler.
candidate 3 (found by 2 of 51 passes): There is consensus for the undefined behavior enumeration, and not the architecture.
candidate 4 (found by 1 of 51 passes): There is consensus for the undefined behavior enumeration, and not the architecture. By separating the two, a profile inherits this consensus without the architecture that rides along with it.

## coordination - grade 0.67 (fired in 1 of 17 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   1/2/1  -> 1.33
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

## implementation - grade 2.00  [binary: max] (fired in 6 of 17 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Guarantee                             0/0/0  -> 0.00
  [6] 3. Activation and Response                   2/1/2  -> 1.67
  [7] 4. How to sever each case from the archit... 2/2/2  -> 2.00
  [8] 5. Prototype                                 2/2/2  -> 2.00
  [9] 6. Checking Tiers and Composition            0/0/0  -> 0.00
  [10] 7. Deployed Practice                         2/2/2  -> 2.00
  [11] 8. Potential Concerns                        2/2/2  -> 2.00
  [12] 9. Questions for the Committee               0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgments                              0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
  [17] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Apple's `-fbounds-safety` and libc++ hardening ship this.
candidate 2 (found by 3 of 51 passes): The prototype (Section 5) demonstrates this case live on Compiler Explorer: https://godbolt.org/z/s5Exo86K6
candidate 3 (found by 3 of 51 passes): The C++ Alliance Clang fork implements `std::core_ub` enforcement for 7 cases across the locally-checkable subset. [15] The prototype is available on Compiler Explorer as "clang (std::core_ub profile - P4317)".
candidate 4 (found by 3 of 51 passes): Section 5 demonstrates the profile's own prototype: 7 locally-checkable cases enforced under `std::core_ub`, with live Compiler Explorer links.

-->
