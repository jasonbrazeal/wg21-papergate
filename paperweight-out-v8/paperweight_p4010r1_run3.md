Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for the existence and prior art of funnel shifts, but its case for standardization rests heavily on assertion rather than demonstrated need, with the thinnest support around why a library solution would be insufficient and whether the proposed facility has meaningful implementation experience beyond existing compiler intrinsics.

- The strongest support is the established prior art, showing that C++20 added related bit operations without funnel shifts and that compilers already recognize manual patterns.
- The paper clearly establishes why the operation matters by pointing to native hardware support and the awkwardness of current manual implementations.
- The claims about affected users and ecosystem convergence are plausible but not backed by concrete evidence of widespread C++ programmer demand.
- The most glaring omission is the absence of any argument for why a library facility cannot adequately provide these operations, leaving the need for language or standard-library standardization unproven.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.17   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.00  implementation 1.00
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.50 / 8.00 / 6.50   (all 3 samples: 7.00)
headings: h2 11
on threshold: vehicle
splits: motivation[6] 2/1/1  audience[4] 1/1/0  audience[5] 1/0/1  audience[6] 1/0/0
        coordination[4] 0/1/0  coordination[7] 1/0/0  implementation[6] 0/2/0
        implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Prior Art                                 2/1/1  -> 1.33
  [7] 5. Design                                    2/2/2  -> 2.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 3 of 36 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 3 (found by 3 of 36 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 4 (found by 2 of 36 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation

## audience - grade 0.67 (fired in 3 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/0  -> 0.67
  [5] 3. Motivation                                1/0/1  -> 0.67
  [6] 4. Prior Art                                 1/0/0  -> 0.33
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 2 of 36 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:
candidate 3 (found by 1 of 36 passes): All major software ecosystems provide funnel shift operations

## prior_art - grade 2.00 (fired in 3 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 2/2/2  -> 2.00
  [7] 5. Design                                    2/2/2  -> 2.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 3 of 36 passes): Modern compilers already optimize manual funnel shift patterns to native instructions
candidate 3 (found by 1 of 36 passes): This paper follows the latter, prioritising safety over backwards-consistent style, and aligning with the direction that new shift-related facilities in `<bit>` are taking.
candidate 4 (found by 1 of 36 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.

## vehicle - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    2/2/2  -> 2.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD), ARM: "Extract" (EXTR), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q). However, the software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 2 (found by 1 of 36 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 3 (found by 1 of 36 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD = Shift Left/Right Double), ARM: "Extract" (EXTR = Extract Register), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q = Packed Align Right, Vector Align D/Q).

## coordination - grade 0.33 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    1/0/0  -> 0.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 1 of 36 passes): However, the software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 3 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/2/0  -> 0.67
  [7] 5. Design                                    0/1/0  -> 0.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 2 (found by 1 of 36 passes): **LLVM**: `fshl`/`fshr` intrinsics (widely used in LLVM IR) [LLVM-Funnel]
candidate 3 (found by 1 of 36 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.
candidate 4 (found by 1 of 36 passes): The practical implementation uses only N-bit operations, avoiding the need for 2N-bit types:

-->
