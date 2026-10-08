Verdict: Strong (8/14)

The paper offers meaningful support in a few areas, particularly in explaining the motivation, surveying prior art, and showing implementation experience, but it leaves several important parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why a library solution would be insufficient, and the claims about affected users and the need for a standard interface are not backed by evidence.

- The strongest support comes from the discussion of prior art and alternatives, which credibly shows why the current design is problematic and why other approaches would be costly or inconsistent.
- Implementation experience is also well supported, with links to a patch series and benchmark details indicating the change has been tried in practice.
- The paper claims the change matters for affected users and that standardization is necessary for a minimal, interoperable interface, but it does not establish who is concretely affected or why a library-only approach cannot suffice.
- The most glaring omission is the absence of any established argument for why this cannot be done as a library, leaving a central part of the standardization rationale unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 6.33   accumulate 8.00   max 10.33

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.50  vehicle 0.17  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 7.50   (all 3 samples: 7.50)
headings: h2 4
on threshold: motivation, audience, prior_art, coordination
splits: vehicle[5] 0/1/0  coordination[4] 1/0/1
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

## prior_art - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    1/1/1  -> 1.00
candidate 1 (found by 2 of 15 passes): This change would be breaking after C++26 is shipped.
candidate 2 (found by 2 of 15 passes): One argument for using the *input span* as the value of `stride_slice::extent` was consistency with other programming languages' range slicing interface. However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 3 (found by 2 of 15 passes): We could imagine introducing a separate `canonical_strided_slice` type in a later standard. However, in contrast to amending `strided_slice`, this would essentially duplicate the number of types that layouts would need to handle
candidate 4 (found by 1 of 15 passes): Introduce a non-canonical `range_slice` slice type, that expresses the `(first, last, stride)` interface provided for range slicing in other programming languages.

## vehicle - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle and polls                    0/1/0  -> 0.33
candidate 1 (found by 1 of 15 passes): Thus, it is important that the interface is both mininal (reducing the burden on layouts implementers) and able to represent a wide range of input without loss of information.

## coordination - grade 1.33 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/0/1  -> 0.67
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
candidate 1 (found by 3 of 15 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.
candidate 2 (found by 2 of 15 passes): To provide a interface consistent with existing practice in many languages, we propose to introduce a new vocabulary type for "range" slice

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
