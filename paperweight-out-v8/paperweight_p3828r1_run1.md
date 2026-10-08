Verdict: Weak (2/14)

The paper offers only a thin, largely rhetorical case for its proposed rename, resting on assertions about naming convention and intuition rather than evidence or analysis. The support is thinnest where the proposal should show who is actually affected, why existing practice is insufficient, and whether the change is feasible or necessary in the standard itself.

- The strongest support is the appeal to existing naming patterns like `as_const` and `as_rvalue`, which at least gestures toward consistency with established library conventions.
- The paper claims the current name is misleading and the proposed name more intuitive, but it does not demonstrate who encounters this problem or how seriously it affects them.
- The proposal offers no evidence of prior discussion, implementation experience, or coordination with related facilities, leaving the standardization need almost entirely unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.83/14)

Provisionally addressed: 3 of 7. Provisional points: 1.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.83   corroborated 2.33   accumulate 1.83   max 3.00

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 0.83  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 2.00 / 2.00 / 1.50   (all 3 samples: 1.83)
headings: h2 4
on threshold: motivation
splits: motivation[1] 1/2/2  prior_art[2] 1/1/0  vehicle[1] 1/0/0
## END SUMMARY

## motivation - grade 0.83 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/2/2  -> 1.67
  [2] Proposed Wording                             0/0/0  -> 0.00
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The current name of the "to_input" view is misleading, because this sounds like the elements of the underlying range are actively processed (like with std::ranges::to).

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Proposed Wording                             0/0/0  -> 0.00
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.83 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Proposed Wording                             1/1/0  -> 0.67
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): For views like this we usually use the name “as_...” (e.g. as_const or as_rvalue).
candidate 2 (found by 2 of 15 passes): Nicolai Josuttis: P3828R1: Rename the to_input view to as_input and rename inside:

## vehicle - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] Proposed Wording                             0/0/0  -> 0.00
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): This is both more intuitive and consistent.

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Proposed Wording                             0/0/0  -> 0.00
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Proposed Wording                             0/0/0  -> 0.00
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Proposed Wording                             0/0/0  -> 0.00
  [3] Acknowledgements                             0/0/0  -> 0.00
  [4] Rev0:                                        0/0/0  -> 0.00
  [5] Rev1:                                        0/0/0  -> 0.00
candidates: (none validated)

-->
