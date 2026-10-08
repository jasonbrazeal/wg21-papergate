Verdict: Adequate to Strong (7/14)

The paper gives a credible account of why a reflection-based protocol facility would be useful and shows that the idea has been explored in working code, but it leans heavily on assertion rather than demonstration when arguing that this belongs in the standard and that existing library techniques cannot cover the same ground. The strongest support concerns the existence of a reference implementation and the recognition of prior work; the thinnest concerns the necessity of standardization and the paper’s fit with existing library facilities.

- The paper clearly establishes implementation experience through a reference implementation that simulates the needed code injection.
- It also establishes relevant prior art by situating the proposal alongside `proxy` and other type-erasure facilities.
- The case for why the standard should adopt this, rather than leaving it to a library, is asserted but not substantiated.
- The most glaring omission is the lack of established evidence about who is affected and how the proposal would coordinate with existing standard library components.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.33   accumulate 8.50   max 9.33

## SUMMARY
grades: motivation 1.67  audience 0.50  prior_art 1.50  vehicle 1.00  coordination 0.50  insufficiency 0.33  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 8.00 / 6.50 / 8.00   (all 3 samples: 7.50)
headings: h2 11
on threshold: motivation, prior_art, implementation
splits: motivation[6] 2/1/1  prior_art[2] 1/0/1  vehicle[6] 0/0/1  coordination[5] 0/0/1
        coordination[6] 2/0/0  insufficiency[6] 0/0/2
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     1/1/1  -> 1.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       2/1/1  -> 1.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Any type that provides member functions with the same names and function signatures as those specified by the interface is considered to be *conforming* to the protocol.
candidate 2 (found by 3 of 36 passes): This paper explores a different approach to proxy and relies on reflection rather than templates for a smaller API surface.
candidate 3 (found by 3 of 36 passes): Standard librarie facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 4 (found by 3 of 36 passes): There is currently no function-type in the standard library that can represent an overload set.

## audience - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 36 passes): Standard librarie facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.

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
candidate 2 (found by 3 of 36 passes): Standard librarie facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 3 (found by 3 of 36 passes): `proxy` (P3086, implemented in `ngcpp/proxy`) occupies an overlapping region of the design space: both proposals provide type-erased, non-intrusive runtime polymorphism without requiring inheritance.
candidate 4 (found by 3 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at https://github.com/jbcoe/ccprotocol.

## vehicle - grade 1.00 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design                                       0/0/1  -> 0.33
  [7] Impact on the Standard                       1/1/1  -> 1.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes protocol types as a first-class library feature that fills this gap.
candidate 2 (found by 2 of 36 passes): It requires language support for code injection from static reflection and the addition of a new standard library header `<protocol>`.
candidate 3 (found by 1 of 36 passes): Code generation is currently implemented in a reference implementation with a custom build step but would be better implemented with generative reflection post C++26.
candidate 4 (found by 1 of 36 passes): It requires language support for code injection from static reflection and the addition of a new standard library header `<protocol>.

## coordination - grade 0.50 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   0/0/1  -> 0.33
  [6] Design                                       2/0/0  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Standard librarie facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other type-erasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 1 of 36 passes): Both proposals provide type-erased, non-intrusive runtime polymorphism without requiring inheritance.

## insufficiency - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design                                       0/0/2  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): `proxy` instead requires the author to build a *Facade* explicitly using the `pro::facade_builder` template, combining dispatch objects such as `pro::member_dispatch` with `add_convention` calls.

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
candidate 2 (found by 3 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at https://github.com/jbcoe/ccprotocol.

-->
