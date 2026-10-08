Verdict: Adequate to Strong (7/14)

The paper offers solid support for the central architectural question it raises, particularly in showing that the layering decision is contested, consequential, and grounded in a documented history of prior work. Its case is much thinner, however, when it comes to demonstrating why standardization is necessary, how the affected communities would coordinate, and what implementation experience actually validates the preferred architecture.

- The strongest support is the reconstruction of the seven-poll history and the published record showing that the layering question is substantive and unresolved.
- The paper clearly establishes that the choice between Labels and Profiles determines who controls runtime checking configuration, and that the two bodies of work cannot both serve as the foundation.
- The claims about deployment cost and the named-guarantee form having more implementation history are asserted but not substantiated with evidence sufficient to carry the standardization argument.
- The most glaring omission is the absence of any case for why a library solution would not suffice, leaving the core rationale for standardization unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 17. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.00   accumulate 6.67   max 8.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 1.83  vehicle 0.17  coordination 0.83  insufficiency 0.00  implementation 0.67
sample agreement: 88 of 98 section-criterion pairs unanimous (90%)
single-sample totals would have been: 6.50 / 8.50 / 6.00   (all 3 samples: 6.50)
headings: h2 13
on threshold: audience
splits: motivation[11] 1/2/1  prior_art[6] 1/2/2  prior_art[7] 2/0/0  prior_art[8] 0/0/2
        prior_art[9] 0/2/2  vehicle[9] 1/0/0  coordination[9] 0/2/2  coordination[11] 0/1/0
        implementation[9] 0/2/0  implementation[12] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 3)  (SHARED PASSAGE)
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
  [11] 6. Six Objections, Answered from Evidence... 1/2/1  -> 1.33
  [12] 7. Three Polls Make the Architecture Ques... 2/2/2  -> 2.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The two competing bodies of work named in Section 1 can coexist, but they cannot both be the foundation.
candidate 2 (found by 3 of 42 passes): The deployment record speaks to which architecture matches existing practice.
candidate 3 (found by 3 of 42 passes): Interrupting that default now is cheap where reversing it later has cost the committee years.
candidate 4 (found by 2 of 42 passes): The claim decides who owns the configuration of runtime checking.

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
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): deployed across Google server-side production at approximately 0.30% average cost [20].

## prior_art - grade 1.83 (fired in 6 of 14 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              1/2/2  -> 1.67
  [7] 2. P3100 Characterizes Profiles as a Pres... 2/0/0  -> 0.67
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/2  -> 0.67
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/2/2  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 2/2/2  -> 2.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper reconstructs the proposal's seven-poll history and shows none adopted the architecture, reports that no published paper contests the characterization, and illustrates that the layering question is substantive, contested, and grounded in a decade of deployment evidence.
candidate 2 (found by 3 of 42 passes): The layering claim sits between two competing bodies of published work: P3100R8's implicit contract assertions, configured through the Labels facility of P3400R3, and the Profiles work of P3984R0, P3081R2, and P3589R2.
candidate 3 (found by 2 of 42 passes): P3100R8's Section 7.2 requires that either Labels or the Profiles framework be specified in terms of the other, and the proposal nominates Labels, sketching a profile as "essentially a declaration that expands to [P3400R3] directives".
candidate 4 (found by 2 of 42 passes): P3100R8's Section 7.2 says that if both features are kept, one must be specified in terms of the other, and the proposal makes that choice in Labels' favor.

## vehicle - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
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
  [9] 4. The Claim Decides Who Owns Runtime-Che... 1/0/0  -> 0.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The deployment record speaks to which architecture matches existing practice.

## coordination - grade 0.83 (fired in 2 of 14 sections, strong in 0)
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
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/2/2  -> 1.33
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/1/0  -> 0.33
  [12] 7. Three Polls Make the Architecture Ques... 0/0/0  -> 0.00
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Every one of these is a named, vendor-defined set of guarantees. None routes through the `std::contracts` violation handler adopted for C++26, and none is configured by a Label.
candidate 2 (found by 1 of 42 passes): P3100R8's Section 5.6 withdrew the `detection_mode` enumerators that P3081R2's wording still depends on, leaving that dependency without the mechanism that would satisfy it.

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

## implementation - grade 0.67  [binary: max] (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] Revision History                             0/0/0  -> 0.00
  [6] 1. Introduction                              0/0/0  -> 0.00
  [7] 2. P3100 Characterizes Profiles as a Pres... 0/0/0  -> 0.00
  [8] 3. Seven Polls Advanced the Paper; None A... 0/0/0  -> 0.00
  [9] 4. The Claim Decides Who Owns Runtime-Che... 0/2/0  -> 0.67
  [10] 5. No Published Paper Contests the Charac... 0/0/0  -> 0.00
  [11] 6. Six Objections, Answered from Evidence... 0/0/0  -> 0.00
  [12] 7. Three Polls Make the Architecture Ques... 1/0/0  -> 0.33
  [13] 8. Disclosure                                0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The deployment record speaks to which architecture matches existing practice.
candidate 2 (found by 1 of 42 passes): One asymmetry belongs on the table: the named-guarantee form has more deployment history today than the implicit-contract-assertion form (Section 4).

-->
