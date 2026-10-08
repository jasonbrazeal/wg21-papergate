Verdict: Weak to Adequate (3/14)

The paper offers only a narrow slice of the case needed for standardization: it gestures at the motivation and names some prior naming discussion, but leaves the core standardization questions essentially unaddressed. The thinnest areas are the absence of any argument for why this belongs in the standard, why a library solution is insufficient, or how it would interoperate with existing practice.

- The strongest support is the record of prior art and alternatives, particularly the naming history from P3091 and the rejection of `lookup`.
- The paper claims the change matters because it would be the first fallible `get()` in the library, but it does not develop that claim into a demonstrated need.
- The paper does not establish who is concretely affected beyond a general assertion of obvious utility.
- The most glaring omission is the complete lack of discussion of why standardization is required, why a library cannot provide the facility, or how it would coordinate with existing interfaces.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 3.33   accumulate 3.17   max 3.33

## SUMMARY
grades: motivation 1.00  audience 0.17  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 25 of 28 section-criterion pairs unanimous (89%)
single-sample totals would have been: 3.50 / 3.00 / 2.50   (all 3 samples: 3.00)
headings: h3 3   <- NOT h2, check the unit list
on threshold: none
splits: motivation[1] 1/2/0  audience[1] 1/0/0  prior_art[1] 2/1/2
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/2/0  -> 1.00
  [2] Discussion                                   1/1/1  -> 1.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): The goal of this paper is not to advocate for a particular choice, but rather for any practical choice consistent with other usage in the library, and more descriptive and apt than the opaque `get`.
candidate 2 (found by 2 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.

## audience - grade 0.17 (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.

## prior_art - grade 1.83 (fired in 3 of 4 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/1/2  -> 1.67
  [2] Discussion                                   2/2/2  -> 2.00
  [3] Proposal                                     1/1/1  -> 1.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): P3091 instituted a member `get` for associative containers, a monadic analog of `op[]` and `at()`.
candidate 2 (found by 3 of 12 passes): Here I propose `try_at(key)` but would welcome other suggestions consistent with established usage in the Standard.
candidate 3 (found by 2 of 12 passes): P3091 offered `get_optional`, `lookup`, and `lookup_optional`, which failed to evoke enthusiasm.
candidate 4 (found by 1 of 12 passes): The only alternative seriously considered at the time was `lookup`, which was rejected by weak consensus.

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
