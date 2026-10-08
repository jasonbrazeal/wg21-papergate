Verdict: Adequate to Strong (7/14)

The paper gives a solid account of why funnel shifts matter and what prior work has already established, but its case for standardization rests heavily on assertions about affected users, portability, and implementation experience rather than demonstrated evidence. The thinnest part is the absence of any argument for why a library solution would be insufficient, which leaves a central justification for standardizing the interface unaddressed.

- The strongest support is the clear explanation of the operation’s fundamental nature and the existing hardware and compiler precedent for funnel shifts.
- The paper also credibly establishes prior art by showing how C++20 bit manipulation facilities omitted this operation and how other ecosystems have converged on the terminology.
- The claims about who is affected and why the standard is needed lean on general statements about widespread use and compiler pattern recognition without concrete examples or user evidence.
- The most glaring omission is the lack of any discussion of why a library implementation would not suffice, leaving the necessity of standardization itself unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.67   accumulate 7.33   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.00  implementation 1.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 6.50   (all 3 samples: 7.17)
headings: h2 10
on threshold: none
splits: motivation[2] 1/0/1  audience[4] 1/1/0  prior_art[8] 0/0/1  vehicle[8] 0/0/1
        coordination[6] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Introduction                              0/0/0  -> 0.00
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
candidate 4 (found by 2 of 33 passes): providing both scalar and SIMD interfaces for this fundamental bit manipulation primitive.

## audience - grade 0.83 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                1/1/0  -> 0.67
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 2 of 33 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:

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
  [8] 6. Implementation Experience                 0/0/1  -> 0.33
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 3 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 3 (found by 1 of 33 passes): Modern compilers already optimize manual funnel shift patterns to native instructions

## vehicle - grade 1.00 (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/1  -> 0.33
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 3 of 33 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 3 (found by 1 of 33 passes): Modern compilers already optimize manual funnel shift patterns to native instructions

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/1/0  -> 0.67
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): The software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.
candidate 2 (found by 1 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift", ARM: "Extract", x86 SIMD: "Align"

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
candidate 2 (found by 3 of 33 passes): The proposed operations are straightforward to implement and have been proven in practice.

-->
