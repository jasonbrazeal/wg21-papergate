Verdict: Excellent (12/14)

The paper offers substantial support for standardizing its proposed profile, with the strongest evidence coming from deployed production systems and measured costs, and with clear reasoning about how the mechanism fits alongside existing Contracts and assertion facilities. The support is thinnest where the paper claims a library alone cannot provide the terminating response, since that point is asserted rather than demonstrated against the specific core-language UB checks being proposed.

- The paper most convincingly establishes that the named-guarantee, terminating-check form is already shipping in eight production systems with measured overhead as low as 0.30%, which grounds the proposal in real implementation experience and prior art.
- It clearly shows why the standard is the right venue by tying the profile to the C++26 Contracts machinery and SD-10 principles, and by demonstrating that enforced and unenforced translation units can interoperate without ODR or ABI hazards.
- The paper adequately explains who is affected and why the feature matters, since it addresses a finite, enumerable set of core-language UB operations and positions the profile relative to existing `assert` and project-specific assertion facilities.
- The most glaring omission is the claim that a library cannot do the job: the paper asserts the terminating response is deployed and measured for the library-hardening tier, but it does not establish why that same response cannot be delivered through a library for the core-language cases in question.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 21. Replies missing: 0. Sections: 21. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 11.33   accumulate 12.17   max 12.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.83  coordination 1.50  insufficiency 0.17  implementation 2.00
sample agreement: 125 of 147 section-criterion pairs unanimous (85%)
single-sample totals would have been: 11.50 / 12.00 / 11.50   (all 3 samples: 11.50)
headings: h2 20
on threshold: coordination
splits: motivation[6] 2/0/2  motivation[8] 2/0/1  motivation[13] 2/2/0  motivation[15] 0/2/2
        audience[13] 0/2/0  audience[15] 0/0/2  prior_art[6] 2/2/0  prior_art[14] 0/1/0
        prior_art[15] 2/0/2  vehicle[2] 1/2/1  vehicle[5] 0/1/1  vehicle[6] 2/1/1
        vehicle[8] 2/2/1  vehicle[13] 0/2/2  coordination[2] 0/1/0  coordination[7] 0/2/1
        coordination[13] 0/2/0  insufficiency[13] 1/0/0  implementation[5] 0/1/0
        implementation[6] 1/1/2  implementation[7] 1/0/0  implementation[13] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    0/0/0  -> 0.00
  [6] 3. Relationship to P3100R8                   2/0/2  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/0/1  -> 1.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/0  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/2/2  -> 1.33
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): The C++ standard specifies a finite, enumerable set of core-language operations whose misuse has undefined behavior, and most of those operations can be checked at run time.
candidate 3 (found by 3 of 63 passes): The standard `assert` macro and the many project-specific assertion facilities deployed across the C++ ecosystem already check preconditions and invariants, and a new mechanism should say how it sits alongside them.
candidate 4 (found by 3 of 63 passes): It provides that coverage with zero foundational changes to the definitional machinery of the standard, where the alternative routing requires six.

## audience - grade 2.00 (fired in 5 of 21 sections, strong in 2)  (SHARED PASSAGE)
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
  [13] form                                         0/2/0  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/2  -> 0.67
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): it standardizes the named-guarantee form that ships in production across eight systems today.
candidate 3 (found by 2 of 63 passes): Standardizes the named-guarantee form shipping in eight production systems (Section 6).
candidate 4 (found by 1 of 63 passes): Active: a trap, one instruction, measured at about 0.30% in production (Section 6).

## prior_art - grade 2.00 (fired in 11 of 21 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   2/2/0  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         2/2/2  -> 2.00
  [14] 7. The Committee's Recorded Direction        0/1/0  -> 0.33
  [15] 8. Potential Concerns                        2/0/2  -> 1.33
  [16] 9. Suggested Straw Polls                     1/1/1  -> 1.00
  [17] 10. Conclusion                               2/2/2  -> 2.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): This profile takes that enumeration and specifies it as a profile rather than as an extension of the C++26 Contracts machinery.
candidate 3 (found by 3 of 63 passes): P3608R0's profile switches on standard-library hardening, while `std::core_ub` applies the same shape to the core-language cases enumerated in Appendix A.
candidate 4 (found by 3 of 63 passes): Under the Profiles routing the same need is met through the profile's own response rather than the contract-violation handler; what follows is how, and where the profile deliberately stops short.

## vehicle - grade 1.83 (fired in 7 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    0/1/1  -> 0.67
  [6] 3. Relationship to P3100R8                   2/1/1  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/0  -> 0.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/1  -> 1.67
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/2  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): It follows every principle in SD-10, and it standardizes the named-guarantee form that ships in production across eight systems today.
candidate 3 (found by 2 of 63 passes): A profile of exactly this shape has been proposed before.
candidate 4 (found by 2 of 63 passes): This profile could not have been specified without it.

## coordination - grade 1.50 (fired in 4 of 21 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   0/0/0  -> 0.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/2/1  -> 1.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 0/0/0  -> 0.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/0  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               0/0/0  -> 0.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): An enforced translation unit and an unenforced one link and run together with no ODR or ABI hazard.
candidate 2 (found by 1 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 3 (found by 1 of 63 passes): a library API that lets legacy macros invoke the C++26 contract-violation handler, and an opt-in macro (`ASSERT_USES_CONTRACTS`) that routes the standard `assert` macro through that handler.
candidate 4 (found by 1 of 63 passes): The standard `assert` macro fits the same pattern.

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
  [13] form                                         1/0/0  -> 0.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               0/0/0  -> 0.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 1 of 63 passes): The terminating response the profile standardizes is thus both deployed and measured for the library-hardening tier, and is the shape the Contracts model already names.

## implementation - grade 2.00  [binary: max] (fired in 10 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    0/1/0  -> 0.33
  [6] 3. Relationship to P3100R8                   1/1/2  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 1/0/0  -> 0.33
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/0  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     1/1/1  -> 1.00
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Section 6 gives the deployment record.
candidate 3 (found by 3 of 63 passes): Framework implemented in Clang (C++ Alliance, public); the profile's UB checks not yet implemented
candidate 4 (found by 3 of 63 passes): Yes. Standardizes the named-guarantee form shipping in eight production systems (Section 6).

-->
