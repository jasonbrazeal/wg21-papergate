Verdict: Weak to Adequate (3/14)

The paper offers only partial support for its own standardization, with its strongest contribution being a review of prior work and alternatives. Its case is thinnest in explaining who is affected, why the standard is the right venue, how the feature would coordinate with existing practice, and why a library solution cannot suffice.

- The paper does establish that it engages with prior art and alternatives, particularly by responding to P3937 and referencing the rejection of P3858.
- The paper claims but does not establish why the problem matters, resting on an unsupported leap from a specific implementation model to a general requirement for trivial relocation.
- The paper claims but does not establish implementation experience, since the cited implementation was removed after trivial relocation was voted down.
- The paper does not establish who is affected, why the standard is needed, how the proposal coordinates with other work, or why a library approach would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.33   accumulate 3.33   max 3.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 2.50 / 3.50 / 2.50   (all 3 samples: 2.83)
headings: h2 5
on threshold: prior_art
splits: implementation[5] 0/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): There are an array of problems with P3937.
candidate 2 (found by 2 of 18 passes): The paper does not however include a discussion on what other implementation options are available to type erased containers, and why changing trivial relocation to reduce the number of types that are trivially relocatable is the best solution.
candidate 3 (found by 1 of 18 passes): The problem occurs when the authors leap from existence of that problem in a specific implementation model of that specific data structure, to the assumption the such a model *must* be supported by trivial relocation.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               2/2/2  -> 2.00
  [6] 5 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): While P3937 is described as a discussion of the requirements of type erased data structures, it is fundamentally just a re-hash of existing papers that are arguing that trivial relocation should be a bitwise copy.
candidate 2 (found by 3 of 18 passes): P3858 was rejected because incorrect fixup logic could cause undefined behavior.
candidate 3 (found by 3 of 18 passes): There are an array of problems with P3937.
candidate 4 (found by 2 of 18 passes): P3937 presents a discussion of the type erasure requirements for any future trivial relocation feature in C++. This paper is a very short response to that paper addressing various issue in the presented requirements, and erroneous technical arguments.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.33  [binary: max] (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/1/0  -> 0.33
  [6] 5 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): It was already implemented prior to trivial relocation being voted down, and the implementation of trivial relocation was removed from clang.

-->
