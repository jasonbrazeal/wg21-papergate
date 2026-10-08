Verdict: Weak to Adequate (3/14)

The paper offers a reasonably clear motivation for the wording simplification it envisions, and it grounds that motivation in an approved related proposal and a concrete count of affected operations. Its support is thinnest, however, around the practical and procedural dimensions: it does not identify who would be affected, explain why the change belongs in the standard rather than in implementation or guidance, or provide any implementation experience.

- The strongest support is the established prior art, including the approved design in P3668 and LWG review of this paper.
- The paper also establishes why the change matters by pointing to repeated boilerplate in the standard library and the benefit of a universally accepted default.
- A notable gap is the absence of any discussion of who is affected by the change.
- The most glaring omission is the lack of implementation experience, leaving the practical consequences of the wording change unexamined.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 2.33   accumulate 3.67   max 4.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.67  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.00 / 3.00 / 3.00   (all 3 samples: 3.33)
headings: h2 6
on threshold: motivation, prior_art
splits: prior_art[6] 2/1/1  vehicle[4] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Proposal  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 3. Proposal  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): it would be possible to significantly shrink the standard library wording by defaulting those operations where appropriate.
candidate 2 (found by 2 of 24 passes): This pattern of explicitly defining the default meaning of the postfix operation is repeated on every iterator which exhibits the default behaviour in the standard.
candidate 3 (found by 1 of 24 passes): it would be possible to significantly shrink the standard library wording by defaulting those operations where appropriate
candidate 4 (found by 1 of 24 passes): This allows users to write shorter code using this sensible default with a universally-accepted meaning.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 3. Proposal  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Proposal  (part 1 of 2)                   1/1/1  -> 1.00
  [6] 3. Proposal  (part 2 of 2)                   2/1/1  -> 1.33
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Following design-approval of P3668 Defaulting Postfix Increment and Decrement Operations, it would be possible to significantly shrink the standard library wording by defaulting those operations where appropriate.
candidate 2 (found by 3 of 24 passes): The authors have identified 51 candidate operations in the standard which may be defaulted.
candidate 3 (found by 2 of 24 passes): LWG reviewed this paper at the Brno meeting, on 2026-06-10.
candidate 4 (found by 1 of 24 passes): [P3668] proposes explicitly defaulting postfix increment and decrement operations, giving them a definition equivalent to:

## vehicle - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/0/0  -> 0.33
  [5] 3. Proposal  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 3. Proposal  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): We consider this a strictly non-semantic, wording only change to the specification; and do not anticipate that implementations will have to update around this paper.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 3. Proposal  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 3. Proposal  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal  (part 1 of 2)                   0/0/0  -> 0.00
  [6] 3. Proposal  (part 2 of 2)                   0/0/0  -> 0.00
  [7] 4. Proposed Wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
