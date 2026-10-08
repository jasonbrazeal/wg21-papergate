Verdict: Weak (1/14)

The paper offers almost no support for its own standardization, resting its case on a single passing reference to an in-review implementation. That leaves the motivation, affected users, prior art, need for a standard rather than a library, and coordination questions entirely unaddressed.

- The only substantive support is the claim of implementation experience in a libstdc++ patch currently under review.
- The paper does not explain why the feature matters or who would be affected by standardizing it.
- It gives no account of prior art, alternatives, or why a library solution would be insufficient.
- Most glaringly, it never articulates why the standard should take this on at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.00/14)

Provisionally addressed: 1 of 7. Provisional points: 1.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00

## SUMMARY
grades: motivation 0.00  audience 0.00  prior_art 0.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 35 of 35 section-criterion pairs unanimous (100%)
single-sample totals would have been: 1.00 / 1.00 / 1.00   (all 3 samples: 1.00)
headings: h2 4
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  0/0/0  -> 0.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  0/0/0  -> 0.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  0/0/0  -> 0.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  0/0/0  -> 0.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  0/0/0  -> 0.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  0/0/0  -> 0.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 IMPLEMENTATION EXPERIENCE                  1/1/1  -> 1.00
  [5] 3 WORDING                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This has been implemented and tested in the patch that’s currently in review for libstdc++.

-->
