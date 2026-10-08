Verdict: Strong (10/14)

The paper offers solid support for its central claim that optional contract assertions are the wrong vehicle for undefined behavior mitigation, and it grounds that argument well in the concessions and unresolved questions of the existing contracts work. The case is thinnest where it moves from conceptual necessity to practical evidence: the affected audience, the interoperability failure modes, the inadequacy of library alternatives, and the state of implementation experience are asserted rather than demonstrated with concrete data or reproducible examples.

- The strongest support is the paper’s use of P3846R1’s own admissions that guaranteed enforcement is a distinct need and that portable in-code guarantees are unavailable in C++26.
- The paper also establishes clearly why the standard is the right venue by showing that undefined behavior checks cannot be specified as ordinary optional contracts without losing their defining property.
- The most glaring omission is the lack of established evidence about who is actually affected and what implementation experience exists, since the only support offered is a pair of status claims about GCC and Clang.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 10.00   accumulate 10.83   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.83  coordination 1.17  insufficiency 1.00  implementation 1.00
sample agreement: 70 of 84 section-criterion pairs unanimous (83%)
single-sample totals would have been: 10.50 / 10.00 / 10.00   (all 3 samples: 9.83)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience
splits: audience[8] 2/2/1  prior_art[4] 2/0/0  vehicle[2] 2/1/1  vehicle[3] 1/1/2
        vehicle[4] 2/0/2  vehicle[5] 1/1/0  vehicle[6] 2/2/1  vehicle[9] 0/1/0
        vehicle[10] 2/0/0  coordination[3] 2/0/2  coordination[4] 1/1/0  coordination[5] 1/0/0
        insufficiency[7] 0/1/0  insufficiency[8] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 12 sections, strong in 10)
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

## audience - grade 0.83 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 0/0/0  -> 0.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     2/2/1  -> 1.67
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
  [4] What P3846R1 says about guaranteed enforc... 2/0/0  -> 0.67
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
candidate 3 (found by 3 of 36 passes): P3846R1 says that requiring uniform semantics across an entire program would result in a feature "unusable at scale," and that requiring linker QoI for mixed mode would "greatly hinder adoption."
candidate 4 (found by 3 of 36 passes): P3846R1 says labels are "required" to make non-ignorable checks directly expressible, are "not yet ready to adopt," and have not reached consensus to move forward in any subgroup.

## vehicle - grade 1.83 (fired in 10 of 12 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/1/1  -> 1.33
  [3] UB checks have to actually run               1/1/2  -> 1.33
  [4] What P3846R1 says about guaranteed enforc... 2/0/2  -> 1.33
  [5] "But that's complementarity, not a failure"  1/1/0  -> 0.67
  [6] "Mixed mode is just the C++ build model; ... 2/2/1  -> 1.67
  [7] "We'll ship a minimal core now and do lab... 1/1/1  -> 1.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          0/1/0  -> 0.33
  [10] "But P3100 only describes semantics; enfo... 2/0/0  -> 0.67
  [11] Conclusion                                   1/1/1  -> 1.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Those properties are fine for optional correctness annotations. They are wrong for undefined behavior mitigation.
candidate 2 (found by 3 of 36 passes): It also shows why that mechanism must not be reused for undefined behavior checks that have to be known to be done.
candidate 3 (found by 3 of 36 passes): Undefined behavior checks cannot wait on an unfinished follow-on while being specified as if they were ordinary contracts.
candidate 4 (found by 3 of 36 passes): Building language-level UB mitigation on a facility whose deployment model (build-time evaluation semantics; mixed translation units; header / inline / template interactions) still cannot express "this check is known to be done" is premature.

## coordination - grade 1.17 (fired in 4 of 12 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               2/0/2  -> 1.33
  [4] What P3846R1 says about guaranteed enforc... 1/1/0  -> 0.67
  [5] "But that's complementarity, not a failure"  1/0/0  -> 0.33
  [6] "Mixed mode is just the C++ build model; ... 1/1/1  -> 1.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     0/0/0  -> 0.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Third-party code, package binaries, and client TUs compiled with `ignore` are normal.
candidate 2 (found by 2 of 36 passes): Standardising contract assertions doesn’t hinder the continued use of this approach.
candidate 3 (found by 1 of 36 passes): An inline function in a header carries an implicit UB check. Translation unit A is built with a checked semantic; translation unit B includes the same header built with `ignore`.
candidate 4 (found by 1 of 36 passes): Translation unit A is built with a checked semantic; translation unit B includes the same header built with `ignore`. The program links.

## insufficiency - grade 1.00 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 0/0/0  -> 0.00
  [7] "We'll ship a minimal core now and do lab... 0/1/0  -> 0.33
  [8] Not enough usage experience for this use     0/0/1  -> 0.33
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): A contract assertion, as specified in P2900, is optional with respect to the meaning of a correct program.
candidate 2 (found by 2 of 36 passes): Telling people to keep writing `if` statements, or to wait for a labels proposal that "has not yet reached consensus in any WG21 subgroup," is admitting that contracts are not the mechanism for checks that must run.
candidate 3 (found by 1 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 4 (found by 1 of 36 passes): A check that is "there" in the source can still be compiled as `ignore` in another translation unit.

## implementation - grade 1.00  [binary: max] (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 0/0/0  -> 0.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     1/1/1  -> 1.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented

-->
