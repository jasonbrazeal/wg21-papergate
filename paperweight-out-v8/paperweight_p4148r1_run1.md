Verdict: Adequate to Strong (7/14)

The paper gives a mixed account of its own readiness, with real grounding in prior art and implementation experience but little direct evidence about who would be affected or why a library solution is insufficient. The thinnest parts concern coordination, interoperability, and the core claim that this cannot be done as a library.

- The strongest support comes from the demonstrated overlap with existing type-erasure facilities and the availability of a reference implementation simulating the proposed mechanism.
- The paper establishes that the need for dynamic structural interfaces is recurring, but it does not show who specifically is affected or how widespread that need is.
- The argument for standardization rather than a library is asserted through the absence of language support, but the paper does not establish why a library cannot fill the gap.
- The most glaring omission is any discussion of coordination and interoperability with existing or forthcoming standardization efforts in this space.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.67   accumulate 7.17   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 1.50  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 7.50 / 6.50   (all 3 samples: 6.67)
headings: h2 11
on threshold: prior_art, implementation
splits: audience[5] 0/1/1  vehicle[6] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 3 of 36 passes): There is currently no function-type in the standard library that can represent an overload set.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.

## prior_art - grade 1.50 (fired in 6 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
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
candidate 2 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 3 (found by 3 of 36 passes): `proxy` (P3086, implemented in `ngcpp/proxy`) occupies an overlapping region of the design space: both proposals provide type-erased, non-intrusive runtime polymorphism without requiring inheritance.
candidate 4 (found by 3 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at https://github.com/jbcoe/ccprotocol.

## vehicle - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design                                       0/2/0  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 1 of 36 passes): This paper proposes protocol types as a first-class library feature that fills this gap.
candidate 3 (found by 1 of 36 passes): The absence of a language-supported mechanism for dynamic structural typing explains the proliferation of type-erasure-based abstractions.
candidate 4 (found by 1 of 36 passes): The `protocol` approach is unobtrusive: any existing struct, including those in third-party headers, can serve as an interface without modification.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 2 (found by 2 of 36 passes): A reference implementation, using an AST-based Python code generator to [simulate post-C++26 code injection, is available at https://github.com/jbcoe/ccprotocol.](https://github.com/jbcoe/cc-protocol)
candidate 3 (found by 1 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at https://github.com/jbcoe/ccprotocol.

-->
