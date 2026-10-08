Verdict: Adequate to Strong (7/14)

The paper gives a solid account of why funnel shifts matter and what prior work has omitted, but it leans heavily on assertion when it comes to the people affected, the need for a standard facility, and interoperability. The thinnest parts are the absence of any argument for why a library solution would be insufficient and the lack of concrete implementation experience beyond naming LLVM intrinsics.

- The strongest support is the clear motivation that manual bit-manipulation patterns are error-prone and that major hardware already provides native funnel shift instructions.
- The prior-art discussion is well grounded, showing that C++20 added related bit operations but left this gap unfilled.
- The paper claims broad impact and portability benefits but does not demonstrate who specifically is affected or how existing codebases suffer.
- The most glaring omission is the complete lack of a case for why a standard library facility, rather than a compiler builtin or third-party library, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.33   accumulate 7.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 1.50  vehicle 0.83  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.00 / 6.00 / 7.50   (all 3 samples: 6.50)
headings: h2 11
on threshold: prior_art
splits: motivation[2] 1/0/0  motivation[6] 1/2/1  motivation[7] 2/2/1  prior_art[9] 0/1/1
        vehicle[4] 1/0/1  vehicle[5] 1/0/0  coordination[4] 1/0/0  implementation[6] 0/0/2
        implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Prior Art                                 1/2/1  -> 1.33
  [7] 5. Design                                    2/2/1  -> 1.67
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 3 of 36 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 3 (found by 3 of 36 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 4 (found by 2 of 36 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation

## audience - grade 1.00 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 3 of 36 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:

## prior_art - grade 1.50 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 1/1/1  -> 1.00
  [7] 5. Design                                    2/2/2  -> 2.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/1/1  -> 0.67
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 3 of 36 passes): As noted by Jan Schultke, a general-purpose `std::wide` type that bundles high and low parts into a single object could unify the interface across these operations.
candidate 3 (found by 2 of 36 passes): Modern compilers already optimize manual funnel shift patterns to native instructions

## vehicle - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/1  -> 0.67
  [5] 3. Motivation                                1/0/0  -> 0.33
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    1/1/1  -> 1.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 2 (found by 1 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 3 (found by 1 of 36 passes): However, it would be more useful and readable if programmers could directly specify the use of this operation through an explicit library function.
candidate 4 (found by 1 of 36 passes): there is no standard SIMD interface, so portable code must rely on platform-specific intrinsics (with differing names, semantics, and availability).

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/0  -> 0.33
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

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
  [6] 4. Prior Art                                 0/0/2  -> 0.67
  [7] 5. Design                                    0/1/0  -> 0.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 2 (found by 1 of 36 passes): **LLVM**: `fshl`/`fshr` intrinsics (widely used in LLVM IR) [LLVM-Funnel]
candidate 3 (found by 1 of 36 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.

-->
