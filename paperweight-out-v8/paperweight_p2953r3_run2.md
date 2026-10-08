Verdict: Adequate (5/14)

The paper offers a solid, concrete case that the declarations it targets are implausible and that implementers have already tested the proposed direction, but it leaves several parts of the standardization argument largely asserted rather than demonstrated. The thinnest support concerns why this needs to be done in the standard itself, how it coordinates with related work, and why a library-level or non-standard remedy would be insufficient.

- The strongest support is the implementation experience, which includes a concrete divergence table and compilation of large codebases with a Clang fork.
- The paper clearly establishes why the issue matters by identifying implausible declarations and the corner case they would otherwise create.
- The discussion of affected users and prior art is suggestive but rests on expectations and assertions rather than demonstrated usage or a fuller exploration of alternatives.
- The most glaring omission is the absence of any established case for why the standard is the necessary venue, or how the change interoperates with adjacent standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 4 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.00   accumulate 5.33   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.50 / 5.00 / 5.00   (all 3 samples: 5.17)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: motivation[6] 0/1/0  prior_art[7] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/1/0  -> 0.33
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This permits implausible declarations like `A& operator=(const A&) && = default`, where the left-hand operand is rvalue-ref-qualified.
candidate 2 (found by 3 of 27 passes): The possibility of these unrealistic declarations makes C++ harder to understand.
candidate 3 (found by 1 of 27 passes): Without P2953 these changes add a corner case to the language. We should prevent that corner case by applying P2953 at the same time as P2952.

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   1/1/1  -> 1.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          0/0/0  -> 0.00
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): These signatures are similarly arcane, we expect that no users make use of them, and these signatures don’t help with template programming either
candidate 2 (found by 1 of 27 passes): But programmers aren’t clamoring for that declaration to be supported, so we do not propose it here.

## prior_art - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation and proposal                   2/2/2  -> 2.00
  [5] 3. Implementation experience                 0/0/0  -> 0.00
  [6] 4. Straw poll results                        0/0/0  -> 0.00
  [7] 5. Proposed wording                          1/0/0  -> 0.33
  [8] 6. Proposed wording (conservative)           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Additional papers in this space (such as [P3834]) must consider adding new, similarly implausible signatures to the language to remain consistent with this oddity.
candidate 2 (found by 1 of 27 passes): Also note that right now a difference in `noexcept`-ness is handled explicitly by [dcl.fct.def.default] for special member functions but only by omission-and-note in [[class.compare]](https://eel.is/c++draft/class.compare#default-note-1) for comparison operators.

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
