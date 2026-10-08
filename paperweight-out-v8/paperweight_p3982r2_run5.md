Verdict: Adequate to Strong (8/14)

The paper offers solid grounding for its central design change, particularly through its discussion of alternatives and its implementation experience, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why a library-only solution would be insufficient, which is not addressed at all.

- The strongest support comes from the concrete implementation work and the clear comparison with alternative designs, showing the proposal is more than speculative.
- The paper also establishes why the current `strided_slice` behavior matters by tying it to ergonomic and performance problems in `submdspan`.
- The claims about who is affected and why the standard is the right venue rest on assertions and survey references without enough evidence to move beyond plausible but unproven.
- The most glaring omission is the absence of any argument for why a library cannot provide the proposed functionality, leaving a core requirement of the standardization case unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.00   accumulate 8.00   max 10.67

## SUMMARY
grades: motivation 1.50  audience 0.83  prior_art 1.50  vehicle 0.50  coordination 1.17  insufficiency 0.00  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.50 / 8.00   (all 3 samples: 7.50)
headings: h2 4
on threshold: motivation, audience, prior_art, coordination
splits: audience[4] 1/2/2  coordination[4] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): This change preserve more ergonomic and familiar interface for `submdspan`.
candidate 2 (found by 3 of 15 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).

## audience - grade 0.83 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/2/2  -> 1.67
  [5] 4. Ship vehicle and polls                    0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): Results from a benchmark similar to one used above show no significant performance difference.
candidate 2 (found by 1 of 15 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.

## prior_art - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): This paper proposes two changes: 1. Rename `strided_slice` to `extent_slice` and adjust the meaning of its `extent` member, to designate the desired number of elements in the range produced by `submdspan`.
candidate 2 (found by 3 of 15 passes): One argument for using the *input span* as the value of `stride_slice::extent` was consistency with other programming languages' range slicing interface. However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 3 (found by 2 of 15 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard. However, in contrast to amending `strided_slice`, this would essentially duplicate the number of types that layouts would need to handle
candidate 4 (found by 1 of 15 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard.

## vehicle - grade 0.50 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): As this document explains, the current specification of `strided_slice` fails in both accounts (it incurs cost of division, and cannot be used for non-unique layouts).

## coordination - grade 1.17 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/1  -> 0.33
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.
candidate 2 (found by 1 of 15 passes): To provide a interface consistent with existing practice in many languages, we propose to introduce a new vocabulary type for "range" slice:

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
