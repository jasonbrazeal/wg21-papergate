Verdict: Strong (8/14)

The paper offers a solid conceptual foundation for the problem and for why a purely library-based fix is insufficient, but its case for standardization is uneven: the strongest material concerns motivation and alternatives, while the weakest concerns evidence about real-world impact, interoperability, and implementation experience.

- The paper clearly establishes why the current padding behavior of `std::bit_cast` is a dangerous and nearly useless footgun, and it credibly frames the choice between changing `std::bit_cast` and adding a new function.
- The argument that a library-only solution cannot work is well supported by the lack of any standard way to detect padding bits and by the constant-evaluation limitations of `std::memcpy`.
- The claim that this affects a broad or frequent class of users rests mainly on speculation about `_BitInt` and limited compiler observations, rather than demonstrated widespread impact.
- The paper does not establish coordination or interoperability considerations, leaving a notable gap in how the proposed change would interact with existing implementations, ABIs, or related standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 6 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.00   accumulate 8.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 1.67  implementation 1.00
sample agreement: 43 of 49 section-criterion pairs unanimous (88%)
single-sample totals would have been: 7.50 / 9.00 / 8.50   (all 3 samples: 8.17)
headings: h2 6
on threshold: insufficiency
splits: motivation[5] 1/2/1  audience[3] 0/1/0  audience[5] 2/1/1  vehicle[5] 0/2/2
        insufficiency[3] 1/0/0  insufficiency[4] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/2/1  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): When bit-casting a type containing padding bits to a type with no padding bits, `std::bit_cast` degenerates into an alternative spelling for `std::unreachable` (some exceptions apply).
candidate 2 (found by 3 of 21 passes): This behavior is a footgun, and is not very useful. If users wanted a function that always has UB, they should be writing `std::unreachable`, not `std::bit_cast`.
candidate 3 (found by 3 of 21 passes): The single-function solution is problematic because `std::bit_cast` can be used to convert padded types to a byte array without undefined behavior and with zero overhead.
candidate 4 (found by 2 of 21 passes): It appears that the proposed behavior of `std::bit_cast_zero_padding` (which is the behavior of `std::bit_cast` in the single-function solution) is already implemented by MSVC, and to a limited extent, by GCC.

## audience - grade 0.83 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/1/0  -> 0.33
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 2/1/1  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): It appears that the proposed behavior of `std::bit_cast_zero_padding` (which is the behavior of `std::bit_cast` in the single-function solution) is already implemented by MSVC, and to a limited extent, by GCC.
candidate 2 (found by 1 of 21 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R2]](https://wg21%2elink/p3666r2)), considering that most `_BitInt` types (at least 7/8) have padding bits.
candidate 3 (found by 1 of 21 passes): At the time of writing, GCC and Clang reject the example because it is considered access of an uninitialized byte. MSVC accepts the example, and the assertion passes.

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Two viable solutions to the problem are presented: diagnosing `std::bit_cast` and adding a `std::bit_cast_zero_padding` function with alternative behavior, or simply changing the current behavior of `std::bit_cast`.
candidate 2 (found by 3 of 21 passes): proposed in [[P3666R2]](https://wg21%2elink/p3666r2)
candidate 3 (found by 3 of 21 passes): It should be noted that [[P0476R1]](https://wg21%2elink/p0476r1) never motivated this lack of diagnostics, and it is likely wording defect.
candidate 4 (found by 3 of 21 passes): It appears that the proposed behavior of `std::bit_cast_zero_padding` (which is the behavior of `std::bit_cast` in the single-function solution) is already implemented by MSVC, and to a limited extent, by GCC.

## vehicle - grade 0.67 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/2/2  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): such detection would require compiler support because there exists no way to query which bits or bytes of a type are padding bits, or whether a type has padding bits in the first place.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.67 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/0/0  -> 0.33
  [4] 2. Design                                    0/2/2  -> 1.33
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): such detection would require compiler support because there exists no way to query which bits or bytes of a type are padding bits, or whether a type has padding bits in the first place.
candidate 2 (found by 2 of 21 passes): With only a single function, there is also no way to opt out of that cost other than using `std::memcpy` instead, and that only works outside of constant evaluation.
candidate 3 (found by 1 of 21 passes): It is possible to implement a proper conversion from `long double` to `__int128`, although it requires multiple steps:

## implementation - grade 1.00  [binary: max] (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): It appears that the proposed behavior of `std::bit_cast_zero_padding` (which is the behavior of `std::bit_cast` in the single-function solution) is already implemented by MSVC, and to a limited extent, by GCC.

-->
