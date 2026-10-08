Verdict: Adequate to Strong (7/14)

The paper offers a reasonably solid case for standardizing these migration hooks, with its strongest material concentrated in the rationale for centralized violation handling, interoperability with existing facilities, and prior art. The support is thinnest where the paper asserts practical necessity and implementation readiness without fully demonstrating either.

- The paper most convincingly establishes why the standard is the right venue by tying the hooks to a central, user-selectable contract-violation handler and a coherent diagnostic strategy across large programs.
- It also does well in showing prior art and alternatives, including existing assertion semantics and related naming proposals, and in describing how the hooks can coexist with legacy facilities.
- The claim that a library-only solution will not suffice is asserted rather than shown, leaving the boundary between what the core language must provide and what a library could accomplish unclear.
- Implementation experience is the most glaring omission, since the paper acknowledges the work exists but is not publicly available or upstreamed, offering no verifiable evidence of practical use.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 5.67   accumulate 8.50   max 9.67

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.50  vehicle 1.50  coordination 1.50  insufficiency 0.17  implementation 1.00
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.50 / 7.00 / 7.50   (all 3 samples: 7.33)
headings: h2 9
on threshold: motivation, prior_art, vehicle, coordination
splits: audience[9] 0/0/1  coordination[2] 1/0/0  insufficiency[4] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): One of the primary purposes of adopting a Contracts facility into the Standard in lieu of continuing to use bespoke solutions is to centralize the management, response, and mitigation approach to detected bugs in large-scale software.
candidate 2 (found by 3 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 0/0/1  -> 0.33
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## prior_art - grade 1.50 (fired in 5 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  1/1/1  -> 1.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Pre- existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.
candidate 2 (found by 3 of 33 passes): In another, similar proposal, [P3311R0], the name `ASSERT_USES_CONTRACTS` was proposed.
candidate 3 (found by 3 of 33 passes): All of these changes have been implemented (but not yet made publicly available at the time of this revision) in libc++ and libstdc++, alongside the ongoing implementations of [P2900R14] in those compilers.
candidate 4 (found by 3 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## vehicle - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 2 (found by 3 of 33 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 3 (found by 2 of 33 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.
candidate 4 (found by 1 of 33 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## coordination - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposals  (part 1 of 2)                   2/2/2  -> 2.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 2 (found by 3 of 33 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.
candidate 3 (found by 1 of 33 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.

## insufficiency - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/0/0  -> 0.33
  [5] 2 Proposals  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  0/0/0  -> 0.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Because many existing assertion facilities will need to remain committed to behaviors and control mechanisms that may never be perfectly replicated by the core-language Contracts facility

## implementation - grade 1.00  [binary: max] (fired in 2 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Proposals  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 2 Proposals  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 3 Implementation Experience                  1/1/1  -> 1.00
  [8] 4 Wording Changes                            0/0/0  -> 0.00
  [9] 5 Conclusion                                 0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Implementations have been performed in both libc++ and libstdc++, although they have not yet been updated and upstreamed as the updates to the shared Itanium ABI that those implementations will call into are still in progress.
candidate 2 (found by 2 of 33 passes): All of these changes have been implemented (but not yet made publicly available at the time of this revision) in libc++ and libstdc++.
candidate 3 (found by 1 of 33 passes): All of these changes have been implemented (but not yet made publicly available at the time of this revision) in libc++ and libstdc++

-->
