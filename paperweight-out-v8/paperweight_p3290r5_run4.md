Verdict: Strong (8/14)

The paper offers solid evidence of implementation experience and some useful discussion of prior art and interoperability, but its case for standardization is uneven: it does not identify who is affected, explain why a library solution would be insufficient, or fully establish why the feature matters enough to belong in the standard.

- The strongest support comes from concrete implementation experience in both libc++ and libstdc++, with available Compiler Explorer branches demonstrating the proposed API and `assert` integration.
- The paper also establishes meaningful prior art and coordination considerations, including ABI entry points and cross-committee naming suggestions.
- The argument for why the standard should adopt this is only claimed, leaning on migration and centralization benefits without fully demonstrating that they require standardization.
- Most glaringly, the paper never establishes who is affected or why a library-only approach would not suffice, leaving the affected user base and the necessity of standard action unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 5 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.83   max 8.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 2.00  vehicle 1.33  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 81 of 84 section-criterion pairs unanimous (96%)
single-sample totals would have been: 9.00 / 8.00 / 8.00   (all 3 samples: 8.33)
headings: h2 8 + bold numbered 2
on threshold: vehicle, implementation
splits: motivation[2] 2/0/1  vehicle[4] 2/2/1  coordination[5] 2/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/0/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  0/0/0  -> 0.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.
candidate 2 (found by 2 of 36 passes): Pre- existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  0/0/0  -> 0.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  2/2/2  -> 2.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Pre- existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.
candidate 2 (found by 3 of 36 passes): In another, similar proposal, [P3311R0], the name `ASSERT_USES_CONTRACTS` was proposed.
candidate 3 (found by 3 of 36 passes): We chose to have the shared contracts ABI perform enforced contract-termination with `std::abort()` rather than `std::terminate()`.
candidate 4 (found by 3 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## vehicle - grade 1.33 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/1  -> 1.67
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  0/0/0  -> 0.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 2 (found by 3 of 36 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 3 (found by 2 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.
candidate 4 (found by 1 of 36 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.

## coordination - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                2/0/1  -> 1.00
  [6] 3 Implementation Experience                  2/2/2  -> 2.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 2 (found by 3 of 36 passes): The two standard libraries share a single ABI entry point for the `assert` integration.
candidate 3 (found by 3 of 36 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.
candidate 4 (found by 2 of 36 passes): Given that we hope WG14, the C Standard committee, also pursues adopting a compatible contract-checking facility and integrates it with the same contract-violation handler, we suggest using the common term `ASSERT` instead of the C++-specific spelling of `CASSERT`.

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  0/0/0  -> 0.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                1/1/1  -> 1.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  2/2/2  -> 2.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Implementations have been performed in both libc++ and libstdc++, although they have not yet been updated and upstreamed as the updates to the shared Itanium ABI that those implementations will call into are still in progress.
candidate 2 (found by 3 of 36 passes): The library API and `assert` integration proposed in this paper have been implemented in branches of GCC (libstdc++) and Clang (libc++) that are available on Compiler Explorer: `[Compiler` `Explorer]`.

-->
