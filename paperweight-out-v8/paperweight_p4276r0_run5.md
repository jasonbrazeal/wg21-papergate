Verdict: Adequate (5/14)

The paper gives a reasonably clear account of why a general rule about scalar overloads is worth having and what the rule should be, but it does not build a complete case that this guidance belongs in the standard itself. The strongest material concerns the technical distinction between broadcast-compatible operations and operations such as shifts where a scalar form has a real lowering benefit. The thinnest areas are the absence of evidence about who is affected, why existing practice or a library-level guideline is insufficient, and whether the proposed guidance has been applied or tested in real implementations.

- The paper establishes the motivating problem well, showing that the question recurs across data-parallel proposals and that answering it once would avoid repeated per-paper debate.
- It credibly establishes the relevant prior art and the principle that scalar overloads are justified only when broadcasting cannot achieve the same result or implementation benefit.
- It claims but does not establish that the guidance needs to be standardized, since the argument for a normative rule rather than design advice is asserted mainly through the cost of redundant API surface.
- It offers no implementation experience, coordination analysis, or evidence about affected users, leaving the practical uptake and standardization need largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 3 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.00   accumulate 5.50   max 5.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.50 / 5.00 / 5.50   (all 3 samples: 5.17)
headings: h2 8
on threshold: vehicle
splits: motivation[4] 1/2/1  vehicle[2] 0/0/1  vehicle[3] 1/1/0  vehicle[5] 0/0/1
        vehicle[6] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Background                                1/2/1  -> 1.33
  [5] 3. std::simd already broadcasts scalars      2/2/2  -> 2.00
  [6] 4. Provide a scalar overload only when th... 2/2/2  -> 2.00
  [7] 5. Proposed guideline                        1/1/1  -> 1.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This has inadvertently created an expectation that every new operation should provide scalar overloads too, but they are not needed by default.
candidate 2 (found by 3 of 27 passes): The question applies far beyond that one paper since it recurs whenever a new data-parallel operation is proposed, so it is worth answering once in general terms, rather than per paper.
candidate 3 (found by 3 of 27 passes): An explicit scalar overload of `saturating_add` would therefore be redundant, while forcing more API surface, more wording, and more tests for no behavioural benefit.
candidate 4 (found by 3 of 27 passes): A shift by a scalar (or compile-time-constant) count can lower to a shift-by-scalar or shift-by-immediate instruction, whereas a shift by a vector count lowers to a per-element variable-shift instruction.

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

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)
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
candidate 2 (found by 3 of 27 passes): Recent papers continue this theme, with better shifts [P3793R1] and funnel shifts [P4010R0] adding scalar-operand variants.
candidate 3 (found by 3 of 27 passes): The question this guideline answers came up concretely during review of the saturating-arithmetic paper [P2956R2], where it was questioned whether the saturating operations should accept a `simd::vec` together with a scalar, as some other `std::simd` operations do.
candidate 4 (found by 2 of 27 passes): The shift, rotate, and funnel-shift [P4010] overloads are not a precedent for "scalar parameter overloads everywhere". Instead, they are a precedent for the principle that a scalar overload is added when, and only when, it does something the broadcast cannot.

## vehicle - grade 1.17 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] 1. Introduction                              1/1/0  -> 0.67
  [4] 2. Background                                0/0/0  -> 0.00
  [5] 3. std::simd already broadcasts scalars      0/0/1  -> 0.33
  [6] 4. Provide a scalar overload only when th... 2/1/2  -> 1.67
  [7] 5. Proposed guideline                        0/0/0  -> 0.00
  [8] 6. Possible polls                            0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): An explicit scalar overload is therefore only useful when it offers a concrete implementation benefit that the broadcast cannot.
candidate 2 (found by 2 of 27 passes): The shift and rotate overloads are the canonical example. A shift by a scalar (or compile-time-constant) count can lower to a shift-by-scalar or shift-by-immediate instruction, whereas a shift by a vector count lowers to a per-element variable-shift instruction.
candidate 3 (found by 1 of 27 passes): provide a scalar overload only when there is a demonstrable benefit over broadcasting.
candidate 4 (found by 1 of 27 passes): An explicit scalar overload of `saturating_add` would therefore be redundant, while forcing more API surface, more wording, and more tests for no behavioural benefit.

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
