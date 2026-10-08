Verdict: Strong (9/14)

The paper makes a clear and well-supported case that guaranteed enforcement of undefined behavior checks is a distinct need that the existing contracts mechanism cannot satisfy, and it effectively shows why neither the standard library nor current compiler implementations close that gap. The support is thinnest where the paper relies on claims about real-world usage and implementation status without providing the evidence needed to establish who is affected or what implementation experience actually exists.

- The strongest support is the paper’s demonstration that a check which may be compiled away cannot serve as undefined behavior mitigation, and that P2900’s semantics are therefore unsuitable for this purpose.
- The paper also convincingly establishes that prior art and alternatives, including P2900 itself and library-based approaches, do not provide a portable in-code guarantee that a check will run.
- The weakest established element is the claim about who is affected, since the paper asserts that third-party code and client translation units compiled with `ignore` are normal but does not substantiate that prevalence.
- The most glaring omission is implementation experience, where the paper cites compiler status but offers no evidence of actual deployment or use of the proposed mechanism.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.00   accumulate 9.67   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 0.33  insufficiency 1.50  implementation 0.33
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 8.50 / 10.00   (all 3 samples: 9.17)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience, insufficiency
splits: motivation[11] 2/1/2  prior_art[4] 2/0/0  prior_art[6] 0/2/2  vehicle[3] 2/1/1
        vehicle[9] 1/0/1  coordination[6] 1/0/1  insufficiency[7] 1/0/0  insufficiency[11] 0/1/0
        implementation[8] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 12 sections, strong in 10)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] UB checks have to actually run               2/2/2  -> 2.00
  [4] What P3846R1 says about guaranteed enforc... 2/2/2  -> 2.00
  [5] "But that's complementarity, not a failure"  2/2/2  -> 2.00
  [6] "Mixed mode is just the C++ build model; ... 2/2/2  -> 2.00
  [7] "We'll ship a minimal core now and do lab... 2/2/2  -> 2.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          2/2/2  -> 2.00
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   2/1/2  -> 1.67
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A check for undefined behavior that is not guaranteed to run is not a check.
candidate 2 (found by 3 of 36 passes): A UB check that can be compiled away is not a substitute for defined behavior or for a check that you know will run.
candidate 3 (found by 3 of 36 passes): A central concern is that P2900 provides no method to guarantee *in code* that a particular assertion, or all assertions in a given ‘component of a program’, will always be checked.
candidate 4 (found by 3 of 36 passes): If the check does not run, the undefined behavior remains.

## audience - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 0/0/0  -> 0.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented

## prior_art - grade 2.00 (fired in 10 of 12 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] UB checks have to actually run               2/2/2  -> 2.00
  [4] What P3846R1 says about guaranteed enforc... 2/0/0  -> 0.67
  [5] "But that's complementarity, not a failure"  2/2/2  -> 2.00
  [6] "Mixed mode is just the C++ build model; ... 0/2/2  -> 1.33
  [7] "We'll ship a minimal core now and do lab... 2/2/2  -> 2.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          2/2/2  -> 2.00
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   2/2/2  -> 2.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 2 (found by 3 of 36 passes): As specified in P2900, the evaluation semantic is chosen outside the source.
candidate 3 (found by 3 of 36 passes): P3100 proposes to implement runtime checks for core-language undefined behavior as implicit contract assertions, using the same evaluation semantics as P2900.
candidate 4 (found by 3 of 36 passes): P3846R1 Concern 17 might reply that P2900 is implemented in two major compilers and that macros have decades of prior art.

## vehicle - grade 2.00 (fired in 10 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               2/1/1  -> 1.33
  [4] What P3846R1 says about guaranteed enforc... 2/2/2  -> 2.00
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 2/2/2  -> 2.00
  [7] "We'll ship a minimal core now and do lab... 1/1/1  -> 1.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          1/0/1  -> 0.67
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   1/1/1  -> 1.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A check for undefined behavior that is not guaranteed to run is not a check.
candidate 2 (found by 3 of 36 passes): Those properties are fine for optional correctness annotations. They are wrong for undefined behavior mitigation.
candidate 3 (found by 3 of 36 passes): A different need is precisely why it must not share the ignorable substrate, not a reason it may.
candidate 4 (found by 3 of 36 passes): It also shows why that mechanism must not be reused for undefined behavior checks that have to be known to be done.

## coordination - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 1/0/1  -> 0.67
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     0/0/0  -> 0.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Third-party code, package binaries, and client TUs compiled with `ignore` are normal.

## insufficiency - grade 1.50 (fired in 7 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               2/2/2  -> 2.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 1/1/1  -> 1.00
  [7] "We'll ship a minimal core now and do lab... 1/0/0  -> 0.33
  [8] Not enough usage experience for this use     1/1/1  -> 1.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/1/0  -> 0.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 2 (found by 3 of 36 passes): Telling people to keep writing `if` statements, or to wait for a labels proposal that "has not yet reached consensus in any WG21 subgroup," is admitting that contracts are not the mechanism for checks that must run.
candidate 3 (found by 3 of 36 passes): C `assert` was never proposed as the standard mechanism for redefining or checking core-language undefined behavior.
candidate 4 (found by 3 of 36 passes): libc++ experiments that still need Clang-specific attributes to approximate component-level control (as both P3846R1 and P3835R0 note) show the gap; they do not close it.

## implementation - grade 0.33  [binary: max] (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 0/0/0  -> 0.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     0/0/1  -> 0.33
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented

-->
