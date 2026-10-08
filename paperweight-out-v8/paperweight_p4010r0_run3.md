Verdict: Adequate (7/14)

The paper gives a reasonably solid account of why funnel shifts matter and what prior art exists, but its case for standardization is uneven: several important points are asserted rather than demonstrated, and one essential point is left entirely unaddressed. The thinnest support concerns the inability of a library solution to meet the need, which is a central justification for any standard library addition.

- The strongest support is the established motivation, including native hardware support and the omission of funnel shifts from the C++20 `<bit>` additions.
- The prior art and alternatives section is also well grounded, showing ecosystem convergence on terminology and existing compiler recognition of manual patterns.
- The paper claims but does not establish who is affected, why the standard is the right venue, how the proposal coordinates with existing vendor naming, or what implementation experience exists.
- The most glaring omission is the absence of any argument for why a library cannot provide these operations, leaving a key requirement for standardization unmet.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.33   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.67  vehicle 0.67  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 10
on threshold: prior_art, coordination
splits: motivation[2] 1/0/0  motivation[3] 0/0/2  audience[4] 0/1/0  prior_art[5] 2/1/1
        vehicle[3] 0/0/1  implementation[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Introduction                              0/0/2  -> 0.67
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Prior Art                                 1/1/1  -> 1.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 2 (found by 3 of 33 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation
candidate 3 (found by 3 of 33 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 4 (found by 1 of 33 passes): providing both scalar and SIMD interfaces for this fundamental bit manipulation primitive.

## audience - grade 0.67 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                0/1/0  -> 0.33
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 1 of 33 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:

## prior_art - grade 1.67 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 2/1/1  -> 1.33
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 3 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 3 (found by 3 of 33 passes): Modern compilers already optimize manual funnel shift patterns to native instructions

## vehicle - grade 0.67 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/1  -> 0.33
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 2 (found by 1 of 33 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD), ARM: "Extract" (EXTR), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q).
candidate 2 (found by 1 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 3 (found by 1 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD = Shift Left/Right Double), ARM: "Extract" (EXTR = Extract Register), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q = Packed Align Right, Vector Align D/Q)

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
  [6] 4. Design                                    0/0/1  -> 0.33
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 2 (found by 1 of 33 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.

-->
