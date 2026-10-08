Verdict: Excellent (13/14)

The paper makes a reasonably strong case that bit-precise integers need language-level standardization, particularly for C23 compatibility and ABI interoperability, and it documents relevant implementation experience in Clang. The thinnest part of the argument is the evidence about who is affected: the paper gestures at existing users and code-search examples, but does not establish the breadth or significance of that population.

- The strongest support is the demonstration that C++ currently has no portable way to call C functions using `_BitInt` parameters or to pass C structs containing bit-precise integer fields across language boundaries.
- The paper also clearly establishes that a library type cannot solve the problem, since class types cannot be used in bit-fields and cannot reproduce the required overload resolution or ABI behavior.
- The implementation-experience case is solid, with Clang’s multi-year support for `_BitInt` as an extension and libc++ already treating it as an integral type.
- The most glaring omission is the lack of established evidence about who is actually affected, since the cited code-search examples and target support do not by themselves show a substantial or representative user base.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (13.00/14)

Provisionally addressed: 7 of 7. Provisional points: 13.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 13.00   corroborated 12.00   accumulate 13.33   max 13.67

## SUMMARY
grades: motivation 2.00  audience 1.33  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.67  implementation 2.00
sample agreement: 86 of 98 section-criterion pairs unanimous (88%)
single-sample totals would have been: 13.00 / 13.50 / 12.50   (all 3 samples: 13.00)
headings: h2 11
on threshold: audience, insufficiency
splits: motivation[7] 2/2/1  audience[5] 0/0/1  audience[6] 1/0/0  audience[8] 1/2/2
        prior_art[7] 2/0/2  prior_art[11] 0/1/2  vehicle[2] 0/1/1  coordination[8] 0/2/0
        insufficiency[5] 2/2/0  implementation[5] 1/0/0  implementation[6] 1/1/2
        implementation[9] 1/1/2
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
  [7] 4. Core design  (part 2 of 2)                2/2/1  -> 1.67
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 42 passes): However, there has always been some enthusiasm in the committee for such a feature.
candidate 3 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 4 (found by 3 of 42 passes): In conclusion, discrepancies between the standard integers and bit-precise integers are undesirable; they introduce a lot of unnecessary problems.

## audience - grade 1.33 (fired in 4 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/1  -> 0.33
  [6] 4. Core design  (part 1 of 2)                1/0/0  -> 0.33
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            1/2/2  -> 1.67
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 2 (found by 2 of 42 passes): libc++ already makes `std::is_integral_v<_BitInt(N)>` `true`, so what LEWG wants is silently altering the behavior of existing traits.
candidate 3 (found by 1 of 42 passes): There are already targets with `_BitInt` supported by major compilers, and used by C developers:
candidate 4 (found by 1 of 42 passes): If we look at how C users use `_BitInt`, [GitHub code search for `"_BitInt" language:C`](https://github.com/search?q=%22_BitInt%22+language%3AC+&type=code) yields examples such as:

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/0/2  -> 1.33
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/1/1  -> 1.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/1/2  -> 1.00
  [12] 8. Wording  (part 2 of 2)                    1/1/1  -> 1.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 42 passes): [[P3161R4]](https://wg21%2elink/p3161r4) proposes library features such as `add_carry` or `mul_wide` which produce a wider integer result than the operands.
candidate 3 (found by 3 of 42 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 4 (found by 3 of 42 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.

## vehicle - grade 2.00 (fired in 3 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
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
candidate 1 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 2 of 42 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.

## coordination - grade 2.00 (fired in 4 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            0/2/0  -> 0.67
  [9] 6. Implementation experience                 0/0/0  -> 0.00
  [10] 7. Impact on the standard                    0/0/0  -> 0.00
  [11] 8. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [12] 8. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [13] 9. Acknowledgements                          0/0/0  -> 0.00
  [14] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);`
candidate 2 (found by 3 of 42 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 42 passes): Without a single platform ABI, there would also be no portable way for code generated by different compilers to interoperate, such as compiling a C library with GCC and using it from Clang-compiled C++ code.
candidate 4 (found by 1 of 42 passes): Due to the current wording in [[range.iota.view] paragraph 1](https://eel.is/c++draft/range.iota.view#1), adding bit-precise integers or extended integers of greater width than `long long` potentially forces the implementation to redefine `ranges::iota_view::iterator::difference_type`.

## insufficiency - grade 1.67 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/0  -> 1.33
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
candidate 2 (found by 1 of 42 passes): While one could rely on the ABI of `uint32_t` and `_BitInt(32)` to be identical in the first overload, there certainly is no way to portably invoke the second overload.
candidate 3 (found by 1 of 42 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y); _BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`

## implementation - grade 2.00  [binary: max] (fired in 5 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/0/0  -> 0.33
  [6] 4. Core design  (part 1 of 2)                1/1/2  -> 1.33
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            2/2/2  -> 2.00
  [9] 6. Implementation experience                 1/1/2  -> 1.33
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
