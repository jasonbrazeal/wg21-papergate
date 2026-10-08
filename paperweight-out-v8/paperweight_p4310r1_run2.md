Verdict: Strong (8/14)

The paper’s strongest support comes from its survey of deployed implementations and its alignment with the already-adopted direction in P3878R1, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest areas are coordination with existing or in-flight specifications and any explanation of why the same guarantees could not be delivered through a library.

- The paper firmly establishes that production hardened implementations already treat detected core-language precondition violations as terminating by default.
- It also establishes that this position matches the adjacent standard-library hardening decision in C++26 and is consistent with prior art.
- The claims about who is affected and why the standard must act rest on the same deployment evidence but are not independently established.
- The paper does not establish coordination and interoperability with other specifications or explain why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 5 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 8.50 / 8.50 / 8.50   (all 3 samples: 8.33)
headings: h2 11
on threshold: audience, vehicle, implementation
splits: motivation[8] 0/0/1  motivation[9] 2/1/1  audience[2] 0/1/1  audience[9] 1/0/0
        prior_art[5] 0/2/0  prior_art[9] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       2/2/2  -> 2.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/1  -> 0.33
  [9] 6. Conclusion                                2/1/1  -> 1.33
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 2 (found by 3 of 36 passes): It leaves one question open (P4317R1 Section 2.3): after a guarded operation's precondition is detected as violated, does execution continue past the violation or does the program terminate?
candidate 3 (found by 3 of 36 passes): Every entry terminates or traps, and none makes continuation its production default; the continue modes that ship - libc++ `observe`, Bloomberg `bsls_review`, UBSan's recover mode - are documented as adoption or testing aids, not standing configuration.
candidate 4 (found by 3 of 36 passes): Continuing executes user code on a state the language does not define.

## audience - grade 1.33 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                1/0/0  -> 0.33
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The sampled population is every implementation the authors could identify that detects such a violation in production, in its default configuration.
candidate 2 (found by 2 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 3 (found by 1 of 36 passes): Of the responses to a detected core-language violation, the terminating one - invoke the handler, log, terminate - is the production default across every hardened implementation surveyed, and the continuing response is the default in none.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. What ships, terminates                    0/2/0  -> 0.67
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 2/2/2  -> 2.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                2/2/1  -> 1.67
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): continuation runs against P3878R1, the adjacent case C++26 already decided, and it executes on the corrupted state the security literature treats as the more dangerous failure.
candidate 2 (found by 3 of 36 passes): Berne and Lakos recommend in P3558R1 [19] "a default evaluation semantic, when nothing else is specified, of `enforce` for all core-language preconditions."
candidate 3 (found by 3 of 36 passes): It runs against P3878R1 [16] and executes on a state the language does not define.
candidate 4 (found by 2 of 36 passes): P3878R1 [16], adopted into C++26, already settled the same response question for standard-library hardening;

## vehicle - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    0/0/0  -> 0.00
  [6] 3. Why continuing is the wrong default       2/2/2  -> 2.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/0  -> 0.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/0/0  -> 0.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): For a core-language check whose continuation is likewise undefined - a detected null dereference or out-of-bounds access - the same reasoning applies one level down.
candidate 2 (found by 1 of 36 passes): The committee has already decided the adjacent case. P3878R1 [16], adopted into C++26, established that a standard-library hardened precondition may not be evaluated with a non-terminating semantic

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
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
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
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
candidates: (none validated)

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
