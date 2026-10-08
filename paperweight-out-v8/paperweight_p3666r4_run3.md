Verdict: Excellent (13/14)

The paper offers substantial support for standardizing bit-precise integers, particularly through its discussion of C compatibility, existing implementation experience, and the impossibility of a library-only solution. The case is thinnest when it comes to showing who is actually affected: the paper gestures at compiler extension use and community interest, but does not establish a concrete user base or demand.

- The strongest support is the demonstration that C++ currently cannot portably call C functions using `_BitInt` parameters or return types, including cases where no ordinary integer type can stand in.
- The paper also convincingly shows that a library type cannot solve the problem because class types are not permitted in bit-fields and cannot reproduce the necessary ABI and overload behavior.
- The implementation experience is well grounded in Clang’s existing `_BitInt` extension and libc++’s current trait behavior, which gives the proposal a practical foundation.
- The most glaring omission is the lack of established evidence about who is affected, since the paper cites compiler extension availability and committee enthusiasm but does not show meaningful existing use or user demand.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.83/14)

Provisionally addressed: 7 of 7. Provisional points: 12.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.83   corroborated 13.00   accumulate 13.17   max 13.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 2.00  implementation 2.00
sample agreement: 85 of 98 section-criterion pairs unanimous (87%)
single-sample totals would have been: 13.00 / 13.00 / 13.00   (all 3 samples: 12.83)
headings: h2 11
on threshold: none
splits: motivation[9] 0/0/1  audience[4] 1/0/0  audience[5] 0/1/0  audience[8] 1/0/1
        prior_art[7] 0/0/2  prior_art[11] 1/2/2  prior_art[12] 0/1/0  vehicle[8] 1/0/1
        vehicle[9] 0/1/0  coordination[4] 0/0/1  implementation[6] 2/2/1
        implementation[8] 2/1/2  implementation[9] 2/2/1
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
  [9] 6. Implementation experience                 0/0/1  -> 0.33
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): However, there has always been some enthusiasm in the committee for such a feature.
candidate 3 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 4 (found by 3 of 42 passes): In conclusion, discrepancies between the standard integers and bit-precise integers are undesirable; they introduce a lot of unnecessary problems.

## audience - grade 0.83 (fired in 4 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/0/0  -> 0.33
  [5] 3. Motivation                                0/1/0  -> 0.33
  [6] 4. Core design  (part 1 of 2)                0/0/0  -> 0.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/0/1  -> 0.67
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 2 (found by 1 of 42 passes): However, there has always been some enthusiasm in the committee for such a feature.
candidate 3 (found by 1 of 42 passes): There are already targets with `_BitInt` supported by major compilers, and used by C developers
candidate 4 (found by 1 of 42 passes): This poll result caused widespread backlash from members of the committee, Clang implementers, and the C++ community at large.

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/2  -> 0.67
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    1/2/2  -> 1.67
  [12] 8. Wording  (part 2 of 2)                    0/1/0  -> 0.33
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 42 passes): [[P3161R4]](https://wg21%2elink/p3161r4) proposes library features such as `add_carry` or `mul_wide` which produce a wider integer result than the operands.
candidate 3 (found by 3 of 42 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 4 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## vehicle - grade 2.00 (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/0/1  -> 0.67
  [9] 6. Implementation experience                 0/1/0  -> 0.33
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 2 of 42 passes): This happens because bit-precise integers are proposed to be signed and unsigned integer types, so they would be supported by any facility that supports integer types (e.g. `<bit>`).
candidate 4 (found by 1 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now. The core language changes are essentially standardizing that compiler extension.

## coordination - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/1  -> 0.33
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
candidate 3 (found by 1 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Core design  (part 1 of 2)                2/2/1  -> 1.67
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/1/2  -> 1.67
  [9] 6. Implementation experience                 2/2/1  -> 1.67
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
