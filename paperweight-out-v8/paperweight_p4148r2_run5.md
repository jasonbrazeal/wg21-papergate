Verdict: Adequate (7/14)

The paper gives a partial account of why protocol types might belong in the standard, with its strongest evidence coming from the existence of a reference implementation and a clear recognition of related work, but it leaves several core justifications asserted rather than demonstrated. The thinnest support concerns the central question of why this cannot be delivered as a library, which is not addressed at all, and the claims about affected users and interoperability lean heavily on a single recurring sentence about existing type-erasure facilities.

- The paper establishes meaningful implementation experience through a reference implementation and a concrete path toward generative reflection after C++26.
- It shows adequate awareness of prior art, particularly the overlapping `proxy` proposal and the distinction from current reflection facilities.
- Its argument for why the standard should contain this feature is mostly asserted through the claimed gap and the proliferation of type-erasure abstractions, without showing that standardization is necessary.
- The most glaring omission is the absence of any case for why a library solution will not suffice, which leaves the proposal’s standardization rationale incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.33   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 1.83  audience 0.33  prior_art 1.50  vehicle 0.50  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 79 of 84 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 7.00 / 6.50   (all 3 samples: 6.50)
headings: h2 11
on threshold: prior_art, implementation
splits: motivation[4] 0/0/1  motivation[6] 1/2/2  audience[5] 1/1/0  prior_art[2] 1/0/1
        coordination[5] 0/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/1  -> 0.33
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       1/2/2  -> 1.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Any type that provides member functions with the same names and function signatures as those specified by the interface is considered to be *conforming* to the protocol.
candidate 2 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 3 (found by 3 of 36 passes): There is currently no function-type in the standard library that can represent an overload set.
candidate 4 (found by 1 of 36 passes): This paper explores a different approach to proxy and relies on reflection rather than templates for a smaller API surface.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   1/1/0  -> 0.67
  [6] Design                                       0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.

## prior_art - grade 1.50 (fired in 6 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     1/1/1  -> 1.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      1/1/1  -> 1.00
candidate 1 (found by 3 of 36 passes): This paper explores a different approach to proxy and relies on reflection rather than templates for a smaller API surface.
candidate 2 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 3 (found by 3 of 36 passes): `proxy` (P3086, implemented in `ngcpp/proxy`) occupies an overlapping region of the design space: both proposals provide type-erased, non-intrusive runtime polymorphism without requiring inheritance.
candidate 4 (found by 3 of 36 passes): Identifiers in UPPER CASE denote hypothetical reflection primitives or language features that are not currently part of the C++26 reflection proposal ([P2996R13]).

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): This paper proposes protocol types as a first-class library feature that fills this gap.
candidate 2 (found by 1 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 3 (found by 1 of 36 passes): The absence of a language-supported mechanism for dynamic structural typing explains the proliferation of typeerasure-based abstractions.

## coordination - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   0/1/1  -> 0.67
  [6] Design                                       0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     2/2/2  -> 2.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Code generation is currently implemented in a reference implementation with a custom build step but would be better implemented with generative reflection post C++26.
candidate 2 (found by 3 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at [https://github.com/jbcoe/cc-protocol.](https://github.com/jbcoe/cc-protocol)

-->
