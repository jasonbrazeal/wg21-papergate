Verdict: Strong to Excellent (12/14)

The paper offers substantial support for standardizing its proposed facility, with particularly strong evidence of deployed practice, independent convergence on the same design, and unresolved coordination problems with the competing proposal. The support is thinnest where the paper must show that the standard is the right home and that a library solution cannot suffice: those arguments are asserted rather than demonstrated, and the implementation record for the underlying contract-violation machinery is still narrow.

- The strongest support is the convergence of independent, production-scale deployments on the same named-guarantee check-set and per-facility handler shape, including the Linux kernel, Redpanda, and multiple vendor hardening modes.
- The paper also establishes a live coordination problem: two active proposals now answer the same configuration question and have become inconsistent in the record, which gives the committee a concrete reason to resolve ownership.
- The most glaring omission is the absence of a demonstrated case for why the standard, rather than a library or existing vendor facility, must own this mechanism; the paper claims the need but does not establish it from the deployment record or the limits of library approaches.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 7 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 33. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 12.00   accumulate 12.17   max 13.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.67  coordination 2.00  insufficiency 1.33  implementation 2.00
sample agreement: 114 of 133 section-criterion pairs unanimous (86%)
single-sample totals would have been: 13.00 / 11.00 / 12.50   (all 3 samples: 12.00)
headings: h2 16
on threshold: insufficiency
splits: motivation[6] 1/2/1  motivation[15] 1/1/2  audience[10] 1/0/1  audience[13] 1/2/2
        audience[15] 2/0/0  prior_art[6] 2/0/2  prior_art[8] 2/2/1  prior_art[13] 0/2/0
        prior_art[14] 0/2/2  vehicle[12] 2/0/2  coordination[5] 1/1/0  coordination[15] 2/0/0
        coordination[16] 0/0/1  insufficiency[9] 2/0/0  insufficiency[15] 0/0/1
        implementation[3] 1/0/1  implementation[13] 2/1/2  implementation[16] 2/2/1
        implementation[17] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 19 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 1/2/1  -> 1.33
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               1/1/2  -> 1.33
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two proposals answer one question - how a program configures the runtime checking of core-language undefined behavior - and, as P3100R8's own Section 7.2 states, if both are kept then one must be specified in terms of the other.
candidate 2 (found by 3 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 3 (found by 3 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].
candidate 4 (found by 3 of 57 passes): It is coordination cost: when the P3100 proposal moved category encoding to Labels, P3081R2's enumerators lost the mechanism that would have produced them, and the dependency sat unreconciled through the next revision cycle.

## audience - grade 2.00 (fired in 5 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
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
  [10] 6. Existing Practice Reads Both Ways         1/0/1  -> 0.67
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 1/2/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               2/0/0  -> 0.67
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.
candidate 2 (found by 3 of 57 passes): Public code search finds no installation of the BDE violation handler outside BDE itself, its forks, and its vendored copies.
candidate 3 (found by 2 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 4 (found by 2 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].

## prior_art - grade 2.00 (fired in 10 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 2/0/2  -> 1.33
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    2/2/1  -> 1.67
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/2/0  -> 0.67
  [14] 9. What Configuration Ownership Costs in ... 0/2/2  -> 1.33
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The P3100 model leads on systematic coverage, the one criterion carrying a poll, but that lead does not resolve ownership, because both owners consume the enumeration identically; existing practice reads both ways and names different owners.
candidate 2 (found by 3 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.
candidate 3 (found by 3 of 57 passes): Both proposals' specifications are unshipped, and applied evenly the deployment record settles the base role for neither: each pairs a deployed lineage with an unshipped specification, and both can express the terminating named-guarantee set that ships.
candidate 4 (found by 2 of 57 passes): Under the P3100 model, the implicit-contract-assertion machinery is the base and a profile is a named preset that selects a configuration of it.

## vehicle - grade 0.67 (fired in 1 of 19 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
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
  [12] 8. One Architecture for Every Facility: T... 2/0/2  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The deployed record is per-facility handlers under application ownership.

## coordination - grade 2.00 (fired in 7 of 19 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/0  -> 0.67
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               2/0/0  -> 0.67
  [16] 11. Conclusion                               0/0/1  -> 0.33
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 2 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 3 (found by 2 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 4 (found by 2 of 57 passes): Consumers deploy the same form at vendor scale.

## insufficiency - grade 1.33 (fired in 3 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/0/0  -> 0.67
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
candidate 1 (found by 2 of 57 passes): Replaceable violation handlers are in fact common in user space, and their record sharpens the scope finding instead of blunting it.
candidate 2 (found by 1 of 57 passes): The C++26 contract-violation runtime the P3100 model builds on ([P2900R14] [18]) has one compiler implementation, GCC 16.1 (April 2026), opt-in under GCC's experimental C++26 label [19]. Clang reports "No" [20].
candidate 3 (found by 1 of 57 passes): What no deployed handler spans is facilities: each serves exactly one assertion family's checks, and one process routinely runs multiple policies side by side
candidate 4 (found by 1 of 57 passes): The sanitizers, trap flags, and hardened libraries deploy no violation object, no replaceable cross-facility handler, no in-source selection among evaluation semantics

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/0/1  -> 0.67
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         1/1/1  -> 1.00
  [8] 4. The Record at a Glance                    2/2/2  -> 2.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/1/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/1  -> 1.67
  [17] 12. Disclosure                               2/1/2  -> 1.67
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): libc++ hardening | LLVM 18, 2024 [13] | Xcode 16 build setting [14] | Google: ~0.30% [15] | trap instruction [33]
candidate 2 (found by 3 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 3 (found by 3 of 57 passes): GCC's contracts code asks per condition whether the predicate "might throw" and wraps the check in a try-catch expression when it can.
candidate 4 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].

-->
