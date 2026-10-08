Verdict: Weak (3/14)

The paper offers some useful context around naming and prior discussion, but it does not yet build a case that this facility belongs in the standard. The strongest material concerns the history of the idea and the alternatives already considered, while the argument for standardization itself is largely absent.

- The paper establishes that a similar proposal was previously considered and that naming alternatives have been discussed, which grounds the design conversation in real committee history.
- The paper gestures at why the facility might be useful, but it does not establish who would be affected or what problem would go unsolved without standardization.
- The paper does not explain why the standard is the right venue, why a library implementation would be insufficient, or whether any implementation experience exists to validate the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 3.00   accumulate 3.00   max 3.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 3.00 / 2.50 / 3.00   (all 3 samples: 2.83)
headings: h3 4   <- NOT h2, check the unit list
on threshold: none
splits: motivation[1] 1/1/2  motivation[2] 1/0/1  prior_art[1] 2/2/1
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/2  -> 1.33
  [2] Discussion                                   1/0/1  -> 0.67
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail, and that takes a runtime-variable key.
candidate 2 (found by 2 of 15 passes): The library has accumulated an assortment of `try_xxxxx` members that share the feature of reporting failure, but return a variety of result types

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.83 (fired in 3 of 5 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/1  -> 1.67
  [2] Discussion                                   2/2/2  -> 2.00
  [3] Proposal                                     1/1/1  -> 1.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): P3091 proposed a member `get` for associative containers, a monadic analog of `op[]` and `at()`.
candidate 2 (found by 3 of 15 passes): The only alternative seriously considered at the time was `lookup`, which was rejected by weak consensus.
candidate 3 (found by 3 of 15 passes): Suggested names include `try_at(key)`, `lookup(key)`, and `try_lookup(key)`, but suggestions for other alternatives consistent with existing library usage are welcome.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

-->
