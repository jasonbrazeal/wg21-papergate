Verdict: Strong (9/14)

The paper offers a mixed case for its own standardization, with its strongest material going to prior art, implementation experience, and the procedural risk it identifies, while the affirmative case for putting this in the standard remains largely asserted rather than demonstrated. The thinnest areas are the absence of any argument for why a library cannot satisfy the need and the unestablished claims about who is affected and how the work would coordinate with existing standardization.

- The paper is most persuasive in showing that the layering question is real, contested, and grounded in a decade of shipped, vendor-named check-set implementations.
- It also credibly establishes that the procedural history of P3100R8 may be closing the design space without an explicit EWG decision.
- The claim that the deployment record shows which architecture belongs in the standard is asserted, but the paper does not connect that record to a standardization requirement.
- Most glaringly, the paper offers no case at all for why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 6 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 9.00   accumulate 8.83   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.83  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 93 of 98 section-criterion pairs unanimous (95%)
single-sample totals would have been: 9.00 / 10.00 / 7.50   (all 3 samples: 8.83)
headings: h2 13
on threshold: audience, vehicle, implementation
splits: motivation[11] 0/0/2  prior_art[12] 2/0/0  vehicle[9] 2/2/1  coordination[9] 2/2/0
        coordination[11] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 2/2/2  -> 2.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/0/2  -> 0.67
  [12] 7. Making the Design Commitment Explicit     2/2/2  -> 2.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The claim decides who owns the configuration of runtime checking.
candidate 2 (found by 3 of 42 passes): The concern behind the ask rests on one assumption, stated plainly so a delegate can test it: a design settled through accumulated approvals, with no single poll deciding it, is harder to revisit than one decided by an explicit ballot.
candidate 3 (found by 3 of 42 passes): The concern this paper raises requires no intent on anyone's part. Through the formulations of P3100R8's Sections 4.4 and 7.2, EWG may be unintentionally committing itself to closing the design space for Profiles, one approval at a time.
candidate 4 (found by 2 of 42 passes): Without explicit input from EWG, approving the outcomes of the case-by-case review may close the evolution path for Profiles.

## audience - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/0/0  -> 0.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): deployed across Google server-side production at approximately 0.30% average cost [20].

## prior_art - grade 2.00 (fired in 5 of 14 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                2/2/2  -> 2.00
  [12] 7. Making the Design Commitment Explicit     2/0/0  -> 0.67
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 2 (found by 3 of 42 passes): The layering claim sits between two competing bodies of published work: P3100R8's implicit contract assertions, configured through the Labels facility of P3400R3, and the Profiles work of P3984R0, P3081R2, and P3589R2.
candidate 3 (found by 3 of 42 passes): By contrast, the proposal's distinctive machinery ships nowhere.
candidate 4 (found by 3 of 42 passes): P3100R8's Section 7.2 says that if both features are kept, one must be specified in terms of the other, and the proposal makes that choice in Labels' favor.

## vehicle - grade 0.83 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/1  -> 1.67
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/0/0  -> 0.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The deployment record speaks to which architecture matches existing practice.

## coordination - grade 1.00 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/0  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/2/0  -> 0.67
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The deployment record speaks to which architecture matches existing practice.
candidate 2 (found by 1 of 42 passes): Every one of these is a named, vendor-defined check-set. None routes through the `std::contracts` violation handler adopted for C++26, and none is configured by a Label.
candidate 3 (found by 1 of 42 passes): P3100R8's Section 5.6 withdrew the `detection_mode` enumerators that P3081R2's wording still depends on, leaving that dependency without the mechanism that would satisfy it.

## insufficiency - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/0/0  -> 0.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/0/0  -> 0.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/0/0  -> 0.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): For a decade, the named-check-set form the Profiles papers describe has shipped under vendor names: * **Core Guidelines checkers:** clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].
candidate 2 (found by 1 of 42 passes): For a decade, the named-check-set form the Profiles papers describe has shipped under vendor names: Core Guidelines checkers: clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].

-->
