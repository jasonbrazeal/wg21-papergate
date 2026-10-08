Verdict: Excellent (12/14)

The paper offers substantial support for standardizing the named-guarantee hardening form, with its strongest evidence coming from production deployment across multiple systems and measured cost data. The support is thinnest where the paper needs to show that a library mechanism cannot deliver the same guarantees, since that argument is asserted rather than developed.

- The paper establishes that the proposed form is already shipping in production across eight systems, with fleet-scale measurements showing roughly 0.30% overhead and meaningful defect reduction.
- The paper clearly situates the proposal against prior art, including the standard assert macro, profile-based hardening, and continuation-based contract handlers.
- The paper defines the boundary between enforced and unenforced translation units and explains how the guarantee degrades across it.
- The paper does not establish why a library facility would be insufficient, leaving the core justification for standardization incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 19. Replies missing: 0. Sections: 21. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 12.00   accumulate 11.83   max 12.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.83  coordination 2.00  insufficiency 0.17  implementation 1.67
sample agreement: 126 of 147 section-criterion pairs unanimous (86%)
single-sample totals would have been: 12.50 / 12.00 / 12.00   (all 3 samples: 11.67)
headings: h2 20
on threshold: none
splits: motivation[5] 1/2/1  motivation[6] 1/2/2  motivation[13] 2/2/0  motivation[17] 1/0/1
        audience[4] 1/0/0  audience[13] 0/2/2  prior_art[6] 2/0/0  prior_art[14] 1/0/0
        prior_art[17] 1/2/2  prior_art[21] 2/0/2  vehicle[2] 2/1/2  vehicle[4] 1/0/1
        vehicle[5] 1/0/0  vehicle[13] 1/2/1  coordination[2] 1/0/1  coordination[7] 2/2/0
        insufficiency[17] 1/0/0  implementation[5] 2/1/2  implementation[8] 2/2/1
        implementation[15] 0/2/2  implementation[16] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 21 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    1/2/1  -> 1.33
  [6] 3. Relationship to P3100R8                   1/2/2  -> 1.67
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/0  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/0/1  -> 0.67
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The C++ standard specifies a finite, enumerable set of core-language operations whose misuse has undefined behavior, and most of those operations can be checked at run time.
candidate 3 (found by 3 of 63 passes): The standard `assert` macro and the many project-specific assertion facilities deployed across the C++ ecosystem already check preconditions and invariants, and a new mechanism should say how it sits alongside them.
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
  [13] form                                         0/2/2  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Yes. A trap instruction is as low-level as the response gets. Yes. Inactive: zero cost. Active: a trap, one instruction, measured at about 0.30% in production (Section 6).
candidate 3 (found by 3 of 63 passes): It standardizes the named-guarantee form that ships in production across eight systems today.
candidate 4 (found by 2 of 63 passes): Hardening libc++ across its production services - hundreds of millions of lines of C++ - was measured at an average 0.30% performance overhead, cut the baseline fleet segmentation-fault rate by roughly 30%, and surfaced more than 1,000 bugs during rollout

## prior_art - grade 2.00 (fired in 13 of 21 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   2/0/0  -> 0.67
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/2  -> 2.00
  [14] 7. The Committee's Recorded Direction        1/0/0  -> 0.33
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     1/1/1  -> 1.00
  [17] 10. Conclusion                               1/2/2  -> 1.67
  [18] 11. Disclosure                               1/1/1  -> 1.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 2/0/2  -> 1.33
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The relationship between the two approaches, and where they differ, is the subject of the companion papers P4297R0 [4] and P4306R0 [2]; this paper does not restate their arguments, and cites them where they apply.
candidate 3 (found by 3 of 63 passes): P3608R0's profile switches on standard-library hardening, while `std::core_ub` applies the same shape to the core-language cases enumerated in Appendix A.
candidate 4 (found by 3 of 63 passes): P3290R4 offers `handle_observed_contract_violation()`, which continues after the handler returns; the profile stops instead.

## vehicle - grade 1.83 (fired in 6 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/2  -> 1.67
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
  [13] form                                         1/2/1  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The profile standardizes the guarantee, the enumeration of what it guards, and the response to a violation.
candidate 3 (found by 3 of 63 passes): The profile standardizes the form the field already runs; Section 8 draws the scope boundary exactly, including the type-and-lifetime cases not yet a production default anywhere.
candidate 4 (found by 3 of 63 passes): It follows every principle in SD-10, and it standardizes the named-guarantee form that ships in production across eight systems today.

## coordination - grade 2.00 (fired in 4 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/0  -> 1.33
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
candidate 1 (found by 3 of 63 passes): The boundary between an enforced translation unit and an unenforced one is well defined, and the guarantee degrades gracefully across it.
candidate 2 (found by 2 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 3 (found by 2 of 63 passes): The standard `assert` macro and the many project-specific assertion facilities deployed across the C++ ecosystem already check preconditions and invariants, and a new mechanism should say how it sits alongside them.
candidate 4 (found by 2 of 63 passes): The one deployment with a published fleet-scale cost figure is Google's. Hardening libc++ across its production services - hundreds of millions of lines of C++ - was measured at an average 0.30% performance overhead

## insufficiency - grade 0.17 (fired in 1 of 21 sections, strong in 0)  (SHARED PASSAGE)
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
  [13] form                                         0/0/0  -> 0.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/0/0  -> 0.33
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 1 of 63 passes): It standardizes the named-guarantee form that ships in production across eight systems today.

## implementation - grade 1.67  [binary: max] (fired in 8 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    2/1/2  -> 1.67
  [6] 3. Relationship to P3100R8                   1/1/1  -> 1.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/1  -> 1.67
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/0/0  -> 0.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/2/2  -> 1.33
  [16] 9. Suggested Straw Polls                     1/0/0  -> 0.33
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Section 6 gives the deployment record.
candidate 3 (found by 3 of 63 passes): Framework implemented in Clang (C++ Alliance, public); the profile's UB checks not yet implemented
candidate 4 (found by 3 of 63 passes): it standardizes the named-guarantee form that ships in production across eight systems today.

-->
