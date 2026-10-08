Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of why funnel shifts matter and what existing practice looks like, but it leans heavily on assertion when it comes to the breadth of affected users and the necessity of standardization rather than a library solution. The strongest material concerns prior art and the gap left by C++20’s bit-manipulation additions, while the thinnest parts are the absence of any case for why a library cannot suffice and only a cursory claim of implementation experience.

- The paper establishes that funnel shifts are a recognized primitive with existing hardware support and that prior standardization efforts stopped short of including them.
- It claims but does not substantiate the widespread user impact, relying on general statements about domains and architectural availability rather than concrete evidence of need.
- It does not establish why a library implementation would be inadequate, leaving a central standardization question unaddressed.
- Its implementation experience is asserted through a reference to LLVM intrinsics rather than demonstrated through reported use or evaluation of the proposed interface.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 8.00   accumulate 7.33   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.67  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 8.00 / 7.00   (all 3 samples: 7.00)
headings: h2 11
on threshold: none
splits: motivation[4] 2/2/1  motivation[6] 1/1/0  audience[5] 1/0/1  audience[6] 0/2/0
        prior_art[9] 1/1/0  vehicle[4] 0/1/0  implementation[7] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/1  -> 1.67
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Prior Art                                 1/1/0  -> 0.67
  [7] 5. Design                                    2/2/2  -> 2.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 2 (found by 3 of 36 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 3 (found by 2 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 4 (found by 2 of 36 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation

## audience - grade 0.83 (fired in 3 of 12 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                1/0/1  -> 0.67
  [6] 4. Prior Art                                 0/2/0  -> 0.67
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 2 of 36 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:
candidate 3 (found by 1 of 36 passes): This is a fundamental primitive bit operation with widespread use across many domains including cryptography, hashing, compression, and pseudo-random number generation.
candidate 4 (found by 1 of 36 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation:

## prior_art - grade 2.00 (fired in 3 of 12 sections, strong in 2)
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
  [9] 7. Implementation Experience                 1/1/0  -> 0.67
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 2 of 36 passes): This paper follows the latter, prioritising safety over backwards-consistent style, and aligning with the direction that new shift-related facilities in `<bit>` are taking.
candidate 3 (found by 2 of 36 passes): Modern compilers already optimize manual funnel shift patterns to native instructions:
candidate 4 (found by 1 of 36 passes): As noted by Jan Schultke, a general-purpose `std::wide` type that bundles high and low parts into a single object could unify the interface across these operations.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    1/1/1  -> 1.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 2 (found by 1 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

## coordination - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

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

## implementation - grade 1.00  [binary: max] (fired in 2 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    1/0/1  -> 0.67
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 2 (found by 2 of 36 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.

-->
