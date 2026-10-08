Verdict: Excellent (12/14)

The paper offers substantial support for standardizing `_BitInt` in C++, particularly through its arguments about C23 compatibility, ABI interoperability, and the impossibility of expressing the feature as a library type. The case is thinnest when it comes to demonstrating who is actually affected, where the evidence amounts to a claim about existing compiler extension usage rather than a concrete demonstration of user need.

- The strongest support is the interoperability argument: without a standard spelling and ABI, C++ cannot portably call C functions using `_BitInt` or pass C structs containing bit-precise integers.
- The paper also clearly establishes that a library type cannot solve the problem, since class types are not permitted in bit-fields and cannot match C calling conventions for these types.
- Implementation experience is well supported by Clang’s existing `_BitInt` extension and its use in C code, which grounds the proposal in practice rather than speculation.
- The most glaring omission is the lack of established evidence about who is affected: the GitHub search is offered as support, but the paper does not demonstrate that the cited usage reflects a meaningful or representative population of C++ developers.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.33/14)

Provisionally addressed: 7 of 7. Provisional points: 12.33 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.33   corroborated 12.00   accumulate 12.33   max 13.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.50  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 12.00 / 12.00 / 13.00   (all 3 samples: 12.33)
headings: h2 12
on threshold: insufficiency
splits: audience[6] 1/0/1  prior_art[9] 2/1/2  prior_art[13] 1/1/0  vehicle[10] 1/0/0
        coordination[2] 0/1/1  insufficiency[5] 0/1/2  implementation[5] 0/1/0
        implementation[6] 2/2/1
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
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
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

## audience - grade 0.83 (fired in 2 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Core design  (part 1 of 2)                1/0/1  -> 0.67
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 2 (found by 2 of 45 passes): If we look at how C users use `_BitInt`, [GitHub code search for `"_BitInt" language:C`](https://github.com/search?q=%22_BitInt%22+language%3AC+&type=code) yields examples such as:

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 6)
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
  [9] 6. Education                                 2/1/2  -> 1.67
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    1/1/1  -> 1.00
  [12] 9. Wording  (part 1 of 2)                    2/2/2  -> 2.00
  [13] 9. Wording  (part 2 of 2)                    1/1/0  -> 0.67
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 45 passes): Proposals like these are arguably obsolete if the same operation can be expressed by simply casting the operands to an integer with double the width prior to the multiplication.
candidate 3 (found by 3 of 45 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 4 (found by 3 of 45 passes): [[P3140R0]](https://wg21%2elink/p3140r0) got substantial criticism just for attempting to standardize 128-bit integers for embedded developers.

## vehicle - grade 2.00 (fired in 5 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/1/1  -> 1.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 1/0/0  -> 0.33
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 45 passes): If WG21 didn't standardize such a spelling for C++, users would likely create their own type aliases.
candidate 4 (found by 2 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`

## coordination - grade 2.00 (fired in 4 of 15 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/0/0  -> 0.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 2 (found by 3 of 45 passes): Without a single platform ABI, there would also be no portable way for code generated by different compilers to interoperate, such as compiling a C library with GCC and using it from Clang-compiled C++ code.
candidate 3 (found by 2 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 4 (found by 2 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`

## insufficiency - grade 1.50 (fired in 2 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/2  -> 1.00
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
candidate 2 (found by 1 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 3 (found by 1 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y); _BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`

## implementation - grade 2.00  [binary: max] (fired in 4 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/0  -> 0.33
  [6] 4. Core design  (part 1 of 2)                2/2/1  -> 1.67
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
candidate 4 (found by 1 of 45 passes): There are already targets with `_BitInt` supported by major compilers, and used by C developers:

-->
