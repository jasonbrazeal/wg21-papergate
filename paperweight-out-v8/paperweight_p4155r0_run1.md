Verdict: Weak to Adequate (3/14)

The paper offers only partial support for its own standardization, mainly by situating itself against prior work and identifying what it sees as errors in P3937. Its case is thinnest where it needs to show who is affected, how the feature would coordinate with existing practice, and whether there is any implementation experience to draw on.

- The strongest support is the paper’s engagement with prior art and alternatives, including its response to P3937 and its reference to the earlier rejection of P3858.
- The argument for why the standard must change is asserted rather than demonstrated, since the paper does not show that prior decisions were wrong or that its approach is the best possible solution.
- The paper does not establish that a library solution is insufficient, because its performance comparison is acknowledged to have used an unrealistically pessimistic baseline.
- The most glaring omission is the absence of any discussion of who is affected, coordination and interoperability, or implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 3.67   accumulate 3.67   max 4.67

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 1.50  vehicle 0.50  coordination 0.00  insufficiency 0.33  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.50 / 3.00 / 3.00   (all 3 samples: 3.17)
headings: h2 5
on threshold: prior_art
splits: motivation[6] 1/1/0  insufficiency[6] 1/0/1
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    1/1/0  -> 0.67
candidate 1 (found by 3 of 18 passes): The problem occurs when the authors leap from existence of that problem in a specific implementation model of that specific data structure, to the assumption the such a model *must* be supported by trivial relocation.
candidate 2 (found by 2 of 18 passes): There are an array of problems with P3937.

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
candidate 1 (found by 3 of 18 passes): P3937 presents a discussion of the type erasure requirements for any future trivial relocation feature in C++. This paper is a very short response to that paper addressing various issue in the presented requirements, and erroneous technical arguments.
candidate 2 (found by 3 of 18 passes): P3858 was rejected because incorrect fixup logic could cause undefined behavior.
candidate 3 (found by 3 of 18 passes): There are an array of problems with P3937.
candidate 4 (found by 2 of 18 passes): The purpose of this paper is to respond to errors in P3937.

## vehicle - grade 0.50 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Given that outcome, the burden is on the authors of this paper to demonstrate why the prior decisions were wrong, which will require addressing the previous discussions, and demonstrating why their proposed change is the best possible solution.

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

## insufficiency - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 The use case                               0/0/0  -> 0.00
  [6] 5 Summary                                    1/0/1  -> 0.67
candidate 1 (found by 2 of 18 passes): The performance comparisons presented did not reflect the actual performance differences of the options, and instead only compared memcpy to the most pessimistic implementation.

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
