Verdict: Adequate (4/14)

The paper offers some support for standardization by pointing to unresolved Core issues and divergent implementation behavior, but it leaves most of the necessary case unstated. The thinnest areas are the absence of any discussion of who is affected, why a library solution is insufficient, and whether there is implementation experience to justify the change.

- The strongest support is the identification of multiple open Core issues and a concrete example of GCC accepting code in violation of the current wording.
- The paper gestures at prior art by citing issue numbers and compiler differences, but does not develop those into a clear argument that standardization is the right path.
- The most glaring omission is the lack of any account of who is affected by the current rules or what practical problem they face.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 3 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 3.00   accumulate 4.67   max 5.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.00 / 3.50 / 4.00   (all 3 samples: 3.83)
headings: h2 6
on threshold: motivation, prior_art, coordination
splits: motivation[5] 1/1/0  prior_art[4] 2/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             1/1/0  -> 0.67
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): There are multiple open Core issues against 6.8.3 [basic.align] and 9.13.2 [dcl.align].
candidate 2 (found by 2 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6))
candidate 3 (found by 1 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]] and 9.13.2 [[dcl.align]].
candidate 4 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6])

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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

## prior_art - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/1/2  -> 1.67
  [5] 4 Issues with status quo wording             1/1/1  -> 1.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]](https://wg21.link/basic.align) ([1211](https://cplusplus.github.io/CWG/issues/1211.html), [2840](https://cplusplus.github.io/CWG/issues/2840.html)) and 9.13.2 [[dcl.align]](https://wg21.link/dcl.align) ([1617](https://cplusplus.github.io/CWG/issues/1617.html), [2223](https://cplusplus.github.io/CWG/issues/2223.html), [3024](https://cplusplus.github.io/CWG/issues/3024.html)).
candidate 2 (found by 3 of 21 passes): Clang rejects alignment-specifiers on non-static data members of reference type, EDG accepts only if the specified alignment is stricter than the alignment in the absence of alignment-specifier, GCC and MSVC accept any alignment-specifier
candidate 3 (found by 3 of 21 passes): [CWG1211](https://cplusplus.github.io/CWG/issues/1211.html): presumably NAD, because [[basic.life]/1](https://wg21.link/basic.life#1) states that lifetime of an object cannot start until “storage with the proper alignment and size for type `T` is obtained”.

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

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
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

-->
