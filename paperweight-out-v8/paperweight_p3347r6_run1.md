Verdict: Adequate (5/14)

The paper gives a partial account of why its topic deserves attention, with the clearest support coming from the existing standard’s lifetime rules and the related proposals it cites. The argument becomes much thinner when it turns to who is actually affected, how the feature would fit with other work, and why a library solution is insufficient. Most notably, the paper does not establish why standardization is the right venue or offer any implementation experience.

- The strongest support is the paper’s identification of the current standard’s pointer-invalidation rule as the source of the problem it wants to address.
- The discussion of prior art and alternatives is also grounded, since it points to specific related proposals and positions the work as complementary to them.
- The claims about affected users and interoperability are asserted rather than demonstrated with concrete examples or evidence.
- The most glaring omission is the absence of any case for why this belongs in the standard rather than in a library, along with no implementation experience to support feasibility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 5 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 5.33   accumulate 4.67   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.17  implementation 0.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 4.50 / 4.50 / 5.00   (all 3 samples: 4.67)
headings: h2 7
on threshold: none
splits: audience[4] 1/0/1  prior_art[6] 1/0/1  coordination[7] 0/0/1  insufficiency[3] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Background                                   0/0/0  -> 0.00
  [5] What We Are Asking For                       2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The C++ standard currently specifies that all pointers to an object become invalid at the end of its lifetime [basic.life]. This is a software-engineering nightmare because **all** operations on invalid pointers are implementation-defined, even loads and stores.
candidate 2 (found by 3 of 24 passes): Given the current standard, the above code is buggy because it is subject to lifetime-end pointer zap.

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   1/0/1  -> 0.67
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.

## prior_art - grade 2.00 (fired in 6 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Background                                   2/2/2  -> 2.00
  [5] What We Are Asking For                       2/2/2  -> 2.00
  [6] Wording                                      1/0/1  -> 0.67
  [7] Appendix: Relationship to WG14 N2676         2/2/2  -> 2.00
  [8] Appendix: Relation to WG21 P2434R2           1/1/1  -> 1.00
candidate 1 (found by 3 of 24 passes): The C++ standard currently specifies that all pointers to an object become invalid at the end of its lifetime [basic.life].
candidate 2 (found by 3 of 24 passes): Additional proposals for other aspects of the pointer-zap problem are in P2414R9 (“Pointer lifetime-end zap proposed solutions: atomics and volatile”) and P3790R1 (“Pointer lifetime-end zap proposed solutions: bag-of-bits pointer class”).
candidate 3 (found by 3 of 24 passes): We therefore see N2676 as complementary to and compatible with pointer lifetime-end zap.
candidate 4 (found by 3 of 24 passes): This current paper does not conflict with that paper, but rather builds on top of that paper in order to provide more ergonomics for users.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/1  -> 0.33
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): We therefore see N2676 as complementary to and compatible with pointer lifetime-end zap.

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/1/0  -> 0.33
  [4] Background                                   0/0/0  -> 0.00
  [5] What We Are Asking For                       0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Appendix: Relationship to WG14 N2676         0/0/0  -> 0.00
  [8] Appendix: Relation to WG21 P2434R2           0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): This requirement can cause `uintptr_t` to spread throughout unrelated portions of a program using algorithms such as LIFO Push, which is but one example of the aforementioned software-engineering nightmare.

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
