Verdict: Strong (9/14)

The paper offers solid grounding for why the problem matters, what prior work exists, and that the behavior has implementation experience, but it leaves several essential parts of its standardization case asserted rather than demonstrated. The thinnest support is around who is actually affected, why the standard is the right venue, how the change coordinates with existing practice, and why a library solution cannot suffice.

- The strongest support is the paper’s connection to long-standing hardware and device-driver practice, which credibly establishes that the issue matters and has real implementation precedent.
- The discussion of prior art, including Treiber’s 1986 work and the relationship to P2434R4 and N2676, gives a clear technical lineage for the proposal.
- The most glaring omission is the lack of concrete evidence for the claimed decades of production use across large bodies of concurrent and systems code, which underpins several other parts of the case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 10.00   accumulate 9.33   max 10.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 1.17  insufficiency 0.50  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 9.50 / 9.50 / 8.50   (all 3 samples: 9.17)
headings: h2 12
on threshold: implementation
splits: vehicle[6] 0/1/0  coordination[7] 2/2/0  implementation[7] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            2/2/2  -> 2.00
  [8] Examples                                     2/2/2  -> 2.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.
candidate 2 (found by 3 of 39 passes): this paper also proposes that `volatile` accesses forgive invalidity in order to support passing of virtual addresses to and from I/O devices, which has long been supported in hardware
candidate 3 (found by 3 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 4 (found by 3 of 39 passes): This code is buggy because it is subject to lifetime-end pointer zap:

## audience - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     1/1/1  -> 1.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             1/1/1  -> 1.00
  [12] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [13] Appendix: Relation to WG21 P2434R4           2/2/2  -> 2.00
candidate 1 (found by 3 of 39 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 2 (found by 3 of 39 passes): In 1986, R. K. Treiber presented an assembly language implementation of the LIFO Push algorithm in technical report RJ 5118 entitled “Systems Programming: Coping with Parallelism” while at the IBM Almaden Research Center.
candidate 3 (found by 3 of 39 passes): We therefore see N2676 as complementary to and compatible with pointer lifetime-end zap.
candidate 4 (found by 3 of 39 passes): This current paper does not conflict with that paper, but rather builds on top of that paper in order to provide more ergonomic and less user-error-prone ways for the user to avoid pointer zap.

## vehicle - grade 1.00 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/1/0  -> 0.33
  [7] Detailed Proposal                            1/1/1  -> 1.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We therefore need a solution that not only preserves valuable optimizations and debugging tools, but that also works for existing source code.
candidate 2 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 3 (found by 1 of 39 passes): this paper also proposes that `volatile` accesses forgive invalidity in order to support passing of virtual addresses to and from I/O devices, which has long been supported in hardware
candidate 4 (found by 1 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

## coordination - grade 1.17 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            2/2/0  -> 1.33
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 1 of 39 passes): the OS kernel (written in C or C++) is communicating via memory with device firmware (also written in C or C++).
candidate 3 (found by 1 of 39 passes): To see this, keep firmly in mind that the OS kernel (written in C or C++) is communicating via memory with device firmware (also written in C or C++).

## insufficiency - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            1/1/1  -> 1.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.

## implementation - grade 2.00  [binary: max] (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/1/1  -> 0.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             2/2/2  -> 2.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 3 of 39 passes): In 1986, R. K. Treiber presented an assembly language implementation of the LIFO Push algorithm in technical report RJ 5118 entitled “Systems Programming: Coping with Parallelism” while at the IBM Almaden Research Center.
candidate 3 (found by 2 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

-->
