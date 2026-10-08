Verdict: Adequate (6/14)

The paper offers a narrow but real basis for its proposal: it clearly motivates the problem and provides concrete implementation experience, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas are the absence of any discussion of why a library solution cannot address the issue and the lack of coordination or interoperability analysis.

- The strongest support comes from the implementation experience, where the proposed wording and a conservative alternative were both implemented in Clang forks and used to compile large codebases with reported divergences.
- The paper establishes why the feature matters by identifying the confusing and implausible declarations it would remove and arguing that breakage would be insignificant.
- The claim about who is affected rests on a GitHub search and an expectation of no real-world use, but the paper does not establish that the search results are representative or that affected users would not object.
- The most glaring omission is the complete absence of any argument for why the standard, rather than a library or tooling approach, is the necessary venue for this change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 5.00   accumulate 6.50   max 8.00

## SUMMARY
grades: motivation 1.67  audience 1.17  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.50 / 6.50 / 6.00   (all 3 samples: 6.17)
headings: h2 7
on threshold: motivation, audience, prior_art, implementation
splits: motivation[5] 2/2/0  motivation[7] 1/0/1  audience[4] 0/0/1  prior_art[5] 1/1/0
        implementation[4] 2/2/0
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 2/2/0  -> 1.33
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          1/0/1  -> 0.67
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This permits implausible declarations like `A& operator=(const A&) && = default`, where the left-hand operand is rvalue-ref-qualified.
candidate 2 (found by 3 of 24 passes): The possibility of these unrealistic declarations makes C++ harder to understand.
candidate 3 (found by 2 of 24 passes): Removal of rarely-used and confusing feature.
candidate 4 (found by 1 of 24 passes): As such, we are confident that the breakage from making these signatures ill-formed would be insignificant.

## audience - grade 1.17 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/1  -> 0.33
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Searching GitHub for [rvalue-ref-qualified defaulted assignment](https://github.com/search?q=lang%3Acpp+%2Foperator%3D%5C%28%5B%5E%29%5D%2B%5C%29+%26%26+%3D+default%2F+&type=code) currently yields around 1.5k results.
candidate 2 (found by 1 of 24 passes): we expect that no users make use of them, and these signatures don’t help with template programming either

## prior_art - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/0  -> 0.67
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We previously additionally proposed a "conservative" design alternative which simply made the rvalue-ref-qualified case defaulted-as-deleted, but EWG found consensus for them to be ill-formed instead.
candidate 2 (found by 2 of 24 passes): Arthur has implemented both § 5 Proposed wording and our previously-proposed "conservative" design in forks of Clang, and used them to compile both LLVM/Clang/libc++ and another large C++17 codebase.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/0  -> 1.33
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Arthur has implemented both § 5 Proposed wording and our previously-proposed "conservative" design in forks of Clang, and used them to compile both LLVM/Clang/libc++ and another large C++17 codebase.
candidate 2 (found by 2 of 24 passes): Here is a table of the divergences we found, plus our opinion as to the currently conforming behavior, and our proposed behavior.

-->
