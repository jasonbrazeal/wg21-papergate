Verdict: Adequate (4/14)

The paper offers a solid account of why the current specification is unclear and what existing practice looks like, but it leaves several essential parts of the standardization case largely unaddressed. The strongest material concerns the problem statement and the record of prior art and implementation behavior; the thinnest concerns who is affected, why a standard change is the right remedy, and how the change would coordinate with other specifications.

- The paper clearly establishes that the standard does not specify which values a floating-point type may represent, and that this ambiguity matters for the language model.
- It also documents relevant prior art and shows that major implementations already follow the proposed mangling approach.
- The paper does not establish who is affected by the current state of affairs or what practical harm they experience.
- Most notably, it does not make the case that this belongs in the standard rather than in a library or implementation documentation, nor does it address coordination with C or other relevant specifications.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 3 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 3.67   accumulate 4.67   max 4.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.50 / 5.50 / 3.50   (all 3 samples: 4.17)
headings: h2 8
on threshold: motivation
splits: motivation[5] 1/0/0  implementation[5] 0/2/0  implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Q&A                                       1/0/0  -> 0.33
  [6] 4. Impact on the standard                    1/1/1  -> 1.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It is not specified what values a floating-point type may represent in C++, leading to an unclear model for floating-point types.
candidate 2 (found by 3 of 27 passes): The core language wording in the C++ standard does not specify what values a floating-point type may represent.
candidate 3 (found by 3 of 27 passes): In the long run, specifying the handling of NaNs and infinities by C++ expressions, documenting ISO/IEC 60559 conformance, and other large changes may be desirable.
candidate 4 (found by 1 of 27 passes): While neither the C23 wording nor the C++ wording handles these extra implementation-defined classifications well, they nonetheless exist, and it seems like an unmotivated breaking change to drop support for them.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Q&A                                       0/0/0  -> 0.00
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Q&A                                       2/2/2  -> 2.00
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   2/2/2  -> 2.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Bits of information may be found in various parts of the standard, such as in the concept of "adhering to ISO/IEC 60559", `numeric_limits` requirements, the inheritance of C features such as `std::fpclassify`, etc.
candidate 2 (found by 3 of 27 passes): While ISO/IEC 60559 requires a signaling NaN to exist for its interchange formats (see ISO/IEC 60559 §6.2 Operations with NaNs), this is ignored by implementations in practice.
candidate 3 (found by 2 of 27 passes): It was added during C++20 NB comment resolution by [[P1907R1]](https://wg21%2elink/p1907r1), after [[P1714R1]](https://wg21%2elink/p1714r1) (the paper which originally added support for floating-point template parameters) was rejected.
candidate 4 (found by 1 of 27 passes): GCC, Clang, and MSVC implement the design of the original paper by mangling the bit-casting to an integer and mangling it into the name.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Q&A                                       0/0/0  -> 0.00
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Q&A                                       0/0/0  -> 0.00
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Q&A                                       0/0/0  -> 0.00
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.67  [binary: max] (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Q&A                                       0/2/0  -> 0.67
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/1/0  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): GCC, Clang, and MSVC implement the design of the original paper by mangling the bit-casting to an integer and mangling it into the name.
candidate 2 (found by 1 of 27 passes): All proposed wording changes document the current behavior of major implementations.

-->
