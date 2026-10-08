Verdict: Excellent (12/14)

The paper offers substantial support for its standardization case in the areas that matter most: it establishes why the question needs a committee answer, who is affected, what the alternatives are, and that the named-guarantee approach has real implementation and deployment experience. The support is thinnest where the paper needs to show that the standard is the right home for this facility and that a library cannot carry the same weight, since those arguments are asserted rather than demonstrated.

- The strongest support is the decade of shipped, production-default experience with the named-guarantee check-set across three vendors, with measured cost.
- The paper also firmly establishes that two active proposals now answer the same configuration question and are already inconsistent in the record.
- The most glaring omission is a demonstrated reason the standard, rather than a library, must own the facility, since the paper only claims this without establishing it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 26. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 12.00   accumulate 12.17   max 13.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 2.00  insufficiency 1.17  implementation 2.00
sample agreement: 110 of 133 section-criterion pairs unanimous (83%)
single-sample totals would have been: 13.00 / 12.00 / 11.50   (all 3 samples: 12.17)
headings: h2 16
on threshold: insufficiency
splits: motivation[3] 1/2/1  motivation[6] 1/2/1  motivation[12] 2/0/0  motivation[15] 2/0/0
        audience[7] 0/0/2  audience[8] 0/0/2  audience[10] 1/0/0  audience[15] 0/0/1
        prior_art[7] 0/0/2  prior_art[8] 2/2/1  prior_art[12] 2/2/0  prior_art[13] 0/2/2
        prior_art[14] 2/0/0  prior_art[17] 0/1/0  vehicle[9] 2/2/0  vehicle[15] 2/0/0
        coordination[5] 0/0/1  coordination[16] 0/2/0  insufficiency[15] 0/0/1
        implementation[3] 1/0/1  implementation[5] 0/1/0  implementation[8] 0/2/2
        implementation[13] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/2/1  -> 1.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 1/2/1  -> 1.33
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/0/0  -> 0.67
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               2/0/0  -> 0.67
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two proposals answer one question - how a program configures the runtime checking of core-language undefined behavior - and, as P3100R8's own Section 7.2 states, if both are kept then one must be specified in terms of the other.
candidate 2 (found by 3 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 3 (found by 3 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years; both proposals' specifications have none; and the C++26 contract runtime the P3100 model builds on has a single opt-in implementation from April 2026.
candidate 4 (found by 3 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production - and a Profiles framework that standardizes named, enforceable guarantees is the same shape as what deploys today.

## audience - grade 2.00 (fired in 7 of 19 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/2  -> 0.67
  [8] 4. The Record at a Glance                    0/0/2  -> 0.67
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/0/0  -> 0.33
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/1  -> 0.33
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.
candidate 2 (found by 3 of 57 passes): Public code search finds no installation of the BDE violation handler outside BDE itself, its forks, and its vendored copies.
candidate 3 (found by 3 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].
candidate 4 (found by 1 of 57 passes): P3100R8's Appendix A enumerates the cases of core-language undefined behavior - 80 cases, 77 of them runtime-checkable [1]

## prior_art - grade 2.00 (fired in 12 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 2/2/2  -> 2.00
  [7] 3. The Criteria and Their Provenance         0/0/2  -> 0.67
  [8] 4. The Record at a Glance                    2/2/1  -> 1.67
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/0  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 0/2/2  -> 1.33
  [14] 9. What Configuration Ownership Costs in ... 2/0/0  -> 0.67
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               0/1/0  -> 0.33
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Under the P3100 model, the implicit-contract-assertion machinery is the base and a profile is a named preset that selects a configuration of it.
candidate 2 (found by 3 of 57 passes): P2900 Contracts is in C++26, and P3100 extends it.
candidate 3 (found by 2 of 57 passes): This paper assembles the public record and measures both candidate owners against criteria already in the committee's record - existing practice, deployment and field experience, systematic coverage of undefined behavior, and freedom from dialects
candidate 4 (found by 2 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.

## vehicle - grade 1.00 (fired in 2 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/0  -> 1.33
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               2/0/0  -> 0.67
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The Profiles framework standardizes named guarantee sets selected per build, a shape its lineage deploys.
candidate 2 (found by 1 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years; both proposals' specifications have none; and the C++26 contract runtime the P3100 model builds on has a single opt-in implementation from April 2026.
candidate 3 (found by 1 of 57 passes): The sanitizer and trap-flag lineage deploys as opt-in, test-time tooling outside its production instances, and those instances fix a handler-free response in the build - terminating where deployed as mitigation

## coordination - grade 2.00 (fired in 6 of 19 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/1  -> 0.33
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/2/0  -> 0.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 2 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 3 (found by 2 of 57 passes): The deployed answer to existing variation is per-binary uniformity. What has no deployed record is the part the P3100 model adds: selection per translation unit and finer, per construct, across five semantics.
candidate 4 (found by 1 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.

## insufficiency - grade 1.17 (fired in 2 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/1  -> 0.33
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Replaceable violation handlers are in fact common in user space, and their record sharpens the scope finding instead of blunting it.
candidate 2 (found by 1 of 57 passes): The sanitizer and trap-flag lineage deploys as opt-in, test-time tooling outside its production instances, and those instances fix a handler-free response in the build

## implementation - grade 2.00  [binary: max] (fired in 10 of 19 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/0/1  -> 0.67
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/1/0  -> 0.33
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         1/1/1  -> 1.00
  [8] 4. The Record at a Glance                    0/2/2  -> 1.33
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/1/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               2/2/2  -> 2.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 3 of 57 passes): GCC's contracts code asks per condition whether the predicate "might throw" and wraps the check in a try-catch expression when it can.
candidate 3 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 4 (found by 3 of 57 passes): the named-guarantee form runs in production across three vendors' libraries with measured cost - on by default in GCC 15 unoptimized builds and Xcode 16, opt-in in others

-->
