Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it grounds the problem in deployed practice, shows that affected implementations and prior committee work point the same way, and demonstrates real implementation experience. The support is thinnest where the paper needs to connect its proposal to existing ecosystems and to show why the facility cannot be delivered outside the standard, since those arguments lean on analogy and assertion rather than direct evidence.

- The strongest support is the survey of deployed hardened implementations, all of which terminate or trap on detected core-language violations, establishing both who is affected and the implementation reality the paper reasons from.
- The paper also convincingly establishes why the standard is the right venue by pointing to the adopted precedent of P3878R1 and the portable cost of requiring an `observe` semantic.
- The most glaring omission is the coordination and interoperability case, which rests on a single company’s internal tool and a liaison poll rather than on evidence that the proposed facility would fit cleanly with existing contract and hardening machinery.
- Nearly as thin is the claim that a library cannot do the job, since the paper offers no direct demonstration that the needed behavior is impossible or impractical to provide through a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 17. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 12.00   accumulate 11.67   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 2.00  vehicle 1.83  coordination 0.67  insufficiency 0.67  implementation 2.00
sample agreement: 95 of 112 section-criterion pairs unanimous (85%)
single-sample totals would have been: 12.00 / 10.50 / 11.50   (all 3 samples: 11.00)
headings: h2 15
on threshold: implementation
splits: motivation[8] 2/2/1  audience[2] 1/0/1  audience[4] 1/0/2  audience[9] 2/1/2
        audience[13] 0/0/1  vehicle[2] 0/2/0  vehicle[7] 0/0/2  vehicle[8] 2/0/0
        vehicle[9] 0/0/2  vehicle[10] 2/1/2  coordination[2] 0/0/1  coordination[4] 0/0/1
        coordination[9] 0/0/1  coordination[11] 2/1/0  insufficiency[10] 1/0/0
        implementation[5] 2/1/1  implementation[6] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               2/2/1  -> 1.67
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            2/2/2  -> 2.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    1/1/1  -> 1.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 3 of 48 passes): after the violation handler runs on a detected core-language violation, does execution continue past the violation or does the program terminate?
candidate 3 (found by 3 of 48 passes): Availability is the first: a long-running service or a fault-tolerant embedded system may prefer bounded degradation to a hard stop, so that for such a system a violation that terminates is itself the failure.
candidate 4 (found by 3 of 48 passes): A large codebase that turns on a new check needs to find every violation it surfaces before it enforces.

## audience - grade 1.83 (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/0/2  -> 1.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/1/2  -> 1.67
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/1  -> 0.33
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.
candidate 2 (found by 2 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed
candidate 3 (found by 2 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 4 (found by 2 of 48 passes): The population is the implementations that detect a core-language violation in production, and the selection rule is every such implementation the authors could identify, recorded in its default or production configuration.

## prior_art - grade 2.00 (fired in 11 of 16 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  2/2/2  -> 2.00
  [8] 5. Where continuing is defined               2/2/2  -> 2.00
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            2/2/2  -> 2.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    2/2/2  -> 2.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               1/1/1  -> 1.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): P3100R8 [2] proposes to extend that machinery to the runtime-checkable cases of core-language undefined behaviour, and P3878R1, adopted into C++26, already settled the parallel question for standard-library hardening.
candidate 2 (found by 3 of 48 passes): P3100R8 [2] proposes to respecify the runtime-checkable cases of core-language undefined behaviour as implicit contract assertions evaluated with five semantics: the four from C++26 plus a fifth, `assume`, which preserves today's undefined behaviour as an escape hatch.
candidate 3 (found by 3 of 48 passes): Stroustrup's P2698R0 [15] states it: unconditional termination is "a serious problem" for the systems that are not permitted to stop - long-running services, and the fault-tolerant and safety-critical domains where a crash is itself the failure.
candidate 4 (found by 3 of 48 passes): Doumler and Berne write in P3097R2 [20] that once a program *is found to be in a possibly corrupted state, executing any user-defined code could result in a vulnerability.* They keep the `observe` semantic available nonetheless.

## vehicle - grade 1.83 (fired in 6 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/2  -> 0.67
  [8] 5. Where continuing is defined               2/0/0  -> 0.67
  [9] 6. A terminating response                    0/0/2  -> 0.67
  [10] 7. If continuing must be possible            2/1/2  -> 1.67
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): These precedents share three properties, and a continuing facility for core-language checks would need all three.
candidate 2 (found by 2 of 48 passes): P3878R1 [19], adopted into C++26, made the same restriction for standard-library hardened preconditions. The committee adopted it.
candidate 3 (found by 1 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 4 (found by 1 of 48 passes): The cost falls on the portable guarantee rather than on any one build: an implementation required to offer `observe` for all implicit assertions emits the machinery around every checked operation whether or not a given build selects it (Section 5).

## coordination - grade 0.67 (fired in 4 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/1  -> 0.33
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/1  -> 0.33
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               2/1/0  -> 1.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): Bloomberg maintains `bsls_review`, a companion to `bsls_assert` that logs and continues while a newly tightened check is rolled out, and Bloomberg relies on the availability of that log-and-continue response to add checks to working production code.
candidate 2 (found by 1 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 3 (found by 1 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 4 (found by 1 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.

## insufficiency - grade 0.67 (fired in 2 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            1/0/0  -> 0.33
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 1 of 48 passes): The libc++ `observe` semantic is documented in these terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."

## implementation - grade 2.00  [binary: max] (fired in 7 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Two questions inside the one word 'obs... 2/1/1  -> 1.33
  [6] 3. What ships, terminates                    2/0/2  -> 1.33
  [7] 4. The cost, and the rule it already breaks  1/1/1  -> 1.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               1/1/1  -> 1.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 3 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 3 (found by 3 of 48 passes): a sanitizer logs the same violation site and kind with no contract handler in the program, as Android IntSan's log mode [10] and UBSan's diagnostics [11] do through the tool rather than through a handler.
candidate 4 (found by 3 of 48 passes): The implementers who ship hardening declined this.

-->
