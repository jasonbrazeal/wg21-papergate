Verdict: Strong (9/14)

The paper’s strongest support comes from its reconstruction of the procedural history and its evidence of deployment for the named-guarantee form, which together make a credible case that the layering question is real and already has implementation experience behind it. The case is much thinner on why this needs to be settled in the standard itself, and it offers no argument at all for why a library-based approach would be insufficient.

- The paper establishes that the layering question has substantive prior art, a contested history, and a decade of shipped implementation experience behind the named-guarantee form.
- It establishes that the proposal’s own poll history did not adopt the architecture now under review, and that no published paper contests that characterization.
- It claims, but does not establish, who is concretely affected or why the standard is the necessary venue, relying more on asserted stakes than demonstrated need.
- It does not establish why a library will not do, leaving the most basic threshold question for standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 6 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 9.00   accumulate 8.83   max 10.33

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 88 of 98 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 8.50 / 9.50   (all 3 samples: 8.67)
headings: h2 13
on threshold: coordination, implementation
splits: motivation[7] 2/1/2  motivation[11] 2/1/2  audience[9] 2/0/2  audience[12] 0/0/1
        prior_art[8] 0/2/0  prior_art[10] 2/0/0  prior_art[12] 2/2/0  vehicle[9] 0/2/1
        coordination[11] 0/1/0  coordination[12] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              1/1/1  -> 1.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 2/1/2  -> 1.67
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 2/1/2  -> 1.67
  [12] 7. Three Polls Make the Architecture Ques... 2/2/2  -> 2.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The claim decides who owns the configuration of runtime checking.
candidate 2 (found by 3 of 42 passes): The deployment record speaks to which architecture matches existing practice.
candidate 3 (found by 3 of 42 passes): Interrupting that default now is cheap where reversing it later has cost the committee years.
candidate 4 (found by 3 of 42 passes): The concern this paper raises requires no intent on anyone's part. Through the formulations of P3100R8's Sections 4.4 and 7.2, EWG may be unintentionally committing itself to closing the design space for Profiles, one approval at a time.

## audience - grade 0.83 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/0/2  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/1  -> 0.33
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): deployed across Google server-side production at approximately 0.30% average cost [20].
candidate 2 (found by 1 of 42 passes): One asymmetry belongs on the table: the named-guarantee form has more deployment history today than the implicit-contract-assertion form (Section 4).

## prior_art - grade 2.00 (fired in 7 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/2  -> 2.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/2/0  -> 0.67
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 2/0/0  -> 0.67
  [11] 6. Six Objections, Answered from Evidence... 2/2/2  -> 2.00
  [12] 7. Three Polls Make the Architecture Ques... 2/2/0  -> 1.33
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 2 (found by 3 of 42 passes): The layering claim sits between two competing bodies of published work: P3100R8's implicit contract assertions, configured through the Labels facility of P3400R3, and the Profiles work of P3984R0, P3081R2, and P3589R2.
candidate 3 (found by 3 of 42 passes): P3100R8's Section 5.6 withdrew the `detection_mode` enumerators that P3081R2's wording still depends on, leaving that dependency without the mechanism that would satisfy it.
candidate 4 (found by 2 of 42 passes): Poll 2 is a process commitment: the layering gets its own paper and its own poll, from whichever side proposes it.

## vehicle - grade 0.50 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/2/1  -> 1.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The deployment record speaks to which architecture matches existing practice.
candidate 2 (found by 1 of 42 passes): The dialect question implicates both models, P3100's implementation-selected semantics and P3984's profile-defined semantics alike, which is one more reason to settle it in a paper of its own rather than as a byproduct of wording review.

## coordination - grade 1.33 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
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
  [11] 6. Six Objections, Answered from Evidence... 0/1/0  -> 0.33
  [12] 7. Three Polls Make the Architecture Ques... 0/1/1  -> 0.67
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Whoever owns the handler owns the response, and under P3100R8 that owner is neither the operation nor any profile - it is the handler.
candidate 2 (found by 2 of 42 passes): Poll 2 also supplies the agreement P3100R8's own Section 7.2 asks for when it says the two features, if both are kept, must be specified one in terms of the other.
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
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [12] 7. Three Polls Make the Architecture Ques... 1/1/1  -> 1.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): One asymmetry belongs on the table: the named-guarantee form has more deployment history today than the implicit-contract-assertion form (Section 4).
candidate 2 (found by 2 of 42 passes): For a decade, the named-guarantee form the Profiles papers describe has shipped under vendor names: - **Core Guidelines checkers:** clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].
candidate 3 (found by 1 of 42 passes): For a decade, the named-guarantee form the Profiles papers describe has shipped under vendor names: Core Guidelines checkers: clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].

-->
