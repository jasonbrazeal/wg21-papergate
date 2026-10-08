Verdict: Strong (8/14)

The paper gives a reasonably solid account of how its proposed integration could work alongside existing facilities and what has already been tried in implementations, but it leaves the underlying case for standardization uneven. The strongest material concerns prior art, interoperability, and implementation experience, while the weakest concerns the affected audience and why a library-only solution would be insufficient.

- The paper’s clearest support comes from concrete implementation experience in both libc++ and libstdc++, including availability on Compiler Explorer.
- It also establishes meaningful prior art and interoperability considerations by explaining how the proposed hooks can coexist with legacy assertion mechanisms and share a single ABI entry point.
- The argument for why the facility belongs in the standard is present but leans heavily on migration and centralized handling rather than demonstrating that a library approach cannot suffice.
- The most glaring omission is any identification of who is affected by the problem or why that population’s needs require standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.50   max 9.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 2.00  vehicle 1.50  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.00 / 8.00 / 8.00   (all 3 samples: 8.00)
headings: h2 8 + bold numbered 2
on threshold: vehicle, implementation
splits: prior_art[9] 1/1/0  vehicle[6] 0/0/1  coordination[2] 0/1/1  coordination[5] 1/2/0
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
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
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

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

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 2)
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
  [9] 19 Diagnostics library [diagnostics]         1/1/0  -> 0.67
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Pre- existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.
candidate 2 (found by 3 of 36 passes): In another, similar proposal, [P3311R0], the name `ASSERT_USES_CONTRACTS` was proposed.
candidate 3 (found by 2 of 36 passes): We chose to have the shared contracts ABI perform enforced contract-termination with `std::abort()` rather than `std::terminate()`.
candidate 4 (found by 2 of 36 passes): The header `<cassert>` provides a macro for documenting C++ program assertions and a mechanism for disabling the assertion checks through defining the macro NDEBUG, and a mechanism to integrate with the contract-violation handler through defining the macro __STDC_WANT_ASSERT_USES_CONTRACTS__.

## vehicle - grade 1.50 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  0/0/1  -> 0.33
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 2 (found by 3 of 36 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 3 (found by 2 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.
candidate 4 (found by 1 of 36 passes): The two standard libraries share a single ABI entry point for the `assert` integration.

## coordination - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                1/2/0  -> 1.00
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
candidate 4 (found by 2 of 36 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.

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
