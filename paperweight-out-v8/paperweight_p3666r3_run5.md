Verdict: Excellent (13/14)

The paper gives solid support for much of the standardization case, particularly around C compatibility, ABI interoperability, and the impossibility of expressing the feature as a library type. The thinnest part is the claim about who is affected: the paper gestures at existing compiler and target support but does not actually demonstrate a user population or demand.

- The strongest support is the repeated, concrete demonstration that C++ cannot portably call C functions using `_BitInt` or pass structs containing bit-precise fields across the language boundary.
- The paper also clearly establishes that a library type cannot substitute for a fundamental type, especially because class types are not permitted in bit-fields.
- The implementation-experience case is well grounded in Clang’s existing extension and its behavior in deduction.
- The most glaring omission is the lack of evidence for who is affected, since the paper names compilers and targets but offers no substantiation of actual C or C++ developers relying on `_BitInt` today.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.50/14)

Provisionally addressed: 7 of 7. Provisional points: 12.50 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.50   corroborated 12.67   accumulate 12.50   max 12.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 2.00  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 12.00 / 13.00 / 12.50   (all 3 samples: 12.50)
headings: h2 12
on threshold: none
splits: motivation[10] 0/0/1  audience[5] 0/1/0  audience[10] 0/1/1  prior_art[9] 2/1/1
        vehicle[8] 0/1/0  coordination[2] 0/1/1  coordination[8] 0/2/0  implementation[5] 0/0/1
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
  [10] 7. Implementation experience                 0/0/1  -> 0.33
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.
candidate 2 (found by 3 of 45 passes): However, there has always been some enthusiasm in the committee for such a feature.
candidate 3 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 4 (found by 3 of 45 passes): In conclusion, discrepancies between the standard integers and bit-precise integers are undesirable; they introduce a lot of unnecessary problems.

## audience - grade 0.50 (fired in 2 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/1/0  -> 0.33
  [6] 4. Core design  (part 1 of 2)                0/0/0  -> 0.00
  [7] 4. Core design  (part 2 of 2)                0/0/0  -> 0.00
  [8] 5. Library design                            0/0/0  -> 0.00
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/1/1  -> 0.67
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): `_BitInt`, formerly known as `_ExtInt`, has been a compiler extension in Clang for several years now.
candidate 2 (found by 1 of 45 passes): There are already targets with `_BitInt` supported by major compilers, and used by C developers:

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 5)
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
  [9] 6. Education                                 2/1/1  -> 1.33
  [10] 7. Implementation experience                 1/1/1  -> 1.00
  [11] 8. Impact on the standard                    1/1/1  -> 1.00
  [12] 9. Wording  (part 1 of 2)                    2/2/2  -> 2.00
  [13] 9. Wording  (part 2 of 2)                    1/1/1  -> 1.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Following an exploration of possible designs in [[P3639R0]](https://wg21%2elink/p3639r0) "The `_BitInt` Debate", this proposal introduces a new set of fundamental types to C++.
candidate 2 (found by 3 of 45 passes): Proposals like these are arguably obsolete if the same operation can be expressed by simply casting the operands to an integer with double the width prior to the multiplication.
candidate 3 (found by 3 of 45 passes): [[P3639R0]](https://wg21%2elink/p3639r0) explored in detail whether to make it a fundamental type or a library type.
candidate 4 (found by 3 of 45 passes): SG22 and SG6 gave feedback on the library design in this paper. While no clear direction was given, there was scepticism regarding the amount of changes made to the library.

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
  [8] 5. Library design                            0/1/0  -> 0.33
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

## coordination - grade 2.00 (fired in 5 of 15 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Core design  (part 1 of 2)                2/2/2  -> 2.00
  [7] 4. Core design  (part 2 of 2)                2/2/2  -> 2.00
  [8] 5. Library design                            0/2/0  -> 0.67
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/0/0  -> 0.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y); _BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`
candidate 2 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 3 (found by 3 of 45 passes): Without a single platform ABI, there would also be no portable way for code generated by different compilers to interoperate, such as compiling a C library with GCC and using it from Clang-compiled C++ code.
candidate 4 (found by 2 of 45 passes): C23 has introduced so-called "bit-precise integers" into the language, which should be brought to C++ for compatibility, among other reasons.

## insufficiency - grade 2.00 (fired in 2 of 15 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 6. Education                                 0/0/0  -> 0.00
  [10] 7. Implementation experience                 0/0/0  -> 0.00
  [11] 8. Impact on the standard                    0/0/0  -> 0.00
  [12] 9. Wording  (part 1 of 2)                    0/0/0  -> 0.00
  [13] 9. Wording  (part 2 of 2)                    0/0/0  -> 0.00
  [14] 10. Acknowledgements                         0/0/0  -> 0.00
  [15] 11. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Since C++ does not support the use of class types in bit-fields, such a `struct S` could not be passed from C++ to a C API.
candidate 2 (found by 1 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y); _BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`
candidate 3 (found by 1 of 45 passes): C++ currently has no portable way to call C functions such as: `_BitInt(32) plus( _BitInt(32) x, _BitInt(32) y);` `_BitInt(128) plus(_BitInt(128) x, _BitInt(128) y);`
candidate 4 (found by 1 of 45 passes): While one could rely on the ABI of `uint32_t` and `_BitInt(32)` to be identical in the first overload, there certainly is no way to portably invoke the second overload.

## implementation - grade 2.00  [binary: max] (fired in 4 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/1  -> 0.33
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
candidate 4 (found by 1 of 45 passes): There are already targets with `_BitInt` supported by major compilers, and used by C developers:

-->
