Verdict: Adequate to Strong (7/14)

The paper offers a mixed but uneven case for its own standardization, with the strongest support coming from its explanation of the problem and its survey of existing practice, while the arguments about affected users, the need for a standard interface, and interoperability remain asserted rather than demonstrated. The thinnest part is the absence of any discussion of why a library solution would be insufficient, which leaves a central justification for standardization unaddressed.

- The paper clearly establishes why the current `strided_slice` design is problematic and shows that common slicing interfaces elsewhere use `first, last` rather than `offset, length`.
- It also provides concrete implementation experience through a patch series and benchmark details, lending credibility to the feasibility of the proposed change.
- The claims about who is affected and why the standard itself must change are stated but not backed by evidence connecting the problem to real user impact or to a need that a library cannot meet.
- The most glaring omission is the complete lack of an argument for why a library will not do, which is essential for justifying standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 6.33   accumulate 7.83   max 10.00

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.67  vehicle 0.17  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.00 / 7.50 / 8.00   (all 3 samples: 7.17)
headings: h2 4
on threshold: motivation, audience, prior_art, coordination
splits: motivation[4] 0/2/0  prior_art[5] 2/0/2  vehicle[5] 0/0/1  coordination[5] 1/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/2/0  -> 0.67
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): This change preserve more ergonomic and familiar interface for `submdspan`.
candidate 2 (found by 3 of 15 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).
candidate 3 (found by 1 of 15 passes): In most cases, this two meanings are functionally equivalent and they can be transformed into each other. However, due use of the division in the *input span* interpretation does not support the following:

## audience - grade 1.00 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Results from a benchmark similar to one used above show no significant performance difference.

## prior_art - grade 1.67 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    2/0/2  -> 1.33
candidate 1 (found by 2 of 15 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 2 (found by 2 of 15 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard. However, in contrast to amending `strided_slice`, this would essentially duplicate the number of types that layouts would need to handle
candidate 3 (found by 1 of 15 passes): This change would be breaking after C++26 is shipped.
candidate 4 (found by 1 of 15 passes): Introduce a non-canonical `range_slice` slice type, that expresses the `(first, last, stride)` interface provided for range slicing in other programming languages.

## vehicle - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    0/0/1  -> 0.33
candidate 1 (found by 1 of 15 passes): Thus, it is important that the interface is both mininal (reducing the burden on layouts implementers) and able to represent a wide range of input without loss of information.

## coordination - grade 0.83 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    1/2/2  -> 1.67
candidate 1 (found by 3 of 15 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.

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
