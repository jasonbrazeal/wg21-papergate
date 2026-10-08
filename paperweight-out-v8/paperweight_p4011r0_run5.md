Verdict: Weak (3/14)

The paper offers only a narrow foundation for its standardization case: it articulates a conceptual motivation around undefined behavior and erroneous behavior, but leaves nearly every practical justification unaddressed. The support is thinnest where a proposal most needs substance—affected users, the need for a standard rather than a library, interoperability, and implementation experience are all absent.

- The strongest support is the paper’s clear framing of why the distinction between undefined and erroneous behavior matters for expressing contracts.
- The discussion of prior art gestures toward N3248 and related terminology, but does not establish how this proposal improves on or differs from those alternatives.
- The paper never identifies who would be affected by the proposed standardization or what problem they currently cannot solve.
- The most glaring omission is the absence of any argument for why the standard, rather than a library or existing practice, is the right vehicle.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.67/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.67   corroborated 2.00   accumulate 3.00   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 2.50 / 3.00 / 2.50   (all 3 samples: 2.67)
headings: h2 7
on threshold: motivation, prior_art
splits: motivation[6] 0/1/1  prior_art[7] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                2/2/2  -> 2.00
  [6] 4 A NEW DEFINITION                           0/1/1  -> 0.67
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        1/1/1  -> 1.00
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is what we expect of EB: it is still detectable as a bug in the program, but the program can continue without invoking UB.
candidate 2 (found by 2 of 24 passes): The trouble only begins when we introduce syntax that not only encodes the precondition, but at the same time unconditionally removes the undefined behavior
candidate 3 (found by 2 of 24 passes): The goal is to help us speak a common language.
candidate 4 (found by 1 of 24 passes): The trouble only begins when we introduce syntax that not only encodes the precondition, but at the same time unconditionally removes the undefined behavior:

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                0/0/0  -> 0.00
  [6] 4 A NEW DEFINITION                           0/0/0  -> 0.00
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        0/0/0  -> 0.00
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                2/2/2  -> 2.00
  [6] 4 A NEW DEFINITION                           0/0/0  -> 0.00
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        0/1/0  -> 0.33
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Meredith et al. [N3248] defined the terms *narrow* and *wide contract* in terms of *undefined* behavior
candidate 2 (found by 1 of 24 passes): This is what we expect of EB: it is still detectable as a bug in the program, but the program can continue without invoking UB.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                0/0/0  -> 0.00
  [6] 4 A NEW DEFINITION                           0/0/0  -> 0.00
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        0/0/0  -> 0.00
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                0/0/0  -> 0.00
  [6] 4 A NEW DEFINITION                           0/0/0  -> 0.00
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        0/0/0  -> 0.00
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                0/0/0  -> 0.00
  [6] 4 A NEW DEFINITION                           0/0/0  -> 0.00
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        0/0/0  -> 0.00
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 THE PROBLEM                                0/0/0  -> 0.00
  [6] 4 A NEW DEFINITION                           0/0/0  -> 0.00
  [7] 5 A CONNECTION TO ERRONEOUS BEHAVIOR?        0/0/0  -> 0.00
  [8] A BIBLIOGRAPHY                               0/0/0  -> 0.00
candidates: (none validated)

-->
