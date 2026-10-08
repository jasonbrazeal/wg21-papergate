Verdict: Adequate (5/14)

The paper offers a narrow but real basis for standardization by showing that the current wording is actively contradicted by implementations and has accumulated unresolved core issues. Its support is thinnest, however, on the questions that would justify committee action: who is concretely affected, why the standard is the right place to fix the problem, and whether a library or other non-core change could address it.

- The strongest support is the demonstration that alignment rules are already a source of divergent implementation behavior and open core issues.
- The paper also establishes that prior art and alternatives exist, including a CWG issue and observable compiler differences.
- The most glaring omission is the absence of any established account of who is affected by the current wording in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.33   accumulate 5.83   max 7.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.00 / 6.00 / 6.00   (all 3 samples: 5.33)
headings: h2 6
on threshold: motivation, prior_art, coordination
splits: prior_art[6] 0/1/1  implementation[4] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]] and 9.13.2 [[dcl.align]].
candidate 2 (found by 3 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6))

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

## prior_art - grade 1.50 (fired in 4 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             1/1/1  -> 1.00
  [6] 5 Approach                                   0/1/1  -> 0.67
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Clang rejects alignment-specifiers on non-static data members of reference type, EDG accepts only if the specified alignment is stricter than the alignment in the absence of alignment-specifier, GCC and MSVC accept any alignment-specifier
candidate 2 (found by 3 of 21 passes): [CWG1211](https://cplusplus.github.io/CWG/issues/1211.html): presumably NAD, because [[basic.life]/1](https://wg21.link/basic.life#1) states that lifetime of an object cannot start until “storage with the proper alignment and size for type `T` is obtained”.
candidate 3 (found by 2 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]] (1211, 2840) and 9.13.2 [[dcl.align]] (1617, 2223, 3024).
candidate 4 (found by 2 of 21 passes): Alignment is an integral value directly corresponding to layout of objects in memory.

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
candidate 1 (found by 2 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6])
candidate 2 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6))

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
  [4] 3 Implementation divergence                  0/2/2  -> 1.33
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6)) ([Compiler Explorer](https://godbolt.org/z/EfEe4f1zb))

-->
