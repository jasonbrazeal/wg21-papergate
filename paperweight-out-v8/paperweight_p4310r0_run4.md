Verdict: Excellent (13/14)

The paper builds a broadly convincing case that the question it raises belongs in the standard, with most of the necessary support resting on deployed practice and prior committee decisions rather than on direct implementation of the proposed facility. The thinnest part of the argument is the claim that a library cannot provide what is needed, which is asserted more through analogy and cost reasoning than through demonstration.

- The strongest support comes from the consistent production behavior of every surveyed hardened implementation, which terminates or traps by default and treats continuing modes as adoption aids rather than steady-state semantics.
- The paper also grounds its standardization case well in prior art, particularly the C++26 standard-library hardening decision and the documented positions of key authors and study groups.
- The most glaring omission is the failure to establish why a library solution would be insufficient, since the argument leans on an analogy to `std::vector` and a cost claim without showing that a library specification could not carry the same guarantee.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.50/14)

Provisionally addressed: 7 of 7. Provisional points: 12.50 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.50   corroborated 12.00   accumulate 12.67   max 13.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 1.67  insufficiency 0.83  implementation 2.00
sample agreement: 100 of 112 section-criterion pairs unanimous (89%)
single-sample totals would have been: 12.00 / 12.00 / 13.50   (all 3 samples: 12.50)
headings: h2 15
on threshold: coordination, implementation
splits: motivation[8] 2/2/1  audience[4] 2/0/0  prior_art[2] 2/2/0  prior_art[10] 2/0/2
        vehicle[9] 2/2/1  vehicle[10] 1/2/1  coordination[9] 2/0/2  coordination[10] 1/0/0
        insufficiency[8] 0/0/1  insufficiency[9] 0/2/2  implementation[5] 2/2/0
        implementation[8] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 16 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  2/2/2  -> 2.00
  [8] 5. Where continuing is defined               2/2/1  -> 1.67
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            2/2/2  -> 2.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    1/1/1  -> 1.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): For a detected core-language violation, the terminating response - invoke the handler, then terminate - is the default the evidence supports.
candidate 2 (found by 3 of 48 passes): after the violation handler runs on a detected core-language violation, does execution continue past the violation or does the program terminate?
candidate 3 (found by 3 of 48 passes): The cost falls on the portable guarantee rather than on any one build: an implementation required to offer `observe` for all implicit assertions emits the machinery around every checked operation whether or not a given build selects it (Section 5).
candidate 4 (found by 3 of 48 passes): The question the evidence leaves standing is who requires that response, and no surveyed deployment answers it.

## audience - grade 2.00 (fired in 4 of 16 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/0/0  -> 0.67
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
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
candidate 1 (found by 2 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed
candidate 2 (found by 2 of 48 passes): The population is the implementations that detect a core-language violation in production, and the selection rule is every such implementation the authors could identify, recorded in its default or production configuration.
candidate 3 (found by 2 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate. Both bodies reached consensus against, WG21 by 1-0-2-7-2 and WG14 by 0-0-0-5-2
candidate 4 (found by 1 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed; the continue modes that ship, such as UBSan's recover mode and Bloomberg's log-and-continue facility, are documented as adoption aids

## prior_art - grade 2.00 (fired in 11 of 16 sections, strong in 9)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/0  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Two questions inside the one word 'obs... 2/2/2  -> 2.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  2/2/2  -> 2.00
  [8] 5. Where continuing is defined               2/2/2  -> 2.00
  [9] 6. A terminating response                    2/2/2  -> 2.00
  [10] 7. If continuing must be possible            2/0/2  -> 1.33
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    2/2/2  -> 2.00
  [13] 10. Conclusion                               2/2/2  -> 2.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): P3878R1, adopted into C++26, already settled the parallel question for standard-library hardening.
candidate 2 (found by 3 of 48 passes): P3100R8 [2] proposes to respecify the runtime-checkable cases of core-language undefined behaviour as implicit contract assertions evaluated with five semantics: the four from C++26 plus a fifth, `assume`, which preserves today's undefined behaviour as an escape hatch.
candidate 3 (found by 3 of 48 passes): Stroustrup's P2698R0 [15] states it: unconditional termination is "a serious problem" for the systems that are not permitted to stop - long-running services, and the fault-tolerant and safety-critical domains where a crash is itself the failure.
candidate 4 (found by 3 of 48 passes): Doumler and Berne write in P3097R2 [20] that once a program *is found to be in a possibly corrupted state, executing any user-defined code could result in a vulnerability.* They keep the `observe` semantic available nonetheless.

## vehicle - grade 2.00 (fired in 4 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/2/1  -> 1.67
  [10] 7. If continuing must be possible            1/2/1  -> 1.33
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 2 of 48 passes): The standard library already does not throw at these moments: `std::vector` reallocation uses `move_if_noexcept` so that a throwing move cannot corrupt the container mid-operation.
candidate 3 (found by 2 of 48 passes): A continuing response has a defensible shape, and the field already uses it.
candidate 4 (found by 2 of 48 passes): The standard should offer all four semantics and let each deployment decide. Restricting the menu takes a legitimate choice away from teams that need it.

## coordination - grade 1.67 (fired in 3 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/0/2  -> 1.33
  [10] 7. If continuing must be possible            1/0/0  -> 0.33
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 2 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.
candidate 3 (found by 1 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed; the continue modes that ship, such as UBSan's recover mode and Bloomberg's log-and-continue facility, are documented as adoption aids
candidate 4 (found by 1 of 48 passes): The libc++ `observe` semantic is documented in these terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."

## insufficiency - grade 0.83 (fired in 2 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/1  -> 0.33
  [9] 6. A terminating response                    0/2/2  -> 1.33
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): The standard library already does not throw at these moments: `std::vector` reallocation uses `move_if_noexcept` so that a throwing move cannot corrupt the container mid-operation.
candidate 2 (found by 1 of 48 passes): This makes the cost a property of the specification rather than of any deployer's choice: an implementation that offers `observe` must emit the machinery whether or not a given build selects it.

## implementation - grade 2.00  [binary: max] (fired in 7 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Two questions inside the one word 'obs... 2/2/0  -> 1.33
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  1/1/1  -> 1.00
  [8] 5. Where continuing is defined               0/0/1  -> 0.33
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               1/1/1  -> 1.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 3 of 48 passes): The implementers who ship hardening declined this.
candidate 3 (found by 3 of 48 passes): Bloomberg maintains `bsls_review`, a companion to `bsls_assert` that logs and continues while a newly tightened check is rolled out, and Bloomberg relies on the availability of that log-and-continue response to add checks to working production code.
candidate 4 (found by 3 of 48 passes): Because no compiler yet implements these assertions, the finding rests on deployed analogues rather than a conforming implementation.

-->
