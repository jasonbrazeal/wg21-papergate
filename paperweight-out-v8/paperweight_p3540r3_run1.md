Verdict: Adequate (5/14)

The paper’s support for standardization rests almost entirely on the existence of vendor extensions and prior implementation experience, but it does not develop the case for why this feature needs to be in the standard, who specifically benefits, or why a library solution is insufficient. The thinnest parts are the unargued claims about popularity and the complete absence of a discussion of alternatives to language-level standardization.

- The strongest support is the concrete implementation experience in both Clang and GCC, including the note that original tests still pass.
- The paper also establishes some prior art by pointing to the existing `gnu::offset` and `clang::offset` parameters and the earlier design intent.
- The most glaring omission is the lack of any argument for why a library cannot provide the same capability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 6 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.67   accumulate 5.00   max 6.67

## SUMMARY
grades: motivation 0.50  audience 0.50  prior_art 1.50  vehicle 0.50  coordination 0.17  insufficiency 0.00  implementation 1.67
sample agreement: 37 of 42 section-criterion pairs unanimous (88%)
single-sample totals would have been: 5.00 / 4.50 / 5.00   (all 3 samples: 4.83)
headings: h2 5
on threshold: prior_art, implementation
splits: prior_art[2] 1/0/0  vehicle[4] 0/1/1  vehicle[5] 1/0/0  coordination[4] 0/1/0
        implementation[5] 2/1/2
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
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 1 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.
candidate 3 (found by 1 of 18 passes): match the practice for existing implementations `gnu::offset` and `clang::offset`.
candidate 4 (found by 1 of 18 passes): match the practice for existing implementations `gnu::offset` and `clang::offset`. It is also how the original author envisioned this when it was first PR’d to Clang

## vehicle - grade 0.50 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               0/1/1  -> 0.67
  [5] 3. Design                                    1/0/0  -> 0.33
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 1 of 18 passes): it is exactly a standardization of existing practice and what was approved in Austria.

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

## implementation - grade 1.67  [binary: max] (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    2/1/2  -> 1.67
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 2 of 18 passes): It is also how the original author envisioned this when it was first PR’d to Clang, and the original tests (plus new ones) still pass in the LLVM/clang and gnu/gcc repositories.
candidate 3 (found by 1 of 18 passes): These are the only tenets of the design, and match the practice for existing implementations `gnu::offset` and `clang::offset`.

-->
