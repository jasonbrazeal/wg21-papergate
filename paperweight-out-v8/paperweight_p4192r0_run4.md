Verdict: Adequate (6/14)

The paper offers some useful evidence that the current alignment rules are inconsistently implemented and entangled with unresolved core issues, but it leaves large parts of the standardization case unargued. The thinnest areas are the absence of any account of who is affected, why a library solution would not suffice, and why the standard itself is the right place to address the problem.

- The strongest support is the demonstrated implementation divergence, with a concrete compiler example showing GCC accepting code that appears to violate the existing alignment-specifier rule.
- The paper also grounds its relevance in multiple open Core issues against the alignment clauses, indicating that the topic is already a recognized source of confusion.
- The discussion of prior art and alternatives is only partially established, mostly listing divergent compiler behavior and open issues without showing that the proposed direction is the appropriate resolution.
- The most glaring omission is the lack of any established case for who is affected or why the problem cannot be handled outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 4 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.00   accumulate 6.50   max 7.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 5.50 / 6.00   (all 3 samples: 5.83)
headings: h2 6
on threshold: motivation, prior_art, coordination, implementation
splits: prior_art[4] 2/1/2  prior_art[6] 0/0/1
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
candidate 1 (found by 3 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6))
candidate 2 (found by 2 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]](https://wg21.link/basic.align) ([1211](https://cplusplus.github.io/CWG/issues/1211.html), [2840](https://cplusplus.github.io/CWG/issues/2840.html)) and 9.13.2 [[dcl.align]](https://wg21.link/dcl.align) ([1617](https://cplusplus.github.io/CWG/issues/1617.html), [2223](https://cplusplus.github.io/CWG/issues/2223.html), [3024](https://cplusplus.github.io/CWG/issues/3024.html)).
candidate 3 (found by 1 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]](https://wg21.link/basic.align) and 9.13.2 [[dcl.align]](https://wg21.link/dcl.align).

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

## prior_art - grade 1.33 (fired in 4 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/1/2  -> 1.67
  [5] 4 Issues with status quo wording             1/1/1  -> 1.00
  [6] 5 Approach                                   0/0/1  -> 0.33
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Clang rejects alignment-specifiers on non-static data members of reference type, EDG accepts only if the specified alignment is stricter than the alignment in the absence of alignment-specifier, GCC and MSVC accept any alignment-specifier
candidate 2 (found by 3 of 21 passes): [CWG1211](https://cplusplus.github.io/CWG/issues/1211.html): presumably NAD, because [[basic.life]/1](https://wg21.link/basic.life#1) states that lifetime of an object cannot start until “storage with the proper alignment and size for type `T` is obtained”.
candidate 3 (found by 2 of 21 passes): There are multiple open Core issues against 6.8.3 [[basic.align]](https://wg21.link/basic.align) ([1211](https://cplusplus.github.io/CWG/issues/1211.html), [2840](https://cplusplus.github.io/CWG/issues/2840.html)) and 9.13.2 [[dcl.align]](https://wg21.link/dcl.align) ([1617](https://cplusplus.github.io/CWG/issues/1617.html), [2223](https://cplusplus.github.io/CWG/issues/2223.html), [3024](https://cplusplus.github.io/CWG/issues/3024.html)).
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
candidate 1 (found by 2 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6))
candidate 2 (found by 1 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6])

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Implementation divergence                  2/2/2  -> 2.00
  [5] 4 Issues with status quo wording             0/0/0  -> 0.00
  [6] 5 Approach                                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): GCC accepts a defining declaration without an alignment-specifier that happens to have the same alignment as specified in other declarations (in violation of [[dcl.align]/6](https://wg21.link/dcl.align#6)) ([Compiler Explorer](https://godbolt.org/z/EfEe4f1zb)):

-->
