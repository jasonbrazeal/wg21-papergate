Verdict: Strong to Excellent (12/14)

The paper offers substantial support for its standardization case in the areas where field experience and existing practice are concrete, but the argument becomes thinner when it must show why the standard—rather than a library or existing tooling—is the necessary home for the mechanism. The strongest material concerns what has already shipped and been measured in production, while the weakest concerns the positive case for normative action itself.

- The paper most convincingly establishes that the named-guarantee check-set has a decade of shipped, production-default field experience across three vendors, with measured cost and real adoption in systems like the Linux kernel and WebKit.
- It also clearly shows that the two competing models are now inconsistent in the record and that a prior integration into the C++26 contract-violation machinery did not use the unified semantics, which supports the need for coordination.
- The case for why the standard is required, rather than a library or existing deployment practice, is asserted mainly by pointing to the immaturity of the proposals’ specifications and the single opt-in implementation, without establishing that standardization is the only or best remedy.
- The most glaring omission is the absence of a demonstrated reason that a library cannot carry the design, especially given that replaceable violation handlers and deployed in-source controls already exist in user space.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 25. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 12.00   accumulate 12.00   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 2.00  vehicle 0.67  coordination 2.00  insufficiency 1.33  implementation 2.00
sample agreement: 111 of 133 section-criterion pairs unanimous (83%)
single-sample totals would have been: 13.00 / 11.00 / 12.00   (all 3 samples: 11.83)
headings: h2 16
on threshold: insufficiency
splits: motivation[10] 2/2/1  motivation[12] 0/0/2  audience[7] 2/0/0  audience[8] 2/0/0
        audience[10] 0/1/1  audience[12] 2/2/0  audience[13] 1/2/2  audience[16] 2/0/0
        prior_art[5] 0/0/2  prior_art[6] 0/2/2  prior_art[12] 2/2/0  prior_art[13] 2/0/2
        vehicle[9] 2/0/2  coordination[9] 0/0/2  coordination[11] 0/2/0  coordination[16] 2/0/0
        insufficiency[15] 2/0/0  implementation[3] 1/1/0  implementation[7] 0/0/1
        implementation[8] 0/2/2  implementation[11] 0/0/2  implementation[16] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 2/2/2  -> 2.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/1  -> 1.67
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 0/0/2  -> 0.67
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               2/2/2  -> 2.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two bodies of work now answer the same question: how a program configures the runtime checking of core-language undefined behavior.
candidate 2 (found by 3 of 57 passes): If we want to have both, we need to specify one in terms of the other to avoid an incoherent and messy design.
candidate 3 (found by 3 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years; both proposals' specifications have none; and the C++26 contract runtime the P3100 model builds on has a single opt-in implementation from April 2026.
candidate 4 (found by 3 of 57 passes): Where configurability itself was the bug vector, the fix in both organizations was to remove the menu rather than enrich it.

## audience - grade 1.83 (fired in 7 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         2/0/0  -> 0.67
  [8] 4. The Record at a Glance                    2/0/0  -> 0.67
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         0/1/1  -> 0.67
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/0  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 1/2/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/0/0  -> 0.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.
candidate 2 (found by 2 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].
candidate 3 (found by 1 of 57 passes): P3100R8's Appendix A enumerates the cases of core-language undefined behavior - 80 cases, 77 of them runtime-checkable [1] - and no Profiles paper offers an equivalent enumeration.
candidate 4 (found by 1 of 57 passes): Google: ~0.30% [15]

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/2  -> 0.67
  [6] 2. Two Proposals Compete to Own One Confi... 0/2/2  -> 1.33
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    2/2/2  -> 2.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/0  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 2/0/2  -> 1.33
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/2  -> 2.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The P3100 model leads on systematic coverage, the one criterion carrying a poll, but that lead does not resolve ownership, because both owners consume the enumeration identically; existing practice reads both ways and names different owners.
candidate 2 (found by 3 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.
candidate 3 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 4 (found by 2 of 57 passes): Under the P3100 model, the implicit-contract-assertion machinery is the base and a profile is a named preset that selects a configuration of it.

## vehicle - grade 0.67 (fired in 1 of 19 sections, strong in 0)  (SHARED PASSAGE)
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
  [9] 5. Deployment and Field Experience: The R... 2/0/2  -> 1.33
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The named-guarantee form has a decade of shipped, production-default field experience, its cost measured in recent years; both proposals' specifications have none; and the C++26 contract runtime the P3100 model builds on has a single opt-in implementation from April 2026.

## coordination - grade 2.00 (fired in 5 of 19 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 5. Deployment and Field Experience: The R... 0/0/2  -> 0.67
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    0/2/0  -> 0.67
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/0/0  -> 0.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 2 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 3 (found by 1 of 57 passes): Apple's WebKit ships libc++ hardening at its extensive level in release builds and reports, after optimization work, that "The end to end performance cost in WebKit has been zero" [75].
candidate 4 (found by 1 of 57 passes): The Linux kernel pinned `-fno-strict-aliasing` in 2003 and holds the position tree-wide across two decades - "This is why we use -fwrapv, -fno-strict-aliasing etc.

## insufficiency - grade 1.33 (fired in 2 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
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
  [15] 10. Objections                               2/0/0  -> 0.67
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Replaceable violation handlers are in fact common in user space, and their record sharpens the scope finding instead of blunting it.
candidate 2 (found by 1 of 57 passes): The sanitizers, trap flags, and hardened libraries deploy no violation object, no replaceable cross-facility handler, no in-source selection among evaluation semantics (the deployed in-source control is binary suppression, per-site check-or-not attributes), and no translation of predicate exceptions into violations

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/0  -> 0.67
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/1  -> 0.33
  [8] 4. The Record at a Glance                    0/2/2  -> 1.33
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee and the Dialect Question    0/0/2  -> 0.67
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 1/1/1  -> 1.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               1/2/2  -> 1.67
  [17] 12. Disclosure                               2/2/2  -> 2.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 3 (found by 3 of 57 passes): the named-guarantee form runs in production across three vendors' libraries with measured cost - on by default in GCC 15 unoptimized builds and Xcode 16, opt-in in others
candidate 4 (found by 3 of 57 passes): The Clang implementation is public, with regularly released experimental builds that implement the framework attributes and an initial slice of the `std::init` profile [105]

-->
