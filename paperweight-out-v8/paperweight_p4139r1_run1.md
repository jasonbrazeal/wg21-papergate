Verdict: Weak (3/14)

The paper offers only a narrow foundation for its standardization case: it documents some naming history and prior discussion, but leaves most of the burden of justification unaddressed. The thinnest areas are the absence of any account of who would be affected, why a library solution would not suffice, or what implementation experience exists.

- The strongest support is the record of prior art and naming alternatives, including the rejected `lookup` and the earlier P3091 options.
- The paper asserts that a runtime-variable, possibly failing `get()` would be useful, but does not establish why that utility rises to a standardization need.
- It gives no evidence about affected users, implementation experience, or coordination with existing practice.
- Most notably, it never explains why this cannot be done as an ordinary library facility rather than a standard library addition.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 3.00   accumulate 2.50   max 3.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 35 of 35 section-criterion pairs unanimous (100%)
single-sample totals would have been: 2.50 / 2.50 / 2.50   (all 3 samples: 2.50)
headings: h3 4   <- NOT h2, check the unit list
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail, and that takes a runtime-variable key.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Discussion                                   2/2/2  -> 2.00
  [3] Proposal                                     1/1/1  -> 1.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): P3091 proposed a member `get` for associative containers, a monadic analog of `op[]` and `at()`.
candidate 2 (found by 3 of 15 passes): Suggested names include `try_at(key)`, `lookup(key)`, and `try_lookup(key)`, but suggestions for other alternatives consistent with existing library usage are welcome.
candidate 3 (found by 2 of 15 passes): The only alternative seriously considered at the time was `lookup`, which was rejected by weak consensus.
candidate 4 (found by 1 of 15 passes): P3091 offered `get_optional`, `lookup`, and `lookup_optional`, which failed to evoke enthusiasm.

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
