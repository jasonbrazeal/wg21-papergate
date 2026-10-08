Verdict: Weak (3/14)

The paper offers only a narrow foundation for its own standardization, resting almost entirely on its engagement with prior discussions and its critique of P3937. Beyond that prior-art context, the case is thin: the affected users, the need for a standard facility, interoperability concerns, and the impossibility of a library solution are all left unaddressed.

- The strongest support is the paper’s demonstration that the relevant type-erasure concerns were already discussed during earlier trivial relocation design work.
- The paper claims, but does not substantiate, that the removal of an implementation from Clang constitutes meaningful implementation experience.
- The most glaring omission is the absence of any identified user population or concrete problem that standardization would solve.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.33   accumulate 3.33   max 3.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 2.83)
headings: h2 5
on threshold: prior_art
splits: prior_art[5] 2/2/0  prior_art[6] 2/2/1  implementation[5] 0/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): There are an array of problems with P3937.
candidate 2 (found by 1 of 18 passes): The specific issues surrounding type erased containers were discussed during the standardisation and design process of trivial relocation, and following those discussions the non-bitwise copying semantics were accepted by the committee.
candidate 3 (found by 1 of 18 passes): The purpose of this paper is to respond to errors in P3937.
candidate 4 (found by 1 of 18 passes): The problem occurs when the authors leap from existence of that problem in a specific implementation model of that specific data structure, to the assumption the such a model *must* be supported by trivial relocation.

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

## prior_art - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               2/2/0  -> 1.33
  [6] 5 Summary                                    2/2/1  -> 1.67
candidate 1 (found by 3 of 18 passes): P3937 presents a discussion of the type erasure requirements for any future trivial relocation feature in C++.
candidate 2 (found by 3 of 18 passes): While P3937 is described as a discussion of the requirements of type erased data structures, it is fundamentally just a re-hash of existing papers that are arguing that trivial relocation should be a bitwise copy.
candidate 3 (found by 2 of 18 passes): P3858 was rejected because incorrect fixup logic could cause undefined behavior.
candidate 4 (found by 2 of 18 passes): it does not address the prior discussions that led to the designed behavior of trivial relocation, and does not provide new information that was not discussed during the design and earlier standardisation work involved in trivial relocation.

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
  [5] 4 The use case                               0/0/1  -> 0.33
  [6] 5 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): the implementation of trivial relocation was removed from clang.

-->
