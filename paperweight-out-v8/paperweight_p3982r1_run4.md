Verdict: Adequate to Strong (7/14)

The paper offers solid support for the core design rationale and for the existence of working implementation experience, but its broader case for standardization rests on several points that are asserted rather than demonstrated. The thinnest support concerns who is actually affected, why the standard is the right vehicle now, how the feature coordinates with the wider ecosystem, and why a library solution is insufficient.

- The strongest support is the implementation experience, with a patch series and benchmark details showing the proposal has been worked through in practice.
- The paper also clearly establishes the prior art and alternatives, explaining how the proposed slice type differs from existing canonical forms and aligns with other languages.
- The most glaring omission is the lack of established evidence for who is affected, since the paper leans on intuition and analogy rather than showing concrete user or codebase impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 7.33   max 9.33

## SUMMARY
grades: motivation 1.50  audience 0.67  prior_art 1.50  vehicle 0.33  coordination 0.67  insufficiency 0.17  implementation 2.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.00 / 7.50 / 6.50   (all 3 samples: 6.83)
headings: h2 8
on threshold: motivation, prior_art
splits: motivation[4] 0/0/2  audience[4] 1/2/1  prior_art[5] 1/0/0  vehicle[2] 1/0/0
        vehicle[5] 1/0/0  coordination[5] 1/2/1  insufficiency[4] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/2  -> 0.67
  [5] 4. Ship vehicle, proposed polls, and revi... 2/2/2  -> 2.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): it gives `submdspan` a more ergonomic and familiar interface.
candidate 2 (found by 2 of 27 passes): It incurs the cost of division, and it cannot be used for non-unique layouts.
candidate 3 (found by 1 of 27 passes): While this is an extension that can be added in a later standard, we prefer to include it in C++26, as it gives `submdspan` a more ergonomic and familiar interface.
candidate 4 (found by 1 of 27 passes): In most cases, this two meanings are functionally equivalent and they can be transformed into each other. However, due use of the division in the *input span* interpretation does not support the following:

## audience - grade 0.67 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/2/1  -> 1.33
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 2 (found by 1 of 27 passes): Results from a benchmark similar to one used above show no significant performance difference.
candidate 3 (found by 1 of 27 passes): Based on the inituition built from other languages, `submdspan(md, strided_slice{2, 5, 1})`, should select elements `[2, 5)`, instead of `[2, 7)` as currently specified.

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 1/0/0  -> 0.33
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Introduce a non-canonical `range_slice` slice type, that expresses the `(first, last, stride)` interface provided for range slicing in other programming languages.
candidate 2 (found by 3 of 27 passes): One argument for using the *input span* as the value of `stride_slice::extent` was consistency with other programming languages' range slicing interfaces. However, surveying the slicing interface in common languages shows that they all use `first, last` instead of `offset, length`.
candidate 3 (found by 1 of 27 passes): it makes `submdspan` more consistent with slicing facilities in other programming languages.

## vehicle - grade 0.33 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/0/0  -> 0.33
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 1/0/0  -> 0.33
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): While this is an extension that can be added in a later standard, we prefer to include it in C++26, as it gives `submdspan` a more ergonomic and familiar interface.
candidate 2 (found by 1 of 27 passes): Thus, it is important that the interface is both mininal (reducing the burden on layouts implementers) and able to represent a wide range of input without loss of information.

## coordination - grade 0.67 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/0/0  -> 0.00
  [5] 4. Ship vehicle, proposed polls, and revi... 1/2/1  -> 1.33
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/1/0  -> 0.33
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): As mentioned before, such a slice specification is not representable currently.

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle, proposed polls, and revi... 0/0/0  -> 0.00
  [6] 5. Impact and Implementability               2/2/2  -> 2.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): More details about above results may be found [here](https://gcc.gnu.org/pipermail/libstdc++/2026-January/065129.html).
candidate 2 (found by 3 of 27 passes): Here is a [patch series](https://gcc.gnu.org/pipermail/libstdc++/2026-March/065843.html) implementing the proposed wording changes to `submdspan` in libstdc++.

-->
