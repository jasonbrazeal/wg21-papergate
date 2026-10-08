Verdict: Weak (3/14)

The paper offers only a narrow slice of the case needed for standardization: it establishes the historical context and prior art, but leaves most of the rationale for standardizing this change unstated. The support is thinnest around who is affected, why the standard is the right venue, and whether the change has been tried in practice.

- The strongest support is the prior-art discussion, which credibly explains how the trait was previously defined and why that definition changed.
- The paper claims the change matters because an explicit allowance was inadvertently dropped, but it does not show why restoring that allowance is important to users.
- The paper does not establish who is affected by the missing allowance or what practical problems it causes.
- The most glaring omission is the absence of implementation experience, coordination considerations, or any argument that a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 1. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 3.00   accumulate 3.00   max 3.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 7 of 7 section-criterion pairs unanimous (100%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: none found   <- NOT h2, check the unit list
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 1 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
candidate 1 (found by 3 of 3 passes): During that change, the explicit allowance for `type_order<X, Y>` being defined for incomplete `X` or `Y` got inadvertently dropped, so this paper re-introduces that allowance.

## audience - grade 0.00 (fired in 0 of 1 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 1 of 1 sections, strong in 1)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
candidate 1 (found by 3 of 3 passes): It used to be defined in terms of Cpp17BinaryTypeTrait, but changed this in P3778R0 due to std::strong_ordering not being a structural type.

## vehicle - grade 0.00 (fired in 0 of 1 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 1 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 1 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 1 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

-->
