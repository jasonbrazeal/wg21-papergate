Verdict: Excellent (12/14)

The paper offers substantial support for standardizing its proposed behavior, with most of the necessary case built on survey evidence, prior art, and implementation experience. The support is thinnest where the paper needs to show that a library solution cannot suffice, since that argument rests on analogy rather than direct demonstration.

- The strongest support comes from the survey of deployed hardened implementations, which consistently terminate or trap on detected core-language violations and none defaults to continuation.
- The paper also establishes clear prior art and alternatives, including P3100R8’s five-semantic model and documented positions from Stroustrup and others on the risks and needs around termination versus continuation.
- Coordination and interoperability are well grounded through SG22 polling, libc++ documentation, and Bloomberg’s production use of log-and-continue tooling.
- The most glaring omission is the failure to establish why a library cannot provide the needed behavior, since the paper concedes no compiler yet implements the assertions and reasons only from deployed analogues rather than from a direct technical barrier.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 11.67   accumulate 12.50   max 12.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 1.67  insufficiency 0.50  implementation 2.00
sample agreement: 96 of 112 section-criterion pairs unanimous (86%)
single-sample totals would have been: 12.00 / 12.00 / 13.50   (all 3 samples: 12.17)
headings: h2 15
on threshold: coordination
splits: audience[2] 0/0/1  audience[4] 0/2/2  audience[5] 2/0/0  prior_art[14] 0/1/1
        vehicle[2] 2/0/2  vehicle[8] 0/0/2  vehicle[10] 0/2/1  coordination[6] 0/0/2
        coordination[10] 0/2/2  coordination[11] 2/0/0  insufficiency[2] 0/0/1
        insufficiency[9] 0/0/2  implementation[8] 1/0/1  implementation[9] 0/0/1
        implementation[10] 0/2/0  implementation[13] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 16 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  2/2/2  -> 2.00
  [8] 5. Where continuing is defined               2/2/2  -> 2.00
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            2/2/2  -> 2.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): For a detected core-language violation, the terminating response - invoke the handler, then terminate - is the default the evidence supports.
candidate 2 (found by 3 of 48 passes): after the violation handler runs on a detected core-language violation, does execution continue past the violation or does the program terminate?
candidate 3 (found by 3 of 48 passes): Availability is the first: a long-running service or a fault-tolerant embedded system may prefer bounded degradation to a hard stop, so that for such a system a violation that terminates is itself the failure.
candidate 4 (found by 3 of 48 passes): A large codebase that turns on a new check needs to find every violation it surfaces before it enforces.

## audience - grade 2.00 (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/2/2  -> 1.33
  [5] 2. Two questions inside the one word 'obs... 2/0/0  -> 0.67
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): The population is the implementations that detect a core-language violation in production, and the selection rule is every such implementation the authors could identify, recorded in its default or production configuration.
candidate 2 (found by 2 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 3 (found by 2 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.
candidate 4 (found by 1 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed;

## prior_art - grade 2.00 (fired in 12 of 16 sections, strong in 11)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
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
  [14] 11. Disclosure                               0/1/1  -> 0.67
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): P3100R8 [2] proposes to respecify the runtime-checkable cases of core-language undefined behaviour as implicit contract assertions evaluated with five semantics: the four from C++26 plus a fifth, `assume`, which preserves today's undefined behaviour as an escape hatch.
candidate 2 (found by 3 of 48 passes): Stroustrup's P2698R0 [15] states it: unconditional termination is "a serious problem" for the systems that are not permitted to stop - long-running services, and the fault-tolerant and safety-critical domains where a crash is itself the failure.
candidate 3 (found by 3 of 48 passes): Doumler and Berne write in P3097R2 [20] that once a program *is found to be in a possibly corrupted state, executing any user-defined code could result in a vulnerability.* They keep the `observe` semantic available nonetheless.
candidate 4 (found by 3 of 48 passes): P3100R8 [2] Section 5.4 maps the first to the `ignore` semantic and the second to `quick-enforce`.

## vehicle - grade 2.00 (fired in 5 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/0/2  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/2  -> 0.67
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            0/2/1  -> 1.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 2 of 48 passes): The standard library already does not throw at these moments: `std::vector` reallocation uses `move_if_noexcept` so that a throwing move cannot corrupt the container mid-operation.
candidate 3 (found by 2 of 48 passes): The standard should offer all four semantics and let each deployment decide.
candidate 4 (found by 1 of 48 passes): The cost is also class-agnostic: it applies to a signed-overflow check that continues into a defined wrapped result just as it applies to an out-of-bounds check that continues into undefined behaviour.

## coordination - grade 1.67 (fired in 4 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/2  -> 0.67
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            0/2/2  -> 1.33
  [11] 8. Problems with this analysis               2/0/0  -> 0.67
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.
candidate 2 (found by 2 of 48 passes): The libc++ `observe` semantic is documented in these terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."
candidate 3 (found by 1 of 48 passes): The population is the implementations that detect a core-language violation in production, and the selection rule is every such implementation the authors could identify, recorded in its default or production configuration.
candidate 4 (found by 1 of 48 passes): Bloomberg maintains `bsls_review`, a companion to `bsls_assert` that logs and continues while a newly tightened check is rolled out, and Bloomberg relies on the availability of that log-and-continue response to add checks to working production code.

## insufficiency - grade 0.50 (fired in 2 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/2  -> 0.67
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 1 of 48 passes): The standard library already does not throw at these moments: `std::vector` reallocation uses `move_if_noexcept` so that a throwing move cannot corrupt the container mid-operation.

## implementation - grade 2.00  [binary: max] (fired in 9 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  1/1/1  -> 1.00
  [8] 5. Where continuing is defined               1/0/1  -> 0.67
  [9] 6. A terminating response                    0/0/1  -> 0.33
  [10] 7. If continuing must be possible            0/2/0  -> 0.67
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/1/1  -> 0.67
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 3 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 3 (found by 3 of 48 passes): a sanitizer logs the same violation site and kind with no contract handler in the program, as Android IntSan's log mode [10] and UBSan's diagnostics [11] do through the tool rather than through a handler.
candidate 4 (found by 3 of 48 passes): The implementers who ship hardening declined this.

-->
