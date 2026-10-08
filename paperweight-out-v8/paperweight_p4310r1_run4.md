Verdict: Strong (8/14)

The paper offers a solid foundation for the narrow claim that production hardened implementations terminate on detected violations, but it leans heavily on that single deployment observation to carry several distinct burdens. The case is thinnest where the paper needs to show who is affected, why the standard is the right venue, how coordination would work, and why a library cannot suffice, since those points are asserted rather than demonstrated with evidence beyond the survey.

- The strongest support is the implementation record showing that every surveyed hardened implementation terminates or traps by default, which directly grounds the paper’s central factual claim.
- The prior-art discussion is also well supported, particularly the alignment with P3878R1 and the security literature’s treatment of continuing on corrupted state.
- The most glaring omission is the absence of evidence connecting the deployment record to a need for standardization rather than a description of existing practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 7 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.17   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 0.33  coordination 0.17  insufficiency 0.17  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.00 / 8.00 / 8.50   (all 3 samples: 8.00)
headings: h2 11
on threshold: audience, implementation
splits: motivation[7] 2/0/0  motivation[8] 1/0/1  audience[2] 1/0/1  audience[9] 0/1/0
        prior_art[5] 2/0/2  vehicle[2] 1/0/0  vehicle[6] 0/0/1  coordination[2] 0/0/1
        insufficiency[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       2/2/2  -> 2.00
  [7] 4. Two carve-outs, and the shape of the r... 2/0/0  -> 0.67
  [8] 5. The substrate and ownership questions ... 1/0/1  -> 0.67
  [9] 6. Conclusion                                1/1/1  -> 1.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It leaves one question open (P4317R1 Section 2.3): after a guarded operation's precondition is detected as violated, does execution continue past the violation or does the program terminate?
candidate 2 (found by 3 of 36 passes): Continuing executes user code on a state the language does not define.
candidate 3 (found by 3 of 36 passes): It runs against P3878R1 [16] and executes on a state the language does not define.
candidate 4 (found by 2 of 36 passes): every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.

## audience - grade 1.33 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/1/0  -> 0.33
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The sampled population is every implementation the authors could identify that detects such a violation in production, in its default configuration.
candidate 2 (found by 2 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 3 (found by 1 of 36 passes): Of the responses to a detected core-language violation, the terminating one - invoke the handler, log, terminate - is the production default across every hardened implementation surveyed, and the continuing response is the default in none.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. What ships, terminates                    2/0/2  -> 1.33
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 2/2/2  -> 2.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                2/2/2  -> 2.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): continuation runs against P3878R1, the adjacent case C++26 already decided, and it executes on the corrupted state the security literature treats as the more dangerous failure.
candidate 2 (found by 3 of 36 passes): It does not reopen the prior question - whether the C++26 Contracts machinery is the right substrate for these checks, given that a contract assertion may be compiled `ignore` and so may never run - which P4332R0 [23] argues against.
candidate 3 (found by 3 of 36 passes): Berne and Lakos recommend in P3558R1 [19] "a default evaluation semantic, when nothing else is specified, of `enforce` for all core-language preconditions."
candidate 4 (found by 3 of 36 passes): It runs against P3878R1 [16] and executes on a state the language does not define.

## vehicle - grade 0.33 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    0/0/0  -> 0.00
  [6] 3. Why continuing is the wrong default       0/0/1  -> 0.33
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/0/0  -> 0.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 2 (found by 1 of 36 passes): For a core-language check whose continuation is likewise undefined - a detected null dereference or out-of-bounds access - the same reasoning applies one level down.

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    0/0/0  -> 0.00
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/0/0  -> 0.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    0/0/0  -> 0.00
  [6] 3. Why continuing is the wrong default       0/1/0  -> 0.33
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/0/0  -> 0.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): A continuing response under Contracts-based undefined-behaviour handling also carries an exception-handling cost.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/0/0  -> 0.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 2 (found by 3 of 36 passes): The sampled population is every implementation the authors could identify that detects such a violation in production, in its default configuration.

-->
