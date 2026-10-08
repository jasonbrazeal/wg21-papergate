Verdict: Weak (3/14)

The paper offers only a narrow slice of the case for standardization: it explains why direct construction of owning node handles would be useful, but leaves most of the surrounding justification unstated or asserted rather than demonstrated. The strongest material concerns the awkwardness of the current workaround, while the rest of the argument—who is affected, why this belongs in the standard, how it coordinates with existing practice, and whether anyone has tried it—is largely absent.

- The paper does establish that the current API forces users into a wasteful container-construction-and-extraction sequence just to obtain an owning node handle.
- The discussion of prior art and alternatives gestures toward related work and a design preference, but does not substantiate why the chosen approach is better or how it compares in practice.
- The paper offers no evidence that a library-level solution would be insufficient, despite the fact that the motivating example appears to involve ordinary user code rather than something only the standard library can do.
- The most glaring omission is the complete lack of implementation experience, affected-user analysis, or interoperability discussion, leaving the standardization need largely unexamined.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.33   accumulate 3.33   max 3.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 8
on threshold: motivation
splits: motivation[3] 2/1/1  prior_art[6] 1/2/1  insufficiency[3] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   2/1/1  -> 1.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes adding a way to construct owning `node-handle`s without containers.
candidate 2 (found by 3 of 27 passes): being unable to directly create an owning `node-handle` without constructing a container. Creating a container just to emplace one element that is immediately extracted, after which the container is destroyed is silly … yet is necessary with the current API
candidate 3 (found by 2 of 27 passes): //allocate expensive data structure 😬
candidate 4 (found by 1 of 27 passes): //allocate expensive data structure 😬 //then allocate the actual object

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## prior_art - grade 1.17 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design Space                                 1/2/1  -> 1.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): node-handle`s are a great way to transfer expensive-to-move or immovable objects between [node-based containers (which is one of the motivations in P3049 for adding this API to lists).](http://wg21.link/P3049)
candidate 2 (found by 2 of 27 passes): This feature could be provided in different ways: factory functions , or additional constructors for 2 `node-handle`.
candidate 3 (found by 1 of 27 passes): This feature could be provided in different ways: factory functions , or additional constructors for 2 `node-handle`. We prefer the latter option as it is the most logical to us

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

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/1  -> 0.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): //allocate expensive data structure 😬 //then allocate the actual object

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
