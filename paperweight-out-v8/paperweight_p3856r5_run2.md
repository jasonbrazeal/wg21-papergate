Verdict: Weak to Adequate (3/14)

The paper offers only a narrow slice of the case needed for standardization: it gestures at the usefulness of a structural-type query and sketches how reflection might supply it, but it does not establish who needs the facility, why the standard is the right home for it, or that existing library techniques are insufficient. The thinnest areas are the complete absence of discussion about affected users, standardization rationale, interoperability, and library-only alternatives, which leaves the proposal’s motivation largely aspirational.

- The strongest support is the paper’s identification of a plausible gap: there is no current way to query whether a type is structural, despite structural types being required for non-type template parameters.
- The paper at least claims some implementation experience by describing a sample implementation built from existing P2996 reflection metafunctions, though this is asserted rather than demonstrated with concrete details or validation.
- The discussion of prior art and alternatives is only gestured at through comparisons with traditional type traits and a list of other missing metafunctions, without a substantive evaluation of those approaches.
- The most glaring omission is the lack of any established case for why this belongs in the standard rather than in a library, alongside no account of who is affected or how the feature would coordinate with existing and proposed reflection facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.00   accumulate 4.17   max 3.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 4.00 / 3.00   (all 3 samples: 3.33)
headings: h2 6
on threshold: motivation
splits: motivation[4] 2/2/1  prior_art[4] 0/2/0  implementation[3] 1/0/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/1/1  -> 1.00
  [4] 3. Structural types                          2/2/1  -> 1.67
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The *is_structural_type check* is valuable wherever values (including small user-defined structs) have to be treated as compile‑time constants, since NTTPs must be structural types.
candidate 2 (found by 2 of 21 passes): yet there is no way to query whether a type is structural.
candidate 3 (found by 2 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996
candidate 4 (found by 1 of 21 passes): yet there is no way to query whether a type is structural

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
  [4] 3. Structural types                          0/2/0  -> 0.67
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): It also shows the need for more “lower level” metafunctions not included in P2996, such as *is_constexpr(info),* *is_literal_type(info)* and *is_lambda_closure_type(info).*
candidate 2 (found by 2 of 21 passes): In addition, we compare the approaches of using traditional type traits vs. using reflection metafunctions to query type attributes.
candidate 3 (found by 1 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.
candidate 4 (found by 1 of 21 passes): [P2996](http://wg21.link/P2996) introduced several metafunctions *(consteval* functions that operate on *meta::info)* in *<meta>* that mirror existing type traits, such as *is_const_type(info), is_volatile_type(info),* and *is_trivially_copyable_type(info).*

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

## implementation - grade 1.00  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Introduction                              1/0/1  -> 0.67
  [4] 3. Structural types                          0/0/0  -> 0.00
  [5] 6. Conclusion                                1/1/1  -> 1.00
  [6] 7. Acknowledgements                          0/0/0  -> 0.00
  [7] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Our experience in implementing new reflection metafunctions shows how reflection type queries can be implemented using other reflection metafunctions only (no intrinsics or SFINAE).
candidate 2 (found by 2 of 21 passes): We provide a sample implementation using other reflection metafunctions from P2996 to demonstrate how far we can go with the existing batch of reflection type queries included in C++26.

-->
