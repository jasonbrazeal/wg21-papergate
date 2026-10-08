Verdict: Adequate (4/14)

The paper offers some useful framing around the consequences of embedding attributes in types, but it does not build a complete case for standardization. The strongest material concerns the inherent limitations and compatibility surprises of the approach, while the thinnest areas are the absence of any argument for why standardization is needed, why a library cannot suffice, or what implementation experience exists.

- The paper establishes that embedding the attribute in a type creates real complexity and compatibility problems, and that the same capabilities are available without doing so.
- The discussion of affected users, prior art, and ABI coordination is asserted in general terms but not backed by concrete evidence or examples.
- The paper offers no argument for why the standard should adopt this rather than leaving it to implementations or libraries.
- There is no implementation experience presented to show that the proposed direction is viable in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 4.00   accumulate 4.67   max 5.00

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.17  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 0.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 4.00 / 3.50 / 3.50   (all 3 samples: 3.67)
headings: h2 8
on threshold: motivation
splits: motivation[2] 2/2/1  motivation[3] 1/1/2  prior_art[6] 1/1/2  coordination[3] 2/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/1  -> 1.67
  [3] Introduction                                 1/1/2  -> 1.33
  [4] Assume that an attribute cannot be part o... 1/1/1  -> 1.00
  [5] Error handling                               1/1/1  -> 1.00
  [6] Assume that an attribute can be part of a... 1/1/1  -> 1.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): There are also disadvantages, notably some code is more complex than if an attribute was part of the type to which it was applied.
candidate 2 (found by 3 of 27 passes): For compatibility, it seems clear that the answer must be “no”, but that implies some inconveniences (problem/surprises) when used.
candidate 3 (found by 3 of 27 passes): An alias containing an attribute doesn’t transmit the attribute to its users
candidate 4 (found by 3 of 27 passes): However, we don’t get anything we couldn’t achieve without embedding **[[uninit]]** in a type.

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 1/1/1  -> 1.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Since I expect the use of **[[uninit]]** and **[[ref_to_uninit]]** to be rather limited and specialized (compared to the immense amount of C++ code).

## prior_art - grade 1.17 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 1/1/2  -> 1.33
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper shows that we can manage either way, using **[[uninit]]** and **[[ref_to_uninit]]** from the initialization profile as examples.
candidate 2 (found by 2 of 27 passes): For compatibility, it seems clear that the answer must be “no”, but that implies some inconveniences (problem/surprises) when used.
candidate 3 (found by 2 of 27 passes): However, we don’t get anything we couldn’t achieve without embedding **[[uninit]]** in a type.
candidate 4 (found by 1 of 27 passes): current implementations diverge from that in their own attribute systems (e.g., Attributes in Clang — Clang 24.0.0git documentation)

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 0/0/0  -> 0.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 2/1/0  -> 1.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 0/0/0  -> 0.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): In either case, we must modify the ABIs to reflect the use of attributes on function arguments.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 0/0/0  -> 0.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 0/0/0  -> 0.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
