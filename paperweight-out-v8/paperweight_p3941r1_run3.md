Verdict: Adequate (4/14)

The paper offers some support for its standardization case by explaining why the change matters and by situating it against prior discussion and alternatives, but it leaves most of the burden unaddressed. The thinnest areas are the absence of any identified affected audience, any argument for why this belongs in the standard rather than a library, and any evidence of implementation experience.

- The paper most clearly establishes why the change matters by connecting it to concerns raised during discussion of `affine_on` and framing it as removal of a problematic approach.
- It also establishes some grounding in prior art and alternatives by referencing P3796R1 and the earlier `task` design using `continues_on`.
- The paper does not establish who is affected by the proposed change, leaving the practical reach and constituency unclear.
- Most glaringly, it never explains why the standard is the right venue or why a library solution would not suffice, and it offers no implementation experience to support the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 35 of 35 section-criterion pairs unanimous (100%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h2 4
on threshold: motivation
splits: none
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/1  -> 1.00
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 2 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified.
candidate 3 (found by 2 of 15 passes): It isn’t adding any new functionality but removes a problematic way to achieve something which can be better achieved differently.
candidate 4 (found by 1 of 15 passes): The discussion on `affine_on` revealed some aspects which were not quite clear previously and taking these into account points towards a better design than was previously specified:

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Discussion of Changes                      2/2/2  -> 2.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There were multiple concerns raised against the specification of `affine_on` and discussed as part of [P3796R1](https://wg21.link/P3796R1).
candidate 2 (found by 3 of 15 passes): with this guarantee in place, `affine_on` only needs one parameter, i.e., the sender for the work to be executed.
candidate 3 (found by 3 of 15 passes): The original proposal for `task` used `continues_on` to schedule the work back on the original scheduler.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Discussion of Changes                      0/0/0  -> 0.00
  [5] 4 Wording Changes                            0/0/0  -> 0.00
candidates: (none validated)

-->
