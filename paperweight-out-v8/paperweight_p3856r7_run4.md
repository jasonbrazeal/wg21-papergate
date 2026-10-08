Verdict: Adequate (4/14)

The paper offers only a thin, mostly asserted case for standardizing its proposed metafunction, with the strongest material concentrated in a sample implementation and the weakest in any account of who would use it or how it fits with existing practice. The support is largely self-referential: it gestures at reflection facilities and library mandates, but does not demonstrate a concrete user population, compare against viable alternatives, or explain why a library solution is insufficient.

- The most substantive support is the sample implementation using P2996 reflection facilities, which at least shows the feature can be approximated in current tooling.
- The paper asserts that library implementers already need this functionality internally, but it does not establish that exposing it to users addresses a demonstrated need.
- The discussion of prior art and alternatives is limited to naming other reflection metafunctions the author believes are missing, without analyzing how existing techniques fall short for real use cases.
- The most glaring omission is the absence of any established affected audience, coordination story, or argument for why this cannot be provided as a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.67   accumulate 4.17   max 4.00

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 4.00 / 4.50 / 3.50   (all 3 samples: 3.67)
headings: h2 6
on threshold: none
splits: motivation[4] 1/2/1  vehicle[3] 0/0/1  implementation[4] 2/2/0
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          1/2/1  -> 1.33
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The *is_structural_type check* is valuable wherever values (including small user-defined structs) have to be treated as compile‑time constants, since NTTPs must be structural types.
candidate 2 (found by 2 of 21 passes): yet there is no way to query whether a type is structural.
candidate 3 (found by 2 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996
candidate 4 (found by 1 of 21 passes): yet there is no way to query whether a type is structural. Library mandates clauses mean that library implementers must somehow have this functionality, but it is simply not exposed to users.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 7. Conclusion                                0/0/0  -> 0.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 3 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*

## vehicle - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/1  -> 0.33
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 7. Conclusion                                0/0/0  -> 0.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Library mandates clauses mean that library implementers must somehow have this functionality, but it is simply not exposed to users.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 7. Conclusion                                0/0/0  -> 0.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 7. Conclusion                                0/0/0  -> 0.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/0  -> 1.33
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).
candidate 3 (found by 1 of 21 passes): The code below shows a possible implementation of *is_structural_type,* using Bloomberg’s Clang fork.
candidate 4 (found by 1 of 21 passes): The code below shows a possible implementation of *is_structural_type,* using Bloomberg’s Clang fork. [Godbolt link](https://godbolt.org/z/abGPKx1YM)

-->
