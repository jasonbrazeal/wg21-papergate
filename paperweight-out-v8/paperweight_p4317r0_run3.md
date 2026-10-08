Verdict: Excellent (12/14)

The paper offers substantial support for standardizing the named-guarantee hardening form it describes, with its strongest grounding in deployment across eight production systems and measured overhead as low as 0.30%. The case is thinnest where it must explain why a library solution cannot carry the same guarantee, since that argument is not established in the text.

- The paper most convincingly ties its proposal to production practice, citing eight shipping systems and a published fleet-scale cost figure from Google’s hardened libc++.
- It clearly establishes the standardization need by showing how the profile standardizes the guarantee, the enumeration of guarded operations, and the violation response without foundational changes to the standard’s definitional machinery.
- It adequately covers coordination and interoperability by explaining that enforced and unenforced translation units link without ODR or ABI hazard and that the guarantee degrades gracefully across boundaries.
- The most glaring omission is the absence of an established argument for why a library cannot provide the same capability, leaving that required justification unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 6 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 22. Replies missing: 0. Sections: 21. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 12.00   accumulate 12.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 129 of 147 section-criterion pairs unanimous (88%)
single-sample totals would have been: 12.00 / 12.00 / 12.00   (all 3 samples: 12.00)
headings: h2 20
on threshold: none
splits: motivation[6] 0/1/1  motivation[8] 2/0/2  motivation[13] 0/2/0  audience[4] 1/0/0
        audience[17] 1/1/0  prior_art[8] 0/2/2  prior_art[13] 0/2/2  prior_art[18] 0/1/1
        prior_art[21] 2/0/0  vehicle[4] 1/0/0  vehicle[5] 1/2/0  vehicle[7] 0/1/2
        coordination[2] 1/0/1  coordination[7] 1/0/0  implementation[6] 1/1/2
        implementation[7] 0/0/1  implementation[13] 0/0/2  implementation[16] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Design                                    1/1/1  -> 1.00
  [6] 3. Relationship to P3100R8                   0/1/1  -> 0.67
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/0/2  -> 1.33
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/0  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
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

## audience - grade 2.00 (fired in 4 of 21 sections, strong in 2)  (SHARED PASSAGE)
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
  [13] form                                         0/0/0  -> 0.00
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        0/0/0  -> 0.00
  [16] 9. Suggested Straw Polls                     0/0/0  -> 0.00
  [17] 10. Conclusion                               1/1/0  -> 0.67
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Standardizes the named-guarantee form shipping in eight production systems (Section 6).
candidate 3 (found by 2 of 63 passes): it standardizes the named-guarantee form that ships in production across eight systems today.
candidate 4 (found by 1 of 63 passes): The paper assumes one thing, stated plainly: that a safety feature is stronger when it standardizes a form already shipping in production than when it standardizes a form that has not shipped. Section 6 gives the deployment record.

## prior_art - grade 2.00 (fired in 12 of 21 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Design                                    2/2/2  -> 2.00
  [6] 3. Relationship to P3100R8                   2/2/2  -> 2.00
  [7] 4. Coexistence with Legacy Assertion Faci... 2/2/2  -> 2.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 0/2/2  -> 1.33
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/2/2  -> 1.33
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     1/1/1  -> 1.00
  [17] 10. Conclusion                               2/2/2  -> 2.00
  [18] 11. Disclosure                               0/1/1  -> 0.67
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 2/0/0  -> 0.67
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): This profile takes that enumeration and specifies it as a profile rather than as an extension of the C++26 Contracts machinery.
candidate 3 (found by 3 of 63 passes): This profile is built on the work of P3100R8.
candidate 4 (found by 3 of 63 passes): Under the Profiles routing the same need is met through the profile's own response rather than the contract-violation handler; what follows is how, and where the profile deliberately stops short.

## vehicle - grade 2.00 (fired in 9 of 21 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/0/0  -> 0.33
  [5] 2. Design                                    1/2/0  -> 1.00
  [6] 3. Relationship to P3100R8                   2/2/2  -> 2.00
  [7] 4. Coexistence with Legacy Assertion Faci... 0/1/2  -> 1.00
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 1/1/1  -> 1.00
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
candidate 2 (found by 3 of 63 passes): The profile standardizes the guarantee, the enumeration of what it guards, and the response to a violation.
candidate 3 (found by 3 of 63 passes): Yes. Standardizes the named-guarantee form shipping in eight production systems (Section 6).
candidate 4 (found by 3 of 63 passes): The profile standardizes the form the field already runs; Section 8 draws the scope boundary exactly, including the type-and-lifetime cases not yet a production default anywhere.

## coordination - grade 2.00 (fired in 4 of 21 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Design                                    2/2/2  -> 2.00
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
candidate 2 (found by 2 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 3 (found by 2 of 63 passes): An enforced translation unit and an unenforced one link and run together with no ODR or ABI hazard.
candidate 4 (found by 1 of 63 passes): The boundary between an enforced translation unit and an unenforced one is well defined, and the guarantee degrades gracefully across it.

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
  [5] 2. Design                                    1/1/1  -> 1.00
  [6] 3. Relationship to P3100R8                   1/1/2  -> 1.33
  [7] 4. Coexistence with Legacy Assertion Faci... 0/0/1  -> 0.33
  [8] 5. SD-10 Section 4.1 Describes a Safe-by-... 2/2/2  -> 2.00
  [9] Implementation Shipped Scope Response Mea... 0/0/0  -> 0.00
  [10] Scale Matches                                0/0/0  -> 0.00
  [11] cost                                         0/0/0  -> 0.00
  [12] profile                                      0/0/0  -> 0.00
  [13] form                                         0/0/2  -> 0.67
  [14] 7. The Committee's Recorded Direction        0/0/0  -> 0.00
  [15] 8. Potential Concerns                        2/2/2  -> 2.00
  [16] 9. Suggested Straw Polls                     1/0/0  -> 0.33
  [17] 10. Conclusion                               1/1/1  -> 1.00
  [18] 11. Disclosure                               0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
  [20] References                                   0/0/0  -> 0.00
  [21] Appendix A: Enumeration of Guarded Operat... 0/0/0  -> 0.00
candidate 1 (found by 3 of 63 passes): The form it standardizes - a named set of checks selected per build, terminating on a violation - is what production hardening ships across eight systems today, with measured cost as low as a third of a percent.
candidate 2 (found by 3 of 63 passes): Section 6 gives the deployment record.
candidate 3 (found by 3 of 63 passes): Framework implemented in Clang (C++ Alliance, public); the profile's UB checks not yet implemented
candidate 4 (found by 3 of 63 passes): the framework the profile is specified on has a public Clang implementation.

-->
