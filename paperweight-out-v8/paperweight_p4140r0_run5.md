Verdict: Weak (3/14)

The paper offers only a narrow slice of the case for standardization: it can point to a specific prior formulation and a concrete reason that formulation changed, but it does not connect the proposed allowance to any affected users, implementation experience, or a need that a library solution could not meet. The thinnest support is around the practical stakes, since the document never establishes who is harmed by the current wording or why the standard is the right place to fix it.

- The strongest support is the prior-art discussion, which credibly explains how the trait was previously defined and why that definition changed.
- The paper claims the allowance was inadvertently dropped, but it does not establish why that loss matters in practice.
- The paper does not identify any affected users or codebases, leaving the actual impact of the change unstated.
- The most glaring omission is the absence of any implementation experience or evidence that the proposed wording has been tried, tested, or needed outside the author’s reading of the specification.


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
