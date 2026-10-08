Verdict: Strong to Excellent (10/14)

The paper makes a clear and well-supported case that guaranteed enforcement of undefined behavior checks is a distinct need that the current contracts model cannot express, and it grounds that argument in the specification’s own limitations and the absence of a portable in-code guarantee. The support is thinnest where the paper reaches beyond conceptual necessity into claims about current implementation status and the insufficiency of library-only approaches, which are asserted rather than demonstrated.

- The strongest support is the paper’s demonstration that P2900’s evaluation semantics are chosen outside the source and therefore cannot guarantee that a check will run, which directly undermines any use of contracts for UB mitigation.
- The paper also establishes that this is a standardization problem rather than a mere design preference by showing how mixed translation units and third-party binaries make optional checks unreliable for undefined behavior.
- The most glaring omission is the lack of established evidence for the claim that a library cannot address the need, since the paper leans on concessions and assertions about labels rather than showing why existing or proposed library mechanisms fail.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.33/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.33   corroborated 9.67   accumulate 11.50   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 1.50  insufficiency 1.17  implementation 0.67
sample agreement: 70 of 84 section-criterion pairs unanimous (83%)
single-sample totals would have been: 10.50 / 9.50 / 11.50   (all 3 samples: 10.33)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience, coordination
splits: prior_art[4] 2/2/0  vehicle[5] 1/0/1  vehicle[6] 1/1/2  vehicle[7] 2/1/1
        vehicle[9] 0/0/1  coordination[3] 1/2/2  coordination[4] 2/0/0  coordination[6] 1/1/2
        insufficiency[3] 1/1/2  insufficiency[5] 0/1/1  insufficiency[6] 1/0/1
        insufficiency[7] 1/0/1  insufficiency[11] 1/0/0  implementation[8] 1/0/1
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
  [11] Conclusion                                   2/2/2  -> 2.00
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

## prior_art - grade 2.00 (fired in 10 of 12 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] UB checks have to actually run               2/2/2  -> 2.00
  [4] What P3846R1 says about guaranteed enforc... 2/2/0  -> 1.33
  [5] "But that's complementarity, not a failure"  2/2/2  -> 2.00
  [6] "Mixed mode is just the C++ build model; ... 2/2/2  -> 2.00
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

## vehicle - grade 2.00 (fired in 10 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               1/1/1  -> 1.00
  [4] What P3846R1 says about guaranteed enforc... 2/2/2  -> 2.00
  [5] "But that's complementarity, not a failure"  1/0/1  -> 0.67
  [6] "Mixed mode is just the C++ build model; ... 1/1/2  -> 1.33
  [7] "We'll ship a minimal core now and do lab... 2/1/1  -> 1.33
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          0/0/1  -> 0.33
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   1/1/1  -> 1.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A check for undefined behavior that is not guaranteed to run is not a check.
candidate 2 (found by 3 of 36 passes): Those properties are fine for optional correctness annotations. They are wrong for undefined behavior mitigation.
candidate 3 (found by 3 of 36 passes): It also shows why that mechanism must not be reused for undefined behavior checks that have to be known to be done.
candidate 4 (found by 3 of 36 passes): Building language-level UB mitigation on a facility whose deployment model (build-time evaluation semantics; mixed translation units; header / inline / template interactions) still cannot express "this check is known to be done" is premature.

## coordination - grade 1.50 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               1/2/2  -> 1.67
  [4] What P3846R1 says about guaranteed enforc... 2/0/0  -> 0.67
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 1/1/2  -> 1.33
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     0/0/0  -> 0.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Translation unit A is built with a checked semantic; translation unit B includes the same header built with `ignore`.
candidate 2 (found by 3 of 36 passes): Third-party code, package binaries, and client TUs compiled with `ignore` are normal.
candidate 3 (found by 1 of 36 passes): P2900 provides no method to guarantee *in code* that a particular assertion, or all assertions in a given ‘component of a program’, will always be checked.

## insufficiency - grade 1.17 (fired in 6 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               1/1/2  -> 1.33
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/1/1  -> 0.67
  [6] "Mixed mode is just the C++ build model; ... 1/0/1  -> 0.67
  [7] "We'll ship a minimal core now and do lab... 1/0/1  -> 0.67
  [8] Not enough usage experience for this use     0/0/0  -> 0.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   1/0/0  -> 0.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 2 (found by 2 of 36 passes): Telling people to keep writing `if` statements, or to wait for a labels proposal that "has not yet reached consensus in any WG21 subgroup," is admitting that contracts are not the mechanism for checks that must run.
candidate 3 (found by 2 of 36 passes): Labels are, in effect, an attempt to make the P2900 model usable for checks that must run.
candidate 4 (found by 1 of 36 passes): A contract assertion, as specified in P2900, is optional with respect to the meaning of a correct program.

## implementation - grade 0.67  [binary: max] (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 0/0/0  -> 0.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     1/0/1  -> 0.67
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented
candidate 2 (found by 1 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented, so the deployed experience is with partial, opt-out prototypes of optional assertions

-->
