Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of why funnel shifts matter and what existing practice looks like, but it leaves several parts of the standardization case more asserted than demonstrated. The thinnest support is around why a library-only solution would be insufficient and whether the proposed interface has enough implementation experience behind it.

- The strongest support is the prior-art discussion, which shows that related bit operations were standardized without funnel shifts and that compilers already recognize manual funnel-shift patterns.
- The paper also establishes the motivating problem well, particularly the readability and intent-clarity benefits of replacing scattered shift guards with an explicit operation.
- The interoperability and affected-user arguments are weaker because they mostly list architectural or ecosystem names without showing how C++ programmers are concretely limited today.
- The most glaring omission is the absence of any real case for why a standard library facility is needed rather than a non-standard library or compiler builtin.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.67   accumulate 7.33   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.17  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 6.50 / 7.50 / 8.00   (all 3 samples: 7.33)
headings: h2 11
on threshold: vehicle
splits: motivation[2] 1/1/0  motivation[7] 2/1/1  audience[5] 0/0/1  prior_art[9] 1/1/0
        vehicle[4] 0/1/1  vehicle[7] 2/1/2  coordination[4] 0/1/1  coordination[7] 0/1/0
        implementation[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Prior Art                                 1/1/1  -> 1.00
  [7] 5. Design                                    2/1/1  -> 1.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 3 of 36 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 3 (found by 2 of 36 passes): providing both scalar and SIMD interfaces for this fundamental bit manipulation primitive.
candidate 4 (found by 2 of 36 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.

## audience - grade 0.67 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/1  -> 0.33
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 1 of 36 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:

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
candidate 2 (found by 2 of 36 passes): As noted by Jan Schultke, a general-purpose `std::wide` type that bundles high and low parts into a single object could unify the interface across these operations.
candidate 3 (found by 2 of 36 passes): Modern compilers already optimize manual funnel shift patterns to native instructions
candidate 4 (found by 1 of 36 passes): This paper follows the latter, prioritising safety over backwards-consistent style, and aligning with the direction that new shift-related facilities in `<bit>` are taking.

## vehicle - grade 1.17 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    2/1/2  -> 1.67
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 2 (found by 1 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 3 (found by 1 of 36 passes): However, it would be more useful and readable if programmers could directly specify the use of this operation through an explicit library function.
candidate 4 (found by 1 of 36 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.

## coordination - grade 0.50 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/1  -> 0.67
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/1/0  -> 0.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 1 of 36 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD = Shift Left/Right Double), ARM: "Extract" (EXTR = Extract Register), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q = Packed Align Right, Vector Align D/Q).

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
  [7] 5. Design                                    0/0/1  -> 0.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 1/1/1  -> 1.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The proposed operations are straightforward to implement and have been proven in practice.
candidate 2 (found by 1 of 36 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.

-->
