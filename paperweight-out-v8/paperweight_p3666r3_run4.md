Verdict: Excellent (12/14)

The paper makes a reasonably strong case that C++ needs a core-language bit-precise integer type, particularly for C23 compatibility and ABI interoperation, and it grounds that case in existing compiler practice. The support is thinnest around the claimed urgency and breadth of affected users, where the paper asserts a pressing compatibility problem but does not substantiate how widespread or immediate that need is.

- The strongest support is the demonstration that only a core-language type can handle C `_BitInt` function signatures and bit-fields portably, which a library type cannot do.
- The paper also establishes solid prior art and implementation experience by pointing to Clang’s years-long support for `_BitInt` and the design discussions already held in WG21.
- The most glaring omission is the lack of evidence for who is actually affected today, since the paper claims urgency but relies mainly on a reference to another proposal rather than showing concrete user or industry demand.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 11.67   accumulate 12.17   max 12.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.67  implementation 2.00
sample agreement: 91 of 105 section-criterion pairs unanimous (87%)
single-sample totals would have been: 12.00 / 11.50 / 13.00   (all 3 samples: 12.17)
headings: h2 12
on threshold: insufficiency
splits: motivation[7] 2/1/2  audience[5] 0/1/1  audience[10] 0/0/1  prior_art[2] 1/1/2
        prior_art[5] 2/0/2  prior_art[11] 0/1/1  prior_art[12] 2/1/2  prior_art[13] 0/1/0
        vehicle[2] 1/0/0  vehicle[8] 0/1/0  vehicle[10] 0/1/1  coordination[8] 1/1/0
        insufficiency[5] 2/0/2  implementation[5] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 15 sections, strong in 4)  (SHARED PASSAGE)
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
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 3 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 4 (found by 3 of 45 passes): In conclusion, discrepancies between the standard integers and bit-precise integers are undesirable; they introduce a lot of unnecessary problems.

## audience - grade 0.50 (fired in 2 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/1  -> 0.67
  [6] 4. Core design  (part 1 of 2)                0/0/0  -> 0.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/0/1  -> 0.33
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): This compatibility problem is not a hypothetical concern either; it is an urgent problem.
candidate 2 (found by 1 of 45 passes): A large amount of motivation for 128-bit computation can be found in [[P3140R0]](https://wg21%2elink/p3140r0).
candidate 3 (found by 1 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/2  -> 1.33
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/0/2  -> 1.33
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Education                                 2/2/2  -> 2.00
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    0/1/1  -> 0.67
  [12] 9. Wording  (part 1 of 2)                    2/1/2  -> 1.67
  [13] 9. Wording  (part 2 of 2)                    0/1/0  -> 0.33
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 45 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 3 (found by 3 of 45 passes): [[P3140R0]](https://wg21%2elink/p3140r0) got substantial criticism just for attempting to standardize 128-bit integers for embedded developers.
candidate 4 (found by 3 of 45 passes): SG22 and SG6 gave feedback on the library design in this paper. While no clear direction was given, there was scepticism regarding the amount of changes made to the library.

## vehicle - grade 2.00 (fired in 5 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/1/0  -> 0.33
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/1/1  -> 0.67
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 2 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 2 of 45 passes): The core language changes are essentially standardizing that compiler extension.
candidate 4 (found by 1 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.

## coordination - grade 2.00 (fired in 5 of 15 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            1/1/0  -> 0.67
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/0/0  -> 0.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 45 passes): Without a single platform ABI, there would also be no portable way for code generated by different compilers to interoperate, such as compiling a C library with GCC and using it from Clang-compiled C++ code.
candidate 4 (found by 2 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`

## insufficiency - grade 1.67 (fired in 2 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/0/0  -> 0.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 2 (found by 2 of 45 passes): While one could rely on the ABI of `uint32_t` and `_BitInt(32)` to be identical in the first overload, there certainly is no way to portably invoke the second overload.

## implementation - grade 2.00  [binary: max] (fired in 4 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/0/1  -> 0.67
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Clang already supports the `_BitInt` keyword spelling as a compiler extensions, so this is standardizing existing practice.
candidate 2 (found by 3 of 45 passes): This behavior is already implemented by Clang as a C++ compiler extension, and makes deduction behave identically to deducing sizes of arrays.
candidate 3 (found by 3 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 4 (found by 2 of 45 passes): There are already targets with `_BitInt` supported by major compilers, and used by C developers

-->
