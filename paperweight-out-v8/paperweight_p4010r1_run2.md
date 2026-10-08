Verdict: Adequate (7/14)

The paper offers a solid foundation for why funnel shifts are a meaningful primitive and shows that the design space has been explored, but it leans heavily on assertion rather than evidence for several parts of the standardization case. The thinnest support is around the need for a standard library facility specifically, since the paper does not establish why existing library-level implementations or compiler recognition are insufficient.

- The strongest support is the prior art section, which clearly situates the proposal against C++20’s `<bit>` additions and explains why funnel shifts were a deliberate omission now worth revisiting.
- The paper establishes that the operation matters by pointing to common manual implementations and the readability and intent problems those create.
- The case for who is affected is weakened by broad, unsourced claims about universal hardware and software ecosystem support.
- The most glaring omission is the absence of any argument for why a library outside the standard cannot adequately serve this need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.33   accumulate 6.83   max 7.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.67  coordination 0.33  insufficiency 0.00  implementation 0.67
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.00 / 6.50 / 6.50   (all 3 samples: 6.67)
headings: h2 11
on threshold: none
splits: motivation[2] 0/1/0  motivation[4] 2/0/0  motivation[6] 0/0/2  audience[6] 1/0/0
        prior_art[9] 0/1/1  vehicle[7] 1/0/0  coordination[7] 2/0/0  implementation[9] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/0/0  -> 0.67
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Prior Art                                 0/0/2  -> 0.67
  [7] 5. Design                                    2/2/2  -> 2.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Today, C++ programmers typically implement funnel shifts using a small sequence of shifts, ors, and a shift-count adjustment.
candidate 2 (found by 2 of 36 passes): As discussed in [P3793R1], making these boundary cases explicit avoids the common pattern of scattering special-case guards around shift expressions, which can obscure intent.
candidate 3 (found by 1 of 36 passes): providing both scalar and SIMD interfaces for this fundamental bit manipulation primitive.
candidate 4 (found by 1 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.

## audience - grade 1.00 (fired in 3 of 12 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Prior Art                                 1/0/0  -> 0.33
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Evidence for its widespread utility is that both scalar and SIMD forms of these instructions exist in all major architectures.
candidate 2 (found by 3 of 36 passes): Funnel shifts are fundamental bit manipulation operations used extensively in:
candidate 3 (found by 1 of 36 passes): All major software ecosystems provide funnel shift operations

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
  [9] 7. Implementation Experience                 0/1/1  -> 0.67
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The P0553R4 proposal [P0553R4] (which became part of C++20) added bit manipulation functions including `rotl`, `rotr`, `countl_zero`, and `popcount` to the `<bit>` header, but did not include funnel shifts.
candidate 2 (found by 2 of 36 passes): This paper follows the latter, prioritising safety over backwards-consistent style, and aligning with the direction that new shift-related facilities in `<bit>` are taking.
candidate 3 (found by 2 of 36 passes): Modern compilers already optimize manual funnel shift patterns to native instructions
candidate 4 (found by 1 of 36 passes): This paper does not propose or depend on such a type, but should one be adopted in the future, adding overloads that accept it would be a straightforward, non-breaking extension.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    1/0/0  -> 0.33
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Currently, programmers rely on the compiler recognizing manual bit manipulation patterns and optimizing them to these hardware instructions.
candidate 2 (found by 1 of 36 passes): However, it would be more useful and readable if programmers could directly specify the use of this operation through an explicit library function.
candidate 3 (found by 1 of 36 passes): The operations are constrained to unsigned integer types for several reasons:

## coordination - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    2/0/0  -> 0.67
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/0/0  -> 0.00
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Hardware vendors use different names for this operation: Intel/AMD: "Double Shift" (SHLD/SHRD), ARM: "Extract" (EXTR), x86 SIMD: "Align" (PALIGNR/VPALIGNR/VALIGND/Q).

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

## implementation - grade 0.67  [binary: max] (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Design                                    0/0/0  -> 0.00
  [8] 6. Examples                                  0/0/0  -> 0.00
  [9] 7. Implementation Experience                 0/1/1  -> 0.67
  [10] 8. Proposed Wording                          0/0/0  -> 0.00
  [11] 9. Acknowledgements                          0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The proposed operations are straightforward to implement and have been proven in practice.

-->
