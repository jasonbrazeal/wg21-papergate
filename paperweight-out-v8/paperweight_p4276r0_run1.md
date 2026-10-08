Verdict: Adequate (6/14)

The paper offers a reasonably clear rationale for its central design guideline, particularly by grounding it in existing `std::simd` behavior and the concrete case of shift and rotate overloads. The support is thinnest where a standardization document would normally show who is affected, how the rule interacts with other library facilities, and whether the guidance has been applied in practice.

- The strongest support is the explanation that scalar-to-vector broadcast already produces correct results, making many explicit scalar overloads redundant.
- The paper also establishes why the standard is the right place for the guideline, using the distinction between scalar and vector shift lowering as a concrete example.
- The most glaring omission is any account of who is affected by adopting the guideline or what implementation experience exists with applying it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 3 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 5.50   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.50  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 8
on threshold: vehicle
splits: motivation[2] 1/2/1  motivation[4] 1/2/1  prior_art[5] 0/2/0  prior_art[7] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                1/2/1  -> 1.33
  [5] 3. std::simd already broadcasts scalars      2/2/2  -> 2.00
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/1/1  -> 1.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The question applies far beyond that one paper since it recurs whenever a new data-parallel operation is proposed, so it is worth answering once in general terms, rather than per paper.
candidate 2 (found by 3 of 27 passes): An explicit scalar overload of `saturating_add` would therefore be redundant, while forcing more API surface, more wording, and more tests for no behavioural benefit.
candidate 3 (found by 3 of 27 passes): A shift by a scalar (or compile-time-constant) count can lower to a shift-by-scalar or shift-by-immediate instruction, whereas a shift by a vector count lowers to a per-element variable-shift instruction.
candidate 4 (found by 3 of 27 passes): an overload that merely reproduces what an implicit conversion already does should be added only when it offers a distinct, demonstrable benefit over relying on that conversion.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 0/0/0  -> 0.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                1/1/1  -> 1.00
  [5] 3. std::simd already broadcasts scalars      0/2/0  -> 0.67
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/1/0  -> 0.67
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): A scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.
candidate 2 (found by 3 of 27 passes): This paper proposes a design guideline that a scalar overload should only be provided when there is such a benefit, and otherwise rely on the broadcast that the library already performs.
candidate 3 (found by 3 of 27 passes): The question this guideline answers came up concretely during review of the saturating-arithmetic paper [P2956R2], where it was questioned whether the saturating operations should accept a `simd::vec` together with a scalar, as some other `std::simd` operations do.
candidate 4 (found by 3 of 27 passes): The shift, rotate, and funnel-shift [P4010] overloads are not a precedent for "scalar parameter overloads everywhere". Instead, they are a precedent for the principle that a scalar overload is added when, and only when, it does something the broadcast cannot.

## vehicle - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The shift and rotate overloads are the canonical example. A shift by a scalar (or compile-time-constant) count can lower to a shift-by-scalar or shift-by-immediate instruction, whereas a shift by a vector count lowers to a per-element variable-shift instruction.
candidate 2 (found by 2 of 27 passes): An explicit scalar overload is therefore only useful when it offers a concrete implementation benefit that the broadcast cannot.
candidate 3 (found by 1 of 27 passes): The reason scalar overloads are not needed by default is that a scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 0/0/0  -> 0.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 0/0/0  -> 0.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 0/0/0  -> 0.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
