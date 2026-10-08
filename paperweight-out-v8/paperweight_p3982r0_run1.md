Verdict: Strong (8/14)

The paper offers solid grounding for its motivation, prior art, and implementation experience, but it leaves several essential parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why a library solution is insufficient, and the claims about affected users, the need for a standard interface, and coordination with existing practice are more asserted than shown.

- The strongest support comes from the concrete implementation patch series and benchmark details, which give the proposal real implementation experience.
- The paper also clearly establishes why the current behavior is problematic and how the proposed change relates to prior design discussions and alternatives.
- The case for who is affected rests mainly on a performance claim without enough surrounding evidence to establish the broader impact.
- The most glaring omission is the absence of any established argument for why this cannot be handled by a library rather than a standard change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 7.00   accumulate 9.17   max 11.00

## SUMMARY
grades: motivation 1.67  audience 1.00  prior_art 1.50  vehicle 1.00  coordination 1.17  insufficiency 0.00  implementation 2.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.00 / 8.00 / 9.00   (all 3 samples: 8.33)
headings: h2 8
on threshold: motivation, audience, prior_art, coordination
splits: motivation[2] 0/1/1  motivation[4] 0/2/2  prior_art[6] 1/1/0  vehicle[4] 1/0/1
        vehicle[5] 1/1/2  coordination[4] 2/0/0  coordination[5] 1/2/2
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/1/1  -> 0.67
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      0/2/2  -> 1.33
  [5] 4. Ship vehicle and polls                    2/2/2  -> 2.00
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This shows that even for programmers familar with the topic, such computations remain bug-prone.
candidate 2 (found by 2 of 27 passes): This change would be breaking after C++26 is shipped.
candidate 3 (found by 2 of 27 passes): In most cases, this two meanings are functionally equivalent and they can be transformed into each other. However, due use of the division in the *input span* interpretation does not support the following:

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

## prior_art - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/2/2  -> 2.00
  [5] 4. Ship vehicle and polls                    1/1/1  -> 1.00
  [6] 5. Impact and Implementability               1/1/0  -> 0.67
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Note that such extension goes directly against the reasoning for the current design of `strided_slice` expressed in 2.1.1.2 Strided index range slice specifier of the [P2630R4: Submdspan](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2630r4.html), paper:
candidate 2 (found by 3 of 27 passes): Rename `strided_slice` to `extent_stride` and adjust the meaning of `extent` member, to designate the desired number of elements in the produced range.
candidate 3 (found by 2 of 27 passes): This paper proposes three changes:
candidate 4 (found by 2 of 27 passes): This paper only impacts the behavior of the `std::submdspan` library function that was introduced in C++26.

## vehicle - grade 1.00 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      1/0/1  -> 0.67
  [5] 4. Ship vehicle and polls                    1/1/2  -> 1.33
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Thus, it is important that the interface is both mininal (reducing the burden on layouts implementers) and able to represent a wide range of input without loss of information.
candidate 2 (found by 2 of 27 passes): In contrast, with this paper's proposed changes, the members of `strided_slice` directly represent values used by `submdspan` creation.

## coordination - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Revision history                          0/0/0  -> 0.00
  [4] 3. Motivation and Scope                      2/0/0  -> 0.67
  [5] 4. Ship vehicle and polls                    1/2/2  -> 1.67
  [6] 5. Impact and Implementability               0/0/0  -> 0.00
  [7] 6. Proposed Wording                          0/0/0  -> 0.00
  [8] 7. Acknowledgements                          0/0/0  -> 0.00
  [9] 8. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `strided_slice` is one of the canonical slice types that define the interface between `submdspan` (and potentially other components providing such facility) and custom layouts.
candidate 2 (found by 1 of 27 passes): Based on the inituition built from other languages, `submdspan(md, strided_slice{2, 5, 1})`, should select elements `[2, 5)`, instead of `[2, 7)` as currently specified.

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
