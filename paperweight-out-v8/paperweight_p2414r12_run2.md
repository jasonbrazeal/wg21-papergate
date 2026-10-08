Verdict: Strong (8/14)

The paper offers solid grounding for why the problem matters and for the existence of prior art and alternatives, but its case thins considerably when it comes to showing who is affected, why the standard is the right venue, why a library cannot suffice, and whether there is meaningful implementation experience. The strongest support is conceptual and historical, while the weakest areas rely on assertion rather than demonstrated evidence.

- The paper clearly establishes that the issue matters by tying it to long-standing usage and the need for `volatile` accesses to tolerate invalid pointers in I/O contexts.
- It also establishes prior art and alternatives through references to earlier proposals and historical algorithms, showing the problem is not new.
- The paper claims but does not establish that large production codebases are affected, that standardization is necessary, or that a library solution would be inadequate.
- The most glaring omission is the lack of established implementation experience, since the paper asserts de facto status quo without demonstrating it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 7 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.67   accumulate 8.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 1.83  vehicle 1.00  coordination 1.50  insufficiency 0.50  implementation 1.00
sample agreement: 83 of 91 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.50 / 8.50 / 8.00   (all 3 samples: 8.17)
headings: h2 12
on threshold: coordination
splits: audience[4] 1/1/0  prior_art[2] 0/1/0  prior_art[3] 0/1/1  prior_art[4] 2/0/2
        prior_art[8] 2/1/1  prior_art[11] 1/1/2  prior_art[13] 2/2/1  implementation[7] 0/0/1
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

## audience - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/0  -> 0.67
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## prior_art - grade 1.83 (fired in 9 of 13 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/1/0  -> 0.33
  [3] Abstract                                     0/1/1  -> 0.67
  [4] Introduction                                 2/0/2  -> 1.33
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     2/1/1  -> 1.33
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             1/1/2  -> 1.33
  [12] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [13] Appendix: Relation to WG21 P2434R4           2/2/1  -> 1.67
candidate 1 (found by 3 of 39 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 2 (found by 3 of 39 passes): this paper notes that the implementation must prove that a given pointer is invalid before taking action based on invalidity.
candidate 3 (found by 3 of 39 passes): Assuming non-deterministic pointer provenance (see P2434R4) and defined load, stores, copies, and assignments (see P3347R3), the required source-code changes are highlighted in yellow:
candidate 4 (found by 3 of 39 passes): In 1986, R. K. Treiber presented an assembly language implementation of the LIFO Push algorithm in technical report RJ 5118 entitled “Systems Programming: Coping with Parallelism” while at the IBM Almaden Research Center.

## vehicle - grade 1.00 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            1/1/1  -> 1.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We therefore need a solution that not only preserves valuable optimizations and debugging tools, but that also works for existing source code.
candidate 2 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 3 (found by 1 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

## coordination - grade 1.50 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            2/2/2  -> 2.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 3 (found by 1 of 39 passes): the OS kernel (written in C or C++) is communicating via memory with device firmware (also written in C or C++).

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

## implementation - grade 1.00  [binary: max] (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/1  -> 0.33
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 1 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

-->
