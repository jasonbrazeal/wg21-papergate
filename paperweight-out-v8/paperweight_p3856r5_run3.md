Verdict: Adequate (5/14)

The paper offers some useful grounding in prior work and implementation experience, but it leaves the central case for standardization largely undeveloped. The thinnest areas are the absence of any identified user population and the failure to explain why the functionality cannot be delivered through an ordinary library.

- The strongest support is the demonstrated implementation experience, including a working sample using Bloomberg’s Clang fork and a Godbolt link.
- The paper also establishes prior art and alternatives by comparing traditional type traits with reflection metafunctions and situating the proposal alongside P2996.
- The paper claims but does not establish why the feature matters, resting on general statements about structural types and NTTPs without concrete motivating scenarios.
- The most glaring omission is the lack of any account of who is affected, leaving the proposal without a clear constituency or demonstrated demand.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.67   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.50  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 5.00 / 4.50   (all 3 samples: 5.00)
headings: h2 6
on threshold: prior_art, implementation
splits: motivation[4] 2/1/1  vehicle[3] 1/1/0
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/1/1  -> 1.33
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
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
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/2  -> 2.00
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In addition, we compare the approaches of using traditional type traits vs. using reflection metafunctions to query type attributes.
candidate 2 (found by 3 of 21 passes): [P2996](http://wg21.link/P2996) introduced several metafunctions *(consteval* functions that operate on *meta::info)* in *<meta>* that mirror existing type traits, such as *is_const_type(info), is_volatile_type(info),* and *is_trivially_copyable_type(info).*
candidate 3 (found by 2 of 21 passes): The approach of using reflection metafunctions to query type attributes appears promising, and likely to yield richer APIs than possible with prior techniques.
candidate 4 (found by 1 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*

## vehicle - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/0  -> 0.67
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                0/0/0  -> 0.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Library mandates clauses mean that library implementers must somehow have this functionality, but it is simply not exposed to users.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/2  -> 2.00
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 2 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).
candidate 3 (found by 2 of 21 passes): The code below shows a possible implementation of is_structural_type, using Bloomberg’s Clang fork.
candidate 4 (found by 1 of 21 passes): The code below shows a possible implementation of is_structural_type, using Bloomberg’s Clang fork. [Godbolt link](https://godbolt.org/z/abGPKx1YM)

-->
