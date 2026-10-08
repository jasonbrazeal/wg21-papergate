Verdict: Strong (8/14)

The paper offers solid grounding for the existence of a recurring problem and for its chosen technical direction, but it does not convincingly show why the proposed facility belongs in the standard rather than in a library or existing framework. The strongest support concerns prior art and implementation experience, while the case for affected users, standardization need, and interoperability remains largely asserted rather than demonstrated.

- The paper clearly establishes that type-erasure-based facilities are recurring and that a reflection-based approach is a distinct alternative with a working reference implementation.
- The discussion of `proxy` and the available code generator gives credible evidence that the design space has been explored and that the idea is implementable.
- The paper only claims, without substantiating, that the absence of a language-supported mechanism explains the proliferation of type-erasure abstractions and therefore justifies standardization.
- The thinnest part is the failure to establish why a library solution will not suffice, since the objection to `proxy` is described but not developed into a case that standardization is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 7 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 10.00   accumulate 8.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 1.83  vehicle 0.50  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.50 / 7.50 / 8.50   (all 3 samples: 7.83)
headings: h2 11
on threshold: implementation
splits: motivation[2] 0/1/1  motivation[4] 0/1/1  prior_art[5] 1/2/2  insufficiency[6] 1/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/1/1  -> 0.67
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 3 of 36 passes): There is currently no function-type in the standard library that can represent an overload set.
candidate 3 (found by 2 of 36 passes): Any type that provides member functions with the same names and function signatures as those specified by the interface is considered to be *conforming* to the protocol.
candidate 4 (found by 2 of 36 passes): This paper explores a different approach to proxy and relies on reflection rather than templates for a smaller API surface.

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
candidate 1 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.

## prior_art - grade 1.83 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     1/1/1  -> 1.00
  [5] Motivation                                   1/2/2  -> 1.67
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
candidate 4 (found by 3 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at [https://github.com/jbcoe/cc-protocol.](https://github.com/jbcoe/cc-protocol)

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
candidate 1 (found by 2 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 1 of 36 passes): The absence of a language-supported mechanism for dynamic structural typing explains the proliferation of typeerasure-based abstractions.

## coordination - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.

## insufficiency - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design                                       1/0/2  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): `proxy` requires the author to build a *Facade* explicitly using the `pro::facade_builder` template, combining dispatch objects such as `pro::member_dispatch` with `add_convention` calls.

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
candidate 2 (found by 3 of 36 passes): A reference implementation, using an AST-based Python code generator to simulate post-C++26 code injection, is available at [https://github.com/jbcoe/cc-protocol.](https://github.com/jbcoe/cc-protocol)

-->
