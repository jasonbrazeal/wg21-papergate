Verdict: Strong to Excellent (11/14)

The paper offers substantial support for the need to standardize a named-guarantee mechanism, particularly through its deployment history, vendor implementation experience, and the coordination problems already visible in the record. The case is thinnest where it must show why the standard, rather than a library or existing practice, is the necessary vehicle, since the paper asserts application ownership and per-facility handlers without fully establishing that standardization is required to preserve them.

- The strongest support comes from the decade of shipping, production-default use across three vendors, including measured costs and real integration with contract-violation machinery.
- The paper also convincingly documents that two active proposals now answer the same configuration question and have already diverged in wording, making coordination a live standardization problem.
- The most glaring omission is the unestablished claim that deployed practice requires a standard rather than remaining a library-level or vendor-level facility, since no deployed handler is shown to span multiple facilities or require core-language integration.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 27. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 11.67   accumulate 11.33   max 12.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 2.00  insufficiency 0.33  implementation 2.00
sample agreement: 119 of 133 section-criterion pairs unanimous (89%)
single-sample totals would have been: 11.00 / 11.00 / 12.00   (all 3 samples: 11.33)
headings: h2 16
on threshold: vehicle
splits: motivation[10] 2/0/2  motivation[15] 0/2/2  audience[7] 2/0/2  audience[10] 1/1/0
        audience[16] 0/0/1  prior_art[8] 1/1/2  prior_art[14] 0/0/2  coordination[9] 0/0/2
        coordination[16] 1/0/1  insufficiency[12] 0/0/2  implementation[8] 1/0/1
        implementation[10] 0/1/1  implementation[13] 2/1/2  implementation[15] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 7)
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
  [10] 6. Existing Practice Reads Both Ways         2/0/2  -> 1.33
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               0/2/2  -> 1.33
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two proposals answer one question - how a program configures the runtime checking of core-language undefined behavior - and, as P3100R8's own Section 7.2 states, if both are kept then one must be specified in terms of the other.
candidate 2 (found by 3 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 3 (found by 3 of 57 passes): If we want to have both, we need to specify one in terms of the other to avoid an incoherent and messy design.
candidate 4 (found by 3 of 57 passes): The deployed failure responses diverge for stated engineering reasons

## audience - grade 2.00 (fired in 6 of 19 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 2/0/2  -> 1.33
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/0  -> 0.67
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/1  -> 0.33
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The named-guarantee form is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 2 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.
candidate 3 (found by 2 of 57 passes): The deployment report behind that constraint records a two percent binary-size increase from the verbose failure path as a blocker in certain environments, reduced below half a percent by the trap [34].
candidate 4 (found by 1 of 57 passes): P3100R8's Appendix A enumerates the cases of core-language undefined behavior - 80 cases, 77 of them runtime-checkable [1] - and no Profiles paper offers an equivalent enumeration.

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
  [8] 4. The Record at a Glance                    1/1/2  -> 1.33
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/2  -> 0.67
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The Profiles papers, P3589R2 and P3984R0, instead make a Profile the named mechanism that selects and defines such guarantees.
candidate 2 (found by 3 of 57 passes): The named-guarantee form is the shipping practice - a decade of it, across three vendors, measured in production - and a Profiles framework that standardizes named, enforceable guarantees is the same shape as what deploys today.
candidate 3 (found by 3 of 57 passes): The closest deployed analogue of the P3100 model is Bloomberg's BDE assertion family, and it is real and scoped.
candidate 4 (found by 3 of 57 passes): ScyllaDB selected enforce, the handler-running terminating semantic, and pinned it per assertion through a vendor attribute, "Scylla is always enforced. Always.", foreclosing the per-build menu [63].

## vehicle - grade 1.00 (fired in 1 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
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
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The deployed record is per-facility handlers under application ownership.

## coordination - grade 2.00 (fired in 4 of 19 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/2  -> 0.67
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee Has Different Authors an... 0/0/0  -> 0.00
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
candidate 3 (found by 2 of 57 passes): On coordination, ownership left unsettled has already cost one companion paper its wording mechanism through independent revision.
candidate 4 (found by 1 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years.

## insufficiency - grade 0.33 (fired in 1 of 19 sections, strong in 0)
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
candidate 1 (found by 1 of 57 passes): What no deployed handler spans is facilities: each serves exactly one assertion family's checks, and one process routinely runs multiple policies side by side

## implementation - grade 2.00  [binary: max] (fired in 10 of 19 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. Four Criteria Recur, and Their Provena... 1/1/1  -> 1.00
  [8] 4. The Record at a Glance                    1/0/1  -> 0.67
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         0/1/1  -> 0.67
  [11] 7. The Guarantee Has Different Authors an... 2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/1/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/1/0  -> 0.33
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               2/2/2  -> 2.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 2 (found by 3 of 57 passes): the named-guarantee form runs in production across three vendors' libraries with measured cost - on by default in GCC 15 unoptimized builds and Xcode 16, opt-in in others
candidate 3 (found by 3 of 57 passes): The Clang implementation is public, with regularly released experimental builds that implement the framework attributes and an initial slice of the `std::init` profile [105]
candidate 4 (found by 2 of 57 passes): the shipping practice terminates, and P3100's added machinery of implicit assertions, Labels, and a replaceable handler has no implementation.

-->
