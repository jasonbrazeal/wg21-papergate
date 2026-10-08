Verdict: Adequate (4/14)

The paper’s support for its own standardization is uneven: it leans almost entirely on the assertion that the feature is already widely implemented, but it does not develop that assertion into a clear case for why the standard should adopt it, who would benefit, or what problem would be solved. The thinnest areas are the absence of any argument for why a library solution is insufficient and the lack of concrete evidence about implementation experience beyond a passing reference to existing tests.

- The strongest support is the identification of existing `gnu::offset` and `clang::offset` practice as the design basis and prior art.
- The paper claims, but does not establish, that the feature is extremely popular and already implemented in a way that would justify standardization.
- The paper does not address why a library-based approach would be inadequate for the proposed functionality.
- The most glaring omission is the absence of any substantive discussion of implementation experience, coordination with implementers, or interoperability concerns beyond a single repeated sentence.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 6 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 5.00   accumulate 4.50   max 6.00

## SUMMARY
grades: motivation 0.67  audience 0.50  prior_art 1.50  vehicle 0.33  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 4.50 / 4.00 / 4.00   (all 3 samples: 4.17)
headings: h2 5
on threshold: prior_art
splits: motivation[5] 0/0/1  prior_art[2] 1/0/1  vehicle[4] 1/1/0  coordination[4] 1/0/0
## END SUMMARY

## motivation - grade 0.67 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    0/0/1  -> 0.33
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 1 of 18 passes): It is exactly a standardization of existing practice and what was approved in Austria.

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
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 2 (found by 3 of 18 passes): These are the only tenets of the design, and match the practice for existing implementations `gnu::offset` and `clang::offset`.
candidate 3 (found by 2 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.

## vehicle - grade 0.33 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/0  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.

## coordination - grade 0.17 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/0/0  -> 0.33
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

## implementation - grade 1.00  [binary: max] (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction and Motivation               1/1/1  -> 1.00
  [5] 3. Design                                    1/1/1  -> 1.00
  [6] 4. Wording                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): An additional, user-supported embed parameter implemented in Clang and GCC for providing an offset.
candidate 2 (found by 3 of 18 passes): The goal is to add the extremely-popular and already-implemented `gnu::offset` and `clang::offset` parameters as standard parameters.
candidate 3 (found by 2 of 18 passes): These are the only tenets of the design, and match the practice for existing implementations `gnu::offset` and `clang::offset`.
candidate 4 (found by 1 of 18 passes): It is also how the original author envisioned this when it was first PR’d to Clang, and the original tests (plus new ones) still pass in the LLVM/clang and gnu/gcc repositories.

-->
