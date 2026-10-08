Verdict: Weak (3/14)

The paper offers only a thin basis for its own standardization, with most of the necessary case left either unstated or merely asserted. The strongest material appears in the discussion of prior work and implementation intent, but even those points are presented as claims rather than demonstrated support, and the document is largely silent on who would be affected, why the standard is the right venue, and how the feature would coordinate with existing specifications.

- The paper’s clearest support is its acknowledgment of similarity to P2746 and its stated intent to provide an implementation, though both remain claims rather than established evidence.
- The rationale for why the change matters is asserted through brief remarks about complexity and rounding behavior, but the underlying need is not developed.
- The document does not establish who is affected by the proposal or what practical problem it solves for users.
- The most glaring omission is the absence of any case for why a library solution would not suffice or why standardization is necessary at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 2. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 2.67   accumulate 2.50   max 4.00

## SUMMARY
grades: motivation 0.67  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 11 of 14 section-criterion pairs unanimous (79%)
single-sample totals would have been: 2.00 / 2.50 / 3.00   (all 3 samples: 2.50)
headings: h2 1
on threshold: prior_art
splits: motivation[1] 1/1/2  prior_art[2] 1/0/0  implementation[1] 0/1/1
## END SUMMARY

## motivation - grade 0.67 (fired in 1 of 2 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/2  -> 1.33
  [2] Questions                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 6 passes): It is not completely clear to us whether this requires round-to-nearest except in the equidistant case, or allows more implementation freedom.
candidate 2 (found by 1 of 6 passes): But the reasoning behind that simplification is unpleasantly complex

## audience - grade 0.00 (fired in 0 of 2 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Questions                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 2 of 2 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Questions                                    1/0/0  -> 0.33
candidate 1 (found by 3 of 6 passes): This is basically identical to P2746, except that we constrain operations to be IEEE conformant whenever is_iec_559 is `true`.
candidate 2 (found by 1 of 6 passes): The rounding-mode-encapsulated-by-struct-of-templates was agreed upon in the context of explicitly specified rounding modes, which is accepted to be a niche use.

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

## implementation - grade 0.67  [binary: max] (fired in 1 of 2 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] Questions                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 6 passes): We hope to soon provide an “existence-proof” implementation that supports runtime evaluation with fully usable and deterministic semantics, but provides only a low-quality non-IEEE implementation for compile time evaluation.

-->
