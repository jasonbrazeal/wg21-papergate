Verdict: Adequate to Strong (7/14)

The paper offers some concrete grounding for its proposal, chiefly through implementation experience and a clear statement of the problem it aims to solve, but much of the broader case for standardization rests on assertions rather than demonstrated need. The thinnest support appears where the paper relies on general claims about interface familiarity, performance, and the inadequacy of library-only solutions without showing how those claims connect to the specific proposal.

- The strongest support is the implementation experience, with a patch series and benchmark details showing the proposed wording changes have been worked through in libstdc++.
- The paper clearly establishes why the current `strided_slice` specification is problematic, citing division cost and incompatibility with non-unique layouts.
- The case for who is affected and what alternatives exist is asserted through surveys and imagined future types, but the paper does not show how those affected would actually use or benefit from the change.
- The most glaring omission is the absence of any established argument for why a library solution would not suffice, leaving the necessity of standardization itself unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.33   accumulate 7.17   max 8.67

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.17  vehicle 0.67  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.50 / 6.50 / 6.50   (all 3 samples: 6.67)
headings: h2 4
on threshold: motivation, audience
splits: prior_art[4] 0/2/2  vehicle[4] 1/1/0  vehicle[5] 1/0/1  coordination[5] 2/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).
candidate 2 (found by 2 of 15 passes): This change preserve more ergonomic and familiar interface for `submdspan`.
candidate 3 (found by 1 of 15 passes): While this is an extension that can be added in a later standard, this change preserve more ergonomic and familiar interface for `submdspan`.

## audience - grade 1.00 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): Results from a benchmark similar to one used above show no significant performance difference.
candidate 2 (found by 1 of 15 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## prior_art - grade 1.17 (fired in 3 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/2/2  -> 1.33
  [5] 4. Ship vehicle and polls                    1/1/1  -> 1.00
candidate 1 (found by 2 of 15 passes): Introduce a non-canonical `range_slice` slice type, that expresses the `(first, last, stride)` interface provided for range slicing in other programming languages.
candidate 2 (found by 2 of 15 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard.
candidate 3 (found by 1 of 15 passes): This change would be breaking after C++26 is shipped.
candidate 4 (found by 1 of 15 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## vehicle - grade 0.67 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/1/0  -> 0.67
  [5] 4. Ship vehicle and polls                    1/0/1  -> 0.67
candidate 1 (found by 2 of 15 passes): In contrast, with this paper's proposed changes, the members of `strided_slice` directly represent values used by `submdspan` creation.
candidate 2 (found by 2 of 15 passes): Thus, it is important that the interface is both mininal (reducing the burden on layouts implementers) and able to represent a wide range of input without loss of information.

## coordination - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    2/0/0  -> 0.67
candidate 1 (found by 1 of 15 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): More details about above results may be found [here](https://gcc.gnu.org/pipermail/libstdc++/2026-January/065129.html).
candidate 2 (found by 3 of 15 passes): Here is a [patch series](https://gcc.gnu.org/pipermail/libstdc++/2026-March/065843.html) implementing the proposed wording changes to `submdspan` in libstdc++.

-->
