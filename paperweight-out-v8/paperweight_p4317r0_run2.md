Verdict: Excellent (12/14)

The paper offers substantial support for most of the standardization case, particularly in showing that the proposed form is already deployed and measurable in production, but it leaves one essential question unanswered: why this cannot be delivered as a library rather than as a core-language or standard-mandated mechanism. The thinnest part of the argument is therefore not the existence of the problem or the viability of the approach, but the necessity of standardization itself.

- The strongest support is the deployment record across eight production systems, with a published fleet-scale cost figure of about 0.30% overhead.
- The paper also clearly establishes what the feature standardizes, who it affects, and how it coordinates with existing mechanisms like `assert` and Profiles.
- The most glaring omission is the absence of any established argument for why a library cannot provide the same guarantees, leaving the core rationale for standardization incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 21. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 11.00   accumulate 12.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 124 of 147 section-criterion pairs unanimous (84%)
single-sample totals would have been: 12.00 / 12.00 / 11.50   (all 3 samples: 11.67)
headings: h2 20
on threshold: coordination
splits: motivation[4] 2/1/2  motivation[6] 2/1/1  motivation[8] 1/2/2  motivation[13] 2/0/2
        audience[13] 2/0/0  prior_art[2] 1/2/1  prior_art[6] 2/0/2  prior_art[15] 0/2/2
        prior_art[16] 1/1/2  prior_art[17] 2/2/1  prior_art[18] 1/0/1  prior_art[21] 0/2/1
        vehicle[4] 1/0/1  vehicle[5] 1/0/0  vehicle[17] 0/1/1  coordination[2] 1/0/1
        coordination[5] 2/2/0  coordination[7] 2/0/0  implementation[5] 2/1/2
        implementation[6] 1/2/1  implementation[13] 2/0/2  implementation[16] 0/0/1
        implementation[18] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 21 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/1/2  -> 1.67
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   2/1/1  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 1/2/2  -> 1.67
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/0/2  -> 1.33
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
candidate 3 (found by 3 of 63 passes): When `std::core_ub` is enforced over a region of code, no core-language operation in that region has undefined behavior at run time.
candidate 4 (found by 3 of 63 passes): The standard `assert` macro and the many project-specific assertion facilities deployed across the C++ ecosystem already check preconditions and invariants, and a new mechanism should say how it sits alongside them.

## audience - grade 2.00 (fired in 4 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    0/0/0  -> 0.00
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/0/0  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): Yes. A trap instruction is as low-level as the response gets. Yes. Inactive: zero cost. Active: a trap, one instruction, measured at about 0.30% in production (Section 6).
candidate 2 (found by 2 of 63 passes): what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 3 (found by 2 of 63 passes): It standardizes the named-guarantee form that ships in production across eight systems today.
candidate 4 (found by 1 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.

## prior_art - grade 2.00 (fired in 12 of 21 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
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
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/2/2  -> 1.33
  [16] 9. Suggested Straw Polls                     1/1/2  -> 1.33
  [17] 10. Conclusion                               2/2/1  -> 1.67
  [18] 11. Disclosure                               1/0/1  -> 0.67
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/2/1  -> 1.00
candidate 1 (found by 3 of 63 passes): The relationship between the two approaches, and where they differ, is the subject of the companion papers P4297R0 [4] and P4306R0 [2]; this paper does not restate their arguments, and cites them where they apply.
candidate 2 (found by 3 of 63 passes): P3608R0's profile switches on standard-library hardening, while `std::core_ub` applies the same shape to the core-language cases enumerated in Appendix A.
candidate 3 (found by 3 of 63 passes): Under the Profiles routing the same need is met through the profile's own response rather than the contract-violation handler; what follows is how, and where the profile deliberately stops short.
candidate 4 (found by 3 of 63 passes): P3100R8 answers yes to three, all on its non-throwing configurations - no lower-level construct below (3.3), zero-overhead (3.4), and manual control (3.5), where its quick-enforce semantic is itself a trap - and no to the other nine.

## vehicle - grade 2.00 (fired in 7 of 21 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/0/1  -> 0.67
  [5] 2. Design                                    1/0/0  -> 0.33
  [6] 3. Relationship to P3100R8                   2/2/2  -> 2.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 0/0/0  -> 0.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/2  -> 2.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               0/1/1  -> 0.67
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The profile standardizes the guarantee, the enumeration of what it guards, and the response to a violation.
candidate 3 (found by 3 of 63 passes): The profile standardizes the form the field already runs; Section 8 draws the scope boundary exactly, including the type-and-lifetime cases not yet a production default anywhere.
candidate 4 (found by 2 of 63 passes): The paper assumes one thing, stated plainly: that a safety feature is stronger when it standardizes a form already shipping in production than when it standardizes a form that has not shipped.

## coordination - grade 1.67 (fired in 4 of 21 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    2/2/0  -> 1.33
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 2/0/0  -> 0.67
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
candidate 1 (found by 2 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 2 of 63 passes): The boundary between an enforced translation unit and an unenforced one is well defined, and the guarantee degrades gracefully across it.
candidate 3 (found by 2 of 63 passes): The one deployment with a published fleet-scale cost figure is Google's. Hardening libc++ across its production services - hundreds of millions of lines of C++ - was measured at an average 0.30% performance overhead
candidate 4 (found by 1 of 63 passes): The standard `assert` macro fits the same pattern. When `std::core_ub` is enforced and `assert(expr)` fails, the profile's selected response applies and the program ends rather than proceeding.

## insufficiency - grade 0.00 (fired in 0 of 21 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
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
  [13] form                                         0/0/0  -> 0.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               0/0/0  -> 0.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 10 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    2/1/2  -> 1.67
  [6] 3. Relationship to P3100R8                   1/2/1  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 1/1/1  -> 1.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/0/2  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     0/0/1  -> 0.33
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               1/0/1  -> 0.67
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Section 6 gives the deployment record.
candidate 3 (found by 3 of 63 passes): Framework implemented in Clang (C++ Alliance, public); the profile's UB checks not yet implemented
candidate 4 (found by 3 of 63 passes): Third, the framework the profile is specified on has a public Clang implementation.

-->
