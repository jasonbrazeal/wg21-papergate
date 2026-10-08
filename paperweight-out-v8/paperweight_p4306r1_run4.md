Verdict: Strong to Excellent (12/14)

The paper offers substantial support for the existence of a real, deployed problem and for the viability of the general approach it shares with competing work, but its case for why the standard should choose this particular mechanism over the alternative is the thinnest part of the argument. The strongest material concerns field experience and prior art, while the weakest concerns the specific claim that only standardization of this design can resolve the ownership question.

- The paper convincingly shows that runtime checking configuration is a live production concern, with independent deployments at Redpanda, ScyllaDB, Bloomberg, and the Linux kernel, and that the named-guarantee form has a decade of shipped field experience.
- The paper also establishes that the two competing proposals now answer the same question and have already diverged in the record, so coordination and interoperability are genuine standardization concerns rather than hypothetical ones.
- The paper does not establish that the standard must adopt its mechanism rather than the Profiles alternative, since the deployment evidence supports both shapes and the committee’s own criteria do not award ownership to either proposal.
- The paper likewise leaves unestablished why a library solution would not suffice, given that replaceable violation handlers are common in user space and the proposal itself standardizes named presets that resemble existing practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 26. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 12.00   accumulate 12.33   max 12.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 2.00  insufficiency 0.83  implementation 2.00
sample agreement: 108 of 133 section-criterion pairs unanimous (81%)
single-sample totals would have been: 12.50 / 12.50 / 11.00   (all 3 samples: 11.83)
headings: h2 16
on threshold: none
splits: audience[7] 2/0/0  audience[10] 1/0/1  audience[14] 0/1/1  prior_art[7] 0/0/2
        prior_art[12] 0/2/2  prior_art[14] 0/0/2  prior_art[15] 2/0/0  prior_art[16] 0/2/2
        vehicle[3] 0/1/0  vehicle[9] 1/0/0  vehicle[10] 0/1/0  vehicle[12] 0/2/0
        vehicle[15] 1/1/2  coordination[3] 0/0/1  coordination[5] 0/0/1  coordination[11] 0/2/0
        coordination[16] 1/0/1  insufficiency[9] 1/0/0  insufficiency[12] 2/2/0
        implementation[8] 1/0/0  implementation[11] 2/1/0  implementation[13] 2/1/2
        implementation[14] 1/0/0  implementation[15] 1/0/0  implementation[16] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 2/2/2  -> 2.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               2/2/2  -> 2.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two proposals answer one question - how a program configures the runtime checking of core-language undefined behavior - and, as P3100R8's own Section 7.2 states, if both are kept then one must be specified in terms of the other.
candidate 2 (found by 3 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 3 (found by 3 of 57 passes): If we want to have both, we need to specify one in terms of the other to avoid an incoherent and messy design.
candidate 4 (found by 3 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].

## audience - grade 2.00 (fired in 6 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 2/0/0  -> 0.67
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/0/1  -> 0.67
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/1/1  -> 0.67
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].
candidate 2 (found by 2 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.
candidate 3 (found by 2 of 57 passes): Public code search finds no installation of the BDE violation handler outside BDE itself, its forks, and its vendored copies.
candidate 4 (found by 1 of 57 passes): P3100R8's Appendix A enumerates the cases of core-language undefined behavior - 80 cases, 77 of them runtime-checkable [1]

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/2  -> 0.67
  [8] 4. The Record at a Glance                    1/1/1  -> 1.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 0/2/2  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/2  -> 0.67
  [15] 10. Objections                               2/0/0  -> 0.67
  [16] 11. Conclusion                               0/2/2  -> 1.33
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): ScyllaDB selected enforce, the handler-running terminating semantic, and pinned it per assertion through a vendor attribute, "Scylla is always enforced. Always.", foreclosing the per-build menu [63].
candidate 2 (found by 2 of 57 passes): The Profiles papers, P3589R2 and P3984R0, instead make a Profile the named mechanism that selects and defines such guarantees.
candidate 3 (found by 2 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.
candidate 4 (found by 2 of 57 passes): The C++26 contract-violation runtime the P3100 model builds on ([P2900R14] [18]) has one compiler implementation, GCC 16.1 (April 2026), opt-in under GCC's experimental C++26 label [19].

## vehicle - grade 1.00 (fired in 5 of 19 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/1/0  -> 0.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 1/0/0  -> 0.33
  [10] 6. Existing Practice Reads Both Ways         0/1/0  -> 0.33
  [11] 7. The Guarantee Has Different Authors an... 0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 0/2/0  -> 0.67
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               1/1/2  -> 1.33
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The deployment evidence is about the forms, and there the criterion is not neutral
candidate 2 (found by 1 of 57 passes): Measured against the committee's own criteria, no criterion awards ownership of runtime-checking configuration to either proposal.
candidate 3 (found by 1 of 57 passes): The Profiles framework standardizes named guarantee sets selected per build, a shape its lineage deploys.
candidate 4 (found by 1 of 57 passes): The ownership question therefore needs a decision of its own rather than a default - the direction sentence supports both proposals, on different clauses, and only an explicit weighing of the deployment evidence chooses between them.

## coordination - grade 2.00 (fired in 7 of 19 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/1  -> 0.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/1  -> 0.33
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee Has Different Authors an... 0/2/0  -> 0.67
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               1/0/1  -> 0.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 2 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 3 (found by 2 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years.
candidate 4 (found by 2 of 57 passes): On coordination, ownership left unsettled has already cost one companion paper its wording mechanism through independent revision.

## insufficiency - grade 0.83 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 1/0/0  -> 0.33
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee Has Different Authors an... 0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 2/2/0  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): Replaceable violation handlers are in fact common in user space, and their record sharpens the scope finding instead of blunting it.
candidate 2 (found by 1 of 57 passes): The P3100 model standardizes named presets as well - in its model a profile is a named configuration preset (Section 2) - and adds machinery its lineage has not deployed: in-source Labels, the replaceable violation handler, implicit assertions

## implementation - grade 2.00  [binary: max] (fired in 11 of 19 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 1/1/1  -> 1.00
  [8] 4. The Record at a Glance                    1/0/0  -> 0.33
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee Has Different Authors an... 2/1/0  -> 1.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/1/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 1/0/0  -> 0.33
  [15] 10. Objections                               1/0/0  -> 0.33
  [16] 11. Conclusion                               1/2/2  -> 1.67
  [17] 12. Disclosure                               2/2/2  -> 2.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The named-guarantee form is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 3 (found by 3 of 57 passes): ScyllaDB selected enforce, the handler-running terminating semantic, and pinned it per assertion through a vendor attribute, "Scylla is always enforced. Always.", foreclosing the per-build menu [63].
candidate 4 (found by 3 of 57 passes): The Clang implementation is public, with regularly released experimental builds that implement the framework attributes and an initial slice of the `std::init` profile [105]

-->
