Verdict: Strong (8/14)

The paper offers a mixed case for its own standardization: it documents prior art and implementation experience clearly, but leaves several central justifications asserted rather than demonstrated. The thinnest support concerns why the change belongs in the standard at all, since the paper does not show that a library-level solution would be inadequate.

- The strongest support comes from concrete implementation experience, including a patch series and reported benchmark details.
- The paper also establishes coordination and interoperability concerns by explaining how the proposed slice types affect the interface between `submdspan` and custom layouts.
- The case for who is affected rests mainly on a passing benchmark claim without enough surrounding evidence to substantiate it.
- The most glaring omission is the absence of any argument for why a library cannot provide the proposed functionality, leaving the need for standardization itself unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.33   accumulate 8.17   max 10.33

## SUMMARY
grades: motivation 1.00  audience 1.00  prior_art 1.50  vehicle 0.50  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.00 / 7.50 / 7.50   (all 3 samples: 7.67)
headings: h2 8
on threshold: motivation, audience, prior_art
splits: vehicle[4] 0/0/1  vehicle[5] 1/1/0  coordination[4] 2/1/2  coordination[5] 2/2/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).
candidate 2 (found by 1 of 27 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).

## audience - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Results from a benchmark similar to one used above show no significant performance difference.

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    1/1/1  -> 1.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Note that such extension goes directly against the reasoning for the current design of `strided_slice` expressed in 2.1.1.2 Strided index range slice specifier of the [P2630R4: Submdspan](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2630r4.html), paper:
candidate 2 (found by 2 of 27 passes): Rename `strided_slice` to `extent_stride` and adjust the meaning of `extent` member, to designate the desired number of elements in the produced range.
candidate 3 (found by 1 of 27 passes): This paper proposes three changes: 1. Rename `strided_slice` to `extent_stride`... 2. Introduce a non-canonical `range_slice` slice type... 3. Expand slice canonicalization...
candidate 4 (found by 1 of 27 passes): This paper proposes three changes:

## vehicle - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/1  -> 0.33
  [5] 4. Ship vehicle and polls                    1/1/0  -> 0.67
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).
candidate 2 (found by 1 of 27 passes): In contrast, with this paper's proposed changes, the members of `strided_slice` directly represent values used by `submdspan` creation.

## coordination - grade 1.67 (fired in 2 of 9 sections, strong in 2)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/1/2  -> 1.67
  [5] 4. Ship vehicle and polls                    2/2/1  -> 1.67
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.
candidate 2 (found by 2 of 27 passes): To provide a interface consistent with existing practice in many languages, we propose extending the set of accepted slice types to include types that decompose into three values that are compatible with index type.
candidate 3 (found by 1 of 27 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
  [6] 5. Impact and Implementability               2/2/2  -> 2.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): More details about above results may be found [here](https://gcc.gnu.org/pipermail/libstdc++/2026-January/065129.html).
candidate 2 (found by 3 of 27 passes): Here is a [patch series](https://gcc.gnu.org/pipermail/libstdc++/2026-January/065127.html) implementing the proposed wording changes (except the rename) to `submdspan` in libstdc++.

-->
