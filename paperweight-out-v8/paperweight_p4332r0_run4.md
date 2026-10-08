Verdict: Strong (10/14)

The paper offers a solid conceptual case that guaranteed enforcement is a distinct need from the P2900 contracts model, and it is most persuasive when explaining why an ignorable check cannot serve as undefined-behavior mitigation. The support becomes much thinner once the argument moves from principle to practice: the affected population, the interoperability hazards, the inadequacy of library-only approaches, and the state of implementation experience are all asserted rather than demonstrated with concrete evidence.

- The strongest support is the paper’s articulation of why a check that can be compiled away cannot answer the need for defined behavior or guaranteed mitigation.
- The paper also credibly establishes that prior work, including P3846R1 and P3100, either concedes the gap or relies on the same ignorable semantics.
- The most glaring omission is the lack of established evidence for the claimed interoperability failures and real-world deployment constraints, which are central to the argument for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 7 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 10.00   accumulate 11.00   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 1.00  insufficiency 1.00  implementation 1.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.00 / 10.00 / 10.00   (all 3 samples: 10.00)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience
splits: prior_art[4] 0/0/2  vehicle[2] 1/2/1  vehicle[3] 2/2/1  vehicle[4] 0/2/2
        vehicle[6] 2/0/1  vehicle[11] 1/0/0  insufficiency[6] 1/0/0  insufficiency[9] 0/0/1
        insufficiency[11] 1/0/0
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
  [4] What P3846R1 says about guaranteed enforc... 0/0/2  -> 0.67
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
candidate 4 (found by 3 of 36 passes): Labels are, in effect, an attempt to make the P2900 model usable for checks that must run.

## vehicle - grade 2.00 (fired in 9 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/2/1  -> 1.33
  [3] UB checks have to actually run               2/2/1  -> 1.67
  [4] What P3846R1 says about guaranteed enforc... 0/2/2  -> 1.33
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 2/0/1  -> 1.00
  [7] "We'll ship a minimal core now and do lab... 1/1/1  -> 1.00
  [8] Not enough usage experience for this use     2/2/2  -> 2.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 2/2/2  -> 2.00
  [11] Conclusion                                   1/0/0  -> 0.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Those properties are fine for optional correctness annotations. They are wrong for undefined behavior mitigation.
candidate 2 (found by 3 of 36 passes): A different need is precisely why it must not share the ignorable substrate, not a reason it may.
candidate 3 (found by 3 of 36 passes): Building language-level UB mitigation on a facility whose deployment model (build-time evaluation semantics; mixed translation units; header / inline / template interactions) still cannot express "this check is known to be done" is premature.
candidate 4 (found by 3 of 36 passes): A mechanism that can only promise “checked, where the build cooperates” answers a different question than the one undefined behavior poses.

## coordination - grade 1.00 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] UB checks have to actually run               1/1/1  -> 1.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  0/0/0  -> 0.00
  [6] "Mixed mode is just the C++ build model; ... 1/1/1  -> 1.00
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     0/0/0  -> 0.00
  [9] A single contract-violation handler          0/0/0  -> 0.00
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Third-party code, package binaries, and client TUs compiled with `ignore` are normal.
candidate 2 (found by 2 of 36 passes): Translation unit A is built with a checked semantic; translation unit B includes the same header built with `ignore`.
candidate 3 (found by 1 of 36 passes): For inline functions and templates in headers, different TUs may disagree on the semantic.

## insufficiency - grade 1.00 (fired in 6 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] UB checks have to actually run               0/0/0  -> 0.00
  [4] What P3846R1 says about guaranteed enforc... 0/0/0  -> 0.00
  [5] "But that's complementarity, not a failure"  1/1/1  -> 1.00
  [6] "Mixed mode is just the C++ build model; ... 1/0/0  -> 0.33
  [7] "We'll ship a minimal core now and do lab... 0/0/0  -> 0.00
  [8] Not enough usage experience for this use     1/1/1  -> 1.00
  [9] A single contract-violation handler          0/0/1  -> 0.33
  [10] "But P3100 only describes semantics; enfo... 0/0/0  -> 0.00
  [11] Conclusion                                   1/0/0  -> 0.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): P3846R1 concedes that guaranteed enforcement is a different need from what P2900 provides, and that a portable in-code guarantee that a check is performed is not available in C++26.
candidate 2 (found by 3 of 36 passes): Telling people to keep writing `if` statements, or to wait for a labels proposal that "has not yet reached consensus in any WG21 subgroup," is admitting that contracts are not the mechanism for checks that must run.
candidate 3 (found by 3 of 36 passes): libc++ experiments that still need Clang-specific attributes to approximate component-level control (as both P3846R1 and P3835R0 note) show the gap; they do not close it.
candidate 4 (found by 1 of 36 passes): If an implicit check for a UB case is compiled as `ignore`, you do not have mitigation.

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
candidate 1 (found by 2 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented, so the deployed experience is with partial, opt-out prototypes of optional assertions
candidate 2 (found by 1 of 36 passes): as of mid-2026, GCC ships contracts only as an experimental option and Clang lists P2900R14 as unimplemented

-->
