Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing its proposed restriction, particularly through deployed implementation evidence and the committee’s own recent precedent in the standard library, but the case is thinner where it must show that the feature cannot be delivered outside the standard or that coordination across implementations is already settled.

- The strongest support comes from the survey of hardened implementations, which shows termination or trapping as the universal production default for detected core-language violations.
- The paper also benefits from the committee’s adoption of P3878R1, establishing that the same restriction was already accepted for standard-library hardening.
- The weakest area is the claim that a library solution will not suffice, which rests only on the absence of current compiler implementations rather than a demonstrated barrier.
- Coordination and interoperability are asserted through analogy and a single liaison poll, but the paper does not establish that implementers have aligned on the proposed boundary between response and configuration.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 19. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 11.33   accumulate 11.50   max 11.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 1.00  insufficiency 0.17  implementation 2.00
sample agreement: 96 of 112 section-criterion pairs unanimous (86%)
single-sample totals would have been: 11.00 / 11.00 / 12.00   (all 3 samples: 11.17)
headings: h2 15
on threshold: none
splits: motivation[7] 2/0/0  audience[2] 1/0/1  audience[4] 2/1/0  audience[5] 0/2/0
        audience[7] 0/2/0  audience[13] 0/0/1  prior_art[2] 0/2/0  vehicle[9] 0/0/2
        coordination[2] 2/1/1  coordination[9] 0/0/2  coordination[11] 0/1/0
        coordination[12] 0/0/1  insufficiency[2] 0/0/1  implementation[4] 1/1/2
        implementation[8] 1/0/0  implementation[13] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 16 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  2/0/0  -> 0.67
  [8] 5. Where continuing is defined               2/2/2  -> 2.00
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
candidate 3 (found by 3 of 48 passes): The single difference between `enforce` and `observe` is what happens on a normal return from the handler: `enforce` terminates, `observe` continues.
candidate 4 (found by 3 of 48 passes): The deployment record therefore establishes one fact: on a detected core-language violation, the terminating response is the steady-state production default.

## audience - grade 2.00 (fired in 7 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/1/0  -> 1.00
  [5] 2. Two questions inside the one word 'obs... 0/2/0  -> 0.67
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  0/2/0  -> 0.67
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/1  -> 0.33
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate. Both bodies reached consensus against, WG21 by 1-0-2-7-2 and WG14 by 0-0-0-5-2
candidate 2 (found by 2 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 3 (found by 2 of 48 passes): The population is the implementations that detect a core-language violation in production, and the selection rule is every such implementation the authors could identify, recorded in its default or production configuration.
candidate 4 (found by 1 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed

## prior_art - grade 2.00 (fired in 12 of 16 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/0  -> 0.67
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

## vehicle - grade 2.00 (fired in 3 of 16 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/2  -> 0.67
  [10] 7. If continuing must be possible            2/2/2  -> 2.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): P3878R1 [19], adopted into C++26, made the same restriction for standard-library hardened preconditions. The committee adopted it.
candidate 2 (found by 1 of 48 passes): The standard library already does not throw at these moments: `std::vector` reallocation uses `move_if_noexcept` so that a throwing move cannot corrupt the container mid-operation.
candidate 3 (found by 1 of 48 passes): These precedents share three properties, and a continuing facility for core-language checks would need all three.
candidate 4 (found by 1 of 48 passes): The case for a continuing response deserves its strongest statement, and two forms of it are real.

## coordination - grade 1.00 (fired in 4 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/2  -> 0.67
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/1/0  -> 0.33
  [12] 9. The configuration question is separate    0/0/1  -> 0.33
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 1 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.
candidate 3 (found by 1 of 48 passes): Bloomberg maintains `bsls_review`, a companion to `bsls_assert` that logs and continues while a newly tightened check is rolled out, and Bloomberg relies on the availability of that log-and-continue response to add checks to working production code.
candidate 4 (found by 1 of 48 passes): The response question and the configuration question are independent, and a boundary between them is worth stating.

## insufficiency - grade 0.17 (fired in 1 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.

## implementation - grade 2.00  [binary: max] (fired in 8 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/2  -> 1.33
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  1/1/1  -> 1.00
  [8] 5. Where continuing is defined               1/0/0  -> 0.33
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               1/0/0  -> 0.33
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 3 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 3 (found by 3 of 48 passes): a sanitizer logs the same violation site and kind with no contract handler in the program, as Android IntSan's log mode [10] and UBSan's diagnostics [11] do through the tool rather than through a handler.
candidate 4 (found by 3 of 48 passes): Bloomberg maintains `bsls_review`, a companion to `bsls_assert` that logs and continues while a newly tightened check is rolled out, and Bloomberg relies on the availability of that log-and-continue response to add checks to working production code.

-->
