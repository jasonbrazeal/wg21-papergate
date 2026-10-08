Verdict: Adequate (7/14)

The paper offers a mixed but incomplete case for standardization: it grounds the motivation and prior-art discussion well, and it shows some implementation work, but it leaves several essential questions about standards scope and library viability largely unanswered. The thinnest support is around why this change belongs in the standard rather than in a library, and the affected-audience and interoperability claims remain asserted rather than demonstrated.

- The strongest support is the established motivation, which clearly ties the proposed change to ergonomic and performance problems in the current `strided_slice` specification.
- The prior-art and alternatives discussion is also well established, showing how other languages’ slicing interfaces and the existing `submdspan` design point toward the proposed `range_slice` approach.
- The implementation experience is established through linked benchmark details and a patch series, indicating the change has been explored in practice.
- The most glaring omission is the absence of any established argument for why the standard is the right venue, compounded by an unestablished case that a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 7.00   max 9.00

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.83  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.00 / 6.50   (all 3 samples: 6.83)
headings: h2 4
on threshold: motivation, audience
splits: prior_art[5] 1/2/2  coordination[5] 2/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): This change preserve more ergonomic and familiar interface for `submdspan`.
candidate 2 (found by 3 of 15 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).

## audience - grade 1.00 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Results from a benchmark similar to one used above show no significant performance difference.

## prior_art - grade 1.83 (fired in 3 of 5 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    1/2/2  -> 1.67
candidate 1 (found by 3 of 15 passes): Introduce a non-canonical `range_slice` slice type, that expresses the `(first, last, stride)` interface provided for range slicing in other programming languages.
candidate 2 (found by 3 of 15 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard. However, in contrast to amending `strided_slice`, this would essentially duplicate the number of types that layouts would need to handle
candidate 3 (found by 2 of 15 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 4 (found by 1 of 15 passes): Based on the inituition built from other languages, `submdspan(md, strided_slice{2, 5, 1})`, should select elements `[2, 5)`, instead of `[2, 7)` as currently specified.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    2/1/0  -> 1.00
candidate 1 (found by 2 of 15 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.

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
