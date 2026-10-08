Verdict: Adequate (4/14)

The paper offers a narrow but real foundation for its standardization case, chiefly through its engagement with prior art and design alternatives, but it leaves several essential justifications almost entirely unaddressed. The thinnest areas are the absence of any account of who is affected, how the feature would coordinate with existing practice, and why a library solution cannot suffice.

- The strongest support is the paper’s discussion of prior art, including its explicit positioning against P2900 assertions and its stated alignment with P3919R0.
- The motivation is asserted in general terms around guaranteed assertions and safety, but the paper does not develop that into a concrete case for why the problem matters to identifiable users or codebases.
- The paper offers no meaningful implementation experience for the proposal itself, acknowledging that the full form has not been implemented.
- The most glaring omission is the complete lack of discussion of who is affected, coordination and interoperability, or why a library approach would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 4 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 5.00   accumulate 4.00   max 5.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 42 of 42 section-criterion pairs unanimous (100%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 5
on threshold: none
splits: none
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The main motivation                          1/1/1  -> 1.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The main motivation is to provide a *guaranteed* assertion facility.
candidate 2 (found by 1 of 18 passes): Such a guarantee allows programs and users to be certain that the defined conditions are met, and such a guarantee therefore provides various forms of (mostly memory- and ub-) safety for callers, callees, readers, reviewers, and tools that they use.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The main motivation                          0/0/0  -> 0.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] The main motivation                          1/1/1  -> 1.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 2/2/2  -> 2.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Suggestions that such a facility is less necessary and enough functionality can be provided by just a guaranteed-assertion statement miss this goal.
candidate 2 (found by 3 of 18 passes): What is proposed here is that it is ill-formed to mix guaranteed-enforced assertions and P2900 assertions in the same function declaration.
candidate 3 (found by 2 of 18 passes): It follows the design guidance suggestions of P3919R0, and differs from P3911 by proposing a new keyword and new context-sensitive keywords that are separate and different from the P2900 ones
candidate 4 (found by 1 of 18 passes): It follows the design guidance suggestions of P3919R0, and differs from P3911 by

## vehicle - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The main motivation                          1/1/1  -> 1.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Such a guarantee allows programs and users to be certain that the defined conditions are met, and such a guarantee therefore provides various forms of (mostly memory- and ub-) safety for callers, callees, readers, reviewers, and tools that they use.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The main motivation                          0/0/0  -> 0.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The main motivation                          0/0/0  -> 0.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The main motivation                          0/0/0  -> 0.00
  [4] The main parts                               0/0/0  -> 0.00
  [5] Additional semantic bits, and differences... 0/0/0  -> 0.00
  [6] Implementation experience                    1/1/1  -> 1.00
candidate 1 (found by 2 of 18 passes): The full form of this proposal hasn't been implemented yet.
candidate 2 (found by 1 of 18 passes): we have implementation experience with always-enforced contract assertions

-->
