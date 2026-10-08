Verdict: Excellent (12/14)

The paper gives solid support for the core compatibility and standardization rationale, particularly around C23 interoperation and the impossibility of expressing bit-precise integers as library types in all the necessary contexts. The case is thinnest when it comes to showing who is actually affected, where the paper leans on Clang’s extension and a poll result without demonstrating a clear body of existing C++ code or users that would benefit.

- The strongest support is the established need for C and C++ compatibility, since C23 bit-precise integers cannot be represented by class types in bit-fields or portably passed across language boundaries.
- The paper also convincingly shows why a library-only approach is insufficient, because class types cannot appear in bit-fields and cannot portably match C functions using `_BitInt` parameters.
- The implementation experience claim is well supported by Clang’s long-standing `_ExtInt`/`_BitInt` extension and existing libc++ trait behavior.
- The most glaring omission is the lack of established evidence about who is affected, since the paper asserts existing practice and user impact but does not demonstrate substantial real-world C++ code relying on or needing this feature.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.50/14)

Provisionally addressed: 7 of 7. Provisional points: 12.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.50   corroborated 12.00   accumulate 12.83   max 13.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.67  implementation 2.00
sample agreement: 86 of 98 section-criterion pairs unanimous (88%)
single-sample totals would have been: 12.50 / 12.00 / 13.50   (all 3 samples: 12.50)
headings: h2 11
on threshold: insufficiency
splits: motivation[7] 2/1/2  motivation[9] 0/1/1  audience[6] 0/1/1  audience[8] 1/0/2
        audience[9] 0/1/1  prior_art[2] 2/1/1  prior_art[7] 2/0/0  prior_art[12] 0/1/1
        vehicle[4] 0/0/2  coordination[8] 2/1/2  insufficiency[5] 2/0/2  implementation[5] 1/0/0
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
  [7] 4. Core design  (part 2 of 2)                2/1/2  -> 1.67
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 0/1/1  -> 0.67
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 42 passes): In conclusion, discrepancies between the standard integers and bit-precise integers are undesirable; they introduce a lot of unnecessary problems.
candidate 4 (found by 3 of 42 passes): Trying to word and implement support for `_BitInt` all in one paper is simply too much.

## audience - grade 0.83 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Core design  (part 1 of 2)                0/1/1  -> 0.67
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/0/2  -> 1.00
  [9] 6. Implementation experience                 0/1/1  -> 0.67
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Clang already supports the `_BitInt` keyword spelling as a compiler extension, so this is standardizing existing practice.
candidate 2 (found by 2 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 3 (found by 1 of 42 passes): This decision was motivated by the fact that otherwise, large amounts of existing code (not just the standard library, but also user code) would implicitly opt into supporting bit-precise integers
candidate 4 (found by 1 of 42 passes): > **POLL**: We should prevent library support for _BitInt

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/1  -> 1.33
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/0/0  -> 0.67
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    2/2/2  -> 2.00
  [12] 8. Wording  (part 2 of 2)                    0/1/1  -> 0.67
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 42 passes): Proposals like these are arguably obsolete if the same operation can be expressed by simply casting the operands to an integer with double the width prior to the multiplication.
candidate 3 (found by 3 of 42 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 4 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## vehicle - grade 2.00 (fired in 5 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/2  -> 0.67
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
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 42 passes): The core language changes are essentially standardizing that compiler extension.
candidate 4 (found by 2 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`

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
  [8] 5. Library design                            2/1/2  -> 1.67
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

## insufficiency - grade 1.67 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/0/2  -> 1.33
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

## implementation - grade 2.00  [binary: max] (fired in 5 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/0/0  -> 0.33
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/2/2  -> 2.00
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
