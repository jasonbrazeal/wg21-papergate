Verdict: Strong (10/14)

The paper offers substantial support for its standardization case in the areas that matter most: the problem is real, the affected population is concrete and measurable, and the named-guarantee approach has a decade of shipped production experience behind it. The case is thinnest where it needs to explain why a library solution cannot carry the design, and the paper also leaves the standard-setting rationale more asserted than demonstrated.

- The strongest support is the deployment record: the named-guarantee form runs in production across three vendors with measured cost, including a documented binary-size issue and its mitigation.
- The paper also establishes coordination and interoperability clearly, showing that two active proposals now answer the same question and that adoption of both would require specifying one in terms of the other.
- The most glaring omission is the absence of any established argument for why a library will not do, leaving the central question of standardization necessity unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.33/14, close to Excellent)

Provisionally addressed: 6 of 7. Provisional points: 10.33 of 14. Unsupported quotes rejected: 35. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.33   corroborated 10.67   accumulate 10.33   max 10.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.33  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 117 of 133 section-criterion pairs unanimous (88%)
single-sample totals would have been: 10.00 / 10.00 / 11.00   (all 3 samples: 10.33)
headings: h2 16
on threshold: none
splits: audience[7] 2/2/0  audience[15] 0/2/0  audience[16] 2/0/2  prior_art[8] 2/1/2
        prior_art[12] 0/2/0  prior_art[14] 0/2/0  vehicle[12] 0/0/2  coordination[3] 1/1/2
        coordination[5] 1/0/1  coordination[9] 2/2/0  coordination[11] 0/2/0
        coordination[13] 0/2/0  coordination[16] 0/2/0  implementation[8] 0/0/2
        implementation[16] 1/2/2  implementation[17] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 1/1/1  -> 1.00
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
candidate 3 (found by 3 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years.
candidate 4 (found by 3 of 57 passes): The deployed answer to existing variation is per-binary uniformity. What has no deployed record is the part the P3100 model adds: selection per translation unit and finer, per construct, across five semantics.

## audience - grade 2.00 (fired in 7 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 2/2/0  -> 1.33
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/2/0  -> 0.67
  [16] 11. Conclusion                               2/0/2  -> 1.33
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The named-guarantee form is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 3 of 57 passes): The deployment report behind that constraint records a two percent binary-size increase from the verbose failure path as a blocker in certain environments, reduced below half a percent by the trap [34].
candidate 3 (found by 2 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.
candidate 4 (found by 2 of 57 passes): the named-guarantee form runs in production across three vendors' libraries with measured cost - on by default in GCC 15 unoptimized builds and Xcode 16, opt-in in others

## prior_art - grade 2.00 (fired in 9 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    2/1/2  -> 1.67
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 0/2/0  -> 0.67
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/2/0  -> 0.67
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.
candidate 2 (found by 3 of 57 passes): The named-guarantee form is the shipping practice - a decade of it, across three vendors, measured in production - and a Profiles framework that standardizes named, enforceable guarantees is the same shape as what deploys today.
candidate 3 (found by 2 of 57 passes): The Profiles papers, P3589R2 and P3984R0, instead make a Profile the named mechanism that selects and defines such guarantees.
candidate 4 (found by 2 of 57 passes): The C++26 contract-violation runtime the P3100 model builds on ([P2900R14]) has one compiler implementation, GCC 16.1 (April 2026), opt-in under GCC's experimental C++26 label [19].

## vehicle - grade 0.33 (fired in 1 of 19 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee Has Different Authors an... 0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 0/0/2  -> 0.67
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The deployed record is per-facility handlers under application ownership.

## coordination - grade 2.00 (fired in 8 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/2  -> 1.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/0/1  -> 0.67
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/0  -> 1.33
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee Has Different Authors an... 0/2/0  -> 0.67
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/2/0  -> 0.67
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/2/0  -> 0.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Both mechanisms can affect the same check and, as P3100R8's own Section 7.2 states, if both are adopted, one must be specified in terms of the other.
candidate 2 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 3 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 4 (found by 2 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.

## insufficiency - grade 0.00 (fired in 0 of 19 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee Has Different Authors an... 0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 1/1/1  -> 1.00
  [8] 4. The Record at a Glance                    0/0/2  -> 0.67
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               1/2/2  -> 1.67
  [17] 12. Disclosure                               0/0/2  -> 0.67
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 2 (found by 3 of 57 passes): ScyllaDB selected enforce, the handler-running terminating semantic, and pinned it per assertion through a vendor attribute, "Scylla is always enforced. Always.", foreclosing the per-build menu [63].
candidate 3 (found by 2 of 57 passes): On a strict reading - has this proposal's own specification shipped - neither has: the P3100 machinery and the P3589/P3984 framework syntax are both unshipped.
candidate 4 (found by 2 of 57 passes): The named-guarantee form is the shipping practice - a decade of it, across three vendors, measured in production

-->
