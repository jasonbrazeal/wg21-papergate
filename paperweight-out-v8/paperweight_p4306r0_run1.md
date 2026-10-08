Verdict: Excellent (13/14)

The paper offers substantial support for its own standardization, with the strongest material concentrated in deployment evidence, prior art, and the demonstrated need for a committee-level decision. The support is thinnest where the paper must show that a library solution will not do, since the record it cites actually documents replaceable violation handlers working in user space rather than failing there.

- The paper establishes that two active proposals now answer the same configuration question and that leaving ownership unsettled has already produced inconsistent wording and lost mechanisms.
- The named-guarantee approach is backed by a decade of shipping practice across three vendors, measured production cost, and independent adoption at Redpanda and WebKit.
- The paper shows the standard is the right venue because the deployed record favors per-facility handlers under application ownership, and the P2900 precedent does not support the alternative reading.
- The most glaring omission is the failure to establish why a library will not do, since the evidence presented shows replaceable violation handlers are common and workable in user space.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.50/14)

Provisionally addressed: 7 of 7. Provisional points: 12.50 of 14. Unsupported quotes rejected: 33. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.50   corroborated 12.00   accumulate 12.83   max 13.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.67  coordination 2.00  insufficiency 0.83  implementation 2.00
sample agreement: 113 of 133 section-criterion pairs unanimous (85%)
single-sample totals would have been: 13.00 / 12.50 / 12.50   (all 3 samples: 12.50)
headings: h2 16
on threshold: vehicle, insufficiency
splits: motivation[3] 1/2/1  motivation[6] 1/2/2  motivation[10] 0/2/2  audience[7] 2/2/0
        audience[10] 0/0/1  audience[16] 2/2/0  prior_art[5] 0/2/0  prior_art[9] 0/2/2
        prior_art[12] 2/0/2  prior_art[16] 2/0/0  vehicle[10] 0/1/1  vehicle[12] 2/0/2
        coordination[9] 2/0/2  coordination[11] 2/0/0  coordination[15] 2/0/2
        insufficiency[12] 2/2/1  implementation[7] 1/0/0  implementation[8] 0/0/2
        implementation[13] 2/1/2  implementation[16] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 19 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/2/1  -> 1.33
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              1/1/1  -> 1.00
  [6] 2. Two Proposals Compete to Own One Confi... 1/2/2  -> 1.67
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 2/2/2  -> 2.00
  [10] 6. Existing Practice Reads Both Ways         0/2/2  -> 1.33
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
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
  [7] 3. The Criteria and Their Provenance         2/2/0  -> 1.33
  [8] 4. The Record at a Glance                    0/0/0  -> 0.00
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         0/0/1  -> 0.33
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/2/0  -> 1.33
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Public code search finds no installation of the BDE violation handler outside BDE itself, its forks, and its vendored copies.
candidate 2 (found by 3 of 57 passes): Redpanda reached the same endpoint independently, replacing build-conditional asserts after "at least 2 difficult-to-analyze bugs" were introduced because checks were "compiled out due to our use of -DNDEBUG" [100].
candidate 3 (found by 2 of 57 passes): the named-guarantee form runs in production across three vendors' libraries with measured cost - on by default in GCC 15 unoptimized builds and Xcode 16, opt-in in others
candidate 4 (found by 1 of 57 passes): P3100R8's Appendix A enumerates the cases of core-language undefined behavior - 80 cases, 77 of them runtime-checkable [1]

## prior_art - grade 2.00 (fired in 9 of 19 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/2/0  -> 0.67
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         0/0/0  -> 0.00
  [8] 4. The Record at a Glance                    2/2/2  -> 2.00
  [9] 5. Deployment and Field Experience: The R... 0/2/2  -> 1.33
  [10] 6. Existing Practice Reads Both Ways         2/2/2  -> 2.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/0/2  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               2/0/0  -> 0.67
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The P3100 model leads on systematic coverage, the one criterion carrying a poll, but that lead does not resolve ownership, because both owners consume the enumeration identically; existing practice reads both ways and names different owners.
candidate 2 (found by 3 of 57 passes): The surviving committee handlers own single-purpose protocols. The removed or condemned mechanisms either adjudicated a violation class program-wide or exposed a writable global slot.
candidate 3 (found by 2 of 57 passes): The C++ Core Guidelines checkers (domain: static analysis): clang-tidy has carried the `cppcoreguidelines-*` checks since LLVM 3.8 (March 2016) [11], and the MSVC Core Guidelines checker has been installed by default since Visual Studio 2017 [12].
candidate 4 (found by 2 of 57 passes): The field-experience gloss on this reading comes from P3608R0 [6], which applied it in this exact domain: "the standard library hardening is existing practice, and comes with very positive field experience reports."

