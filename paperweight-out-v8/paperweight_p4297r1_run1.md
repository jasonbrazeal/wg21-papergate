Verdict: Strong (10/14)

The paper’s strongest support comes from its reconstruction of the proposal’s poll history and its documentation of a decade of deployment for the named-guarantee form, which together make a concrete case that the architectural question is real and already settled in practice. The case is much thinner on the points that would justify committee action now: it does not establish who is concretely affected beyond a single cost figure, why a standard is needed rather than continued vendor practice, or how the competing features would coordinate if both moved forward. Most glaringly, the paper never addresses why a library or existing vendor mechanism cannot satisfy the need it describes.

- The paper establishes that the layering question is substantive and contested, with a documented poll history showing no single decision adopted the architecture.
- The paper establishes meaningful implementation experience for the named-guarantee form through clang-tidy and MSVC deployment over roughly a decade.
- The paper claims but does not establish who is affected, offering only a single approximate cost figure and a table of polls rather than a clear picture of users or codebases at stake.
- The paper does not establish why a library will not do, leaving unaddressed the most basic question about whether standardization is necessary at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 9.67   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.00  coordination 1.17  insufficiency 0.00  implementation 2.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 10.00 / 9.00 / 10.00   (all 3 samples: 9.50)
headings: h2 13
on threshold: audience, vehicle, coordination, implementation
splits: motivation[11] 1/2/2  audience[8] 2/0/0  prior_art[9] 2/2/0  coordination[7] 0/0/2
        coordination[9] 2/1/2  coordination[12] 0/1/0  implementation[12] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 1/1/1  -> 1.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 1/2/2  -> 1.67
  [12] 7. Three Polls Make the Architecture Ques... 2/2/2  -> 2.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The concern behind the ask rests on one assumption, stated plainly so a delegate can test it: a design settled through accumulated approvals, with no single poll deciding it, is harder to revisit than one decided by an explicit ballot.
candidate 2 (found by 3 of 42 passes): Without explicit input from EWG, approving the outcomes of the case-by-case review may close the evolution path for Profiles.
candidate 3 (found by 3 of 42 passes): The deployment record speaks to which architecture matches existing practice.
candidate 4 (found by 3 of 42 passes): Interrupting that default now is cheap where reversing it later has cost the committee years.

## audience - grade 1.33 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 2/0/0  -> 0.67
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): deployed across Google server-side production at approximately 0.30% average cost [20].
candidate 2 (found by 1 of 42 passes): Table 1: The six polls in P3100R8's self-reported history (its Section 2, rows 1-6), plus a seventh poll taken at Brno after that history's coverage (row 7, from the public paper tracker).

## prior_art - grade 2.00 (fired in 4 of 14 sections, strong in 2)
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
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/0  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 2/2/2  -> 2.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 2 (found by 3 of 42 passes): The layering claim sits between two competing bodies of published work: P3100R8's implicit contract assertions, configured through the Labels facility of P3400R3, and the Profiles work of P3984R0, P3081R2, and P3589R2.
candidate 3 (found by 3 of 42 passes): P3100R8's Section 5.6 withdrew the `detection_mode` enumerators that P3081R2's wording still depends on, leaving that dependency without the mechanism that would satisfy it.
candidate 4 (found by 1 of 42 passes): P3081R1 took the complementary path - it adopted the proposal's API into its own wording - and P3100R8's Section 5.6 then withdrew that API, as Section 2 showed.

## vehicle - grade 1.00 (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The deployment record speaks to which architecture matches existing practice.

## coordination - grade 1.17 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/2  -> 0.67
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/1/2  -> 1.67
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/1/0  -> 0.33
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Whoever owns the handler owns the response, and under P3100R8 that owner is neither the operation nor any profile - it is the handler.
candidate 2 (found by 1 of 42 passes): When one feature owns the configuration mechanism, a change to it can leave another paper's wording stranded through independent revision, without the coordination that P3100R8's own Section 7.2 now says is needed.
candidate 3 (found by 1 of 42 passes): Every one of these is a named, vendor-defined set of guarantees. None routes through the `std::contracts` violation handler adopted for C++26, and none is configured by a Label.
candidate 4 (found by 1 of 42 passes): Poll 2 also supplies the agreement P3100R8's own Section 7.2 asks for when it says the two features, if both are kept, must be specified one in terms of the other.

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
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)
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
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/1  -> 0.33
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): For a decade, the named-guarantee form the Profiles papers describe has shipped under vendor names: Core Guidelines checkers: clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].
candidate 2 (found by 1 of 42 passes): For a decade, the named-guarantee form the Profiles papers describe has shipped under vendor names: - **Core Guidelines checkers:** clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].
candidate 3 (found by 1 of 42 passes): One asymmetry belongs on the table: the named-guarantee form has more deployment history today than the implicit-contract-assertion form (Section 4).

-->
