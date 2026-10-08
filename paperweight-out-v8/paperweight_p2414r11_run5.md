Verdict: Strong (8/14)

The paper offers a solid foundation for why the problem matters and shows familiarity with the surrounding standardization landscape, but its case thins considerably when it moves from motivation to evidence that existing practice, affected communities, and implementation experience justify standardization. The strongest material concerns the inconsistency between current lifetime rules and long-standing `volatile` usage, while the weakest areas rely on repeated assertions rather than demonstrated need or experience.

- The paper clearly establishes that current pointer invalidation rules conflict with established `volatile` access patterns, especially for I/O and device communication.
- It also establishes awareness of prior work and alternatives, grounding the proposal in an ongoing standardization conversation.
- The paper claims but does not establish that large production codebases and concurrent algorithms are actually affected in ways that standardization would resolve.
- The most glaring omission is the absence of demonstrated implementation experience or evidence that a library solution cannot address the stated need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 7 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.67   accumulate 8.33   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 1.33  insufficiency 0.50  implementation 1.00
sample agreement: 79 of 91 section-criterion pairs unanimous (87%)
single-sample totals would have been: 8.00 / 8.50 / 8.50   (all 3 samples: 8.33)
headings: h2 12
on threshold: coordination
splits: motivation[4] 0/2/0  motivation[12] 0/1/1  motivation[13] 1/0/0  prior_art[2] 1/0/1
        prior_art[4] 1/2/1  prior_art[8] 1/2/1  prior_art[10] 0/1/0  prior_art[11] 1/2/0
        coordination[7] 1/2/2  insufficiency[4] 1/0/0  insufficiency[7] 0/1/1
        implementation[7] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 0/2/0  -> 0.67
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            2/2/2  -> 2.00
  [8] Examples                                     2/2/2  -> 2.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/1/1  -> 0.67
  [13] Appendix: Relation to WG21 P2434R4           1/0/0  -> 0.33
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

## prior_art - grade 2.00 (fired in 10 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   1/0/1  -> 0.67
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 1/2/1  -> 1.33
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Examples                                     1/2/1  -> 1.33
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/1/0  -> 0.33
  [11] The Ancient History of LIFO Push             1/2/0  -> 1.00
  [12] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [13] Appendix: Relation to WG21 P2434R4           2/2/2  -> 2.00
candidate 1 (found by 3 of 39 passes): The C++ standard currently specifies that all pointers to an object become invalid at the end of its lifetime [basic.life].
candidate 2 (found by 3 of 39 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 3 (found by 3 of 39 passes): Those interested in seeing a wider array of historical options are invited to review [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf) and [P2188R1](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2188r1.html).
candidate 4 (found by 3 of 39 passes): Assuming non-deterministic pointer provenance (see P2434R4) and defined load, stores, copies, and assignments (see P3347R3), the required source-code changes are highlighted in yellow:

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
candidate 2 (found by 3 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.

## coordination - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            1/2/2  -> 1.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 2 of 39 passes): To see this, keep firmly in mind that the OS kernel (written in C or C++) is communicating via memory with device firmware (also written in C or C++).
candidate 3 (found by 1 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.

## insufficiency - grade 0.50 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/1/1  -> 0.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Note that `volatile` accesses must necessarily forgive invalidity in order to support passing of virtual addresses to and from I/O devices.
candidate 2 (found by 1 of 39 passes): However, (1) concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## implementation - grade 1.00  [binary: max] (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 3                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            1/1/0  -> 0.67
  [8] Examples                                     0/0/0  -> 0.00
  [9] Wording                                      0/0/0  -> 0.00
  [10] History                                      0/0/0  -> 0.00
  [11] The Ancient History of LIFO Push             0/0/0  -> 0.00
  [12] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [13] Appendix: Relation to WG21 P2434R4           0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 2 of 39 passes): We believe this to be de facto status quo given the current semantics required of `volatile` by real-world device drivers.

-->
