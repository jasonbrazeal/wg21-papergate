Verdict: Strong (10/14)

The paper offers substantial support for its standardization case in the areas that matter most: it explains why the Lakos Rule remains important, identifies who is affected with concrete quantitative evidence, situates the proposal against prior policy discussions, and argues why the standard library specifically needs this policy. The support is thinnest where the paper moves from principle to practice, since its claims about implementation experience, interoperability with major implementations, and the inadequacy of library-level alternatives are asserted rather than demonstrated.

- The strongest support is the quantitative study showing the Lakos Rule is already the dominant practice in the C++ Standard Library specification.
- The paper also clearly connects the proposal to prior committee work and explains why the standard library, rather than some other context, is the right place for the policy.
- The most glaring omission is the lack of demonstrated implementation experience beyond a brief reference to Bloomberg’s BDE, with no detail on how that experience validates the proposed policy.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 7 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 9.00   accumulate 11.00   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.17  insufficiency 1.00  implementation 1.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 10.50 / 10.50 / 10.00   (all 3 samples: 10.17)
headings: h2 12
on threshold: audience, vehicle, insufficiency
splits: motivation[9] 2/2/1  audience[8] 1/0/1  coordination[7] 2/2/0  implementation[2] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     2/2/2  -> 2.00
  [5] 1 Rationale                                  2/2/2  -> 2.00
  [6] 2 Prior art in the C++ Standard              2/2/2  -> 2.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            2/2/1  -> 1.67
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We briefly summarise the rationale why the Lakos Rule is still an important and valuable design principle today – and even more so now that contract assertions are in C++26.
candidate 2 (found by 3 of 39 passes): There are important engineering reasons why the Lakos Rule is still valid and useful today; abandoning it would inflict avoidable damage to the C++ language.
candidate 3 (found by 3 of 39 passes): There are many applications (e.g., in gaming, desktop publishing, host-plugin systems) for which throwing an exception on precondition failure and recovering programmatically is vastly preferable to terminating the program.
candidate 4 (found by 2 of 39 passes): Our analysis demonstrates that the Lakos Rule is the norm in the C++ Standard Library today. Therefore, reinstating the Lakos Rule as official LEWG policy is the only choice consistent with the status quo in the C++ Standard Library specification.

## audience - grade 1.50 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/0/0  -> 0.00
  [6] 2 Prior art in the C++ Standard              2/2/2  -> 2.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            1/0/1  -> 0.67
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We present a quantitative study showing that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification
candidate 2 (found by 3 of 39 passes): we counted 1284 narrow-contract functions in the C++ Standard library (out of 7165 total, i.e. 17.9%).
candidate 3 (found by 2 of 39 passes): the vast majority of the C++ Standard Library follows today

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     2/2/2  -> 2.00
  [5] 1 Rationale                                  2/2/2  -> 2.00
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

## coordination - grade 1.17 (fired in 3 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  1/1/1  -> 1.00
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      2/2/0  -> 1.33
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            1/1/1  -> 1.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The C++ Standard Library is foundational, therefore it should follow the rule.
candidate 2 (found by 2 of 39 passes): The three major implementations of the C++ Standard Library (GCC, Clang, and Microsoft) do not use the Lakos Rule and generally tighten *Throws:* *nothing* to `noexcept`, making them incompatible with these techniques
candidate 3 (found by 2 of 39 passes): The C++ Standard Library continues to drift apart on this question, with the bulk of it adhering to the Lakos Rule as originally intended but newer (C++26) facilities departing from it.
candidate 4 (found by 1 of 39 passes): This creates inconsistencies and growing technical debt that will need to be retroactively fixed via Defect Reports once we have an agreed-upon policy, which will consume even more committee time.

## insufficiency - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  2/2/2  -> 2.00
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): All known alternatives (death tests via fork, clone, or spawn, `setjmp`/`longjmp`, child threads, signals, conditionalnoexcept macros) are variously platform-specific and non-portable, orders of magnitude slower, UB-prone, or change the code under test

## implementation - grade 1.00  [binary: max] (fired in 2 of 13 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/0/0  -> 0.00
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      1/1/1  -> 1.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): other implementations of the Standard Library, or parts of it, such as Bloomberg’s BDE, follow the Lakos Rule and make extensive use of exception-based recovery and negative testing.
candidate 2 (found by 1 of 39 passes): We present a quantitative study showing that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification, with exceptions to the rule being principled and clearly localised.

-->
