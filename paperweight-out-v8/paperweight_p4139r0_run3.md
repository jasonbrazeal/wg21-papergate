Verdict: Adequate (4/14)

The paper offers only a narrow foundation for its own standardization, centered on the history of a related name choice, while leaving most of the burden of justification unaddressed. The thinnest areas are the absence of any argument for why this belongs in the standard rather than in user code, and the lack of implementation experience or interoperability discussion.

- The strongest support is the account of prior art and alternatives, which shows the naming question was considered before and that a rejected option existed.
- The paper asserts the utility of a fallible `get()` and its novelty in the library, but does not establish who is concretely affected or why the problem is significant enough to warrant standardization.
- The paper offers no case for why the standard should address this rather than a library solution.
- The paper is silent on coordination, interoperability, and implementation experience, leaving the practical case for standardization almost entirely undeveloped.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.33   accumulate 3.50   max 4.00

## SUMMARY
grades: motivation 1.33  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 26 of 28 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h3 3   <- NOT h2, check the unit list
on threshold: motivation
splits: motivation[1] 1/2/2  audience[1] 1/0/0
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 4 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/2/2  -> 1.67
  [2] Discussion                                   1/1/1  -> 1.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.
candidate 2 (found by 3 of 12 passes): The goal of this paper is not to advocate for a particular choice, but rather for any practical choice consistent with other usage in the library, and more descriptive and apt than the opaque `get`.

## audience - grade 0.17 (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.

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
