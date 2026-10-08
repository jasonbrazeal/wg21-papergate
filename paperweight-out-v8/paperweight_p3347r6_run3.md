Verdict: Adequate (5/14)

The paper offers a solid foundation for why the pointer lifetime-end problem deserves attention and how this work relates to adjacent proposals, but it leaves several essential parts of the standardization case largely unargued. The strongest material concerns motivation and positioning within the existing proposal landscape, while the thinnest concerns practical evidence and the necessity of a standard-language solution rather than a library facility.

- The paper clearly establishes why the current rules create a serious problem and how the proposal fits alongside related efforts on pointer lifetime-end zap.
- It identifies the affected audience only in general terms, without showing who specifically depends on the behavior or how widespread that dependence is.
- The argument for standardization itself rests on a single example of implementation freedom rather than a broader demonstration that the standard is the right place to act.
- The paper does not establish implementation experience, interoperability considerations, or why a library approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 4 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 5.33   accumulate 4.67   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 4.50 / 4.50 / 5.00   (all 3 samples: 4.67)
headings: h2 7
on threshold: none
splits: motivation[4] 2/2/0  motivation[7] 1/0/0  prior_art[3] 1/0/0  prior_art[8] 1/1/2
        vehicle[4] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Background                                   2/2/0  -> 1.33
  [5] What We Are Asking For                       2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         1/0/0  -> 0.33
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The C++ standard currently specifies that all pointers to an object become invalid at the end of its lifetime [basic.life]. This is a software-engineering nightmare because **all** operations on invalid pointers are implementation-defined, even loads and stores.
candidate 2 (found by 3 of 24 passes): Given the current standard, the above code is buggy because it is subject to lifetime-end pointer zap.
candidate 3 (found by 2 of 24 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.
candidate 4 (found by 1 of 24 passes): This technical specification puts forward a number of potential models of pointer provenance, most notably PNVI-ae-udi.

## audience - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.

## prior_art - grade 2.00 (fired in 5 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/0/0  -> 0.33
  [4] Background                                   2/2/2  -> 2.00
  [5] What We Are Asking For                       2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [8] Appendix: Relation to WG21 P2434R2           1/1/2  -> 1.33
candidate 1 (found by 3 of 24 passes): Additional proposals for other aspects of the pointer-zap problem are in P2414R9 (“Pointer lifetime-end zap proposed solutions: atomics and volatile”) and P3790R1 (“Pointer lifetime-end zap proposed solutions: bag-of-bits pointer class”).
candidate 2 (found by 3 of 24 passes): We therefore see N2676 as complementary to and compatible with pointer lifetime-end zap.
candidate 3 (found by 3 of 24 passes): This current paper does not conflict with that paper, but rather builds on top of that paper in order to provide more ergonomics for users.
candidate 4 (found by 2 of 24 passes): This paper assumes that this paper is adopted, and builds on the additional ergonomics described in that paper by defining loads and stores on invalid and prospective pointers, as is required in order for certain concurrent algorithms.

## vehicle - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   0/0/1  -> 0.33
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): This means that an implementation is permitted to (for example) return a random number from a load of an invalid pointer.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidates: (none validated)

-->
