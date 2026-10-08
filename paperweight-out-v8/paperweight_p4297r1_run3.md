Verdict: Strong (8/14)

The paper gives its strongest support on the procedural and historical terrain: it shows that the layering question has been contested across multiple polls and published papers, and that the implementation experience behind the named-guarantee form is real and long-standing. The case is much thinner where it needs to connect that history to a positive reason for standardization now, particularly in explaining why a library solution cannot carry the design and in showing who is concretely affected beyond a single reported cost figure.

- The paper is most persuasive when it reconstructs the seven-poll history and shows that no poll adopted the architecture, while also documenting a decade of shipped vendor implementations for the named-guarantee form.
- It also establishes a genuine coordination problem by showing that P3100R8’s withdrawal of `detection_mode` and related API changes can strand P3081R2’s wording without the coordination the proposal itself says is needed.
- The argument that the standard must act is asserted rather than demonstrated, resting mainly on the claim that the layering decision itself is the standardization question.
- The most glaring omission is the absence of any established explanation for why a library approach will not do, leaving the central justification for a language or standard-level facility unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.33   accumulate 8.50   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.83  vehicle 0.17  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 88 of 98 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.00 / 8.50 / 8.00   (all 3 samples: 8.33)
headings: h2 13
on threshold: coordination, implementation
splits: motivation[7] 0/1/2  motivation[11] 2/1/2  audience[9] 2/0/2  prior_art[6] 2/2/1
        prior_art[8] 1/0/0  prior_art[9] 2/0/2  prior_art[10] 0/2/2  prior_art[12] 2/2/0
        vehicle[9] 0/1/0  coordination[7] 2/2/0
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
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/1/2  -> 1.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 2/1/2  -> 1.67
  [12] 7. Three Polls Make the Architecture Ques... 2/2/2  -> 2.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Interrupting that default now is cheap where reversing it later has cost the committee years.
candidate 2 (found by 2 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 3 (found by 2 of 42 passes): The layering claim sits between two competing bodies of published work
candidate 4 (found by 2 of 42 passes): Without explicit input from EWG, approving the outcomes of the case-by-case review may close the evolution path for Profiles.

## audience - grade 0.67 (fired in 1 of 14 sections, strong in 0)
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
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/0/2  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): deployed across Google server-side production at approximately 0.30% average cost [20].

## prior_art - grade 1.83 (fired in 7 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              2/2/1  -> 1.67
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 1/0/0  -> 0.33
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/0/2  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/2/2  -> 1.33
  [11] 6. Six Objections, Answered from Evidence... 2/2/2  -> 2.00
  [12] 7. Three Polls Make the Architecture Ques... 2/2/0  -> 1.33
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 2 (found by 3 of 42 passes): The layering claim sits between two competing bodies of published work: P3100R8's implicit contract assertions, configured through the Labels facility of P3400R3, and the Profiles work of P3984R0, P3081R2, and P3589R2.
candidate 3 (found by 3 of 42 passes): P3100R8's Section 5.6 withdrew the `detection_mode` enumerators that P3081R2's wording still depends on, leaving that dependency without the mechanism that would satisfy it.
candidate 4 (found by 2 of 42 passes): P3081R1 took the complementary path - it adopted the proposal's API into its own wording - and P3100R8's Section 5.6 then withdrew that API, as Section 2 showed.

## vehicle - grade 0.17 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/1/0  -> 0.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The layering is the decision, not a detail.

## coordination - grade 1.67 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 2/2/0  -> 1.33
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 2/2/2  -> 2.00
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Whoever owns the handler owns the response, and under P3100R8 that owner is neither the operation nor any profile - it is the handler.
candidate 2 (found by 2 of 42 passes): When one feature owns the configuration mechanism, a change to it can leave another paper's wording stranded through independent revision, without the coordination that P3100R8's own Section 7.2 now says is needed.

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
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): For a decade, the named-guarantee form the Profiles papers describe has shipped under vendor names: - **Core Guidelines checkers:** clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].
candidate 2 (found by 1 of 42 passes): For a decade, the named-guarantee form the Profiles papers describe has shipped under vendor names: Core Guidelines checkers: clang-tidy since LLVM 3.8 (March 2016) [16]; MSVC installed by default from VS 2017 [17].

-->
