Verdict: Adequate (4/14)

The paper offers a narrow but genuine foundation for its standardization case, centered on the absence of a structural-type query and the value such a query would have for compile-time programming. Beyond that motivating gap, however, the support thins quickly: the affected audience, the need for standardization rather than a library solution, and the interoperability story are all left unaddressed, while the discussion of alternatives and implementation experience remains asserted rather than demonstrated.

- The strongest support is the clearly articulated need for a way to query whether a type is structural, tied to the practical requirement that non-type template parameters be structural types.
- The paper gestures toward prior art and alternatives by referencing P2996 and showing a sample implementation, but it does not establish how its approach compares to or improves upon existing techniques.
- The implementation experience is claimed through a sample using Bloomberg’s Clang fork, yet the paper does not establish that this experience is broad or mature enough to justify standardization.
- The most glaring omission is the complete absence of any case for why this facility belongs in the standard rather than in a library, or how it would coordinate with existing type traits and reflection facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 3 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 3.33   accumulate 4.67   max 4.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 4.50 / 5.00   (all 3 samples: 3.83)
headings: h2 6
on threshold: motivation
splits: prior_art[4] 0/0/2  implementation[3] 0/1/0  implementation[4] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/2  -> 2.00
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): yet there is no way to query whether a type is structural.
candidate 2 (found by 3 of 21 passes): The *is_structural_type check* is valuable wherever values (including small user-defined structs) have to be treated as compile‑time constants, since NTTPs must be structural types.
candidate 3 (found by 2 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996
candidate 4 (found by 1 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          0/0/2  -> 0.67
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 2 of 21 passes): The approach of using reflection metafunctions to query type attributes appears promising, and likely to yield richer APIs than possible with prior techniques.
candidate 3 (found by 1 of 21 passes): Given that we now have two similar facilities in the standard library for inspecting type attributes, how should programmers approach them? Should type traits and reflection metafunctions evolve independently? Should one be implemented in terms of the other?
candidate 4 (found by 1 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/0  -> 0.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/1/0  -> 0.33
  [4] 3. Structural types                          0/2/2  -> 1.33
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).
candidate 2 (found by 2 of 21 passes): The code below shows a possible implementation of *is_structural_type,* using Bloomberg’s Clang fork.
candidate 3 (found by 1 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.

-->
