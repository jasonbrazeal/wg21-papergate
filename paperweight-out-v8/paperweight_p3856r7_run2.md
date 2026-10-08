Verdict: Adequate (4/14)

The paper offers a narrow but genuine justification for why a structural-type query would be useful, but it leaves most of the standardization case unargued. The strongest material concerns motivation and a tentative implementation path; the thinnest concerns who is affected, why a library solution is insufficient, and why the standard itself must act.

- The paper establishes that the absence of a structural-type query matters for code that must treat values as compile-time constants through non-type template parameters.
- The paper claims, but does not demonstrate, that prior art and alternatives are meaningfully addressed by its reflection-based sample implementation.
- The paper claims implementation experience, but offers only a sample implementation rather than evidence of broader use or validation.
- The paper does not establish who is affected, why the standard is the right venue, how the feature coordinates with existing or planned features, or why a library cannot suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h2 6
on threshold: motivation
splits: implementation[3] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/2  -> 2.00
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): yet there is no way to query whether a type is structural.
candidate 2 (found by 3 of 21 passes): The *is_structural_type check* is valuable wherever values (including small user-defined structs) have to be treated as compile‑time constants, since NTTPs must be structural types.
candidate 3 (found by 3 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996

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
candidate 2 (found by 3 of 21 passes): The approach of using reflection metafunctions to query type attributes appears promising, and likely to yield richer APIs than possible with prior techniques.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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

## implementation - grade 1.00  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/0/1  -> 0.67
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).
candidate 2 (found by 2 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.

-->
