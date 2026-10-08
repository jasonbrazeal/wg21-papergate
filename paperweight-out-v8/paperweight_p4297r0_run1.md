Verdict: Strong (9/14)

The paper offers solid support on the procedural stakes, the history of the design question, and the existence of shipping implementations, but it leaves the affirmative case for standardization resting on claims about deployment cost, existing practice, and interoperability that are asserted rather than demonstrated. The thinnest part is the absence of any argument that a library solution cannot carry the design, which is a gap the paper does not even attempt to fill.

- The strongest support is the reconstruction of the committee’s seven-poll history and the showing that no poll adopted the architecture now being advanced.
- The paper also establishes that the named-check-set form has real implementation experience, shipping in clang-tidy and MSVC for roughly a decade.
- The interoperability argument is only claimed, since the paper points to proposed wording and vendor-defined check-sets but does not establish how they would coordinate with the C++26 contracts violation handler.
- The most glaring omission is the complete absence of a case for why a library will not do, leaving the need for standardization itself unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.00   max 10.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.67  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 13
on threshold: audience, implementation
splits: motivation[4] 2/1/2  motivation[6] 0/1/1  motivation[11] 1/2/2  prior_art[8] 1/1/0
        prior_art[9] 0/0/2  vehicle[9] 2/2/0  coordination[7] 2/0/2  coordination[9] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/1/2  -> 1.67
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/1/1  -> 0.67
  [7] 2. P3100 Characterizes Profiles as a Pres... 2/2/2  -> 2.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                1/2/2  -> 1.67
  [12] 7. Making the Design Commitment Explicit     2/2/2  -> 2.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Interrupting that default now is cheap where reversing it later has cost the committee years.
candidate 2 (found by 2 of 42 passes): The claim decides who owns the configuration of runtime checking.
candidate 3 (found by 2 of 42 passes): The concern behind the ask rests on one assumption, stated plainly so a delegate can test it: a design settled through accumulated approvals, with no single poll deciding it, is harder to revisit than one decided by an explicit ballot.
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

## prior_art - grade 2.00 (fired in 5 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 1/1/0  -> 0.67
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/0/2  -> 0.67
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                2/2/2  -> 2.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 2 (found by 3 of 42 passes): The layering claim sits between two competing bodies of published work: P3100R8's implicit contract assertions, configured through the Labels facility of P3400R3, and the Profiles work of P3984R0, P3081R2, and P3589R2.
candidate 3 (found by 2 of 42 passes): It walked away from [P0443R14](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p0443r14.html) [12] after the unified executor design absorbed fourteen revisions of committee direction and was never deployed as designed
candidate 4 (found by 2 of 42 passes): P3100R8's Section 7.2 says that if both features are kept, one must be specified in terms of the other, and the proposal makes that choice in Labels' favor.

## vehicle - grade 0.67 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
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
  [11] 6. Objections                                0/0/0  -> 0.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): The deployment record speaks to which architecture matches existing practice.

## coordination - grade 1.33 (fired in 2 of 14 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 2/0/2  -> 1.33
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/2/2  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Objections                                0/0/0  -> 0.00
  [12] 7. Making the Design Commitment Explicit     0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): P3081R2's proposed wording still adds those enumerators - `detection_mode::type`, `detection_mode::bounds`, and `detection_mode::lifetime`, each defined as indicating that "the contract assertion was evaluated as part of" the corresponding profile
candidate 2 (found by 2 of 42 passes): Every one of these is a named, vendor-defined check-set. None routes through the `std::contracts` violation handler adopted for C++26, and none is configured by a Label.

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
candidate 1 (found by 3 of 42 passes): For a decade, the named-check-set form the Profiles papers describe has shipped under vendor names: Core Guidelines checkers: clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].

-->
