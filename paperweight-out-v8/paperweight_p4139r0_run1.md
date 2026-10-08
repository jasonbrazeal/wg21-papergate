Verdict: Weak (2/14)

The paper offers only a narrow foundation for its standardization case: it establishes that the naming question has prior art and alternatives, but leaves most of the burden—who is affected, why the standard must act, why a library cannot suffice, and whether anyone has implemented the idea—entirely unaddressed. The thinnest support lies in the absence of any demonstrated need for standardization beyond the author’s preference for a more descriptive name.

- The strongest support is the account of prior art and alternatives, showing that `get` was adopted in P3091 and that `lookup` was considered and rejected.
- The paper asserts the utility of a fallible `get` and the opacity of the current name, but does not establish why that matters to users or the library’s design.
- The paper never identifies who is affected by the proposed change or what practical problem they face.
- The most glaring omission is the complete lack of implementation experience, coordination considerations, or any argument for why this cannot be done outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.00   accumulate 2.83   max 3.00

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 27 of 28 section-criterion pairs unanimous (96%)
single-sample totals would have been: 2.00 / 2.00 / 3.00   (all 3 samples: 2.33)
headings: h3 3   <- NOT h2, check the unit list
on threshold: prior_art
splits: motivation[1] 0/0/2
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 4 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/2  -> 0.67
  [2] Discussion                                   1/1/1  -> 1.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): The goal of this paper is not to advocate for a particular choice, but rather for any practical choice consistent with other usage in the library, and more descriptive and apt than the opaque `get`.
candidate 2 (found by 1 of 12 passes): While of obvious utility, it is the first instance in the library of a `get()` that can fail.

## audience - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Discussion                                   0/0/0  -> 0.00
  [3] Proposal                                     0/0/0  -> 0.00
  [4] Reference                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
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
