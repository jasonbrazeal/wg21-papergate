Verdict: Adequate (6/14)

The paper offers some support for its standardization case, chiefly by identifying a real language inconsistency and showing that the proposed overloads have been implemented and tested. However, the argument is thin where it matters most: it does not establish why this belongs in the standard rather than in a library, nor does it address coordination with other proposals or existing practice beyond a single implementation.

- The strongest support is the identification of an inconsistency in how `constant_wrapper` behaves for call and subscript operators compared with other operators.
- The paper also benefits from concrete implementation experience, including shipping code and testing on GCC trunk with libstdc++.
- The most glaring omission is the absence of any case for why the standard is the right venue, as opposed to a library solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 1.83  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 6.00 / 5.50   (all 3 samples: 6.00)
headings: h2 8
on threshold: implementation
splits: motivation[5] 2/2/1  audience[4] 1/0/0  prior_art[4] 2/0/2
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                2/2/2  -> 2.00
  [5] 4 DISCUSSION                                 2/2/1  -> 1.67
  [6] 5 HEADER FOR CONSTANTWRAPPER                 1/1/1  -> 1.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The most glaring question on this issue is why would we do this for `operator()` and `operator[]` but for none of the other operators. This seems inconsistent.
candidate 2 (found by 2 of 27 passes): Because of language inconsistencies, std::constant_wrapper is inconsistently not unwrapping for call and subscript operators whereas all other operators can be found via ADL and the conversion operator implemented in constant_wrapper.
candidate 3 (found by 2 of 27 passes): We should reconsider the placement of `constant_wrapper` in `<type_traits>`.
candidate 4 (found by 1 of 27 passes): As discussed in [P3948R0], because of language inconsistencies, std::constant_wrapper is inconsistently not unwrapping for call and subscript operators whereas all other operators can be found via ADL and the conversion operator implemented in constant_wrapper.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                1/0/0  -> 0.33
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): I always had these unwrapping overloads in my implementation of constant_wrapper shipping in the vir-simd library1 (vir::constexpr_wrapper).

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                2/0/2  -> 1.33
  [5] 4 DISCUSSION                                 2/2/2  -> 2.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 1/1/1  -> 1.00
  [7] 6 FUTURE WORK?                               2/2/2  -> 2.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Relative to [P3978R1], this paper’s wording has the following change:
candidate 2 (found by 3 of 27 passes): For reference in libstdc++ we have the following dependencies:
candidate 3 (found by 3 of 27 passes): With this paper, `constant_wrapper` almost achieves parity with what was proposed for `fn_t` / `function_wrapper` by Schultke et al. [P3774R0] and Müller [P3843R2].
candidate 4 (found by 2 of 27 passes): As discussed in [P3948R0], because of language inconsistencies, std::constant_wrapper is inconsistently not unwrapping for call and subscript operators whereas all other operators can be found via ADL and the conversion operator implemented in constant_wrapper.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                2/2/2  -> 2.00
  [5] 4 DISCUSSION                                 1/1/1  -> 1.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [9] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): I always had these unwrapping overloads in my implementation of constant_wrapper shipping in the vir-simd library1 (vir::constexpr_wrapper).
candidate 2 (found by 3 of 27 passes): tested on GCC trunk with libstdc++

-->
