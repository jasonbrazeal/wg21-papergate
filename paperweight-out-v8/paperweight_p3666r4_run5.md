Verdict: Excellent (13/14)

The paper offers substantial support for standardizing bit-precise integers, particularly through its alignment with C23, existing Clang implementation experience, and clear demonstrations of why library types cannot fill the interoperability gap. The thinnest part of the case is the claim about who is affected: the paper asserts that large amounts of existing code would be impacted, but does not actually establish that this code exists or would opt in.

- The strongest support comes from the concrete C and C++ interoperability failures, especially the inability to pass bit-field structs or call C functions with `_BitInt` parameters portably.
- The paper also convincingly shows that a library-only approach cannot work because class types are disallowed in bit-fields and overload resolution across widths has no portable ABI fallback.
- Implementation experience is well documented, with Clang’s multi-year support for `_BitInt` and libc++’s existing trait behavior serving as evidence of practical viability.
- The most glaring omission is the unsupported claim about affected users: the paper says large amounts of existing code would implicitly opt in, but offers no evidence of such code or the scale of that impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.67/14)

Provisionally addressed: 7 of 7. Provisional points: 12.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.67   corroborated 12.67   accumulate 12.67   max 12.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 2.00  implementation 2.00
sample agreement: 93 of 98 section-criterion pairs unanimous (95%)
single-sample totals would have been: 12.50 / 13.00 / 12.50   (all 3 samples: 12.67)
headings: h2 11
on threshold: none
splits: audience[8] 1/1/0  audience[9] 0/1/1  prior_art[7] 0/2/2  implementation[6] 1/2/2
        implementation[8] 1/1/2
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
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): However, there has always been some enthusiasm in the committee for such a feature.
candidate 3 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 4 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.

## audience - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Core design  (part 1 of 2)                0/0/0  -> 0.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/1/0  -> 0.67
  [9] 6. Implementation experience                 0/1/1  -> 0.67
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 2 (found by 1 of 42 passes): This decision was motivated by the fact that otherwise, large amounts of existing code (not just the standard library, but also user code) would implicitly opt into supporting bit-precise integers
candidate 3 (found by 1 of 42 passes): This decision was motivated by the fact that otherwise, large amounts of existing code (not just the standard library, but also user code) would implicitly opt into supporting bit-precise integers, despite never being written with that intent.

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
  [12] 8. Wording  (part 2 of 2)                    1/1/1  -> 1.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 42 passes): Proposals like these are arguably obsolete if the same operation can be expressed by simply casting the operands to an integer with double the width prior to the multiplication.
candidate 3 (found by 3 of 42 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 4 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## vehicle - grade 2.00 (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 3 (found by 3 of 42 passes): The core language changes are essentially standardizing that compiler extension.
candidate 4 (found by 2 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.

## coordination - grade 2.00 (fired in 5 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 0/0/0  -> 0.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 3 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 4 (found by 3 of 42 passes): Without a single platform ABI, there would also be no portable way for code generated by different compilers to interoperate, such as compiling a C library with GCC and using it from Clang-compiled C++ code.

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
candidate 2 (found by 2 of 42 passes): While one could rely on the ABI of `uint32_t` and `_BitInt(32)` to be identical in the first overload, there certainly is no way to portably invoke the second overload.
candidate 3 (found by 1 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);` `_BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`

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
  [8] 5. Library design                            1/1/2  -> 1.33
  [9] 6. Implementation experience                 2/2/2  -> 2.00
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
