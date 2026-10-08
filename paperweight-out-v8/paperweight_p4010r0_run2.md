Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for the problem and the existence of prior art, but it does not convincingly demonstrate why standardization is necessary or why a library solution would be insufficient. The thinnest parts are the absence of any argument against a non-standard library approach and only indirect evidence about who would actually use the feature.

- The strongest support is the clear demonstration that funnel shifts are a fundamental primitive already present in hardware and in other language ecosystems.
- The paper also credibly establishes that existing C++ facilities omit this operation and that manual patterns are already optimized by compilers.
- The case for affected users rests on broad domain claims and architectural precedent rather than concrete examples or reported demand.
- The most glaring omission is the complete lack of discussion about why a library implementation would not satisfy the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 8.00   accumulate 7.50   max 8.00

## SUMMARY
grades: motivation 1.83  audience 0.50  prior_art 2.00  vehicle 0.83  coordination 0.83  insufficiency 0.00  implementation 1.00
sample agreement: 70 of 77 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.50 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 10
on threshold: none
splits: motivation[2] 0/0/1  motivation[5] 2/1/2  motivation[6] 2/1/2  vehicle[3] 1/0/1
        coordination[3] 1/0/1  coordination[4] 1/1/0  coordination[6] 1/2/0
## END SUMMARY

## motivation - grade 1.83 (fired in 4 of 11 sections, strong in 3)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Prior Art                                 2/1/2  -> 1.67
  [6] 4. Design                                    2/1/2  -> 1.67
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 2 (found by 3 of 33 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation
candidate 3 (found by 2 of 33 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 4 (found by 1 of 33 passes): providing both scalar and SIMD interfaces for this fundamental bit manipulation primitive.

## audience - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This is a fundamental primitive bit operation with widespread use across many domains including cryptography, hashing, compression, and pseudo-random number generation.
candidate 2 (found by 1 of 33 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.

## prior_art - grade 2.00 (fired in 3 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 3 of 33 passes): Modern compilers already optimize manual funnel shift patterns to native instructions
candidate 3 (found by 2 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 4 (found by 1 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD = Shift Left/Right Double), ARM: "Extract" (EXTR = Extract Register), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q = Packed Align Right, Vector Align D/Q).

## vehicle - grade 0.83 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/1  -> 0.67
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 2 (found by 2 of 33 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

## coordination - grade 0.83 (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/1  -> 0.67
  [4] 2. Motivation                                1/1/0  -> 0.67
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/2/0  -> 1.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Hardware vendors use different terminology. Intel calls these "double shifts" (SHLD/SHRD) or "aligns" (PALIGNR, VALIGND), while ARM calls them "extract" (EXTR).
candidate 2 (found by 2 of 33 passes): there is no standard SIMD interface, so portable code must rely on platform-specific intrinsics (with differing names, semantics, and availability).
candidate 3 (found by 1 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift", ARM: "Extract", x86 SIMD: "Align".
candidate 4 (found by 1 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.

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
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.
candidate 2 (found by 2 of 33 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 3 (found by 1 of 33 passes): The practical implementation uses only N-bit operations, avoiding the need for 2N-bit types:

-->
