Verdict: Adequate (6/14)

The paper offers some support for its standardization case, but that support is concentrated in motivation, prior art, and implementation experience, while several essential parts of the case are left unaddressed. The thinnest areas concern who is affected, why the standard is the right venue, coordination with other features, and why a library solution would not suffice.

- The paper most clearly establishes why the inconsistency matters and that alternatives and prior work exist.
- It also provides credible implementation experience from a shipping library and testing on current toolchains.
- The most glaring omission is any explanation of who is affected by the problem or why standardization, rather than a library-only approach, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 3 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.50 / 5.50 / 6.00   (all 3 samples: 5.67)
headings: h2 9
on threshold: motivation, implementation
splits: motivation[5] 1/1/2  motivation[6] 1/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                2/2/2  -> 2.00
  [5] 4 DISCUSSION                                 1/1/2  -> 1.33
  [6] 5 HEADER FOR CONSTANTWRAPPER                 1/0/1  -> 0.67
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): As discussed in [P3948R0], because of language inconsistencies, std::constant_wrapper is inconsistently not unwrapping for call and subscript operators whereas all other operators can be found via ADL and the conversion operator implemented in constant_wrapper.
candidate 2 (found by 3 of 30 passes): The most glaring question on this issue is why would we do this for `operator()` and `operator[]` but for none of the other operators. This seems inconsistent.
candidate 3 (found by 2 of 30 passes): We should reconsider the placement of `constant_wrapper` in `<type_traits>`.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                2/2/2  -> 2.00
  [5] 4 DISCUSSION                                 2/2/2  -> 2.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 1/1/1  -> 1.00
  [7] 6 FUTURE WORK?                               2/2/2  -> 2.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): As discussed in [P3948R0], because of language inconsistencies, std::constant_wrapper is inconsistently not unwrapping for call and subscript operators whereas all other operators can be found via ADL and the conversion operator implemented in constant_wrapper.
candidate 2 (found by 3 of 30 passes): Consider the examples discussed in Kozicki [P3792R0], which overload on `constant_wrapper` and the type it is convertible to.
candidate 3 (found by 3 of 30 passes): For reference in libstdc++ we have the following dependencies:
candidate 4 (found by 3 of 30 passes): With this paper, `constant_wrapper` almost achieves parity with what was proposed for `fn_t` / `function_wrapper` by Schultke et al. [P3774R0] and Müller [P3843R2].

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 4 DISCUSSION                                 0/0/0  -> 0.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                2/2/2  -> 2.00
  [5] 4 DISCUSSION                                 1/1/1  -> 1.00
  [6] 5 HEADER FOR CONSTANTWRAPPER                 0/0/0  -> 0.00
  [7] 6 FUTURE WORK?                               0/0/0  -> 0.00
  [8] 7 WORDING                                    0/0/0  -> 0.00
  [9] A ACKNOWLEDGMENTS                            0/0/0  -> 0.00
  [10] B BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): I always had these unwrapping overloads in my implementation of constant_wrapper shipping in the vir-simd library1 (vir::constexpr_wrapper).
candidate 2 (found by 3 of 30 passes): tested on GCC trunk with libstdc++

-->
