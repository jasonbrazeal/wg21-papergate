Verdict: Adequate (4/14)

The paper offers some useful framing around the design questions and tradeoffs, but it does not build a complete case for standardization. The strongest material concerns prior art and the recognition that current practice already diverges, while the thinnest areas are the absence of a standards-based rationale, implementation experience, and any explanation of why a library solution would be insufficient.

- The paper establishes that the relevant design choices are real and that existing implementations already diverge in how attributes behave.
- It acknowledges the affected population only in passing, describing the expected use as limited and specialized without substantiating who would actually depend on standardization.
- It claims ABI coordination would be necessary but does not show how standardization would resolve that coordination or interoperate with existing practice.
- It offers no implementation experience and no argument for why the standard, rather than a library or existing vendor attribute system, is the right vehicle.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 4 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 3.67   accumulate 4.83   max 5.33

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.67  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 0.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 8
on threshold: motivation, prior_art
splits: motivation[2] 1/2/2  motivation[4] 2/1/1  motivation[5] 0/1/0  prior_art[6] 1/1/2
        coordination[3] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/2/2  -> 1.67
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Assume that an attribute cannot be part o... 2/1/1  -> 1.33
  [5] Error handling                               0/1/0  -> 0.33
  [6] Assume that an attribute can be part of a... 1/1/1  -> 1.00
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): There are also disadvantages, notably some code is more complex than if an attribute was part of the type to which it was applied.
candidate 2 (found by 3 of 27 passes): For compatibility, it seems clear that the answer must be “no”, but that implies some inconveniences (problem/surprises) when used.
candidate 3 (found by 2 of 27 passes): An alias containing an attribute doesn’t transmit the attribute to its users
candidate 4 (found by 2 of 27 passes): Since I expect the use of **[[uninit]]** and **[[ref_to_uninit]]** to be rather limited and specialized (compared to the immense amount of C++ code).

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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

## prior_art - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Assume that an attribute cannot be part o... 0/0/0  -> 0.00
  [5] Error handling                               0/0/0  -> 0.00
  [6] Assume that an attribute can be part of a... 1/1/2  -> 1.33
  [7] WP wording                                   0/0/0  -> 0.00
  [8] Acknowledgement                              0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper shows that we can manage either way, using **[[uninit]]** and **[[ref_to_uninit]]** from the initialization profile as examples.
candidate 2 (found by 2 of 27 passes): However, we don’t get anything we couldn’t achieve without embedding **[[uninit]]** in a type.
candidate 3 (found by 1 of 27 passes): current implementations diverge from that in their own attribute systems (e.g., Attributes in Clang — Clang 24.0.0git documentation)
candidate 4 (found by 1 of 27 passes): That seems to be a clear “no” but current implementations diverge from that in their own attribute systems (e.g., Attributes in Clang — Clang 24.0.0git documentation).

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

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/0  -> 0.67
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
