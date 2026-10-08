Verdict: Strong to Excellent (12/14)

The paper offers substantial support for its standardization case, with the strongest evidence coming from deployed practice and the concrete cost of leaving the ownership question unsettled. The thinnest parts are the arguments that the standard is the necessary venue and that a library solution cannot suffice, where the paper asserts more than it demonstrates.

- The paper convincingly establishes that the question matters and affects real users, citing independent convergence by Redpanda and a decade of shipping practice across three vendors.
- It also establishes coordination and interoperability problems with concrete evidence, showing that one companion paper’s wording has already been stranded by the other’s revision.
- The most glaring omission is the lack of a demonstrated case for why the standard, rather than a library or existing committee mechanism, must own the configuration.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 40. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 11.67   accumulate 11.67   max 12.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.50  coordination 2.00  insufficiency 1.00  implementation 2.00
sample agreement: 114 of 133 section-criterion pairs unanimous (86%)
single-sample totals would have been: 12.00 / 12.00 / 11.00   (all 3 samples: 11.50)
headings: h2 16
on threshold: insufficiency
splits: motivation[3] 0/0/1  motivation[6] 2/1/1  motivation[10] 2/1/1  motivation[15] 2/1/2
        audience[3] 1/0/0  audience[10] 2/0/1  audience[13] 2/1/2  prior_art[3] 1/2/2
        prior_art[8] 1/2/2  prior_art[13] 0/2/2  vehicle[5] 1/0/0  vehicle[10] 1/0/0
        vehicle[12] 0/2/0  coordination[5] 0/1/1  coordination[16] 1/2/2
        implementation[3] 0/0/1  implementation[7] 0/1/1  implementation[8] 2/0/2
        implementation[17] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 19 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/1  -> 0.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 2/1/1  -> 1.33
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/1/1  -> 1.33
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               2/1/2  -> 1.67
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 2 (found by 3 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].
candidate 3 (found by 3 of 57 passes): Section 9 shows the cost of leaving the question unsettled: one paper's wording has already been stranded by the other's revision.
candidate 4 (found by 2 of 57 passes): If we want to have both, we need to specify one in terms of the other to avoid an incoherent and messy design.

## audience - grade 2.00 (fired in 5 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/0/0  -> 0.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         2/0/1  -> 1.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/1/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Public code search finds no installation of the BDE violation handler outside BDE itself, its forks, and its vendored copies.
candidate 2 (found by 2 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 3 (found by 2 of 57 passes): P0709R3 measured the fragmentation from that single binary toggle - over half of surveyed developers under partial or total exception bans, "using a divergent language dialect" [83].
candidate 4 (found by 2 of 57 passes): ScyllaDB selected enforce, the handler-running terminating semantic, and pinned it per assertion through a vendor attribute, "Scylla is always enforced. Always.", foreclosing the per-build menu

## prior_art - grade 2.00 (fired in 8 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/2/2  -> 1.67
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    1/2/2  -> 1.67
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/2/2  -> 1.33
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.
candidate 2 (found by 3 of 57 passes): The C++26 contract-violation runtime the P3100 model builds on ([P2900R14]) has one compiler implementation, GCC 16.1 (April 2026), opt-in under GCC's experimental C++26 label [19].
candidate 3 (found by 3 of 57 passes): The C committee's record contains the same precedent, run to the same end.
candidate 4 (found by 3 of 57 passes): Under P3100's menu it attaches to every checkable operation, where the proposal's own resolution leaves the `noexcept` operator answering true for expressions that can throw.

## vehicle - grade 0.50 (fired in 3 of 19 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/0/0  -> 0.33
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/0/0  -> 0.33
  [11] 7. The Guarantee and the Dialect Question    0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 0/2/0  -> 0.67
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The comparison below measures the two candidate owners of that configuration against criteria already in the committee's record, and it is the dedicated comparison its companion P4297R0 [8] asks EWG to weigh
candidate 2 (found by 1 of 57 passes): The ownership question therefore needs a decision of its own rather than a default - the direction sentence supports both proposals, on different clauses, and only an explicit weighing of the deployment evidence chooses between them.
candidate 3 (found by 1 of 57 passes): The deployed record is per-facility handlers under application ownership. Expressing that policy matrix through one cross-facility handler would need exactly the per-check category metadata whose standardized form was withdrawn in favor of unimplemented Labels (Section 9).

## coordination - grade 2.00 (fired in 6 of 19 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/1/1  -> 0.67
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
  [16] 11. Conclusion                               1/2/2  -> 1.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 2 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 3 (found by 3 of 57 passes): On coordination, ownership left unsettled has already cost one companion paper its wording mechanism through independent revision.
candidate 4 (found by 2 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.

## insufficiency - grade 1.00 (fired in 1 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
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
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Replaceable violation handlers are in fact common in user space, and their record sharpens the scope finding instead of blunting it.

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/1  -> 0.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/1/1  -> 0.67
  [8] 4. The Record at a Glance                    2/0/2  -> 1.33
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 1/1/1  -> 1.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               2/2/0  -> 1.33
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 3 of 57 passes): GCC's contracts code asks per condition whether the predicate "might throw" and wraps the check in a try-catch expression when it can.
candidate 3 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 4 (found by 3 of 57 passes): ScyllaDB selected enforce, the handler-running terminating semantic, and pinned it per assertion through a vendor attribute, "Scylla is always enforced. Always.", foreclosing the per-build menu

-->
