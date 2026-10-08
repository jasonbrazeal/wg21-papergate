Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates why the problem is real, who is affected, what alternatives exist, and that deployed implementation experience points toward termination as the steady-state default. The support is thinnest where the paper must connect that experience to the specific standardization vehicle it proposes, particularly in showing that a library solution cannot suffice and that the relevant implementers and adjacent standards bodies are aligned on the design.

- The strongest support comes from the survey of deployed hardened implementations, which shows termination or trapping as the production default across every system the authors could identify.
- The paper also establishes prior art and alternatives convincingly, including P3100R8’s mapping of existing semantics and the documented adoption-aid role of log-and-continue modes.
- The thinnest support is in coordination and interoperability, where the paper relies on analogues and a single liaison poll rather than direct evidence that the proposed core-language assertions will interoperate cleanly with existing hardening practice.
- The most glaring omission is the case for why a library will not do, since the paper cites deployed library facilities like libc++’s `observe` semantic and Bloomberg’s `bsls_review` without showing why those cannot carry the needed behavior.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 16. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 10.67   accumulate 12.50   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 2.00  vehicle 1.67  coordination 1.33  insufficiency 0.50  implementation 2.00
sample agreement: 91 of 112 section-criterion pairs unanimous (81%)
single-sample totals would have been: 11.00 / 12.00 / 13.00   (all 3 samples: 11.33)
headings: h2 15
on threshold: vehicle, implementation
splits: audience[2] 1/2/1  audience[4] 2/1/2  audience[9] 2/1/2  audience[10] 1/1/0
        audience[13] 1/0/0  prior_art[2] 0/2/2  vehicle[2] 0/2/2  vehicle[4] 1/0/0
        vehicle[9] 1/2/0  vehicle[10] 0/0/1  coordination[2] 0/2/1  coordination[7] 0/0/2
        coordination[9] 0/2/2  coordination[10] 2/2/0  insufficiency[2] 1/0/0
        insufficiency[10] 0/0/2  implementation[5] 1/2/0  implementation[6] 0/0/2
        implementation[7] 2/1/1  implementation[8] 0/1/1  implementation[13] 1/0/1
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
candidate 3 (found by 3 of 48 passes): The word `observe` bundles two things that can be separated, the first being the handler invocation (termed "hook" henceforth): the handler is invoked, and it logs the violation, giving a deployment one place to record and report it.
candidate 4 (found by 3 of 48 passes): The deployment record therefore establishes one fact: on a detected core-language violation, the terminating response is the steady-state production default.

## audience - grade 1.83 (fired in 6 of 16 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/1/2  -> 1.67
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    2/2/2  -> 2.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    2/1/2  -> 1.67
  [10] 7. If continuing must be possible            1/1/0  -> 0.67
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               1/0/0  -> 0.33
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 2 (found by 3 of 48 passes): The population is the implementations that detect a core-language violation in production, and the selection rule is every such implementation the authors could identify, recorded in its default or production configuration.
candidate 3 (found by 2 of 48 passes): Termination or trapping is the steady-state production default of every hardened implementation surveyed; the continue modes that ship, such as UBSan's recover mode and Bloomberg's log-and-continue facility, are documented as adoption aids
candidate 4 (found by 2 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate. Both bodies reached consensus against, WG21 by 1-0-2-7-2 and WG14 by 0-0-0-5-2

## prior_art - grade 2.00 (fired in 11 of 16 sections, strong in 10)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/2  -> 1.33
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
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): P3100R8 [2] proposes to respecify the runtime-checkable cases of core-language undefined behaviour as implicit contract assertions evaluated with five semantics: the four from C++26 plus a fifth, `assume`, which preserves today's undefined behaviour as an escape hatch.
candidate 2 (found by 3 of 48 passes): Doumler and Berne write in P3097R2 [20] that once a program *is found to be in a possibly corrupted state, executing any user-defined code could result in a vulnerability.* They keep the `observe` semantic available nonetheless.
candidate 3 (found by 3 of 48 passes): P3100R8 [2] Section 5.4 maps the first to the `ignore` semantic and the second to `quick-enforce`.
candidate 4 (found by 3 of 48 passes): The libc++ `observe` semantic is documented in these terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."

## vehicle - grade 1.67 (fired in 5 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/2  -> 1.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/0/0  -> 0.33
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    1/2/0  -> 1.00
  [10] 7. If continuing must be possible            0/0/1  -> 0.33
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 2 of 48 passes): The standard library already does not throw at these moments: `std::vector` reallocation uses `move_if_noexcept` so that a throwing move cannot corrupt the container mid-operation.
candidate 3 (found by 2 of 48 passes): The standard should offer all four semantics and let each deployment decide.
candidate 4 (found by 1 of 48 passes): The analysis rests on three assumptions, each stated where it is used and gathered here for the reader who reads only the surface:

## coordination - grade 1.33 (fired in 4 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/2  -> 0.67
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/2/2  -> 1.33
  [10] 7. If continuing must be possible            2/2/0  -> 1.33
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 2 of 48 passes): On 2026-07-08, SG22 (C/C++ Liaison) polled whether `assert` should let exceptions thrown from contract-violation handlers propagate.
candidate 3 (found by 1 of 48 passes): The implementers who ship hardening declined this.
candidate 4 (found by 1 of 48 passes): The libc++ `observe` semantic is documented in these terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."

## insufficiency - grade 0.50 (fired in 2 of 16 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Two questions inside the one word 'obs... 0/0/0  -> 0.00
  [6] 3. What ships, terminates                    0/0/0  -> 0.00
  [7] 4. The cost, and the rule it already breaks  0/0/0  -> 0.00
  [8] 5. Where continuing is defined               0/0/0  -> 0.00
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            0/0/2  -> 0.67
  [11] 8. Problems with this analysis               0/0/0  -> 0.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               0/0/0  -> 0.00
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 1 of 48 passes): The libc++ `observe` semantic is documented in these terms: "Continuing execution after a hardening check fails results in undefined behavior; the `observe` semantic is meant to make adopting hardening easier but should not be used outside of the adoption period."

## implementation - grade 2.00  [binary: max] (fired in 8 of 16 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Two questions inside the one word 'obs... 1/2/0  -> 1.00
  [6] 3. What ships, terminates                    0/0/2  -> 0.67
  [7] 4. The cost, and the rule it already breaks  2/1/1  -> 1.33
  [8] 5. Where continuing is defined               0/1/1  -> 0.67
  [9] 6. A terminating response                    0/0/0  -> 0.00
  [10] 7. If continuing must be possible            0/0/0  -> 0.00
  [11] 8. Problems with this analysis               2/2/2  -> 2.00
  [12] 9. The configuration question is separate    0/0/0  -> 0.00
  [13] 10. Conclusion                               1/0/1  -> 0.67
  [14] 11. Disclosure                               0/0/0  -> 0.00
  [15] Acknowledgements                             0/0/0  -> 0.00
  [16] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 48 passes): No compiler yet implements these assertions with any semantic, so the comparison reasons from deployed analogues.
candidate 2 (found by 3 of 48 passes): Bloomberg maintains `bsls_review`, a companion to `bsls_assert` that logs and continues while a newly tightened check is rolled out, and Bloomberg relies on the availability of that log-and-continue response to add checks to working production code.
candidate 3 (found by 2 of 48 passes): A survey of deployed hardened implementations, finding that every one terminates or traps on a detected core-language violation and none makes continuation its production default (Section 3).
candidate 4 (found by 2 of 48 passes): The implementers who ship hardening declined this.

-->
