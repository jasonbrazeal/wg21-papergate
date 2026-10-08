Verdict: Adequate (5/14)

The paper rests almost entirely on the assertion that `gnu::offset` and `clang::offset` are already popular and implemented, but it does not substantiate that popularity or explain who would be affected by standardization. The strongest concrete support is the existence of prior implementations and passing tests in both Clang and GCC, while the case for why this belongs in the standard rather than remaining a vendor extension is essentially absent.

- The paper establishes that the feature has prior art and implementation experience in both Clang and GCC, including passing tests.
- The paper claims, but does not demonstrate, that the feature is extremely popular or that users are affected by its absence from the standard.
- The paper does not establish why a library solution would be insufficient, leaving that required argument entirely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 6 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.67   accumulate 5.33   max 6.67

## SUMMARY
grades: motivation 0.50  audience 0.50  prior_art 1.50  vehicle 0.17  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.50 / 5.50 / 4.50   (all 3 samples: 4.83)
headings: h2 5
on threshold: prior_art, implementation
splits: vehicle[4] 0/1/0  coordination[4] 0/1/0
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
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.
candidate 2 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 3 (found by 3 of 18 passes): These are the only tenets of the design, and match the practice for existing implementations `gnu::offset` and `clang::offset`.

## vehicle - grade 0.17 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               0/1/0  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.

## coordination - grade 0.17 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               0/1/0  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.
candidate 2 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 3 (found by 3 of 18 passes): It is also how the original author envisioned this when it was first PR’d to Clang, and the original tests (plus new ones) still pass in the LLVM/clang and gnu/gcc repositories.

-->
