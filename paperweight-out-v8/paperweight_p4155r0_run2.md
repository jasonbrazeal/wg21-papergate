Verdict: Weak (2/14)

The paper offers only a narrow foundation for its own standardization case: it shows familiarity with prior discussions and alternatives, but leaves most of the burden of justification unaddressed. The thinnest areas are the absence of any identified affected users, any reason the standard is the right venue, and any evidence that a library solution or implementation experience supports the proposal.

- The strongest support is the paper’s engagement with prior art, particularly its discussion of P3937 and the rejected P3858, which grounds the conversation in existing committee history.
- The claim that the issue matters rests on an interpretive leap from a specific implementation model to a general requirement, so it is asserted rather than demonstrated.
- The paper does not establish who is affected, leaving the practical stakes of the problem entirely unspecified.
- Most glaringly, it offers no case for why the standard should act, why a library cannot suffice, or what implementation experience exists, so the central standardization questions remain unanswered.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.00   accumulate 2.83   max 3.00

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 2.50 / 3.00 / 2.00   (all 3 samples: 2.33)
headings: h2 5
on threshold: prior_art
splits: motivation[6] 1/1/0  prior_art[5] 0/2/0
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    1/1/0  -> 0.67
candidate 1 (found by 2 of 18 passes): The specific issues surrounding type erased containers were discussed during the standardisation and design process of trivial relocation, and following those discussions the non-bitwise copying semantics were accepted by the committee.
candidate 2 (found by 2 of 18 passes): There are an array of problems with P3937.
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

## prior_art - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/2/0  -> 0.67
  [6] 5 Summary                                    2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): P3937 presents a discussion of the type erasure requirements for any future trivial relocation feature in C++.
candidate 2 (found by 3 of 18 passes): While P3937 is described as a discussion of the requirements of type erased data structures, it is fundamentally just a re-hash of existing papers that are arguing that trivial relocation should be a bitwise copy.
candidate 3 (found by 2 of 18 passes): There are an array of problems with P3937. At a basic level it does not address the prior discussions that led to the designed behavior of trivial relocation
candidate 4 (found by 1 of 18 passes): P3858 was rejected because incorrect fixup logic could cause undefined behavior.

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

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidates: (none validated)

-->
