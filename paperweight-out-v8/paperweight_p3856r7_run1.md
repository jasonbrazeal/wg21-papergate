Verdict: Adequate (4/14)

The paper offers some useful groundwork by situating the proposed trait alongside existing reflection facilities and by supplying a sample implementation, but it leaves most of the case for standardization unargued. The thinnest areas are the absence of any concrete affected audience, any reason the standard rather than a library is required, and any discussion of coordination or interoperability.

- The strongest support is the comparison with P2996 reflection metafunctions and the demonstration that the trait can be implemented with existing reflection queries.
- The paper claims the trait matters for compile-time programming and library mandates, but it does not establish who specifically needs it or what problem they cannot solve today.
- The paper does not explain why this belongs in the standard rather than in a user or vendor library.
- The most glaring omission is the complete lack of discussion about coordination with existing proposals or interoperability with other standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 3 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 3.33   accumulate 5.00   max 4.67

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.50 / 4.00 / 4.50   (all 3 samples: 4.00)
headings: h2 6
on threshold: prior_art
splits: motivation[4] 1/2/1  implementation[4] 2/0/2
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
candidate 2 (found by 3 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996
candidate 3 (found by 1 of 21 passes): yet there is no way to query whether a type is structural.
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

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/2  -> 2.00
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In addition, we compare the approaches of using traditional type traits vs. using reflection metafunctions to query type attributes.
candidate 2 (found by 3 of 21 passes): [P2996](http://wg21.link/P2996) introduced several metafunctions *(consteval* functions that operate on *meta::info)* in *<meta>* that mirror existing type traits, such as *is_const_type(info), is_volatile_type(info),* and *is_trivially_copyable_type(info).*
candidate 3 (found by 2 of 21 passes): The approach of using reflection metafunctions to query type attributes appears promising, and likely to yield richer APIs than possible with prior techniques.
candidate 4 (found by 1 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*

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

## implementation - grade 1.33  [binary: max] (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/0/2  -> 1.33
  [5] 7. Conclusion                                1/1/1  -> 1.00
  [6] 8. Acknowledgements                          0/0/0  -> 0.00
  [7] 9. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).
candidate 3 (found by 2 of 21 passes): The code below shows a possible implementation of *is_structural_type,* using Bloomberg’s Clang fork.

-->
