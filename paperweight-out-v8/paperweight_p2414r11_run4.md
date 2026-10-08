Verdict: Strong (9/14)

The paper offers solid grounding in prior work and interoperability concerns, but its case for standardization rests heavily on assertions about existing practice rather than demonstrated evidence. The thinnest support appears where the paper needs to show that real-world code depends on the behavior in question and that no library-level remedy could suffice.

- The strongest support comes from the paper’s engagement with prior C and C++ efforts and its clear explanation of how the proposal fits alongside related work on pointer provenance and lifetime-end zap.
- The interoperability argument is well developed, particularly the point that device firmware and drivers written in C or C++ must communicate through memory using exactly the kind of pointer operations the paper addresses.
- The paper claims broad production use of these pointer techniques over decades, but it does not substantiate that claim with concrete examples, codebases, or reports.
- The most glaring omission is the lack of established implementation experience or evidence that the proposed semantics reflect what real compilers and systems already do.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 7 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 9.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 1.83  vehicle 1.00  coordination 1.50  insufficiency 0.67  implementation 1.00
sample agreement: 83 of 91 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.50 / 8.50 / 8.50   (all 3 samples: 8.50)
headings: h2 12
on threshold: coordination
splits: motivation[3] 2/1/1  prior_art[3] 0/1/0  prior_art[4] 2/2/1  prior_art[5] 1/2/1
        prior_art[11] 2/1/1  coordination[6] 1/1/0  insufficiency[4] 0/0/1
        implementation[7] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     2/1/1  -> 1.33
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
candidate 2 (found by 3 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 3 (found by 3 of 39 passes): This code is buggy because it is subject to lifetime-end pointer zap:
candidate 4 (found by 1 of 39 passes): this paper also proposes that `volatile` accesses forgive invalidity in order to support passing of virtual addresses to and from I/O devices, which has long been supported in hardware

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

## prior_art - grade 1.83 (fired in 8 of 13 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/1/0  -> 0.33
  [4] Introduction                                 2/2/1  -> 1.67
  [5] Terminology                                  1/2/1  -> 1.33
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     1/1/1  -> 1.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             2/1/1  -> 1.33
  [12] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [13] Appendix: Relation to WG21 P2434R4           1/1/1  -> 1.00
candidate 1 (found by 3 of 39 passes): See WG14 [N2369](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2369.pdf) and [N2443](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2443.pdf) for more details on the C language’s handling of pointers to lifetime-ended objects and WG21 [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf) for the corresponding C++ language details.
candidate 2 (found by 3 of 39 passes): Assuming non-deterministic pointer provenance (see P2434R4) and defined load, stores, copies, and assignments (see P3347R3), the required source-code changes are highlighted in yellow:
candidate 3 (found by 3 of 39 passes): We therefore see N2676 as complementary to and compatible with pointer lifetime-end zap.
candidate 4 (found by 3 of 39 passes): This current paper does not conflict with that paper, but rather builds on top of that paper in order to provide more ergonomic and less user-error-prone ways for the user to avoid pointer zap.

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

## coordination - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/1/0  -> 0.67
  [7] Detailed Proposal                            2/2/2  -> 2.00
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 3 of 39 passes): To see this, keep firmly in mind that the OS kernel (written in C or C++) is communicating via memory with device firmware (also written in C or C++).
candidate 3 (found by 2 of 39 passes): For example, consider a device whose firmware and driver are both written in C++.

## insufficiency - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 0/0/1  -> 0.33
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
candidate 2 (found by 1 of 39 passes): the current standards and working drafts for both C and C++ do not permit reliable loading, storing, casting, or comparison of such pointers.

## implementation - grade 1.00  [binary: max] (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            1/0/1  -> 0.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 2 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

-->
