Verdict: Weak (3/14)

The paper offers only a narrow foundation for its standardization case: it identifies a prior proposal and naming discussion, but leaves most of the burden—who is affected, why the standard is the right venue, how the feature would coordinate with existing library practice, and whether it has been implemented—essentially unaddressed. The thinnest support is around the practical and procedural justification for taking this work into the standard.

- The strongest support is the acknowledgment of prior art in P3091 and the recorded naming alternatives, which at least situates the proposal within an existing conversation.
- The paper asserts the feature’s importance by noting it would be the first failing, runtime-keyed `get()` in the library, but does not develop that observation into a demonstrated need.
- The most glaring omission is the absence of any implementation experience or evidence that a library-level solution is insufficient, leaving the case for standardization largely speculative.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 3.00   accumulate 2.50   max 3.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 34 of 35 section-criterion pairs unanimous (97%)
single-sample totals would have been: 2.50 / 2.50 / 2.50   (all 3 samples: 2.50)
headings: h3 4   <- NOT h2, check the unit list
on threshold: none
splits: prior_art[5] 0/1/0
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

## prior_art - grade 2.00 (fired in 4 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Discussion                                   2/2/2  -> 2.00
  [3] Proposal                                     1/1/1  -> 1.00
  [4] History                                      0/0/0  -> 0.00
  [5] Reference                                    0/1/0  -> 0.33
candidate 1 (found by 3 of 15 passes): P3091 proposed a member `get` for associative containers, a monadic analog of `op[]` and `at()`.
candidate 2 (found by 3 of 15 passes): The only alternative seriously considered at the time was `lookup`, which was rejected by weak consensus.
candidate 3 (found by 3 of 15 passes): Suggested names include `try_at(key)`, `lookup(key)`, and `try_lookup(key)`, but suggestions for other alternatives consistent with existing library usage are welcome.
candidate 4 (found by 1 of 15 passes): [1]: [P3091R3] Pablo Halpern - Better lookups for `map` and `unordered map` [https://wg21.link/p3091r3](https://wg21.link/p3091r3)

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
