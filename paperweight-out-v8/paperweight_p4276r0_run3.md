Verdict: Adequate (5/14)

The paper offers a clear and useful rationale for when scalar overloads are unnecessary, and it grounds that rationale in concrete review history and existing practice. Its support is thinnest, however, in showing that this guidance belongs in the standard itself rather than in committee documentation or a standing design note, and it does not address who would be affected by adopting it or how it would interact with existing wording and implementations.

- The strongest support is the established argument that scalar-to-vector broadcast already produces correct results, making default scalar overloads redundant.
- The paper also credibly establishes prior art by citing the saturating-arithmetic review and the shift/rotate/funnel-shift precedent for adding scalar overloads only when they enable a distinct implementation benefit.
- The most glaring omission is the absence of any established case for why this guideline requires standardization, as opposed to remaining an internal design principle or library-authoring convention.
- The paper similarly offers no established discussion of who is affected, how the guideline would coordinate with existing standard facilities, or any implementation experience with applying it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 4 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.33   accumulate 5.17   max 5.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.00 / 5.50 / 5.00   (all 3 samples: 5.17)
headings: h2 8
on threshold: none
splits: motivation[7] 1/1/0  vehicle[3] 1/1/0  vehicle[6] 1/2/1  insufficiency[3] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                1/1/1  -> 1.00
  [5] 3. std::simd already broadcasts scalars      2/2/2  -> 2.00
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/1/0  -> 0.67
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): A scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.
candidate 2 (found by 3 of 27 passes): The reason scalar overloads are not needed by default is that a scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.
candidate 3 (found by 3 of 27 passes): The question applies far beyond that one paper since it recurs whenever a new data-parallel operation is proposed, so it is worth answering once in general terms, rather than per paper.
candidate 4 (found by 3 of 27 passes): An explicit scalar overload of `saturating_add` would therefore be redundant, while forcing more API surface, more wording, and more tests for no behavioural benefit.

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

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                1/1/1  -> 1.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): A scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.
candidate 2 (found by 3 of 27 passes): The question this guideline answers came up concretely during review of the saturating-arithmetic paper [P2956R2], where it was questioned whether the saturating operations should accept a `simd::vec` together with a scalar, as some other `std::simd` operations do.
candidate 3 (found by 3 of 27 passes): The shift, rotate, and funnel-shift [P4010] overloads are not a precedent for "scalar parameter overloads everywhere". Instead, they are a precedent for the principle that a scalar overload is added when, and only when, it does something the broadcast cannot.
candidate 4 (found by 2 of 27 passes): Recent papers continue this theme, with better shifts [P3793R1] and funnel shifts [P4010R0] adding scalar-operand variants.

## vehicle - grade 1.00 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/0  -> 0.67
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 1/2/1  -> 1.33
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The shift, rotate, and funnel-shift [P4010] overloads are not a precedent for "scalar parameter overloads everywhere".
candidate 2 (found by 1 of 27 passes): An explicit scalar overload is therefore only useful when it offers a concrete implementation benefit that the broadcast cannot.
candidate 3 (found by 1 of 27 passes): The reason scalar overloads are not needed by default is that a scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.
candidate 4 (found by 1 of 27 passes): The shift and rotate overloads are the canonical example. A shift by a scalar (or compile-time-constant) count can lower to a shift-by-scalar or shift-by-immediate instruction, whereas a shift by a vector count lowers to a per-element variable-shift instruction.

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

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/1  -> 0.33
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 0/0/0  -> 0.00
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): An explicit scalar overload is therefore only useful when it offers a concrete implementation benefit that the broadcast cannot.

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
