Verdict: Strong (9/14)

The paper offers solid grounding for why the problem matters and for its relationship to prior work, but its broader case for standardization rests heavily on assertion rather than demonstrated evidence. The thinnest support appears wherever the paper relies on claims about widespread production use, de facto status quo, or the necessity of a standard-language solution without supplying concrete substantiation.

- The strongest support is the established explanation of why the issue matters, including the conflict with long-standing usage and the need for `volatile` accesses to forgive invalidity for I/O device communication.
- The paper also establishes its prior-art and alternatives context through explicit references to WG14 N2676, P2434R4, P1726R5, and P2188R1.
- The most consistent weakness is the repeated reliance on unestablished claims about decades of production use and de facto status quo, which are asserted rather than demonstrated.
- The most glaring omission is implementation experience, where even the cited Treiber reference describes assembly language rather than C++ implementation, leaving the standardization need empirically unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 7 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 8.83   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.83  vehicle 1.33  coordination 1.00  insufficiency 0.33  implementation 1.33
sample agreement: 77 of 91 section-criterion pairs unanimous (85%)
single-sample totals would have been: 10.00 / 7.50 / 9.50   (all 3 samples: 8.50)
headings: h2 12
on threshold: vehicle
splits: audience[7] 0/0/1  prior_art[3] 1/1/0  prior_art[4] 2/1/2  prior_art[8] 1/2/2
        prior_art[10] 1/0/1  prior_art[11] 2/1/2  prior_art[13] 2/1/2  vehicle[6] 1/0/0
        vehicle[7] 2/1/2  coordination[4] 1/1/0  coordination[7] 2/1/1  insufficiency[7] 1/0/1
        implementation[7] 0/1/0  implementation[11] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 2)  (SHARED PASSAGE)
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
  [12] Appendix: Relationship to WG14 N2676         1/1/1  -> 1.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.
candidate 2 (found by 3 of 39 passes): this paper also proposes that `volatile` accesses forgive invalidity in order to support passing of virtual addresses to and from I/O devices, which has long been supported in hardware
candidate 3 (found by 3 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 4 (found by 3 of 39 passes): This code is buggy because it is subject to lifetime-end pointer zap:

## audience - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
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

## prior_art - grade 1.83 (fired in 10 of 13 sections, strong in 5)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   1/1/1  -> 1.00
  [3] Abstract                                     1/1/0  -> 0.67
  [4] Introduction                                 2/1/2  -> 1.67
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     1/2/2  -> 1.67
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      1/0/1  -> 0.67
  [11] The Ancient History of LIFO Push             2/1/2  -> 1.67
  [12] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [13] Appendix: Relation to WG21 P2434R4           2/1/2  -> 1.67
candidate 1 (found by 3 of 39 passes): Appendix: Relationship to WG14 N2676
candidate 2 (found by 3 of 39 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 3 (found by 3 of 39 passes): Those interested in seeing a wider array of historical options are invited to review [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf) and [P2188R1](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2188r1.html).
candidate 4 (found by 3 of 39 passes): Assuming non-deterministic pointer provenance (see P2434R4) and defined load, stores, copies, and assignments (see P3347R3), the required source-code changes are highlighted in yellow:

## vehicle - grade 1.33 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/0/0  -> 0.33
  [7] Detailed Proposal                            2/1/2  -> 1.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We therefore need a solution that not only preserves valuable optimizations and debugging tools, but that also works for existing source code.
candidate 2 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 3 (found by 1 of 39 passes): this paper proposes a convenience mechanism in which `std::atomic<T*>` and `volatile` have special behavior so that the associated pointer values become prospective
candidate 4 (found by 1 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

## coordination - grade 1.00 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/0  -> 0.67
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            2/1/1  -> 1.33
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 3 (found by 1 of 39 passes): To see this, keep firmly in mind that the OS kernel (written in C or C++) is communicating via memory with device firmware (also written in C or C++).

## insufficiency - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            1/0/1  -> 0.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.

## implementation - grade 1.33  [binary: max] (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/1/0  -> 0.33
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             2/0/2  -> 1.33
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 2 of 39 passes): In 1986, R. K. Treiber presented an assembly language implementation of the LIFO Push algorithm in technical report RJ 5118 entitled “Systems Programming: Coping with Parallelism” while at the IBM Almaden Research Center.
candidate 3 (found by 1 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

-->