## vehicle - grade 1.67 (fired in 3 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
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
  [10] 6. Existing Practice Reads Both Ways         0/1/1  -> 0.67
  [11] 7. The Guarantee and the Dialect Question    0/0/0  -> 0.00
  [12] 8. One Architecture for Every Facility: T... 2/0/2  -> 1.33
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               2/2/2  -> 2.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The ownership question therefore needs a decision of its own rather than a default - the direction sentence supports both proposals, on different clauses, and only an explicit weighing of the deployment evidence chooses between them.
candidate 2 (found by 2 of 57 passes): The deployed record is per-facility handlers under application ownership.
candidate 3 (found by 2 of 57 passes): The P2900 precedent, read closely, runs the other way: that minimum-viable-product scope was limited to explicit assertions at API boundaries, with BDE-class design experience behind it (Section 8).
candidate 4 (found by 1 of 57 passes): The named-guarantee lineage deploys in production with measured cost, at operating-system-vendor and hyperscaler scale.

## coordination - grade 2.00 (fired in 6 of 19 sections, strong in 2)
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
  [9] 5. Deployment and Field Experience: The R... 2/0/2  -> 1.33
  [10] 6. Existing Practice Reads Both Ways         0/0/0  -> 0.00
  [11] 7. The Guarantee and the Dialect Question    2/0/0  -> 0.67
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 2/2/2  -> 2.00
  [15] 10. Objections                               2/0/2  -> 1.33
  [16] 11. Conclusion                               1/1/1  -> 1.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The first integration of a pre-existing checking facility into the C++26 contract-violation machinery is on the record, and it does not use the unified semantics.
candidate 2 (found by 3 of 57 passes): The two papers are now inconsistent in the record: P3081R2's proposed wording still adds the `detection_mode` enumerators, while P3100R8 proposes none and routes category encoding through Labels instead.
candidate 3 (found by 3 of 57 passes): On coordination, ownership left unsettled has already cost one companion paper its wording mechanism through independent revision.
candidate 4 (found by 1 of 57 passes): Apple's WebKit ships libc++ hardening at its extensive level in release builds and reports, after optimization work, that "The end to end performance cost in WebKit has been zero" [75].

## insufficiency - grade 0.83 (fired in 1 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
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
  [12] 8. One Architecture for Every Facility: T... 2/2/1  -> 1.67
  [13] 8. One Architecture for Every Facility: T... 0/0/0  -> 0.00
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               0/0/0  -> 0.00
  [17] 12. Disclosure                               0/0/0  -> 0.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Replaceable violation handlers are in fact common in user space, and their record sharpens the scope finding instead of blunting it.

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Introduction                              0/0/0  -> 0.00
  [6] 2. Two Proposals Compete to Own One Confi... 0/0/0  -> 0.00
  [7] 3. The Criteria and Their Provenance         1/0/0  -> 0.33
  [8] 4. The Record at a Glance                    0/0/2  -> 0.67
  [9] 5. Deployment and Field Experience: The R... 0/0/0  -> 0.00
  [10] 6. Existing Practice Reads Both Ways         1/1/1  -> 1.00
  [11] 7. The Guarantee and the Dialect Question    2/2/2  -> 2.00
  [12] 8. One Architecture for Every Facility: T... 2/2/2  -> 2.00
  [13] 8. One Architecture for Every Facility: T... 2/1/2  -> 1.67
  [14] 9. What Configuration Ownership Costs in ... 0/0/0  -> 0.00
  [15] 10. Objections                               0/0/0  -> 0.00
  [16] 11. Conclusion                               1/2/2  -> 1.67
  [17] 12. Disclosure                               2/2/2  -> 2.00
  [18] References  (part 1 of 2)                    0/0/0  -> 0.00
  [19] References  (part 2 of 2)                    0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The named-guarantee check-set is the shipping practice - a decade of it, across three vendors, measured in production
candidate 2 (found by 3 of 57 passes): Bloomberg has also rebased bsls_assert's enforced macro onto `contract_assert` under an experimental implementation and built BDE plus four large internal libraries on the result [93].
candidate 3 (found by 3 of 57 passes): The Clang implementation is public, with regularly released experimental builds that implement the framework attributes and an initial slice of the `std::init` profile [105]
candidate 4 (found by 2 of 57 passes): what the record establishes is narrower - the shipping practice terminates, and P3100's added machinery of implicit assertions, Labels, and a replaceable handler has no implementation.

-->
