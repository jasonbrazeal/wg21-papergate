Verdict: Weak to Adequate (3/14)

The paper offers only a thin, largely rhetorical case for its own standardization, resting on assertions about prior committee discussions and the existence of a removed implementation rather than on evidence or analysis. The support is thinnest where the paper should be most concrete: it does not identify who is affected, show why a library solution is insufficient, or explain how the proposed change would interoperate with existing practice.

- The strongest support is the claim that the issue was previously discussed during trivial relocation’s design and that non-bitwise copying semantics were accepted, though the paper does not actually engage with those discussions.
- The paper asserts that an implementation existed before trivial relocation was voted down, but offers no usable implementation experience for the change it now proposes.
- The paper does not establish who would be affected by the proposed change, leaving the motivating audience entirely unspecified.
- The most glaring omission is the absence of any demonstration that a library-level solution cannot address the stated concerns, which leaves the need for standardization unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.33   accumulate 4.17   max 3.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.17  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 2.50 / 4.50 / 3.50   (all 3 samples: 3.33)
headings: h2 5
on threshold: none
splits: prior_art[5] 0/2/0  prior_art[6] 1/1/2  vehicle[4] 1/0/0  implementation[5] 0/2/1
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
candidate 2 (found by 1 of 18 passes): The problem occurs when the authors leap from existence of that problem in a specific implementation model of that specific data structure, to the assumption the such a model *must* be supported by trivial relocation.
candidate 3 (found by 1 of 18 passes): The paper does not however include a discussion on what other implementation options are available to type erased containers, and why changing trivial relocation to reduce the number of types that are trivially relocatable is the best solution.
candidate 4 (found by 1 of 18 passes): The specific issues surrounding type erased containers were discussed during the standardisation and design process of trivial relocation, and following those discussions the non-bitwise copying semantics were accepted by the committee.

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

## prior_art - grade 1.17 (fired in 4 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/2/0  -> 0.67
  [6] 5 Summary                                    1/1/2  -> 1.33
candidate 1 (found by 3 of 18 passes): While P3937 is described as a discussion of the requirements of type erased data structures, it is fundamentally just a re-hash of existing papers that are arguing that trivial relocation should be a bitwise copy.
candidate 2 (found by 2 of 18 passes): P3937 presents a discussion of the type erasure requirements for any future trivial relocation feature in C++.
candidate 3 (found by 2 of 18 passes): There are an array of problems with P3937.
candidate 4 (found by 1 of 18 passes): P3937 presents a discussion of the type erasure requirements for any future trivial relocation feature in C++. This paper is a very short response to that paper addressing various issue in the presented requirements, and erroneous technical arguments.

## vehicle - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/0/0  -> 0.33
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): Given that outcome, the burden is on the authors of this paper to demonstrate why the prior decisions were wrong, which will require addressing the previous discussions, and demonstrating why their proposed change is the best possible solution.

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/2/1  -> 1.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): It was already implemented prior to trivial relocation being voted down, and the implementation of trivial relocation was removed from clang.

-->
