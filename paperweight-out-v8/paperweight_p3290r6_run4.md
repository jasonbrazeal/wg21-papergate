Verdict: Strong (9/14)

The paper offers a mixed case for its own standardization, with its strongest material concentrated in implementation experience, prior art, and the rationale for standardizing rather than leaving the facility to libraries. The support is thinnest where the paper needs to show that a library-only approach is insufficient and to substantiate the claimed importance and affected audience.

- The paper’s implementation experience is its strongest asset, with working branches in both libc++ and libstdc++ available on Compiler Explorer.
- The discussion of prior art and alternatives is well supported, including comparison with P3311R0 and the practical header-delegation changes required.
- The case for why the standard should own this facility is established through the value of a central, user-selectable violation handler and a shared ABI entry point.
- The most glaring omission is the absence of any established argument for why a library will not do, leaving a central pillar of the standardization case unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.33/14)

Provisionally addressed: 6 of 7. Provisional points: 9.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.33   corroborated 8.67   accumulate 10.33   max 10.33

## SUMMARY
grades: motivation 1.33  audience 0.50  prior_art 2.00  vehicle 1.50  coordination 2.00  insufficiency 0.00  implementation 2.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 9.00 / 9.00 / 10.00   (all 3 samples: 9.33)
headings: h2 8 + bold numbered 2
on threshold: motivation, vehicle, implementation
splits: motivation[2] 2/2/1  audience[6] 0/0/2  audience[10] 0/0/1  vehicle[5] 1/0/0
        coordination[2] 1/1/0  coordination[5] 0/0/1  coordination[10] 1/1/0
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/1  -> 1.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 2)                1/1/1  -> 1.00
  [6] 3 Implementation Experience                  0/0/0  -> 0.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Pre-existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.
candidate 2 (found by 3 of 36 passes): The primary goal of the integration with `cassert` is not to change the semantics of `cassert` itself but to allow integration with the user’s violation reporting mechanisms.
candidate 3 (found by 3 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## audience - grade 0.50 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                0/0/0  -> 0.00
  [5] 1 Introduction  (part 2 of 2)                0/0/0  -> 0.00
  [6] 3 Implementation Experience                  0/0/2  -> 0.67
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 0/0/1  -> 0.33
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The library API and `assert` integration proposed in this paper have been implemented in branches of GCC (libstdc++) and Clang (libc++) that are available on Compiler Explorer: `https://godbolt.` `org/z/7nvPdYzfc`.
candidate 2 (found by 1 of 36 passes): Providing the beginnings of a migration path for users of legacy assertion facilities — both `assert` and homegrown solutions — is an essential part of making early use of the Contracts facility viable for many users.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                2/2/2  -> 2.00
  [6] 3 Implementation Experience                  1/1/1  -> 1.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Pre-existing contract-checking facilities, such as `assert`, occasionally have fundamentally different semantics and provide completely different control mechanisms for their behavior.
candidate 2 (found by 3 of 36 passes): In another, similar proposal, [P3311R0], the name `ASSERT_USES_CONTRACTS` was proposed.
candidate 3 (found by 3 of 36 passes): An alternative proposal, [P3311R0], proposed using a user-defined macro to control that choice (on the command line or in code).
candidate 4 (found by 3 of 36 passes): The changes to assert are similar, with the most impactful one being that both libraries needed to begin providing their own versions of `assert.h` that delegates to the underlying C library header using `#include_next`.

## vehicle - grade 1.50 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                1/0/0  -> 0.33
  [6] 3 Implementation Experience                  0/0/0  -> 0.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/1  -> 1.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 2 (found by 3 of 36 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 3 (found by 2 of 36 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.
candidate 4 (found by 1 of 36 passes): This is being done intentionally as we hope to see the same macro eventually introduced in C, with the same effective semantics, and having multiple distinct mechanisms for achieving the same results is harmful in the long term.

## coordination - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction  (part 1 of 2)                2/2/2  -> 2.00
  [5] 1 Introduction  (part 2 of 2)                0/0/1  -> 0.33
  [6] 3 Implementation Experience                  2/2/2  -> 2.00
  [7] 4 Wording Changes                            0/0/0  -> 0.00
  [8] 17 Language support library [support]        0/0/0  -> 0.00
  [9] 19 Diagnostics library [diagnostics]         0/0/0  -> 0.00
  [10] 5 Conclusion                                 1/1/0  -> 0.67
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): By having a central and user-selectable contract-violation handler, those who assemble large programs can avoid having distinct libraries producing different bug responses that do not fit into a single and consistent diagnostic and mitigation strategy.
candidate 2 (found by 3 of 36 passes): The two standard libraries share a single ABI entry point for the `assert` integration.
candidate 3 (found by 2 of 36 passes): Integrating these facilities with the contract-violation handler, however, can be an incredibly useful tool for enabling a gradual migration from older facilities to the newer tools provided by the language itself.
candidate 4 (found by 2 of 36 passes): The hooks proposed in this paper allow for such legacy facilities to live side-by-side with C++ contracts, require no major changes to legacy facilities’ existing semantics, and open the door to integration with Contracts as soon as they are available.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 36 passes): Implementations have been performed in both libc++ and libstdc++, which we elaborate on further in Section 3.
candidate 2 (found by 3 of 36 passes): The library API and `assert` integration proposed in this paper have been implemented in branches of GCC (libstdc++) and Clang (libc++) that are available on Compiler Explorer: `https://godbolt.` `org/z/7nvPdYzfc`.

-->
