Verdict: Adequate (6/14)

The paper offers solid evidence that the problem is real, that a language change is implementable, and that related proposals will need to account for it, but it leaves several core justifications for standardization essentially unargued. The thinnest parts concern why the standard itself must change, how the change interacts with other work, and why a library solution cannot suffice.

- The strongest support is the implementation experience, with both wording options compiled against large real-world codebases.
- The paper also clearly establishes why the current permissiveness matters and that alternatives have been considered.
- The most glaring omission is the absence of any established case for why the standard is the necessary place to address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 5.00   accumulate 6.33   max 8.00

## SUMMARY
grades: motivation 1.50  audience 1.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 6.50 / 6.00   (all 3 samples: 6.17)
headings: h2 8
on threshold: motivation, audience, prior_art
splits: audience[4] 0/1/0  prior_art[6] 0/1/0
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
candidate 1 (found by 3 of 27 passes): The possibility of these unrealistic declarations makes C++ harder to understand.
candidate 2 (found by 2 of 27 passes): Current C++ permits explicitly-defaulted special members to differ from their implicitly-defaulted counterparts in various ways, including parameter type and ref-qualification.
candidate 3 (found by 1 of 27 passes): This permits implausible declarations like `A& operator=(const A&) && = default`, where the left-hand operand is rvalue-ref-qualified.

## audience - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   0/1/0  -> 0.33
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Searching GitHub for [rvalue-ref-qualified defaulted assignment](https://github.com/search?q=lang%3Acpp+%2Foperator%3D%5C%28%5B%5E%29%5D%2B%5C%29+%26%26+%3D+default%2F+&type=code) currently yields around 1.5k results.
candidate 2 (found by 1 of 27 passes): However, as nobody ever writes `B& operator=(const B&) && = default` we do not need to add any *new* carveouts.

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Straw poll results                        0/1/0  -> 0.33
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Arthur has implemented both § 5 Proposed wording and § 6 Proposed wording (conservative) in forks of Clang, and used them to compile both LLVM/Clang/libc++ and another large C++17 codebase.
candidate 2 (found by 2 of 27 passes): Additional papers in this space (such as [P3834]) must consider adding new, similarly implausible signatures to the language to remain consistent with this oddity.
candidate 3 (found by 1 of 27 passes): [P2952] (currently in CWG for C++29) proposes that defaulted `operator=` overloads should (also) be allowed to have a placeholder return type.
candidate 4 (found by 1 of 27 passes): Arthur O’Dwyer presented P2592R1 (not P2953, but P2952) in the EWG telecon of 2025-01-08.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Here is a table of the divergences we found, plus our opinion as to the currently conforming behavior, and our proposed behavior.
candidate 2 (found by 3 of 27 passes): Arthur has implemented both § 5 Proposed wording and § 6 Proposed wording (conservative) in forks of Clang, and used them to compile both LLVM/Clang/libc++ and another large C++17 codebase.

-->
