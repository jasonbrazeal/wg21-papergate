Verdict: Strong (8/14)

The paper offers solid grounding for why the Lakos Rule matters and for the existence of prior policy debate, but it leaves much of the case for standardization asserted rather than demonstrated. The thinnest support is around why a library-level solution cannot suffice and whether the proposed policy has meaningful implementation experience behind it.

- The paper convincingly establishes the continued engineering importance of the Lakos Rule and the relevance of prior standardization discussions.
- Its strongest evidentiary claim is the quantitative study of existing Standard Library specification, but the study itself is only described, not shown in enough detail to count as established.
- The argument that this must be standardized rather than handled by libraries rests on asserted drawbacks of alternatives without substantiating evidence.
- The most glaring omission is implementation experience: the paper cites an abandoned experiment and claims about major implementations, but does not establish that the proposed policy has been meaningfully tried or validated in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.67   accumulate 7.50   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.33  coordination 1.17  insufficiency 0.17  implementation 0.33
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 8.50 / 7.50 / 8.50   (all 3 samples: 7.50)
headings: h2 12
on threshold: vehicle
splits: vehicle[5] 1/2/2  coordination[5] 2/0/2  insufficiency[5] 1/0/0  implementation[2] 1/0/0
        implementation[5] 0/1/0  implementation[7] 0/0/1
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
  [9] 5 Rationale for adopting a policy            2/2/2  -> 2.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We briefly summarise the rationale why the Lakos Rule is still an important and valuable design principle today – and even more so now that contract assertions are in C++26.
candidate 2 (found by 3 of 39 passes): There are important engineering reasons why the Lakos Rule is still valid and useful today; abandoning it would inflict avoidable damage to the C++ language.
candidate 3 (found by 3 of 39 passes): There are many applications (e.g., in gaming, desktop publishing, host-plugin systems) for which throwing an exception on precondition failure and recovering programmatically is vastly preferable to terminating the program.
candidate 4 (found by 3 of 39 passes): Our analysis demonstrates that the Lakos Rule is the norm in the C++ Standard Library today.

## audience - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/0/0  -> 0.00
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): We present a quantitative study showing that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification

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
candidate 1 (found by 3 of 39 passes): [P1656R2] proposed abandoning the Lakos Rule as a design principle for the C++ Standard Library.
candidate 2 (found by 3 of 39 passes): The first and fourth clusters are deliberate, well-motivated divergences from the `noexcept` policy established via [P0884R0]; the second and third are in line with the policy; the last one indicates recent divergence in the absence of a policy.
candidate 3 (found by 3 of 39 passes): Note that this set of rules corresponds to Policy C in [P3005R0], which considers seven possible `noexcept` policies B-H in addition to the null policy A (“no policy”).
candidate 4 (found by 2 of 39 passes): This paper is a LEWG policy proposal as per [SD-9].

## vehicle - grade 1.33 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  1/2/2  -> 1.67
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            1/1/1  -> 1.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The C++ Standard Library is foundational, therefore it should follow the rule.
candidate 2 (found by 3 of 39 passes): For all of the above reasons, we should put this debate to rest and adopt a `noexcept` policy as soon as possible.

## coordination - grade 1.17 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  2/0/2  -> 1.33
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            1/1/1  -> 1.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The C++ Standard Library continues to drift apart on this question, with the bulk of it adhering to the Lakos Rule as originally intended but newer (C++26) facilities departing from it.
candidate 2 (found by 2 of 39 passes): The C++ Standard Library is foundational, therefore it should follow the rule.

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  1/0/0  -> 0.33
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/0  -> 0.00
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): All known alternatives (death tests via fork, clone, or spawn, `setjmp`/`longjmp`, child threads, signals, conditionalnoexcept macros) are variously platform-specific and non-portable, orders of magnitude slower, UB-prone, or change the code under test

## implementation - grade 0.33  [binary: max] (fired in 3 of 13 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision history                             0/0/0  -> 0.00
  [4] 0 Motivation and context                     0/0/0  -> 0.00
  [5] 1 Rationale                                  0/1/0  -> 0.33
  [6] 2 Prior art in the C++ Standard              0/0/0  -> 0.00
  [7] 3 Status quo in the wider C++ community      0/0/1  -> 0.33
  [8] 4 Proposed policy                            0/0/0  -> 0.00
  [9] 5 Rationale for adopting a policy            0/0/0  -> 0.00
  [10] 6 Proposed wording                           0/0/0  -> 0.00
  [11] Disclaimer                                   0/0/0  -> 0.00
  [12] Acknowledgements                             0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): We present a quantitative study showing that the Lakos Rule is overwhelmingly followed in the existing C++ Standard Library specification, with exceptions to the rule being principled and clearly localised.
candidate 2 (found by 1 of 39 passes): libc++’s `_NOEXCEPT_DEBUG` experiment was abandoned as a “horrible decision”
candidate 3 (found by 1 of 39 passes): The three major implementations of the C++ Standard Library (GCC, Clang, and Microsoft) do not use the Lakos Rule and generally tighten *Throws:* *nothing* to `noexcept`

-->
