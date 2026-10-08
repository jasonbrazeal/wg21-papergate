Verdict: Adequate (4/14)

The paper offers only a narrow, fragmentary basis for its own standardization, with most of the necessary case left unaddressed. The strongest material concerns prior art and implementation intent, but even those are asserted rather than demonstrated, and the document is largely silent on who would be affected, why the standard is the right venue, and how the feature would interoperate with existing practice.

- The clearest support is the acknowledgment of a closely related prior proposal and a hoped-for implementation, though neither is yet substantiated.
- The discussion of why the feature matters gestures at real rounding questions but does not connect them to a demonstrated need for standardization.
- The paper does not establish who is affected by the problem or what practical code would gain from the proposed change.
- The most glaring omission is the absence of any argument for why a library solution would be insufficient or why standardization is necessary at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 2. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.00   accumulate 3.67   max 5.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 12 of 14 section-criterion pairs unanimous (86%)
single-sample totals would have been: 4.00 / 3.50 / 3.50   (all 3 samples: 3.67)
headings: h2 1
on threshold: motivation, prior_art
splits: motivation[2] 1/0/1  prior_art[2] 1/1/0
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 2 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Questions                                    1/0/1  -> 0.67
candidate 1 (found by 2 of 6 passes): It is not completely clear to us whether this requires round-to-nearest except in the equidistant case, or allows more implementation freedom.
candidate 2 (found by 2 of 6 passes): What is the current requirement on literal rounding?
candidate 3 (found by 1 of 6 passes): To compute an upper bound on the true result of -0.1 - (x + y) we may write:

## audience - grade 0.00 (fired in 0 of 2 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Questions                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 2 of 2 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Questions                                    1/1/0  -> 0.67
candidate 1 (found by 3 of 6 passes): This is basically identical to P2746, except that we constrain operations to be IEEE conformant whenever is_iec_559 is `true`.
candidate 2 (found by 2 of 6 passes): The rounding-mode-encapsulated-by-struct-of-templates was agreed upon in the context of explicitly specified rounding modes, which is accepted to be a niche use.

## vehicle - grade 0.00 (fired in 0 of 2 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Questions                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 2 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Questions                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 2 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Questions                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 2 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Questions                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 6 passes): We hope to soon provide an “existence-proof” implementation that supports runtime evaluation with fully usable and deterministic semantics, but provides only a low-quality non-IEEE implementation for compile time evaluation.

-->
