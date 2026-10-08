Verdict: Adequate (4/14)

The paper offers only a narrow basis for its own standardization: it establishes that the proposed parameters match existing practice and prior art, but much of the rest of the case is asserted rather than demonstrated. The thinnest areas are the absence of any discussion of coordination, interoperability, or why a library solution would be insufficient.

- The strongest support is the identification of existing `gnu::offset` and `clang::offset` parameters as prior art and the claim that the design matches that practice.
- The paper asserts the feature’s popularity and the existence of implementation experience, but does not substantiate either with evidence beyond the assertion itself.
- The most glaring omission is the complete lack of discussion of coordination and interoperability with other features or implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 5 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 5.00   accumulate 4.50   max 6.00

## SUMMARY
grades: motivation 0.50  audience 0.50  prior_art 1.50  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 4.50 / 4.50 / 4.00   (all 3 samples: 4.33)
headings: h2 5
on threshold: prior_art
splits: prior_art[2] 0/1/0  vehicle[4] 1/0/1  vehicle[5] 1/0/0  implementation[5] 1/2/1
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.

## audience - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.

## prior_art - grade 1.50 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 3 of 18 passes): These are the only tenets of the design, and match the practice for existing implementations `gnu::offset` and `clang::offset`.
candidate 3 (found by 1 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.

## vehicle - grade 0.50 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/0/1  -> 0.67
  [5] 3. Design                                    1/0/0  -> 0.33
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 1 of 18 passes): it is exactly a standardization of existing practice and what was approved in Austria.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    1/2/1  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.
candidate 2 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 3 (found by 3 of 18 passes): It is also how the original author envisioned this when it was first PR’d to Clang, and the original tests (plus new ones) still pass in the LLVM/clang and gnu/gcc repositories.

-->
