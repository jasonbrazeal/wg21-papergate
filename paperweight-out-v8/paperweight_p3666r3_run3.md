Verdict: Excellent (12/14)

The paper offers solid support for the core compatibility and language-level arguments, particularly around C interoperability and the impossibility of a library-only solution. The thinnest part is the claim about who is affected, which rests on a passing reference to Clang’s extension rather than any demonstration of user demand or breadth of impact.

- The strongest support is the repeated, concrete demonstration that C23 bit-precise integers cannot be portably called or represented from C++ without a language feature.
- The paper also establishes that prior design alternatives were explored and that a library type cannot satisfy the bit-field and ABI requirements.
- Implementation experience is credited through Clang’s existing support, though the paper leans heavily on that single implementation.
- The most glaring omission is any real evidence about who is affected, since the only supporting statement merely notes that Clang has shipped the extension for years.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.83/14)

Provisionally addressed: 7 of 7. Provisional points: 11.83 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.83   corroborated 11.67   accumulate 11.83   max 12.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.50  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 12.00 / 12.00 / 11.50   (all 3 samples: 11.83)
headings: h2 12
on threshold: insufficiency
splits: motivation[7] 2/1/2  motivation[8] 1/2/2  audience[10] 1/1/0  prior_art[9] 2/2/1
        prior_art[11] 0/1/1  prior_art[13] 0/1/1  implementation[5] 0/1/1
        implementation[6] 1/2/2
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
  [8] 5. Library design                            1/2/2  -> 1.67
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

## audience - grade 0.33 (fired in 1 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Core design  (part 1 of 2)                0/0/0  -> 0.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 1/1/0  -> 0.67
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## prior_art - grade 2.00 (fired in 9 of 15 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Education                                 2/2/1  -> 1.67
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    0/1/1  -> 0.67
  [12] 9. Wording  (part 1 of 2)                    2/2/2  -> 2.00
  [13] 9. Wording  (part 2 of 2)                    0/1/1  -> 0.67
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 45 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 3 (found by 3 of 45 passes): The closest equivalents to `std::bit_int` and `std::bit_uint` are `std::intN_t` and `std::uintN_t`, respectively.
candidate 4 (found by 3 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## vehicle - grade 2.00 (fired in 4 of 15 sections, strong in 2)  (SHARED PASSAGE)
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
candidate 4 (found by 3 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## coordination - grade 2.00 (fired in 5 of 15 sections, strong in 4)  (SHARED PASSAGE)
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
candidate 4 (found by 3 of 45 passes): The worst possible scenario is a "tower of babel" situation where every code base has a slightly different spelling of the same C++ construct.

## insufficiency - grade 1.50 (fired in 2 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
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
candidate 2 (found by 2 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 3 (found by 1 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y); _BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`

## implementation - grade 2.00  [binary: max] (fired in 4 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/1  -> 0.67
  [6] 4. Core design  (part 1 of 2)                1/2/2  -> 1.67
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
