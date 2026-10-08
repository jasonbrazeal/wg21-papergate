Verdict: Weak (3/14)

The paper offers some useful groundwork by citing existing usage and documenting the naming alternatives it considered, but it does not build a case that this facility belongs in the standard rather than in a library or guideline. The thinnest parts are the absence of any argument for why standardization is necessary, how the feature would coordinate with existing concepts, or what implementation experience exists.

- The strongest support is the prior art section, which points to cppreference and Stack Overflow as evidence that users have sought this semantics.
- The paper claims the feature matters and identifies affected users only through a brief statement about encountering the need across several projects.
- The most glaring omission is the lack of any explanation for why the standard should provide this rather than a library solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.33   accumulate 2.67   max 3.33

## SUMMARY
grades: motivation 1.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 3.00 / 2.50   (all 3 samples: 2.67)
headings: h2 8
on threshold: prior_art
splits: audience[5] 0/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes adding two usability concepts to more concisely express (not) matching a list of types.
candidate 2 (found by 3 of 27 passes): We’ve encountered the need to express a template type parameter matching one of multiple types across several projects.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/1/0  -> 0.33
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): We’ve encountered the need to express a template type parameter matching one of multiple types across several projects.

## prior_art - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): We want to point to both the documentation for `same_as` [on cppreference as](https://en.cppreference.com/w/cpp/concepts/same_as) [as well as stackoverflow for prior usage/requests to express this semantics.](https://stackoverflow.com/questions/73377786/c-concept-that-a-type-is-same-as-any-one-of-several-types)
candidate 2 (found by 3 of 27 passes): We’ve considered the following alternative names and discarded them for the given reasons.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

-->
