Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for the existence and prior art of funnel shifts, but its case for standardization rests heavily on assertion rather than demonstrated need, particularly around who is affected and why a library solution is insufficient. The strongest support is concentrated in the technical background and ecosystem precedent, while the thinnest areas are the absence of concrete user impact and the lack of any argument against non-standard implementations.

- The paper clearly establishes that funnel shifts are a recognized primitive with hardware support, compiler recognition, and widespread use in hashing algorithms.
- It credibly shows that prior standardization efforts and existing software ecosystems have already converged on the terminology and semantics being proposed.
- It asserts but does not substantiate that a meaningful population of C++ programmers is affected by the absence of a standard interface.
- It offers no reasoning at all for why a library implementation would be inadequate, leaving the central question of why this belongs in the standard unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.33   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 1.83  audience 0.83  prior_art 2.00  vehicle 0.83  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 66 of 77 section-criterion pairs unanimous (86%)
single-sample totals would have been: 7.50 / 6.50 / 6.50   (all 3 samples: 6.67)
headings: h2 10
on threshold: none
splits: motivation[2] 0/1/0  motivation[3] 0/0/2  motivation[5] 2/1/0  motivation[6] 2/2/1
        audience[3] 1/0/1  prior_art[4] 1/0/0  prior_art[8] 0/1/1  vehicle[3] 1/0/0
        vehicle[6] 2/1/1  coordination[6] 0/1/0  implementation[6] 0/1/0
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Introduction                              0/0/2  -> 0.67
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Prior Art                                 2/1/0  -> 1.00
  [6] 4. Design                                    2/2/1  -> 1.67
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 2 (found by 3 of 33 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 3 (found by 2 of 33 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation
candidate 4 (found by 1 of 33 passes): providing both scalar and SIMD interfaces for this fundamental bit manipulation primitive.

## audience - grade 0.83 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/1  -> 0.67
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:
candidate 2 (found by 2 of 33 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                1/0/0  -> 0.33
  [5] 3. Prior Art                                 2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/1/1  -> 0.67
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 3 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 3 (found by 2 of 33 passes): Modern compilers already optimize manual funnel shift patterns to native instructions
candidate 4 (found by 1 of 33 passes): MurmurHash, xxHash, and CityHash all use funnel shifts for bit mixing

## vehicle - grade 0.83 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/0  -> 0.33
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    2/1/1  -> 1.33
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 2 (found by 1 of 33 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 3 (found by 1 of 33 passes): The operations are constrained to unsigned integer types for several reasons: ... Right shifts on signed integers have implementation-defined behavior in C++ (arithmetic vs. logical shift). Constraining to unsigned integers ensures portable, predictable semantics across all platforms.

## coordination - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/1/0  -> 0.33
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD = Shift Left/Right Double), ARM: "Extract" (EXTR = Extract Register), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q = Packed Align Right, Vector Align D/Q)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/1/0  -> 0.33
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 2 (found by 1 of 33 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.

-->
