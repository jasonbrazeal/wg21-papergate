Verdict: Strong (8/14)

The paper offers substantial support for its standardization case in the areas that are easiest to verify against deployed practice, but it leaves the argument thinnest where it needs to show that the standard is the right place for the change and that the change would fit with existing machinery.

- The strongest support is the deployment record, which shows that every surveyed hardened implementation that detects the relevant core-language violation in production terminates or traps by default, with none defaulting to continuation.
- The paper also establishes who is affected by grounding its population in the implementations that actually detect such violations in their default configurations, rather than a hypothetical audience.
- The case for prior art and alternatives is established through engagement with existing proposals and the documented `observe` semantic in libc++.
- The most glaring omission is any established account of coordination and interoperability, and the paper likewise does not establish why a library solution would be insufficient or why the standard is the necessary venue.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.33   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.00 / 8.00 / 8.00   (all 3 samples: 8.00)
headings: h2 11
on threshold: audience, implementation
splits: motivation[7] 0/1/0  audience[7] 0/0/1  audience[9] 0/1/0  prior_art[2] 0/2/2
        prior_art[6] 2/2/0  prior_art[9] 2/1/2  implementation[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       2/2/2  -> 2.00
  [7] 4. Two carve-outs, and the shape of the r... 0/1/0  -> 0.33
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                1/1/1  -> 1.00
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It leaves one question open (P4317R1 Section 2.3): after a guarded operation's precondition is detected as violated, does execution continue past the violation or does the program terminate?
candidate 2 (found by 3 of 36 passes): What deployed hardening does on a detected core-language violation is uniform; P4317R1 [22] Section 6 assembles the full record with sources, and Table 1 summarizes it.
candidate 3 (found by 3 of 36 passes): Of the responses to a detected core-language violation, the terminating one - invoke the handler, log, terminate - is the production default across every hardened implementation surveyed, and the continuing response is the default in none.
candidate 4 (found by 2 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.

## audience - grade 1.50 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 0/0/1  -> 0.33
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/1/0  -> 0.33
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The sampled population is every implementation the authors could identify that detects such a violation in production, in its default configuration.
candidate 2 (found by 2 of 36 passes): every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 3 (found by 1 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 4 (found by 1 of 36 passes): libc++ documents its `observe` semantic in exactly those terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/2  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       2/2/0  -> 1.33
  [7] 4. Two carve-outs, and the shape of the r... 2/2/2  -> 2.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                2/1/2  -> 1.67
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Berne and Lakos recommend in P3558R1 [19] "a default evaluation semantic, when nothing else is specified, of `enforce` for all core-language preconditions."
candidate 2 (found by 3 of 36 passes): It runs against P3878R1 [16] and executes on a state the language does not define.
candidate 3 (found by 2 of 36 passes): This paper answers terminate. Whether contracts are the right substrate for these checks at all is argued against them in P4332R0; this paper takes a check that runs and argues only the response.
candidate 4 (found by 2 of 36 passes): P4317R1 [22] proposes `std::core_ub`, a profile under the P3589R2 [21] framework that guards the runtime-checkable cases of core-language undefined behaviour and, when enforced over a region, guarantees the check is performed.

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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
candidate 1 (found by 3 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. What ships, terminates                    2/2/2  -> 2.00
  [6] 3. Why continuing is the wrong default       0/0/0  -> 0.00
  [7] 4. Two carve-outs, and the shape of the r... 1/1/1  -> 1.00
  [8] 5. The substrate and ownership questions ... 0/0/0  -> 0.00
  [9] 6. Conclusion                                0/1/0  -> 0.33
  [10] 7. Disclosure                                0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The evidence is the deployment record: every hardened implementation surveyed that detects such a violation in production terminates or traps, and none defaults to continuation.
candidate 2 (found by 3 of 36 passes): The sampled population is every implementation the authors could identify that detects such a violation in production, in its default configuration.
candidate 3 (found by 3 of 36 passes): libc++ documents its `observe` semantic in exactly those terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."
candidate 4 (found by 1 of 36 passes): Of the responses to a detected core-language violation, the terminating one - invoke the handler, log, terminate - is the production default across every hardened implementation surveyed

-->
