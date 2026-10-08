Verdict: Adequate (5/14)

The paper offers solid support in a few narrow areas, particularly in explaining why the current specification is unclear and in surveying existing terminology and practice, but it leaves most of the burden of justification unaddressed. The case is thinnest where it matters most for a standardization proposal: identifying who is affected, explaining why the standard is the right venue, and showing that a library solution would not suffice.

- The strongest support is the paper’s explanation that the core language currently leaves unspecified which values a floating-point type may represent, making the problem concrete and relevant.
- The paper also does well in reviewing prior terminology and alternatives, including the clearer “identical value representations” phrasing and the ISO/IEC 60559 term “bitwise identical.”
- The most glaring omission is the absence of any established account of who is affected by the current wording or who would benefit from the change.
- Equally missing is any demonstration that the standard, rather than a library or implementation guidance, is the necessary place to address the issue.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 3.33   accumulate 5.33   max 5.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 3.50 / 5.00   (all 3 samples: 4.50)
headings: h2 8
on threshold: motivation, prior_art
splits: motivation[5] 0/1/0  prior_art[8] 1/2/1  implementation[5] 2/0/2
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Q&A                                       0/1/0  -> 0.33
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

## prior_art - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Q&A                                       2/2/2  -> 2.00
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   1/2/1  -> 1.33
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Bits of information may be found in various parts of the standard, such as in the concept of "adhering to ISO/IEC 60559", `numeric_limits` requirements, the inheritance of C features such as `std::fpclassify`, etc.
candidate 2 (found by 3 of 27 passes): The original paper used the terminology identical value representations, which makes the intent obvious, unlike the current wording.
candidate 3 (found by 2 of 27 passes): The ISO/IEC 60559 standard also uses the term bitwise identical.
candidate 4 (found by 1 of 27 passes): While ISO/IEC 60559 requires a signaling NaN to exist for its interchange formats (see ISO/IEC 60559 §6.2 Operations with NaNs), this is ignored by implementations in practice.

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 9 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Q&A                                       2/0/2  -> 1.33
  [6] 4. Impact on the standard                    0/0/0  -> 0.00
  [7] 5. Impact on implementations                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): GCC, Clang, and MSVC implement the design of the original paper by mangling the bit-casting to an integer and mangling it into the name.

-->
