Verdict: Weak to Adequate (3/14)

The paper offers only a narrow slice of the case for standardization: it gestures at a real ambiguity in how literal rounding is specified, but leaves nearly every other question about affected users, the need for a standard facility, and practical viability unanswered. The support is thinnest where it matters most—there is no demonstration that this cannot be handled outside the standard, no account of who is burdened by the status quo, and no evidence that the proposed direction is implementable in practice.

- The strongest support is the identification of genuine uncertainty in the current wording around literal rounding and round-to-nearest behavior.
- The paper claims continuity with P2746 and prior discussion of rounding-mode encapsulation, but does not establish that those alternatives were insufficient or that this approach is the right one.
- The paper offers no evidence of implementation experience beyond a hope for a future existence proof with deliberately weak compile-time semantics.
- The most glaring omission is the absence of any argument for why a library solution would not suffice, leaving the central standardization question effectively unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 2. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 2.67   accumulate 3.33   max 4.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 12 of 14 section-criterion pairs unanimous (86%)
single-sample totals would have been: 4.00 / 2.50 / 3.50   (all 3 samples: 3.33)
headings: h2 1
on threshold: motivation, prior_art
splits: prior_art[2] 1/0/0  implementation[1] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 2 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Questions                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 6 passes): What is the current requirement on literal rounding?
candidate 2 (found by 1 of 6 passes): To compute an upper bound on the true result of -0.1 - (x + y) we may write:
candidate 3 (found by 1 of 6 passes): Depending on the reading of the current standard, this might be optional, and can perhaps be abbreviated as simply ... But the reasoning behind that simplification is unpleasantly complex
candidate 4 (found by 1 of 6 passes): It is not completely clear to us whether this requires round-to-nearest except in the equidistant case, or allows more implementation freedom.

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
  [1] (front matter: title, abstract and anythi... 1/0/1  -> 0.67
  [2] Questions                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 6 passes): We hope to soon provide an “existence-proof” implementation that supports runtime evaluation with fully usable and deterministic semantics, but provides only a low-quality non-IEEE implementation for compile time evaluation.

-->
