Verdict: Strong (9/14)

The paper offers solid support for the core conceptual argument—that guaranteed undefined-behavior checks require a mechanism distinct from ignorable contract assertions—and for the claim that existing proposals and prior art acknowledge this gap. The case is thinnest where it reaches beyond principle into current practice: implementation status, real-world translation-unit mixing, and the insufficiency of library-only approaches are asserted rather than demonstrated with concrete evidence.

- The strongest support is the established logical point that a check which may be compiled away cannot serve as a guarantee against undefined behavior.
- The paper also credibly establishes that prior proposals, including P3846R1 and P3100, recognize guaranteed enforcement as an unmet need outside the current contracts model.
- The most glaring omission is the lack of established evidence about actual compiler implementation status or real-world interoperability failures across mixed-evaluation translation units.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.67   accumulate 10.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 0.83  insufficiency 1.00  implementation 0.67
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 10.00 / 9.00 / 9.50   (all 3 samples: 9.50)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience
splits: prior_art[4] 2/0/2  vehicle[3] 1/0/0  vehicle[11] 1/2/1  coordination[3] 0/1/0
        coordination[6] 2/1/1  insufficiency[2] 0/1/1  insufficiency[7] 1/0/1
        implementation[8] 1/0/1
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
candidate 4 (found by 3 of 36 passes): Undefined behavior mitigation is not asking for optional documentation of intent. It needs checks that are known to be done.

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
  [4] What P3846R1 says about guaranteed enforc... 2/0/2  -> 1.33
  [5] "But that's complementarity, not a failure"  2/2/2  -> 2.00
  [6] "Mixed mode is just the C++ build model; ... 2/2/2  -> 2.00
  [7] "We'll ship a minimal core now and do lab... 2/2/2  -> 2.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          2/2/2  -> 2.00
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   2/2/2  -> 2.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 2 (found by 3 of 36 passes): P3100 proposes to implement runtime checks for core-language undefined behavior as implicit contract assertions, using the same evaluation semantics as P2900.
candidate 3 (found by 3 of 36 passes): P3846R1 says labels are "required" to make non-ignorable checks directly expressible, are "not yet ready to adopt," and have not reached consensus to move forward in any subgroup.
candidate 4 (found by 3 of 36 passes): P3846R1 Concern 17 might reply that P2900 is implemented in two major compilers and that macros have decades of prior art.

## vehicle - grade 2.00 (fired in 9 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               1/0/0  -> 0.33
  [4] What P3846R1 says about guaranteed enforc... 2/2/2  -> 2.00
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 2/2/2  -> 2.00
  [7] "We'll ship a minimal core now and do lab... 1/1/1  -> 1.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   1/2/1  -> 1.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A check for undefined behavior that is not guaranteed to run is not a check.
candidate 2 (found by 3 of 36 passes): A different need is precisely why it must not share the ignorable substrate, not a reason it may.
candidate 3 (found by 3 of 36 passes): It also shows why that mechanism must not be reused for undefined behavior checks that have to be known to be done.
candidate 4 (found by 3 of 36 passes): The need for that repair is itself the point: the model being repaired is the wrong basis for undefined behavior checks, and the repair is not in C++26.

## coordination - grade 0.83 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/1/0  -> 0.33
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 2/1/1  -> 1.33
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     0/0/0  -> 0.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Third-party code, package binaries, and client TUs compiled with `ignore` are normal.
candidate 2 (found by 1 of 36 passes): Translation unit A is built with a checked semantic; translation unit B includes the same header built with `ignore`.

## insufficiency - grade 1.00 (fired in 5 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/1/1  -> 0.67
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 1/1/1  -> 1.00
  [7] "We'll ship a minimal core now and do lab... 1/0/1  -> 0.67
  [8] Not enough usage experience for this use     1/1/1  -> 1.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Telling people to keep writing `if` statements, or to wait for a labels proposal that "has not yet reached consensus in any WG21 subgroup," is admitting that contracts are not the mechanism for checks that must run.
candidate 2 (found by 3 of 36 passes): libc++ experiments that still need Clang-specific attributes to approximate component-level control (as both P3846R1 and P3835R0 note) show the gap; they do not close it.
candidate 3 (found by 2 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 4 (found by 2 of 36 passes): Labels are, in effect, an attempt to make the P2900 model usable for checks that must run.

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
candidate 1 (found by 2 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented

-->
