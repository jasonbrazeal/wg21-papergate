Verdict: Weak (2/14)

The paper offers only a thin basis for its own standardization, mostly gesturing at a naming problem and a prior discussion without developing the surrounding case. The support is thinnest where a proposal normally needs concrete evidence: there is no argument for why this belongs in the standard, no interoperability analysis, no reason a library solution would be insufficient, and no implementation experience.

- The strongest support is the acknowledgment that P3091 already introduced a `get` that can fail, giving the naming question a real context in the existing library.
- The paper identifies affected users only in passing, by noting the obvious utility of the operation rather than explaining who needs the change or how they are served.
- The discussion of prior art and alternatives is largely a recap of P3091’s rejected `lookup` option, without establishing why the new name or any alternative would be the right standardization choice.
- The most glaring omission is the complete absence of a case for why the standard should act at all, including why a library cannot address the concern and what implementation experience supports the proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.33   accumulate 2.83   max 3.00

## SUMMARY
grades: motivation 0.83  audience 0.17  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 25 of 28 section-criterion pairs unanimous (89%)
single-sample totals would have been: 2.50 / 1.50 / 3.00   (all 3 samples: 2.33)
headings: h3 3   <- NOT h2, check the unit list
on threshold: prior_art
splits: motivation[1] 1/0/1  audience[1] 0/0/1  prior_art[2] 2/1/2
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/1  -> 0.67
  [2] Discussion                                   1/1/1  -> 1.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.
candidate 2 (found by 2 of 12 passes): The goal of this paper is not to advocate for a particular choice, but rather for any practical choice consistent with other usage in the library, and more descriptive and apt than the opaque `get`.
candidate 3 (found by 1 of 12 passes): P3091 offered `get_optional`, `lookup`, and `lookup_optional`, which failed to evoke enthusiasm.

## audience - grade 0.17 (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.

## prior_art - grade 1.33 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Discussion                                   2/1/2  -> 1.67
  [3] Proposal                                     1/1/1  -> 1.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): P3091 instituted a member `get` for associative containers, a monadic analog of `op[]` and `at()`.
candidate 2 (found by 3 of 12 passes): The only alternative seriously considered at the time was `lookup`, which was rejected by weak consensus.
candidate 3 (found by 3 of 12 passes): Here I propose `try_at(key)` but would welcome other suggestions consistent with established usage in the Standard.

## vehicle - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

-->
