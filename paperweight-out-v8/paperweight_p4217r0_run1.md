Verdict: Weak (2/14)

The paper offers only a narrow, largely asserted rationale for changing the status quo, and it leaves most of the case for standardization unaddressed. The support is thinnest around the practical need for a standard change rather than a library-level workaround, and around evidence that anyone has encountered or would benefit from this change.

- The strongest support is the paper’s observation that the current ill-formedness creates a special case in generic code, though even this is asserted rather than demonstrated.
- The paper gestures at prior art by comparing the empty case to `std::all_of` and `std::execution::just()`, but it does not establish that these analogies reflect existing practice or committee intent.
- The paper does not identify who is affected by the current restriction or provide implementation experience with the proposed change.
- The most glaring omission is the absence of any argument for why this cannot be handled by a library facility outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.83/14)

Provisionally addressed: 2 of 7. Provisional points: 1.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 0.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 2.00 / 1.50 / 2.00   (all 3 samples: 1.83)
headings: h2 5
on threshold: none
splits: motivation[3] 0/0/2  motivation[4] 2/1/1  prior_art[3] 1/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/2  -> 0.67
  [4] Discussion                                   2/1/1  -> 1.33
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

## prior_art - grade 0.83 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/0  -> 0.67
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The standard currently specifies, by fiat, that `std::execution::when_all()` is ill-formed (§33.9.12.12 [exec.when.all])
candidate 2 (found by 2 of 18 passes): it is simply equivalent to `std::execution::just()`.
candidate 3 (found by 1 of 18 passes): Given zero senders “all input senders” have always trivially completed (in the same way that `std::all_of` returns `true` for empty input)

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
