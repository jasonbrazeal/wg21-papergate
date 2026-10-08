Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing the named-guarantee hardening form it describes, with the strongest evidence coming from its deployment record across eight production systems and the measured cost data from Google’s fleet. The case is thinnest where it argues that a library cannot achieve the same result, since that point rests on a single deployment’s published figure rather than a broader demonstration.

- The paper’s strongest support is the production deployment record across eight systems, including a measured average overhead of 0.30% at Google, which grounds the proposal in what already ships.
- The paper clearly establishes why the standard is the right venue by showing that the profile standardizes a guarantee, an enumeration of guarded operations, and a violation response that the field already runs.
- The paper adequately covers prior art and alternatives by distinguishing its terminating, named-guarantee profile from the earlier P3081R2 design and from standard-library hardening approaches.
- The most glaring omission is the claim that a library will not do, which is asserted but not established beyond a single fleet-scale cost figure.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 21. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 10.33   accumulate 11.83   max 12.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.67  coordination 1.50  insufficiency 0.17  implementation 2.00
sample agreement: 132 of 147 section-criterion pairs unanimous (90%)
single-sample totals would have been: 11.00 / 12.00 / 12.00   (all 3 samples: 11.33)
headings: h2 20
on threshold: vehicle, coordination
splits: motivation[5] 0/1/1  audience[4] 1/0/0  audience[13] 0/2/0  audience[17] 1/1/0
        prior_art[6] 2/0/2  prior_art[14] 0/0/1  vehicle[4] 0/1/1  vehicle[13] 0/2/2
        vehicle[15] 0/0/2  vehicle[17] 1/1/0  coordination[5] 0/1/2  coordination[7] 1/0/0
        insufficiency[13] 0/1/0  implementation[8] 1/2/2  implementation[18] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 21 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Design                                    0/1/1  -> 0.67
  [6] 3. Relationship to P3100R8                   2/2/2  -> 2.00
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/2  -> 2.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The C++ standard specifies a finite, enumerable set of core-language operations whose misuse has undefined behavior, and most of those operations can be checked at run time.
candidate 3 (found by 3 of 63 passes): The need is real and the paper names it well.
candidate 4 (found by 3 of 63 passes): The named-guarantee form (a named set of checks selected per build, with a terminating response) is what production systems ship today.

## audience - grade 2.00 (fired in 5 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/0/0  -> 0.33
  [5] 2. Design                                    0/0/0  -> 0.00
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/0  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/0  -> 0.67
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): Yes. A trap instruction is as low-level as the response gets. Yes. Inactive: zero cost. Active: a trap, one instruction, measured at about 0.30% in production (Section 6).
candidate 2 (found by 2 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 3 (found by 2 of 63 passes): It standardizes the named-guarantee form that ships in production across eight systems today.
candidate 4 (found by 1 of 63 passes): what production hardening ships across eight systems today, with measured cost as low as a third of a percent.

## prior_art - grade 2.00 (fired in 11 of 21 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   2/0/2  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/2  -> 2.00
  [14] 7. The Committee's Recorded Direction        0/0/1  -> 0.33
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     1/1/1  -> 1.00
  [17] 10. Conclusion                               2/2/2  -> 2.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The relationship between the two approaches, and where they differ, is the subject of the companion papers P4297R0 [4] and P4306R0 [2]; this paper does not restate their arguments, and cites them where they apply.
candidate 3 (found by 3 of 63 passes): P3608R0's profile switches on standard-library hardening, while `std::core_ub` applies the same shape to the core-language cases enumerated in Appendix A.
candidate 4 (found by 3 of 63 passes): the profile specified here - a terminating response backed by the deployment record of Section 6 - is a different proposition from the 2025 P3081R2 design those votes addressed.

## vehicle - grade 1.67 (fired in 6 of 21 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/1/1  -> 0.67
  [5] 2. Design                                    0/0/0  -> 0.00
  [6] 3. Relationship to P3100R8                   2/2/2  -> 2.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 0/0/0  -> 0.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/2  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/2  -> 0.67
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/0  -> 0.67
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The profile standardizes the guarantee, the enumeration of what it guards, and the response to a violation.
candidate 3 (found by 2 of 63 passes): The paper assumes one thing, stated plainly: that a safety feature is stronger when it standardizes a form already shipping in production than when it standardizes a form that has not shipped.
candidate 4 (found by 2 of 63 passes): The profile standardizes the form the field already runs; Section 8 draws the scope boundary exactly, including the type-and-lifetime cases not yet a production default anywhere.

## coordination - grade 1.50 (fired in 3 of 21 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    0/1/2  -> 1.00
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 1/0/0  -> 0.33
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 0/0/0  -> 0.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/2  -> 2.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               0/0/0  -> 0.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The one deployment with a published fleet-scale cost figure is Google's. Hardening libc++ across its production services - hundreds of millions of lines of C++ - was measured at an average 0.30% performance overhead
candidate 2 (found by 1 of 63 passes): Interoperation with the C++26 contract-violation handler is possible but is not a peer of the three.
candidate 3 (found by 1 of 63 passes): The boundary between an enforced translation unit and an unenforced one is well defined, and the guarantee degrades gracefully across it.
candidate 4 (found by 1 of 63 passes): The standard `assert` macro fits the same pattern. When `std::core_ub` is enforced and `assert(expr)` fails, the profile's selected response applies and the program ends rather than proceeding.

## insufficiency - grade 0.17 (fired in 1 of 21 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    0/0/0  -> 0.00
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 0/0/0  -> 0.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/1/0  -> 0.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               0/0/0  -> 0.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 1 of 63 passes): The one deployment with a published fleet-scale cost figure is Google's.

## implementation - grade 2.00  [binary: max] (fired in 9 of 21 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    1/1/1  -> 1.00
  [6] 3. Relationship to P3100R8                   1/1/1  -> 1.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 1/2/2  -> 1.67
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/0/0  -> 0.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     1/1/1  -> 1.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               1/2/2  -> 1.67
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Section 6 gives the deployment record.
candidate 3 (found by 3 of 63 passes): Framework implemented in Clang (C++ Alliance, public); the profile's UB checks not yet implemented
candidate 4 (found by 3 of 63 passes): Third, the framework the profile is specified on has a public Clang implementation.

-->
