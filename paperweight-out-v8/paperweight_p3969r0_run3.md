Verdict: Strong (8/14)

The paper offers solid support for the existence of a real problem and for the need to solve it at the language or library level rather than through ordinary user code, but it leaves the standardization rationale and interoperability story essentially unargued. The thinnest parts are the absence of any discussion of why this belongs in the standard specifically, and the lack of evidence about how implementations and adjacent specifications would coordinate around the change.

- The strongest support is the demonstration that `std::bit_cast` can become a deliberate trap when padding bits are present, making the current behavior a genuine footgun rather than a useful primitive.
- The paper also credibly establishes that a library-only solution is impractical, since detecting or clearing padding requires compiler support and cannot preserve `constexpr` usability through ordinary `memcpy`.
- The prior-art discussion is adequate, identifying both a single-function change and a separate zero-padding function as plausible directions, with some reference to existing compiler behavior.
- The most glaring omission is the complete absence of a case for why the standard should act here, including any coordination with implementers, ABI considerations, or interaction with other standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 8.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 1.67  implementation 1.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 8.00   (all 3 samples: 7.67)
headings: h2 6
on threshold: audience, insufficiency
splits: motivation[2] 1/2/1  motivation[5] 0/1/1  insufficiency[5] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/1  -> 1.33
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/1/1  -> 0.67
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): When bit-casting a type containing padding bits to a type with no padding bits, `std::bit_cast` degenerates into an alternative spelling for `std::unreachable` (some exceptions apply).
candidate 2 (found by 3 of 21 passes): This behavior is a footgun, and is not very useful. If users wanted a function that always has UB, they should be writing `std::unreachable`, not `std::bit_cast`.
candidate 3 (found by 3 of 21 passes): The single-function solution is problematic because `std::bit_cast` can be used to convert padded types to a byte array without undefined behavior and with zero overhead.
candidate 4 (found by 2 of 21 passes): It appears that the proposed behavior of `std::bit_cast_zero_padding` (which is the behavior of `std::bit_cast` in the single-function solution) is already implemented by MSVC, and to a limited extent, by GCC.

## audience - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design                                    0/0/0  -> 0.00
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): At the time of writing, GCC and Clang reject the example because it is considered access of an uninitialized byte. MSVC accepts the example, and the assertion passes.

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
candidate 2 (found by 3 of 21 passes): Another case where the degenerate form may arise frequently is bit-casting `_BitInt` (supported by Clang as an extension and proposed in [[P3666R2]](https://wg21%2elink/p3666r2))
candidate 3 (found by 3 of 21 passes): In the discussion of this proposal prior to publication, it was suggested to clear the padding *before* bit-casting. That is, standardizing [`__builtin_clear_padding`](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fclear_005fpadding) and using an idiom such as:
candidate 4 (found by 3 of 21 passes): It appears that the proposed behavior of `std::bit_cast_zero_padding` (which is the behavior of `std::bit_cast` in the single-function solution) is already implemented by MSVC, and to a limited extent, by GCC.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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

## insufficiency - grade 1.67 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Design                                    2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/2  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): It is possible to implement a proper conversion from `long double` to `__int128`, although it requires multiple steps:
candidate 2 (found by 3 of 21 passes): such detection would require compiler support because there exists no way to query which bits or bytes of a type are padding bits, or whether a type has padding bits in the first place.
candidate 3 (found by 2 of 21 passes): All of that complexity yields no advantage; even if `std::clear_padding` was `constexpr`, `std::memcpy` isn't, so `cast` cannot be made `constexpr`.
candidate 4 (found by 1 of 21 passes): With only a single function, there is also no way to opt out of that cost other than using `std::memcpy` instead, and that only works outside of constant evaluation.

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
