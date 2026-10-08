Verdict: Weak (2/14)

The paper offers a narrow but real justification for removing the restriction on zero-argument `when_all`, grounded in a concrete failure mode and a generic-programming concern, but it leaves most of the standardization case unaddressed. The support is thinnest around who would actually benefit, why a library-level solution is insufficient, and whether any implementation experience exists.

- The strongest support is the established claim that the current ban creates an unnecessary special case in generic algorithms and that lifting it avoids a hanging asynchronous operation.
- The paper gestures at prior art by citing the current standard’s fiat ban and the vacuous-truth analogy to `std::all_of`, but it does not establish that these amount to meaningful prior art or alternatives.
- The paper never identifies the affected users or codebases, so the practical reach of the change remains unclear.
- The most glaring omission is the absence of any implementation experience, coordination with related proposals, or argument for why this requires a standard change rather than a library workaround.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.00   accumulate 2.33   max 3.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 0.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 2.00 / 2.50   (all 3 samples: 2.33)
headings: h2 5
on threshold: motivation
splits: prior_art[3] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): If this restriction were not present the asynchronous operation which results from connecting the result of `std::execution::when_all()` and starting the operation state yielded thereby would hang
candidate 2 (found by 3 of 18 passes): Banning `std::execution::when_all()` (i.e. the status quo) unnecessarily creates a special case when writing generic algorithms.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.83 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/0/1  -> 0.67
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The standard currently specifies, by fiat, that `std::execution::when_all()` is ill-formed (§33.9.12.12 [exec.when.all])
candidate 2 (found by 1 of 18 passes): Given zero senders “all input senders” have always trivially completed (in the same way that `std::all_of` returns `true` for empty input)
candidate 3 (found by 1 of 18 passes): Given zero senders “all input senders” have always trivially completed (in the same way that `std::all_of` returns `true` for empty input) and therefore there’s no reason to ban `std::execution::when_all()`, it is simply equivalent to `std::execution::just()`.
candidate 4 (found by 1 of 18 passes): it is simply equivalent to `std::execution::just()`.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

-->
