Verdict: Adequate to Strong (7/14)

The paper gives a mixed account of its own readiness, with the strongest material going to prior art, implementation experience, and the general motivation for dynamic structural interfaces, while the case for standardization itself remains largely asserted rather than demonstrated. The thinnest support appears in the areas that would justify putting this in the standard rather than shipping it as a library, and in showing how it would coordinate with existing facilities.

- The paper is most convincing that the problem is real and that a reflection-based alternative to existing type-erasure approaches has been explored in a working implementation.
- It establishes that related facilities and prior proposals occupy an overlapping design space, giving readers a useful point of comparison.
- It does not establish who specifically would be affected beyond a general appeal to recurring type-erasure needs.
- The most glaring omission is a substantiated case for why this cannot remain a library solution, since the discussion of `proxy` mainly describes its API burden without showing that standardization is necessary to overcome it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.00   accumulate 8.17   max 9.00

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 1.50  vehicle 0.83  coordination 0.33  insufficiency 0.67  implementation 2.00
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 8.00 / 6.00   (all 3 samples: 7.17)
headings: h2 11
on threshold: motivation, prior_art, implementation
splits: motivation[2] 1/0/0  motivation[4] 1/0/0  audience[5] 1/1/0  vehicle[2] 1/0/0
        vehicle[6] 0/2/0  coordination[5] 1/1/0  insufficiency[5] 1/0/1  insufficiency[6] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     1/0/0  -> 0.33
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 3 of 36 passes): There is currently no function-type in the standard library that can represent an overload set.
candidate 3 (found by 1 of 36 passes): Any type that provides member functions with the same names and function signatures as those specified by the interface is considered to be *conforming* to the protocol.
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
candidate 1 (found by 3 of 36 passes): This proposal assumes the availability of static reflection and code injection and focuses solely on the design of the class templates `protocol` and `protocol_view`.
candidate 2 (found by 3 of 36 passes): This paper explores a different approach to proxy and relies on reflection rather than templates for a smaller API surface.
candidate 3 (found by 3 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 4 (found by 3 of 36 passes): `proxy` (P3086, implemented in `ngcpp/proxy`) occupies an overlapping region of the design space: both proposals provide type-erased, non-intrusive runtime polymorphism without requiring inheritance.

## vehicle - grade 0.83 (fired in 3 of 12 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
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
candidate 1 (found by 3 of 36 passes): This paper proposes protocol types as a first-class library feature that fills this gap.
candidate 2 (found by 1 of 36 passes): Ideally both `protocol` and `protocol_view` would be generated by the compiler using static reflection, eliminating hand-written type-erasure boilerplate or custom build steps.
candidate 3 (found by 1 of 36 passes): The `protocol` approach is unobtrusive: any existing struct, including those in third-party headers, can serve as an interface without modification.

## coordination - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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

## insufficiency - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Foreword                                     0/0/0  -> 0.00
  [5] Motivation                                   1/0/1  -> 0.67
  [6] Design                                       1/1/0  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Polls                                        0/0/0  -> 0.00
  [9] Reference Implementation                     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
  [12] Appendix A: Illustrative Implementation      0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Standard library facilities such as `std::function`, `std::any`, `std::ranges::any_view` and the many other typeerasure based solutions demonstrate that the need for dynamic structural interfaces is both real and recurring.
candidate 2 (found by 2 of 36 passes): `proxy` requires the author to build a *Facade* explicitly using the `pro::facade_builder` template, combining dispatch objects such as `pro::member_dispatch` with `add_convention` calls.

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
