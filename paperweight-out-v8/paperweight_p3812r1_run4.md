Verdict: Weak (2/14)

The paper offers only a thin case for standardization, resting almost entirely on a brief statement of motivation and a gesture toward existing lifetime rules and a Core Guideline. The support is thinnest around the practical questions that would justify committee action: who is affected, why the standard is the right venue, how the feature would interoperate, and whether any implementation experience exists.

- The strongest support is the paper’s claim that the change would remove a current limitation on default member functions.
- The prior art and alternatives section is credited only as a claim, pointing to lifetime rules and a Core Guideline without developing them into a comparison.
- The paper does not establish who would benefit from the change or how widespread the need is.
- The most glaring omission is the absence of any implementation experience, leaving the proposal without evidence that the feature is feasible or understood in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.00/14)

Provisionally addressed: 2 of 7. Provisional points: 2.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.00   corroborated 2.00   accumulate 2.50   max 2.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 35 of 35 section-criterion pairs unanimous (100%)
single-sample totals would have been: 2.00 / 2.00 / 2.00   (all 3 samples: 2.00)
headings: h2 4
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Impact on the standard                     1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): Allow compilers to be able to generate the default copy assignment operator for classes that have `const` and `&` members by making the class `transparently replaceable` if it has a default copy constructor.
candidate 2 (found by 3 of 15 passes): Without this functionality, besides being more code, constness has to be enforced via even more code instead of it being enforced by use of the `const` keyword or the constness associated with references.
candidate 3 (found by 3 of 15 passes): This features removes a current limitation of default member functions.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the standard                     0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the standard                     1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): See 6.7.4 Lifetime [basic.life] ¶ 9. [N5008]
candidate 2 (found by 3 of 15 passes): [c12] C++ Core Guidelines - C.12: Don’t make data members const or references in a copyable or movable type.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the standard                     0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the standard                     0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the standard                     0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the standard                     0/0/0  -> 0.00
candidates: (none validated)

-->
