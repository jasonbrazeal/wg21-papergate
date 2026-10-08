Verdict: Adequate (5/14)

The paper offers some concrete support for its standardization case, but much of the surrounding rationale remains asserted rather than demonstrated. The strongest evidence is the implementation experience, while the argument for why this belongs in the standard rather than being handled elsewhere is essentially absent.

- The paper establishes implementation experience through a Clang fork used to compile LLVM/Clang/libc++ and another large C++17 codebase, with a table of observed divergences.
- The motivation is established by the paper’s repeated concern that an implausible defaulted assignment operator declaration is currently permitted.
- The claims about who is affected and about prior art and alternatives are stated but not backed by evidence that users or related proposals would actually be impacted.
- The paper does not establish why the standard is the right venue, how the change coordinates with existing practice, or why a library solution cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 4 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.33   accumulate 4.67   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 5.50 / 3.50   (all 3 samples: 4.67)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: audience[4] 1/0/0  audience[5] 0/2/0  implementation[4] 2/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This permits implausible declarations like `A& operator=(const A&) && = default`, where the left-hand operand is rvalue-ref-qualified.
candidate 2 (found by 2 of 27 passes): Our concern is that the *unrealistic* declaration `A& operator=(const A&) && = default` is *permitted!* This has several minor drawbacks:
candidate 3 (found by 1 of 27 passes): Our concern is that the *unrealistic* declaration `A& operator=(const A&) && = default` is *permitted!*

## audience - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   1/0/0  -> 0.33
  [5] 3. Implementation experience                 0/2/0  -> 0.67
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): These signatures are similarly arcane, we expect that no users make use of them, and these signatures don’t help with template programming either
candidate 2 (found by 1 of 27 passes): Arthur has implemented § 6 Proposed wording (conservative) in his fork of Clang, and used it to compile both LLVM/Clang/libc++ and another large C++17 codebase.

## prior_art - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): [P2952] (currently in CWG for C++29) proposes that defaulted `operator=` overloads should (also) be allowed to have a placeholder return type.
candidate 2 (found by 1 of 27 passes): Additional papers in this space (such as [P3834]) must consider adding new, similarly implausible signatures to the language to remain consistent with this oddity.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/0/0  -> 0.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.67  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/1  -> 1.67
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Here is a table of the divergences we found, plus our opinion as to the currently conforming behavior, and our proposed behavior.
candidate 2 (found by 3 of 27 passes): Arthur has implemented § 6 Proposed wording (conservative) in his fork of Clang, and used it to compile both LLVM/Clang/libc++ and another large C++17 codebase.

-->
