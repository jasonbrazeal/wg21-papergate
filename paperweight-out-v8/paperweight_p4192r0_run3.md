Verdict: Adequate (6/14)

The paper offers some useful groundwork by identifying unresolved Core issues and documenting divergent implementation behavior, but it does not build a complete case for standardization. The strongest support concerns the existence of a real specification problem, while the thinnest areas are the absence of any argument for why the standard is the right venue and why a library solution cannot suffice.

- The paper establishes that alignment rules have multiple open Core issues and that implementations already disagree about how to interpret them.
- It also establishes relevant prior art by citing CWG1211 and showing concrete divergence among GCC, Clang, MSVC, and EDG.
- The paper only claims, without establishing, who is affected and what implementation experience exists, relying on a single compiler acceptance example rather than broader evidence.
- It offers no established case for why standardization is needed, why a library will not do, or how coordination and interoperability would be handled.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 5 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.50   max 8.00

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 1.50  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 6.00 / 4.00   (all 3 samples: 5.67)
headings: h2 6
on threshold: motivation, prior_art, coordination
splits: motivation[5] 1/0/1  audience[4] 2/0/0  prior_art[6] 1/0/1  implementation[4] 2/2/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             1/0/1  -> 0.67
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): There are multiple open Core issues against 6.8.3 [basic.align] and 9.13.2 [dcl.align].
candidate 2 (found by 2 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6))
candidate 3 (found by 1 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]] and 9.13.2 [[dcl.align]].
candidate 4 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6])

## audience - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/0/0  -> 0.67
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6)) ([Compiler Explorer](https://godbolt.org/z/EfEe4f1zb))

## prior_art - grade 1.50 (fired in 4 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             1/1/1  -> 1.00
  [6] 5 Approach                                   1/0/1  -> 0.67
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): [CWG1211](https://cplusplus.github.io/CWG/issues/1211.html): presumably NAD, because [[basic.life]/1](https://wg21.link/basic.life#1) states that lifetime of an object cannot start until “storage with the proper alignment and size for type `T` is obtained”.
candidate 2 (found by 2 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]](https://wg21.link/basic.align) ([1211](https://cplusplus.github.io/CWG/issues/1211.html), [2840](https://cplusplus.github.io/CWG/issues/2840.html)) and 9.13.2 [[dcl.align]](https://wg21.link/dcl.align) ([1617](https://cplusplus.github.io/CWG/issues/1617.html), [2223](https://cplusplus.github.io/CWG/issues/2223.html), [3024](https://cplusplus.github.io/CWG/issues/3024.html)).
candidate 3 (found by 2 of 21 passes): Clang and GCC prioritize `#pragma pack` over alignment-specifiers of non-static data members and their types, MSVC does the opposite, while EDG prioritize `#pragma pack` over alignment-specifier of types but not of non-static data members
candidate 4 (found by 1 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]] (1211, 2840) and 9.13.2 [[dcl.align]] (1617, 2223, 3024).

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  0/0/0  -> 0.00
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6])

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  0/0/0  -> 0.00
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/0  -> 1.33
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6)) ([Compiler Explorer](https://godbolt.org/z/EfEe4f1zb)):
candidate 2 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations ([Compiler Explorer](https://godbolt.org/z/EfEe4f1zb))

-->
