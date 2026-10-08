Verdict: Weak (1/14)

The paper offers very little support for its own standardization, resting almost entirely on a passing mention of expressed interest and a speculative aside about implementation combinations. Nearly every element needed to justify a standards change is absent, leaving the proposal without a clear audience, problem statement, or evidence of need. The thinnest areas are the complete lack of implementation experience, any explanation of why a library solution would be insufficient, and any account of who would actually be affected.

- The strongest support is the brief claim that multiple people have expressed a desire to examine the feature, though even this is not substantiated.
- The only other credited point is a hypothetical note that an implementation might want to enable the proposal alongside another proposal separately or together.
- The paper gives no account of who is affected, why the standard is the right venue, or how the feature would coordinate with existing work.
- Most glaringly, it offers no implementation experience and no argument for why a library cannot satisfy the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.00/14)

Provisionally addressed: 2 of 7. Provisional points: 1.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.00   corroborated 1.33   accumulate 1.00   max 2.00

## SUMMARY
grades: motivation 0.17  audience 0.00  prior_art 0.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 1.00 / 1.00 / 1.00   (all 3 samples: 1.00)
headings: h2 4
on threshold: prior_art
splits: motivation[2] 1/0/0  prior_art[4] 1/2/2
## END SUMMARY

## motivation - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           0/0/0  -> 0.00
  [5] Example                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): Because multiple people have expressed a desire to look at that.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           0/0/0  -> 0.00
  [5] Example                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.83 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           1/2/2  -> 1.67
  [5] Example                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): One can envision that an implementation that would want to implement both P2900 and P3100 would allow enabling them separately, or in combination.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           0/0/0  -> 0.00
  [5] Example                                      0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           0/0/0  -> 0.00
  [5] Example                                      0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           0/0/0  -> 0.00
  [5] Example                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The approach                                 0/0/0  -> 0.00
  [4] Is this different for programmers?           0/0/0  -> 0.00
  [5] Example                                      0/0/0  -> 0.00
candidates: (none validated)

-->
