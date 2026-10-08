Verdict: Weak (3/14)

The paper offers only a narrow slice of the case for standardization: it establishes why the problem matters for implementers of `std::execution`, but leaves nearly every other necessary justification unaddressed. The support is thinnest around the questions of who is affected, why a library cannot solve the problem, and whether there is any implementation experience.

- The paper’s strongest support is its explanation of why implementers need a standardized way to compute completion functions for asynchronous operation states.
- The discussion of prior art and alternatives is present but only claimed, not established, so it does not yet show that the proposed approach is the right one.
- The paper does not establish who is affected by the problem, leaving the scope and audience of the proposal unclear.
- The most glaring omission is the absence of any implementation experience, which leaves the feasibility of the wording and the design entirely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.00   accumulate 2.67   max 3.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 2.50 / 2.50   (all 3 samples: 2.67)
headings: h2 7
on threshold: motivation
splits: prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The receiver needs to know the location of the operation state to which asynchronous control flows upon completion of a child operation.
candidate 2 (found by 3 of 24 passes): The above has the effect that implementers of `std::execution` must write code which computes the completion functions potentially-evaluated by the algorithms they are implementing, but does not provide code which performs that computation.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 2 of 8 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/1/1  -> 1.33
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): The above is the primary finding of P3425.
candidate 2 (found by 2 of 24 passes): A similar strategy can be used to word P3425:
candidate 3 (found by 1 of 24 passes): This paper considers an alternate approach.
candidate 4 (found by 1 of 24 passes): The above-described strategy is proposed by this paper. Separate wording is presented for the “allow” and “require” cases. LEWG should poll between the two.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] Review History                               0/0/0  -> 0.00
  [7] Revision History                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
