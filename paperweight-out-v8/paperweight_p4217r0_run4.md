Verdict: Weak (2/14)

The paper offers only a narrow, informal argument that the current restriction on `std::execution::when_all()` is a special case worth removing, but it does not develop the broader case for standardization. The support is thinnest around the practical and procedural questions: who would be affected, what alternatives exist beyond the status quo, why a library solution is insufficient, and whether anyone has implemented or used the proposed behavior.

- The strongest support is the observation that the current standard bans `when_all()` by fiat and that treating zero senders as trivially complete would align with conventions like `std::all_of`.
- The paper gestures at a generic-programming motivation by saying the ban creates an unnecessary special case, but it does not show concrete code or user impact.
- The discussion of prior art and alternatives amounts to asserting equivalence with `std::execution::just()` without examining other possible designs or precedents.
- The most glaring omission is the complete absence of evidence about affected users, implementation experience, or why the change belongs in the standard rather than in a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.17/14)

Provisionally addressed: 2 of 7. Provisional points: 2.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.17   corroborated 2.00   accumulate 2.17   max 2.67

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 2.00 / 1.50 / 3.00   (all 3 samples: 2.17)
headings: h2 5
on threshold: motivation
splits: motivation[3] 0/0/2  motivation[4] 2/1/2
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/2  -> 0.67
  [4] Discussion                                   2/1/2  -> 1.67
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Banning `std::execution::when_all()` (i.e. the status quo) unnecessarily creates a special case when writing generic algorithms.
candidate 2 (found by 1 of 18 passes): If this restriction were not present the asynchronous operation which results from connecting the result of `std::execution::when_all()` and starting the operation state yielded thereby would hang

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

## prior_art - grade 1.00 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The standard currently specifies, by fiat, that `std::execution::when_all()` is ill-formed (§33.9.12.12 [exec.when.all])
candidate 2 (found by 2 of 18 passes): it is simply equivalent to `std::execution::just()`.
candidate 3 (found by 1 of 18 passes): Given zero senders “all input senders” have always trivially completed (in the same way that `std::all_of` returns `true` for empty input) and therefore there’s no reason to ban `std::execution::when_all()`, it is simply equivalent to `std::execution::just()`.

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
