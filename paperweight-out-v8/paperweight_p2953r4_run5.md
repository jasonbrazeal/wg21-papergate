Verdict: Adequate (7/14)

The paper gives a partial account of why the change should be standardized, with its strongest material concerning implementation experience and the relationship to P2952, but it leaves several essential parts of the standardization case unaddressed. The thinnest areas are the absence of a direct argument for why the standard must change, how the change coordinates with existing specifications, and why a library-level solution cannot suffice.

- The paper’s implementation experience is the most concrete support, including a Clang fork used to compile large codebases and a table of divergences from current behavior.
- The paper establishes prior art and alternatives by connecting the proposal to P2952 and noting implementation and discussion history.
- The paper claims but does not establish who is affected, relying on a GitHub search and an expectation that no users depend on the relevant signatures.
- The most glaring omission is that the paper never establishes why the standard is the right place for this change, nor does it address coordination, interoperability, or why a library solution would not work.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.00   accumulate 6.83   max 8.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 7.00 / 6.50   (all 3 samples: 6.67)
headings: h2 8
on threshold: audience, prior_art
splits: motivation[6] 0/0/1  audience[4] 0/1/0  prior_art[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 2/2/2  -> 2.00
  [6] 4. Straw poll results                        0/0/1  -> 0.33
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This permits implausible declarations like `A& operator=(const A&) && = default`, where the left-hand operand is rvalue-ref-qualified.
candidate 2 (found by 3 of 27 passes): The possibility of these unrealistic declarations makes C++ harder to understand.
candidate 3 (found by 3 of 27 passes): We have also searched for any real-world use of these operator overloads to assess deployment.
candidate 4 (found by 1 of 27 passes): The sole voter "Against" P2952’s adoption gave as their rationale (paraphrased): "Without P2953 these changes add a corner case to the language. We should prevent that corner case by applying P2953 at the same time as P2952."

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
candidate 2 (found by 1 of 27 passes): we expect that no users make use of them, and these signatures don’t help with template programming either

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 1/1/1  -> 1.00
  [6] 4. Straw poll results                        0/0/1  -> 0.33
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): [P2952] (currently in CWG for C++29) proposes that defaulted `operator=` overloads should (also) be allowed to have a placeholder return type.
candidate 2 (found by 3 of 27 passes): Arthur has implemented both § 5 Proposed wording and § 6 Proposed wording (conservative) in forks of Clang, and used them to compile both LLVM/Clang/libc++ and another large C++17 codebase.
candidate 3 (found by 1 of 27 passes): Arthur O’Dwyer presented P2592R1 (not P2953, but P2952) in the EWG telecon of 2025-01-08.

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
