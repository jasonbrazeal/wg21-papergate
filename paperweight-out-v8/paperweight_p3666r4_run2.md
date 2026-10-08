Verdict: Excellent (13/14)

The paper offers substantial support for standardizing bit-precise integers, particularly through its alignment with C23, existing Clang implementation experience, and the demonstrated impossibility of achieving the same result through a library type. The case is thinnest around who is affected, where the paper asserts broad utility and existing usage but does not substantiate the scale or nature of the affected codebases.

- The strongest support comes from the interoperability argument: without a core language type, C++ cannot portably call C functions using `_BitInt` or pass C structs containing bit-precise integer fields across the language boundary.
- The paper also convincingly shows that a library type cannot substitute, since class types cannot be used in bit-fields and no portable ABI exists for invoking functions with `_BitInt` parameters through a wrapper.
- Implementation experience is well established by Clang’s years-long support for `_BitInt` as a compiler extension, including the existing behavior of standard library traits.
- The most glaring omission is the lack of evidence about who is affected: the paper claims wide usefulness and existing code impact but offers no concrete examples, user reports, or measurements to establish the breadth of that need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (13.00/14)

Provisionally addressed: 7 of 7. Provisional points: 13.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 13.00   corroborated 13.00   accumulate 13.17   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 2.00  implementation 2.00
sample agreement: 86 of 98 section-criterion pairs unanimous (88%)
single-sample totals would have been: 13.00 / 13.50 / 12.50   (all 3 samples: 13.00)
headings: h2 11
on threshold: none
splits: motivation[9] 1/0/0  audience[5] 0/1/0  audience[8] 1/2/0  prior_art[7] 0/2/2
        prior_art[12] 0/1/0  vehicle[2] 1/0/0  vehicle[4] 0/0/1  vehicle[7] 1/0/2
        vehicle[8] 0/0/1  coordination[8] 2/0/2  implementation[6] 1/2/2
        implementation[9] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/0/0  -> 0.33
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): However, there has always been some enthusiasm in the committee for such a feature.
candidate 3 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 4 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.

## audience - grade 1.00 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/0  -> 0.33
  [6] 4. Core design  (part 1 of 2)                0/0/0  -> 0.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/2/0  -> 1.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 2 (found by 1 of 42 passes): Computation beyond 64 bits, such as with 128-bit integers, is immensely useful.
candidate 3 (found by 1 of 42 passes): This decision was motivated by the fact that otherwise, large amounts of existing code (not just the standard library, but also user code) would implicitly opt into supporting bit-precise integers
candidate 4 (found by 1 of 42 passes): libc++ already makes `std::is_integral_v<_BitInt(N)>` `true`, so what LEWG wants is silently altering the behavior of existing traits.

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/2/2  -> 1.33
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    2/2/2  -> 2.00
  [12] 8. Wording  (part 2 of 2)                    0/1/0  -> 0.33
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 42 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 3 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 4 (found by 3 of 42 passes): This change deviates from C at the time of writing; C2y does not yet allow `_BitInt(1)`, but may allow it following [[N3699]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3699%2epdf).

## vehicle - grade 2.00 (fired in 7 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/1  -> 0.33
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                1/0/2  -> 1.00
  [8] 5. Library design                            0/0/1  -> 0.33
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 42 passes): The core language changes are essentially standardizing that compiler extension.
candidate 4 (found by 2 of 42 passes): The final nail in the coffin is that if the user wants implicit conversions to be restricted, they have the freedom to add those restrictions via compiler warnings and linter checks.

## coordination - grade 2.00 (fired in 5 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/0/2  -> 1.33
  [9] 6. Implementation experience                 0/0/0  -> 0.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 42 passes): Without a single platform ABI, there would also be no portable way for code generated by different compilers to interoperate, such as compiling a C library with GCC and using it from Clang-compiled C++ code.
candidate 4 (found by 2 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`

## insufficiency - grade 2.00 (fired in 2 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Implementation experience                 0/0/0  -> 0.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 2 (found by 2 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`
candidate 3 (found by 1 of 42 passes): While one could rely on the ABI of `uint32_t` and `_BitInt(32)` to be identical in the first overload, there certainly is no way to portably invoke the second overload.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Core design  (part 1 of 2)                1/2/2  -> 1.67
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 2/1/1  -> 1.33
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Clang already supports the `_BitInt` keyword spelling as a compiler extension, so this is standardizing existing practice.
candidate 2 (found by 3 of 42 passes): This behavior is already implemented by Clang as a C++ compiler extension, and makes deduction behave identically to deducing sizes of arrays.
candidate 3 (found by 3 of 42 passes): libc++ already makes `std::is_integral_v<_BitInt(N)>` `true`, so what LEWG wants is silently altering the behavior of existing traits.
candidate 4 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

-->
