Verdict: Weak (3/14)

The paper offers only a narrow slice of the case needed for standardization: it situates the proposed name against a prior rejected alternative and explains the motivation in general terms, but it leaves most of the burden unaddressed. The support is thinnest around the basic question of why this belongs in the standard library at all, since the paper does not identify affected users, argue that a library solution is insufficient, or report any implementation experience.

- The strongest support is the prior-art discussion, which credibly connects the proposal to P3091 and the earlier rejection of `lookup`.
- The paper gestures at why the change matters by noting that a fallible `get()` is a new kind of library API, but it does not develop that observation into a concrete need.
- The most glaring omission is the absence of any account of who is affected or why standardization, rather than a library-level solution, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 3.00   accumulate 3.00   max 3.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 28 of 28 section-criterion pairs unanimous (100%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h3 3   <- NOT h2, check the unit list
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 4 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Discussion                                   1/1/1  -> 1.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.
candidate 2 (found by 3 of 12 passes): The goal of this paper is not to advocate for a particular choice, but rather for any practical choice consistent with other usage in the library, and more descriptive and apt than the opaque `get`.

## audience - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 4 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Discussion                                   2/2/2  -> 2.00
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
