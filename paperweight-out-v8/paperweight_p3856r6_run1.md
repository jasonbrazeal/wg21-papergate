Verdict: Weak to Adequate (4/14)

The paper offers only a partial case for its own standardization, with most of its supporting arguments asserted rather than demonstrated. The thinnest areas are the absence of any identified affected users, the lack of a clear reason why a library solution would not suffice, and the absence of implementation experience beyond a sample built on other proposed facilities.

- The strongest support is the paper’s claim that library implementers already need this functionality internally, even if it is not exposed to users.
- The paper gestures at prior art and alternatives by referencing P2996 and offering a sample implementation, but it does not establish that these approaches are inadequate.
- The paper does not establish who is affected by the missing facility, leaving the motivating audience unclear.
- The most glaring omission is the failure to show why a library cannot provide the capability, which is central to justifying a standard language or library feature.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 5 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 3.67   accumulate 4.83   max 4.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.17  vehicle 0.17  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 3.00 / 4.50 / 4.50   (all 3 samples: 3.83)
headings: h2 6
on threshold: motivation
splits: motivation[4] 1/2/2  prior_art[4] 0/2/2  vehicle[3] 0/0/1  coordination[3] 0/1/0
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          1/2/2  -> 1.67
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The *is_structural_type check* is valuable wherever values (including small user-defined structs) have to be treated as compile‑time constants, since NTTPs must be structural types.
candidate 2 (found by 3 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996
candidate 3 (found by 2 of 21 passes): yet there is no way to query whether a type is structural. Library mandates clauses mean that library implementers must somehow have this functionality, but it is simply not exposed to users.
candidate 4 (found by 1 of 21 passes): yet there is no way to query whether a type is structural.

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

## prior_art - grade 1.17 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          0/2/2  -> 1.33
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 3 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*
candidate 3 (found by 1 of 21 passes): Given that we now have two similar facilities in the standard library for inspecting type attributes, how should programmers approach them? Should type traits and reflection metafunctions evolve independently? Should one be implemented in terms of the other?
candidate 4 (found by 1 of 21 passes): [P2996](http://wg21.link/P2996) introduced several metafunctions *(consteval* functions that operate on *meta::info)* in *<meta>* that mirror existing type traits, such as *is_const_type(info), is_volatile_type(info),* and *is_trivially_copyable_type(info).*

## vehicle - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/0/1  -> 0.33
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Library mandates clauses mean that library implementers must somehow have this functionality, but it is simply not exposed to users.

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              0/1/0  -> 0.33
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Library mandates clauses mean that library implementers must somehow have this functionality, but it is simply not exposed to users.

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

## implementation - grade 1.00  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).

-->
