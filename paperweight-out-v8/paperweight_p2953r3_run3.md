Verdict: Adequate (5/14)

The paper gives a clear and concrete reason that the status quo is worth changing, and it shows that the proposed direction has been implemented and tested against real code. The support is much thinner, however, when it comes to showing who is actually affected, why the change belongs in the standard rather than elsewhere, and how it fits with existing practice and related proposals.

- The strongest part of the paper is its demonstration that the currently permitted declarations are unrealistic and make the language harder to understand.
- The implementation experience is also well supported, with a table of divergences and a Clang implementation used on large codebases.
- The paper only asserts, without evidence, that no users rely on these signatures and that they do not help with template programming.
- The most glaring omission is the absence of any case for why this needs standardization as opposed to a different remedy, with no discussion of coordination, interoperability, or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 4 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.33   accumulate 4.67   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 4.50 / 5.00 / 4.50   (all 3 samples: 4.67)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: audience[4] 0/1/0
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
candidate 3 (found by 1 of 27 passes): This has several minor drawbacks: - The possibility of these unrealistic declarations makes C++ harder to understand.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/1/0  -> 0.33
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): we expect that no users make use of them, and these signatures don’t help with template programming either

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
candidate 1 (found by 3 of 27 passes): [P2952] (currently in CWG for C++29) proposes that defaulted `operator=` overloads should (also) be allowed to have a placeholder return type.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Here is a table of the divergences we found, plus our opinion as to the currently conforming behavior, and our proposed behavior.
candidate 2 (found by 3 of 27 passes): Arthur has implemented § 6 Proposed wording (conservative) in his fork of Clang, and used it to compile both LLVM/Clang/libc++ and another large C++17 codebase.

-->
