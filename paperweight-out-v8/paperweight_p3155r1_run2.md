Verdict: Strong (10/14)

The paper offers substantial support for its standardization case, particularly in showing that the Lakos Rule remains widely followed in the existing standard library specification and that the question has real, ongoing consequences for users and implementers. The thinnest parts are the arguments that a library-level solution cannot suffice and that there is meaningful implementation experience beyond the standard library itself.

- The strongest support comes from the quantitative evidence that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification, grounding the proposal in current practice.
- The paper also clearly establishes why the issue matters and who is affected, including the practical costs of divergence for users who rely on exception-based recovery.
- The case for why a library will not do rests on a single assertion about testing precondition checks, without enough surrounding argument to establish it as a general limitation.
- The most glaring omission is implementation experience, where the paper cites a failed experiment and outside libraries but does not establish that the proposed policy has been validated in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.67/14)

Provisionally addressed: 7 of 7. Provisional points: 9.67 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.67   corroborated 8.33   accumulate 10.33   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 0.17  implementation 1.00
sample agreement: 83 of 91 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.50 / 9.50 / 10.50   (all 3 samples: 9.67)
headings: h2 12
on threshold: audience, vehicle, coordination
splits: motivation[2] 2/1/1  audience[9] 0/0/1  prior_art[5] 0/0/2  coordination[5] 1/2/2
        coordination[7] 2/0/2  insufficiency[5] 0/0/1  implementation[5] 0/1/1
        implementation[7] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/1  -> 1.33
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     2/2/2  -> 2.00
  [5] 1 Rationale                                  2/2/2  -> 2.00
  [6] 2 Prior art in the C++ Standard              2/2/2  -> 2.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We briefly summarise the rationale why the Lakos Rule is still an important and valuable design principle today – and even more so now that contract assertions are in C++26.
candidate 2 (found by 3 of 39 passes): There are important engineering reasons why the Lakos Rule is still valid and useful today; abandoning it would inflict avoidable damage to the C++ language.
candidate 3 (found by 3 of 39 passes): There are many applications (e.g., in gaming, desktop publishing, host-plugin systems) for which throwing an exception on precondition failure and recovering programmatically is vastly preferable to terminating the program.
candidate 4 (found by 3 of 39 passes): While no official policy exists, the C++ Standard Library continues to drift apart on this question, with the bulk of it adhering to the Lakos Rule as originally intended but newer (C++26) facilities departing from it.

## audience - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/0/0  -> 0.00
  [6] 2 Prior art in the C++ Standard              2/2/2  -> 2.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/1  -> 0.33
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We present a quantitative study showing that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification
candidate 2 (found by 3 of 39 passes): we counted 1284 narrow-contract functions in the C++ Standard library (out of 7165 total, i.e. 17.9%).
candidate 3 (found by 1 of 39 passes): The question of which `noexcept` policy the C++ Standard Library should follow has been a hotly debated topic in recent years, taking up a considerable amount of committee time.

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     2/2/2  -> 2.00
  [5] 1 Rationale                                  0/0/2  -> 0.67
  [6] 2 Prior art in the C++ Standard              2/2/2  -> 2.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            2/2/2  -> 2.00
  [9] 5 Rationale for adopting a policy            1/1/1  -> 1.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): It proposes to reconfirm the Lakos Rule (a function having a narrow contract should not be declared `noexcept`), a long-standing design principle of the C++ Standard Library, as an official LEWG design policy.
candidate 2 (found by 3 of 39 passes): [P1656R2] proposed abandoning the Lakos Rule as a design principle for the C++ Standard Library.
candidate 3 (found by 3 of 39 passes): The first and fourth clusters are deliberate, well-motivated divergences from the `noexcept` policy established via [P0884R0]; the second and third are in line with the policy; the last one indicates recent divergence in the absence of a policy.
candidate 4 (found by 3 of 39 passes): Note that this set of rules corresponds to Policy C in [P3005R0], which considers seven possible `noexcept` policies B-H in addition to the null policy A (“no policy”).

## vehicle - grade 1.50 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  2/2/2  -> 2.00
  [6] 2 Prior art in the C++ Standard              1/1/1  -> 1.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The C++ Standard Library is foundational, therefore it should follow the rule.
candidate 2 (found by 3 of 39 passes): Therefore, reinstating the Lakos Rule as official LEWG policy is the only choice consistent with the status quo in the C++ Standard Library specification.

## coordination - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  1/2/2  -> 1.67
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      2/0/2  -> 1.33
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            1/1/1  -> 1.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The C++ Standard Library is foundational, therefore it should follow the rule.
candidate 2 (found by 2 of 39 passes): The three major implementations of the C++ Standard Library (GCC, Clang, and Microsoft) do not use the Lakos Rule and generally tighten *Throws:* *nothing* to `noexcept`, making them incompatible with these techniques
candidate 3 (found by 2 of 39 passes): The question of which `noexcept` policy the C++ Standard Library should follow has been a hotly debated topic in recent years, taking up a considerable amount of committee time.
candidate 4 (found by 1 of 39 passes): The C++ Standard Library continues to drift apart on this question, with the bulk of it adhering to the Lakos Rule as originally intended but newer (C++26) facilities departing from it.

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/0/1  -> 0.33
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): The cleanest, fastest, and only portable and scalable way to test that a precondition check actually fires is to throw from the assertion handler and catch it.

## implementation - grade 1.00  [binary: max] (fired in 3 of 13 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/1/1  -> 0.67
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      1/0/1  -> 0.67
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We present a quantitative study showing that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification, with exceptions to the rule being principled and clearly localised.
candidate 2 (found by 2 of 39 passes): libc++’s `_NOEXCEPT_DEBUG` experiment was abandoned as a “horrible decision”
candidate 3 (found by 2 of 39 passes): other implementations of the Standard Library, or parts of it, such as Bloomberg’s BDE, follow the Lakos Rule and make extensive use of exception-based recovery and negative testing.

-->
