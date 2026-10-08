Verdict: Adequate (6/14)

The paper offers a reasonably clear rationale for why scalar overloads should not be added to saturating arithmetic, and it grounds that rationale in existing `std::simd` behavior and recent precedent. The support is thinnest where the paper treats implementation benefit as the decisive criterion but does not demonstrate that the library-level alternative has actually been explored or found insufficient.

- The paper most convincingly establishes that scalar-to-vector broadcast already provides correct behavior for saturating operations, making a scalar overload redundant.
- It also establishes a coherent general principle, supported by the shift and rotate examples, that scalar overloads are justified only when they enable an implementation benefit the broadcast cannot.
- The paper claims that a library solution will not do, but it offers only the shift/rotate example as analogy rather than evidence specific to saturating arithmetic.
- The paper does not establish who is affected by this design question, nor does it provide implementation experience showing that the proposed guideline works in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.33   accumulate 6.00   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.50  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.50 / 5.50 / 6.00   (all 3 samples: 5.67)
headings: h2 8
on threshold: vehicle
splits: motivation[4] 2/2/1  prior_art[5] 0/0/2  prior_art[7] 1/0/1  vehicle[5] 1/0/0
        vehicle[7] 1/0/0  insufficiency[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                2/2/1  -> 1.67
  [5] 3. std::simd already broadcasts scalars      2/2/2  -> 2.00
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/1/1  -> 1.00
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

## prior_art - grade 2.00 (fired in 6 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                1/1/1  -> 1.00
  [5] 3. std::simd already broadcasts scalars      0/0/2  -> 0.67
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/0/1  -> 0.67
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): A scalar supplied where a vector is expected is already broadcast to a vector by the converting constructor, and that broadcast always produces the correct result.
candidate 2 (found by 3 of 27 passes): Recent papers continue this theme, with better shifts [P3793R1] and funnel shifts [P4010R0] adding scalar-operand variants.
candidate 3 (found by 3 of 27 passes): The shift, rotate, and funnel-shift [P4010] overloads are not a precedent for "scalar parameter overloads everywhere". Instead, they are a precedent for the principle that a scalar overload is added when, and only when, it does something the broadcast cannot.
candidate 4 (found by 2 of 27 passes): The question this guideline answers came up concretely during review of the saturating-arithmetic paper [P2956R2], where it was questioned whether the saturating operations should accept a `simd::vec` together with a scalar, as some other `std::simd` operations do.

## vehicle - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      1/0/0  -> 0.33
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/0/0  -> 0.33
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): An explicit scalar overload is therefore only useful when it offers a concrete implementation benefit that the broadcast cannot.
candidate 2 (found by 3 of 27 passes): The shift and rotate overloads are the canonical example. A shift by a scalar (or compile-time-constant) count can lower to a shift-by-scalar or shift-by-immediate instruction, whereas a shift by a vector count lowers to a per-element variable-shift instruction.
candidate 3 (found by 1 of 27 passes): An explicit scalar overload of `saturating_add` would therefore be redundant, while forcing more API surface, more wording, and more tests for no behavioural benefit.
candidate 4 (found by 1 of 27 passes): Such a benefit should be compelling, and uniformity or convenience alone is not sufficient.

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

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/0  -> 0.00
  [6] 4. Provide a scalar overload only when th... 0/0/1  -> 0.33
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): The shift and rotate overloads are the canonical example.

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
