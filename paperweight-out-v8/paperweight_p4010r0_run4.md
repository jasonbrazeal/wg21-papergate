Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for the problem’s importance and for the existence of prior art, but it leaves several essential parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why a library solution is insufficient and whether the proposed interface has enough implementation experience behind it.

- The strongest support is the clear explanation of why funnel shifts matter and how current manual patterns obscure intent.
- The paper also credibly establishes prior art and alternatives, including hardware terminology and the omission from C++20’s `<bit>` additions.
- The case for who is affected leans on hardware ubiquity but does not show actual C++ user demand or concrete codebases needing the facility.
- The most glaring omission is the absence of any argument for why a library cannot adequately provide this functionality.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.67   accumulate 7.33   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.67  coordination 1.17  insufficiency 0.00  implementation 0.67
sample agreement: 70 of 77 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.00 / 7.50 / 7.00   (all 3 samples: 7.17)
headings: h2 10
on threshold: coordination
splits: motivation[6] 1/2/1  audience[4] 0/0/1  audience[6] 0/0/1  vehicle[4] 1/0/0
        coordination[3] 0/1/1  coordination[6] 1/2/2  implementation[6] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Prior Art                                 1/1/1  -> 1.00
  [6] 4. Design                                    1/2/1  -> 1.33
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 3 of 33 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 3 (found by 3 of 33 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 4 (found by 2 of 33 passes): Both x86 and ARM provide native funnel shift instructions for scalar and SIMD operations, demonstrating the fundamental nature of this operation:

## audience - grade 0.67 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                0/0/1  -> 0.33
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    0/0/1  -> 0.33
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 1 of 33 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:
candidate 3 (found by 1 of 33 passes): The hardware evidence is strong to support this: major ISAs provide distinct operations for each direction (e.g. x86 `SHLD` vs `SHRD`), and compilers/language infrastructure model them as separate primitives (LLVM `fshl`/`fshr`, CUDA `__funnelshift_l*`/`__funnelshift_r*`).

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 1/1/1  -> 1.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Hardware vendors use different terminology. Intel calls these "double shifts" (SHLD/SHRD) or "aligns" (PALIGNR, VALIGND), while ARM calls them "extract" (EXTR).
candidate 2 (found by 3 of 33 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 3 (found by 3 of 33 passes): Modern compilers already optimize manual funnel shift patterns to native instructions
candidate 4 (found by 2 of 33 passes): However, the software ecosystem (LLVM, CUDA, Rust) has converged on funnel shift as the preferred term.

## vehicle - grade 0.67 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Motivation                                1/0/0  -> 0.33
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/1/1  -> 1.00
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This proposal provides a portable intrinsic interface for funnel shifts, intended to map directly to existing target instructions.
candidate 2 (found by 1 of 33 passes): there is no standard SIMD interface, so portable code must rely on platform-specific intrinsics (with differing names, semantics, and availability).

## coordination - grade 1.17 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/1/1  -> 0.67
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Prior Art                                 0/0/0  -> 0.00
  [6] 4. Design                                    1/2/2  -> 1.67
  [7] 5. Examples                                  0/0/0  -> 0.00
  [8] 6. Implementation Experience                 0/0/0  -> 0.00
  [9] 7. Proposed Wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD = Shift Left/Right Double), ARM: "Extract" (EXTR = Extract Register), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q = Packed Align Right, Vector Align D/Q).
candidate 2 (found by 2 of 33 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

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

## implementation - grade 0.67  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
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
candidate 1 (found by 2 of 33 passes): LLVM’s `fshl`/`fshr` intrinsics work identically for both scalar and vector types, demonstrating that the unified design is well-understood and implementable.

-->
